# Wav2progmem

Converts WAV files to C header files. It is inteded for uploading sound into an Arduino with PCM library.

Supported WAV encoding is
- mono 8bps PCM


## Usage

```
> wav2progmem --help

Usage: wav2progmem [OPTIONS] INPUT_FOLDER OUTPUT_FOLDER

  Converts WAV files to C header files

      INPUT_FOLDER    Input folder with *.WAV files (mono 8bps PCM)

      OUTPUT_FOLDER   Output folder for C header files with PROGMEM uint8[]



Options:
  --help  Show this message and exit.

```

### Python

```
from pathlib import Path
from wav2progmem import wav2progmem, WavFile


def convert_files(input_folder: Path, output_folder: Path):
    for f in input_folder.glob("*.wav"):
        wav = WavFile.parse(f.read_bytes())
        header_file = Path(output_folder, f.with_suffix(".h").name)
        header_file.write_text(wav2progmem(wav, f))

```

## Installation

```
poetry install
```

## References

- [Wave Format](http://soundfile.sapp.org/doc/WaveFormat/)
- [PCM Arduino library](https://www.arduino.cc/reference/en/libraries/pcm/)