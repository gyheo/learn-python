"""Data Compression.

@see: https://docs.python.org/3/tutorial/stdlib.html#data-compression

Common data archiving and compression formats are directly supported by modules including: zlib,
gzip, bz2, lzma, zipfile and tarfile.
"""

import zlib


def test_zlib():
    """zlib."""
    string = b'witch which has which witches wrist watch'
    string2 = b'hello'
    assert len(string) == 41
    assert len(string2) == 5

    zlib_compressed_string = zlib.compress(string)
    zlib_compressed_string2 = zlib.compress(string2)
    assert len(zlib_compressed_string) == 37
    assert len(zlib_compressed_string2) == 13

    zlib_decompressed_string = zlib.decompress(zlib_compressed_string)
    zlib_decompressed_string2 = zlib.decompress(zlib_compressed_string2)

    assert zlib_decompressed_string == b'witch which has which witches wrist watch'
    assert zlib_decompressed_string2 == b'hello'

    assert zlib.crc32(string) == 226805979
    assert zlib.crc32(string2) == 907060870
