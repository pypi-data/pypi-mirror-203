pub mod core;
pub mod io;
use std::{
    fs,
    path::{Path, PathBuf},
};

use crate::{
    core::{read_signal_info, VerificationConfig, VerificationResult},
    io::read_config,
};

fn main() {
    let config_path = "config.yaml";
    let audio_dir_path = "./data/";

    let results = match verify_audio_files(config_path, audio_dir_path) {
        Ok(results) => results,
        Err(e) => panic!("Error verifying audio files:\n{:#?}", e),
    };
    println!("{:#?}", results);
}

pub fn verify_audio_files(
    config_fp: &str,
    audio_dir_path: &str,
) -> Result<Vec<VerificationResult>, std::io::Error> {
    let path = std::path::Path::new(config_fp);
    let config = match read_config(&path) {
        Ok(config) => config,
        Err(e) => panic!("Error reading config: {}", e),
    };

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

#[cfg(feature = "rayon")]
fn parallel_verify_audio_files(
    config_fp: &str,
    audio_dir_path: &str,
) -> Result<Vec<VerificationResult>, std::io::Error> {
    use rayon::prelude::*;

    let path = std::path::Path::new(config_fp);
    let config = match read_config(&path) {
        Ok(config) => config,
        Err(e) => panic!("Error reading config: {}", e),
    };

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
