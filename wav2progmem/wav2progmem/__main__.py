from typing import NamedTuple
import struct
from pathlib import Path

class WavHeader(NamedTuple):
    ChunkID : bytes
    ChunkSize : int
    Format : bytes
    Subchunk1ID : bytes
    Subchunk1Size : int
    AudioFormat : int
    NumChannels : int
    SampleRate : int
    ByteRate : int
    BlockAlign : int
    BitsPerSample : int
    Subchunk2ID : bytes
    Subchunk2Size : int

def main():
    audio = Path("../pika_chu_sounds/pika.wav")
    with audio.open("rb") as f:
        data = f.read()
    print(len(data))
    # http://soundfile.sapp.org/doc/WaveFormat/
    wav_header = WavHeader(*struct.unpack("<4sI4s4sIHHIIHH4sI", data[:44]))
    print(wav_header)
    print(list(data[44:][:wav_header.Subchunk2Size]))

    # raw=wav_header.Subchunk2Size()

if __name__ == "__main__":
    main()