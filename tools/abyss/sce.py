"""Cutscene files (SCRIPT.PAK *.SCE): subtitle extraction and rebuild.

Layout (packed, little-endian):
  u16 last_frame, f32 fps, char camera[28]
  u16 n_models, n_models x char name[28]
  u16 n_clips,  n_clips  x (char name[28], u16 start, u16 end, f32 fps)
  u16 n_subs,   n_subs   x (Shift-JIS text, NUL, u16 start_frame, u16 end_frame,
                            u8 flag, [u16, u16 when flag != 0])
  tail (sound/event tables) kept verbatim.
Nothing in the file points into the subtitle block, so subtitles may change length.
"""
import struct


def parse(data):
    p = 6 + 28
    nm = struct.unpack_from('<H', data, p)[0]
    p += 2 + nm * 28
    nc = struct.unpack_from('<H', data, p)[0]
    p += 2 + nc * 36
    head_end = p
    ns = struct.unpack_from('<H', data, p)[0]
    p += 2
    subs = []
    for _ in range(ns):
        e = data.index(b'\0', p)
        text = data[p:e]
        start, end, flag = struct.unpack_from('<HHB', data, e + 1)
        q = e + 6
        extra = b''
        if flag:
            extra = data[q:q + 4]
            q += 4
        subs.append(dict(text=text, start=start, end=end, flag=flag, extra=extra))
        p = q
    return dict(head=data[:head_end], subs=subs, tail=data[p:])


def rebuild(data, texts):
    """texts: list of new text bytes, one per subtitle."""
    f = parse(data)
    if len(texts) != len(f['subs']):
        raise ValueError('subtitle count mismatch')
    out = bytearray(f['head'])
    out += struct.pack('<H', len(texts))
    for sub, t in zip(f['subs'], texts):
        if b'\0' in t:
            raise ValueError('NUL in subtitle')
        out += t + b'\0' + struct.pack('<HHB', sub['start'], sub['end'], sub['flag']) + sub['extra']
    out += f['tail']
    return bytes(out)
