use std::{
    fs::File,
    io::{BufReader, Read, Seek, SeekFrom},
    path::Path,
};

use crate::core::VerificationConfig;

pub fn read_config(verification_config_path: &Path) -> Result<VerificationConfig, std::io::Error> {
    let fp = match File::open(verification_config_path) {
        Ok(fp) => fp,
        Err(e) => {
            return Err(e);
        }
    };
    let config = match serde_yaml::from_reader(&fp) {
        Ok(rdr) => rdr,
        Err(e) => {
            return Err(std::io::Error::new(std::io::ErrorKind::Other, e));
        }
    };

    Ok(config)
}

#[inline(always)]
pub fn find_sub_chunk_id(
    file: &mut BufReader<File>,
    chunk_id: &[u8; 4],
) -> Result<(usize, usize), std::io::Error> {
    let mut buf: [u8; 4] = [0; 4];
    // Find the RIFF Tag
    file.read_exact(&mut buf)?;
    if !buf_eq(&buf, b"RIFF") {
        return Err(std::io::Error::new(
            std::io::ErrorKind::Other,
            format!("Failed to find RIFF tag in {:?}", file.get_ref()),
        ));
    }

    file.seek(SeekFrom::Current(8))?;
    let mut tag_offset: usize = 0;
    let mut bytes_traversed: usize = 12;
    loop {
        // First sub-chunk is guaranteed to begin at byte 12 so seek forward by 8.
        // No other chunk is at a guaranteed offset.
        let bytes_read = file.read(&mut buf)?;
        if bytes_read == 0 {
            break;
        }

        bytes_traversed += bytes_read;

        if buf_eq(&buf, chunk_id) {
            tag_offset = bytes_traversed;
        }

        let bytes_read = file.read(&mut buf)?;
        if bytes_read == 0 {
            break;
        }
        bytes_traversed += bytes_read;

        let chunk_len =
            buf[0] as u32 | (buf[1] as u32) << 8 | (buf[2] as u32) << 16 | (buf[3] as u32) << 24;
        if tag_offset > 0 {
            let chunk_size = chunk_len as usize;
            file.seek(SeekFrom::Start(0))?; // Reset the file offset to the beginning
            return Ok((tag_offset, chunk_size));
        }
        file.seek(SeekFrom::Current(chunk_len as i64))?;

        bytes_traversed += chunk_len as usize;
    }
    file.seek(SeekFrom::Start(0))?;

    Err(std::io::Error::new(
        std::io::ErrorKind::Other,
        format!(
            "Failed to find {:?} tag in {:?}",
            std::str::from_utf8(chunk_id).unwrap(),
            file.get_ref()
        ),
    ))
}

#[inline(always)]
fn buf_eq(buf: &[u8; 4], chunk_id: &[u8; 4]) -> bool {
    buf[0] == chunk_id[0] && buf[1] == chunk_id[1] && buf[2] == chunk_id[2] && buf[3] == chunk_id[3]
}

mod io_test {

    #[test]
    fn read_config_test() {
        let path = std::path::Path::new("config.yaml");
        let config = super::read_config(&path).unwrap();
        assert_eq!(config.sample_rate, Some(16000));
        assert_eq!(config.channels, Some(1));
        assert_eq!(config.sample_format, None);
        assert_eq!(config.bit_depth, Some(16));
        assert_eq!(config.duration, Some(10));
    }
}
