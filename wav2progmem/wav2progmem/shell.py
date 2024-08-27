from pathlib import Path
import click

from .convert import wav2progmem
from .wav_file import WavFile


@click.command()
@click.argument("input_folder", type=Path)
@click.argument("output_folder", type=Path)
def convert_files(input_folder: Path, output_folder: Path):
    """
Converts WAV files to C header files

    INPUT_FOLDER    Input folder with *.WAV files (mono 8bps PCM)

    OUTPUT_FOLDER   Output folder for C header files with PROGMEM uint8[]

    """
    for f in input_folder.glob("*.wav"):
        wav = WavFile.parse(f.read_bytes())
        header_file = Path(output_folder, f.with_suffix(".h").name)
        header_file.write_text(wav2progmem(wav, f))
