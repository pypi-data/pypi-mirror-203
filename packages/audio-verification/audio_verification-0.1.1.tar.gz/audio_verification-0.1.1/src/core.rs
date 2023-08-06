use std::{
    fs::File,
    io::{BufReader, Read, Seek, SeekFrom},
    path::Path,
};

use pyo3::{prelude::*, types::PyDict};
use serde::{Deserialize, Serialize};
use thiserror::Error;

use crate::io::find_sub_chunk_id;

#[derive(Error, Debug)]
pub enum AVError {
    #[error(transparent)]
    IOError(std::io::Error),
    #[error(transparent)]
    ConfigError(std::io::Error),
}

impl From<AVError> for PyErr {
    fn from(e: AVError) -> PyErr {
        match e {
            AVError::IOError(e) => e.into(),
            AVError::ConfigError(e) => e.into(),
        }
    }
}

impl From<std::io::Error> for AVError {
    fn from(e: std::io::Error) -> Self {
        AVError::IOError(e)
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[pyclass]
pub struct VerificationResult {
    pub field: String,
    pub fp: String,
    pub result: bool,
    pub expected: String,
    pub actual: String,
}

impl VerificationResult {
    pub fn new(field: String, fp: String, result: bool, expected: String, actual: String) -> Self {
        Self {
            field,
            fp,
            result,
            expected,
            actual,
        }
    }
}

impl ToPyObject for VerificationResult {
    fn to_object(&self, py: Python) -> PyObject {
        let dict = PyDict::new(py);
        dict.set_item("field", self.field.clone()).unwrap();
        dict.set_item("fp", self.fp.clone()).unwrap();
        dict.set_item("result", self.result).unwrap();
        dict.set_item("expected", self.expected.clone()).unwrap();
        dict.set_item("actual", self.actual.clone()).unwrap();
        dict.to_object(py)
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[pyclass]
pub struct VerificationConfig {
    pub sample_rate: Option<i32>,
    pub channels: Option<u16>,
    pub sample_format: Option<u16>,
    pub bit_depth: Option<u16>,
    pub duration: Option<u64>,
}

impl VerificationConfig {
    pub fn new(
        sample_rate: Option<i32>,
        channels: Option<u16>,
        sample_format: Option<u16>,
        bit_depth: Option<u16>,
        duration: Option<u64>,
    ) -> Self {
        Self {
            sample_rate,
            channels,
            sample_format,
            bit_depth,
            duration,
        }
    }

    pub fn verify(&self, other: &Self, file_name: String) -> Vec<VerificationResult> {
        let mut results = Vec::new();
        match self.sample_rate {
            Some(sr) => {
                if let Some(other_sr) = other.sample_rate {
                    if sr != other_sr {
                        results.push(VerificationResult::new(
                            "sample_rate".to_string(),
                            file_name.clone(),
                            false,
                            sr.to_string(),
                            other_sr.to_string(),
                        ));
                    }
                }
            }
            None => (),
        }

        match self.channels {
            Some(ch) => {
                if let Some(other_ch) = other.channels {
                    if ch != other_ch {
                        results.push(VerificationResult::new(
                            "channels".to_string(),
                            file_name.clone(),
                            false,
                            ch.to_string(),
                            other_ch.to_string(),
                        ));
                    }
                }
            }
            None => (),
        }

        match self.sample_format {
            Some(sf) => {
                if let Some(other_sf) = other.sample_format {
                    if sf != other_sf {
                        results.push(VerificationResult::new(
                            "sample_format".to_string(),
                            file_name.clone(),
                            false,
                            sf.to_string(),
                            other_sf.to_string(),
                        ));
                    }
                }
            }
            None => (),
        }

        match self.bit_depth {
            Some(bd) => {
                if let Some(other_bd) = other.bit_depth {
                    if bd != other_bd {
                        results.push(VerificationResult::new(
                            "bit_depth".to_string(),
                            file_name.clone(),
                            false,
                            bd.to_string(),
                            other_bd.to_string(),
                        ));
                    }
                }
            }
            None => (),
        }

        match self.duration {
            Some(d) => {
                if let Some(other_d) = other.duration {
                    if d != other_d {
                        results.push(VerificationResult::new(
                            "duration".to_string(),
                            file_name.clone(),
                            false,
                            d.to_string(),
                            other_d.to_string(),
                        ));
                    }
                }
            }
            None => (),
        };

        results
    }
}

impl Default for VerificationConfig {
    fn default() -> Self {
        Self {
            sample_rate: Default::default(),
            channels: Default::default(),
            sample_format: Default::default(),
            bit_depth: Default::default(),
            duration: Default::default(),
        }
    }
}

impl From<(FmtChunk, u64)> for VerificationConfig {
    fn from(data: (FmtChunk, u64)) -> Self {
        let (fmt_chunk, duration) = data;
        Self {
            sample_rate: Some(fmt_chunk.sample_rate),
            channels: Some(fmt_chunk.channels),
            sample_format: Some(fmt_chunk.format),
            bit_depth: Some(fmt_chunk.bits_per_sample),
            duration: Some(duration),
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
#[repr(C)]
pub struct FmtChunk {
    pub size: i32,
    pub format: u16,
    pub channels: u16,
    pub sample_rate: i32,
    pub byte_rate: i32,
    pub block_align: u16,
    pub bits_per_sample: u16,
}

impl FmtChunk {
    pub fn new(
        size: i32,            // 4
        format: u16,          // 2
        channels: u16,        // 2
        sample_rate: i32,     // 4
        byte_rate: i32,       // 4
        block_align: u16,     // 2
        bits_per_sample: u16, //2
    ) -> FmtChunk {
        FmtChunk {
            size,
            format,
            channels,
            sample_rate,
            byte_rate,
            block_align,
            bits_per_sample,
        }
    }

    #[inline(always)]
    pub fn from_path(signal_fp: &Path) -> Result<FmtChunk, std::io::Error> {
        let wav_file = File::open(signal_fp)?;
        let mut br = BufReader::new(wav_file);
        FmtChunk::from_buf_reader(&mut br)
    }

    #[inline(always)]
    pub fn from_buf_reader(br: &mut BufReader<File>) -> Result<FmtChunk, std::io::Error> {
        let mut buf: [u8; 4] = [0; 4];
        let mut buf_two: [u8; 2] = [0; 2];
        let (offset, _) = find_sub_chunk_id(br, b"fmt ")?;
        br.seek(SeekFrom::Start(offset as u64))?;
        br.read_exact(&mut buf)?;
        let size = i32::from_le_bytes(buf);

        br.read_exact(&mut buf_two)?;
        let format = u16::from_le_bytes(buf_two);

        br.read_exact(&mut buf_two)?;
        let channels = u16::from_le_bytes(buf_two);

        br.read_exact(&mut buf)?;
        let sample_rate = i32::from_le_bytes(buf);

        br.read_exact(&mut buf)?;
        let byte_rate = i32::from_le_bytes(buf);

        br.read_exact(&mut buf_two)?;
        let block_align = u16::from_le_bytes(buf_two);

        br.read_exact(&mut buf_two)?;
        let bits_per_sample = u16::from_le_bytes(buf_two);
        br.seek(SeekFrom::Start(0))?;
        Ok(FmtChunk::new(
            size,
            format,
            channels,
            sample_rate,
            byte_rate,
            block_align,
            bits_per_sample,
        ))
    }

    #[inline(always)]
    pub fn as_bytes(&self) -> [u8; 24] {
        let mut buf: [u8; 24] = [0; 24];
        buf[0..4].copy_from_slice(b"fmt ");
        buf[4..8].copy_from_slice(&self.size.to_le_bytes());
        buf[8..10].copy_from_slice(&self.format.to_le_bytes());
        buf[10..12].copy_from_slice(&self.channels.to_le_bytes());
        buf[12..16].copy_from_slice(&self.sample_rate.to_le_bytes());
        buf[16..20].copy_from_slice(&self.byte_rate.to_le_bytes());
        buf[20..22].copy_from_slice(&self.block_align.to_le_bytes());
        buf[22..24].copy_from_slice(&self.bits_per_sample.to_le_bytes());
        buf
    }

    // Helper functions to avoid having to use the fmt struct field directly

    #[inline(always)]
    pub fn get_sample_size(&self) -> usize {
        self.bits_per_sample as usize / 8
    }

    #[inline(always)]
    pub fn format(&self) -> u16 {
        self.format
    }

    #[inline(always)]
    pub fn format_mut(&mut self) -> &mut u16 {
        &mut self.format
    }

    #[inline(always)]
    pub fn channels(&self) -> u16 {
        self.channels
    }

    #[inline(always)]
    pub fn channels_mut(&mut self) -> &mut u16 {
        &mut self.channels
    }

    #[inline(always)]
    pub fn sample_rate(&self) -> i32 {
        self.sample_rate
    }

    #[inline(always)]
    pub fn sample_rate_mut(&mut self) -> &mut i32 {
        &mut self.sample_rate
    }

    #[inline(always)]
    pub fn byte_rate(&self) -> i32 {
        self.byte_rate
    }

    #[inline(always)]
    pub fn byte_rate_mut(&mut self) -> &mut i32 {
        &mut self.byte_rate
    }

    #[inline(always)]
    pub fn block_align(&self) -> u16 {
        self.block_align
    }

    #[inline(always)]
    pub fn block_align_mut(&mut self) -> &mut u16 {
        &mut self.block_align
    }

    #[inline(always)]
    pub fn bits_per_sample(&self) -> u16 {
        self.bits_per_sample
    }

    #[inline(always)]
    pub fn bits_per_sample_mut(&mut self) -> &mut u16 {
        &mut self.bits_per_sample
    }
}

pub fn read_signal_info(signal_fp: &Path) -> Result<(FmtChunk, u64), std::io::Error> {
    let wav_file = File::open(signal_fp)?;
    let mut br = BufReader::new(wav_file);
    let fmt_chunk = FmtChunk::from_buf_reader(&mut br)?;

    let (data_offset, _) = find_sub_chunk_id(&mut br, &b"data")?;
    let mut data_size_buf: [u8; 4] = [0; 4];
    br.seek(SeekFrom::Start(data_offset as u64))?;
    br.read_exact(&mut data_size_buf)?;

    Ok((
        fmt_chunk,
        i32::from_le_bytes(data_size_buf) as u64
            / (fmt_chunk.sample_rate()
                * fmt_chunk.channels() as i32
                * (fmt_chunk.bits_per_sample() / 8) as i32) as u64,
    ))
}
