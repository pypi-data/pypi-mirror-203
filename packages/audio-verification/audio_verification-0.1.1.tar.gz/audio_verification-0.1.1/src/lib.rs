pub mod core;
pub mod io;

use crate::core::read_signal_info;
use std::{
    fs,
    path::{Path, PathBuf},
};

use pyo3::{prelude::*, types::PyList};

use crate::core::AVError;
pub use crate::core::{VerificationConfig, VerificationResult};
use io::read_config;

#[pymodule]
fn audio_verification(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<VerificationConfig>()?;
    m.add_class::<VerificationResult>()?;
    m.add_function(wrap_pyfunction!(verify, m)?)?;
    Ok(())
}

#[pyfunction]
fn verify(
    py: Python<'_>,
    config_fp: String,
    audio_dir_path: String,
    parallel: bool,
) -> PyResult<&'_ PyList> {
    if parallel {
        let results: Result<_, _> = py.allow_threads(move || {
            par_verify_audio_files(config_fp.as_str(), audio_dir_path.as_str())
        });
        let r = match results {
            Ok(results) => {
                let results = PyList::new(py, results);
                results
            }
            Err(e) => {
                println!("Error: {}", e);
                return Err(e.into());
            }
        };

        let results = PyList::new(py, r);
        Ok(results)
    } else {
        println!("Not using rayon");
        let results = verify_audio_files(config_fp.as_str(), audio_dir_path.as_str())?;
        let results = PyList::new(py, results);
        Ok(results)
    }
}

pub fn verify_audio_files(
    config_fp: &str,
    audio_dir_path: &str,
) -> Result<Vec<VerificationResult>, AVError> {
    let path = std::path::Path::new(config_fp);
    let config = read_config(&path)?;

    let files = dir_files(audio_dir_path)?;

    Ok(files
        .iter()
        .map(|file| {
            let file_name = file.file_name().unwrap().to_str().unwrap();
            let file_path = file.to_str().unwrap();
            let signal_info = match read_signal_info(Path::new(file_path)) {
                Ok(info) => info,
                Err(e) => {
                    return Err(std::io::Error::new(
                        std::io::ErrorKind::NotFound,
                        format!("Error reading signal info: {}", e),
                    ))
                }
            };
            let file_data = VerificationConfig::from(signal_info);

            Ok(config.verify(&file_data, file_name.to_string()))
        })
        .filter_map(Result::ok)
        .flatten()
        .collect::<Vec<VerificationResult>>())
}

pub fn par_verify_audio_files(
    config_fp: &str,
    audio_dir_path: &str,
) -> Result<Vec<VerificationResult>, AVError> {
    use rayon::prelude::*;
    let path = std::path::Path::new(config_fp);
    let config = read_config(&path)?;

    let files = dir_files(audio_dir_path)?;

    Ok(files
        .par_iter()
        .map(|fp| {
            let file_name = fp.file_name().unwrap().to_str().unwrap();
            let file_path = fp.to_str().unwrap();
            let signal_info = match read_signal_info(Path::new(file_path)) {
                Ok(info) => info,
                Err(e) => {
                    return Err(std::io::Error::new(
                        std::io::ErrorKind::NotFound,
                        format!("Error reading signal info: {}", e),
                    ));
                }
            };
            let file_data = VerificationConfig::from(signal_info);

            let file_results: Vec<VerificationResult> =
                config.verify(&file_data, file_name.to_string());
            Ok(file_results)
        })
        .filter_map(Result::ok)
        .flatten()
        .collect::<Vec<VerificationResult>>())
}

fn dir_files(root: &str) -> Result<Vec<PathBuf>, std::io::Error> {
    let files = match Path::new(root).exists() {
        true => {
            let mut files = Vec::new();
            for entry in fs::read_dir(root)? {
                let entry = entry?;
                let path = entry.path();
                if path.is_file() {
                    files.push(path);
                }
            }
            files
        }
        false => {
            return Err(std::io::Error::new(
                std::io::ErrorKind::NotFound,
                format!("Audio directory {:?} could not be found.", root),
            ))
        }
    };
    Ok(files)
}
