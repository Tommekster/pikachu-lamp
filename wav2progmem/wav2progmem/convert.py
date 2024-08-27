from typing import Iterable
from pathlib import Path
import re
from .wav_file import WavFile


def wav2progmem(wav: WavFile, file: Path):
    assert wav.format.bits_per_sample == 8, "Only 8bits per sample is suppoted"
    assert wav.format.audio_format == 1, "Only PCM encoding is supported"
    assert wav.format.sample_rate == 8000, "Only 8kHz sample rate is supported"
    assert wav.format.num_channels == 1, "Only 1 channel is supported"

    var_name = re.sub(r"[^\w\d]", "_", file.name).upper()
    content = "\n    ".join(
        ", ".join(f"0x{x:02x}" for x in y)
        for y in chunks(wav.data.data, 12)
    )

    return f"""
const unsigned char {var_name} PROGMEM = {{
    {content}
}}
"""


def chunks(lst: bytes, n: int) -> Iterable[bytes]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
