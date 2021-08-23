"""Recognize image file formats based on their first few bytes."""

from os import PathLike

__all__ = ["what"]


# ------------------------- #
# Recognize image headers   #
# ------------------------- #

def what(h: bytes):

    h = h[:32]
    for tf in tests:
        res = tf(h)
        if res:
            return res


# ---------------------------------#
# Subroutines per image file type #
# ---------------------------------#

tests = []


def test_jpeg(h):
    """JPEG data in JFIF or Exif format"""
    if h[6:10] in (b'JFIF', b'Exif'):
        return 'jpeg'


tests.append(test_jpeg)


def test_png(h):
    if h.startswith(b'\211PNG\r\n\032\n'):
        return 'png'


tests.append(test_png)


def test_gif(h):
    """GIF ('87 and '89 variants)"""
    if h[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif'


tests.append(test_gif)


def test_tiff(h):
    """TIFF (can be in Motorola or Intel byte order)"""
    if h[:2] in (b'MM', b'II'):
        return 'tiff'


tests.append(test_tiff)


def test_rgb(h):
    """SGI image library"""
    if h.startswith(b'\001\332'):
        return 'rgb'


tests.append(test_rgb)


def test_pbm(h):
    """PBM (portable bitmap)"""
    if len(h) >= 3 and \
            h[0] == ord(b'P') and h[1] in b'14' and h[2] in b' \t\n\r':
        return 'pbm'


tests.append(test_pbm)


def test_pgm(h):
    """PGM (portable graymap)"""
    if len(h) >= 3 and \
            h[0] == ord(b'P') and h[1] in b'25' and h[2] in b' \t\n\r':
        return 'pgm'


tests.append(test_pgm)


def test_ppm(h):
    """PPM (portable pixmap)"""
    if len(h) >= 3 and \
            h[0] == ord(b'P') and h[1] in b'36' and h[2] in b' \t\n\r':
        return 'ppm'


tests.append(test_ppm)


def test_rast(h):
    """Sun raster file"""
    if h.startswith(b'\x59\xA6\x6A\x95'):
        return 'rast'


tests.append(test_rast)


def test_xbm(h):
    """X bitmap (X10 or X11)"""
    if h.startswith(b'#define '):
        return 'xbm'


tests.append(test_xbm)


def test_bmp(h):
    if h.startswith(b'BM'):
        return 'bmp'


tests.append(test_bmp)


def test_webp(h):
    if h.startswith(b'RIFF') and h[8:12] == b'WEBP':
        return 'webp'


tests.append(test_webp)


def test_exr(h):
    if h.startswith(b'\x76\x2f\x31\x01'):
        return 'exr'


tests.append(test_exr)
