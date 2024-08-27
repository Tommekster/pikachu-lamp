from typing_extensions import Buffer
from dataclasses import dataclass
import struct


class DataStruct:
    _FORMAT: str

    def __init_subclass__(cls, format: str) -> None:
        cls._FORMAT = format

    @classmethod
    def unpack(cls, buffer: Buffer, offset: int = 0):
        return cls(*struct.unpack_from(cls._FORMAT, buffer, offset))


@dataclass
class ChunkHeader(DataStruct, format="<4sI"):
    chunk_id: bytes
    size: int


@dataclass
class DescriptorHeader(ChunkHeader, format="<4sI4s"):
    format: bytes


@dataclass
class FormatHeader(ChunkHeader, format="<4sIHHIIHH"):
    audio_format: int
    num_channels: int
    sample_rate: int
    byte_rate: int
    block_align: int
    bits_per_sample: int


class DataChunk(ChunkHeader, format="<4sI"):
    data: bytes = b""

    @classmethod
    def unpack(cls, buffer: Buffer, offset: int = 0):
        buff = bytes(buffer)[offset:]
        data = super().unpack(buff)
        data.data = buff[8:8+data.size]
        return data

    def pack(self):
        return struct.pack(self._FORMAT, self.chunk_id, self.size) + self.data


@dataclass
class WavFile:
    """\
http://soundfile.sapp.org/doc/WaveFormat/
    """
    descriptor: DescriptorHeader
    format: FormatHeader
    data: DataChunk
    chunks: list[DataChunk]

    @classmethod
    def parse(cls, wav: bytes):
        descriptor = DescriptorHeader.unpack(wav)
        assert descriptor.chunk_id == b"RIFF", "Only RIFF is supported"
        assert descriptor.format == b"WAVE", "Only WAVE is supported"
        chunks = list(cls.__read_chunks__(wav[12:][:descriptor.size]))
        format = next((x for x in chunks if x.chunk_id == b"fmt "), None)
        assert format, "\"fmt \" chunk is missing"
        data = next((x for x in chunks if x.chunk_id == b"data"), None)
        assert data, "\"data\" chunk is missing"
        return cls(descriptor, FormatHeader.unpack(format.pack()), data, chunks)

    @classmethod
    def __read_chunks__(cls, wav: bytes):
        while len(wav) > 8:
            chunk = DataChunk.unpack(wav)
            yield chunk
            wav = wav[8+chunk.size:]
