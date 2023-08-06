from typing import List
from .audio_verification import VerificationResult, verify

def verify_audio(config_fp: str, root_audio_dir: str, parallel: bool = True) -> List[VerificationResult]:
    return verify(config_fp, root_audio_dir, parallel)
