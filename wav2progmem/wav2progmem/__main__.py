from pathlib import Path
from .wav_file import WavFile
from .convert import wav2progmem


def main():
    audio = Path("../pika_chu_sounds/pika.wav")
    with audio.open("rb") as f:
        wav = WavFile.parse(f.read())

    print(wav2progmem(wav, audio))


if __name__ == "__main__":
    main()
