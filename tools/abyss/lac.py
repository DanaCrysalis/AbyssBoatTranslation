"""LAC archives (the game's *.PAK files).

Layout: b"LAC\\0", u32 count, then count x 36-byte entries:
  name[27] (each byte bitwise-inverted, NUL-padded), u8 compressed, u32 size, u32 offset
followed by the data.  A compressed entry is u32 unpacked_size + LZSS (4 KiB ring,
initial position 0xFEE, flag byte LSB-first, 1 = literal, match = 12-bit position +
4-bit length+3).  The game also reads uncompressed entries (flag 0), so BUILD writes
replaced files uncompressed.
"""
import struct

MAGIC = b'LAC\0'
ENTRY = 36


def lzss_decompress(src, outlen):
    ring = bytearray(4096)
    r = 0xFEE
    out = bytearray()
    i = 0
    flags = 0
    while len(out) < outlen and i < len(src):
        flags >>= 1
        if not flags & 0x100:
            flags = src[i] | 0xFF00
            i += 1
        if flags & 1:
            c = src[i]
            i += 1
            out.append(c)
            ring[r] = c
            r = (r + 1) & 0xFFF
        else:
            b1, b2 = src[i], src[i + 1]
            i += 2
            p = b1 | ((b2 & 0xF0) << 4)
            for k in range((b2 & 0x0F) + 3):
                c = ring[(p + k) & 0xFFF]
                out.append(c)
                ring[r] = c
                r = (r + 1) & 0xFFF
    return bytes(out)


def _name_decode(raw):
    return bytes((~b) & 0xFF for b in raw if b).decode('cp932')


def _name_encode(name):
    b = name.encode('cp932')
    if len(b) > 27:
        raise ValueError('name too long for LAC: %s' % name)
    return bytes((~c) & 0xFF for c in b).ljust(27, b'\0')


def read(path):
    """Return a list of (name, data) with data decompressed, in archive order."""
    d = open(path, 'rb').read()
    if d[:4] != MAGIC:
        raise ValueError('%s is not a LAC archive' % path)
    n = struct.unpack_from('<I', d, 4)[0]
    out = []
    for k in range(n):
        e = d[8 + k * ENTRY:8 + (k + 1) * ENTRY]
        name = _name_decode(e[:27])
        comp = e[27]
        size, off = struct.unpack_from('<II', e, 28)
        blob = d[off:off + size]
        if comp:
            ulen = struct.unpack_from('<I', blob, 0)[0]
            blob = lzss_decompress(blob[4:], ulen)
            if len(blob) != ulen:
                raise ValueError('%s: short LZSS stream' % name)
        out.append((name, blob))
    return out


def read_raw(path):
    """Return a list of (name, compressed_flag, stored_bytes) without decompressing."""
    d = open(path, 'rb').read()
    n = struct.unpack_from('<I', d, 4)[0]
    out = []
    for k in range(n):
        e = d[8 + k * ENTRY:8 + (k + 1) * ENTRY]
        size, off = struct.unpack_from('<II', e, 28)
        out.append((_name_decode(e[:27]), e[27], d[off:off + size]))
    return out


def write(path, entries):
    """entries: list of (name, compressed_flag, stored_bytes) -- stored as given."""
    head = bytearray(MAGIC + struct.pack('<I', len(entries)))
    off = 8 + ENTRY * len(entries)
    body = bytearray()
    for name, comp, blob in entries:
        head += _name_encode(name) + bytes([comp]) + struct.pack('<II', len(blob), off + len(body))
        body += blob
    with open(path, 'wb') as f:
        f.write(head + body)
