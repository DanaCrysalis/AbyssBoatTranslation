"""UI strings inside AbyssBoat.exe (the "system" store).

Two renderers:
  fw    -- menus, room names, item text, hints: drawn from the bitmap font, two bytes
           per character (helper 0x4079F0; '\\' is a line break).  Full-width only.
  ascii -- error dialogs, window title: Windows ANSI APIs.  Plain ASCII.
Tables are arrays with a fixed stride (the code indexes them by multiplication), so a
string can never exceed its slot.  Standalone strings get the bytes up to the next
string, capped at their original 4-aligned length.
"""
import struct

IMAGE_BASE = 0x400000

# name, first VA, stride, count, renderer, note
TABLES = [
    ('options', 0x45D258, 90, 6, 'fw', 'option screen help line'),
    ('equip', 0x45D478, 80, 4, 'fw', 'message shown when equipping a weapon'),
    ('rooms', 0x45D5B8, 30, 120, 'fw', 'room name on the map; 6 decks x 20 slots'),
    ('camp', 0x45E3C8, 55, 6, 'fw', 'camp (pause) menu help line'),
    ('items', 0x45E518, 88, 15, 'fw', 'item name in 【】 then description; {br} = new line'),
    ('hints', 0x45EA78, 80, 17, 'fw', 'objective hint'),
    ('decks', 0x45EFC8, 22, 6, 'fw', 'deck name on the map'),
]
# VA, renderer, note
SINGLES = [
    (0x45F174, 'ascii', 'error: save data version'),
    (0x45F1FF, 'ascii', 'question: recreate the save file'),
    (0x45F24C, 'ascii', 'error: save data version'),
    (0x45F26C, 'ascii', 'error: no save data'),
    (0x45F758, 'ascii', 'error: room data version'),
    (0x45F78C, 'ascii', 'error: search table'),
    (0x45F7A8, 'ascii', 'error dialog title'),
    (0x45F884, 'ascii', 'error: %s.PAK not found, cannot start'),
    (0x45FDE2, 'ascii', 'error: file not found'),
    (0x460558, 'ascii', 'question: window mode needs 16-bit colour; go full screen?'),
    (0x4605CC, 'ascii', 'dialog title'),
    (0x4605DC, 'ascii', 'window title'),
    (0x460730, 'ascii', 'error: DirectX 8 required'),
    (0x46076C, 'ascii', 'dialog title (warning)'),
]

# the player's name: 20-byte buffer, and the default copied into it at 0x42A487
NAME_BUFFER = (0x45FCAC, 20)
NAME_DEFAULT_PUSH = 0x42A487          # operand of `push 0x45FE04`
NAME_DEFAULT_VA = 0x45FE04


class PE:
    def __init__(self, data):
        self.data = bytearray(data)
        pe = struct.unpack_from('<I', data, 0x3C)[0]
        nsec = struct.unpack_from('<H', data, pe + 6)[0]
        opt = struct.unpack_from('<H', data, pe + 20)[0]
        self.sections = []
        for k in range(nsec):
            o = pe + 24 + opt + 40 * k
            name = data[o:o + 8].rstrip(b'\0')
            vsize, va, rsize, roff = struct.unpack_from('<IIII', data, o + 8)
            self.sections.append(dict(name=name, va=IMAGE_BASE + va, vsize=vsize,
                                      rsize=rsize, roff=roff, hdr=o))

    def off(self, va):
        for s in self.sections:
            if s['va'] <= va < s['va'] + max(s['vsize'], s['rsize']):
                return s['roff'] + va - s['va']
        raise ValueError('VA %#x not in the file' % va)

    def cstr(self, va):
        o = self.off(va)
        return bytes(self.data[o:self.data.index(b'\0', o)])


def single_slot(pe, va):
    o = pe.off(va)
    end = pe.data.index(b'\0', o)
    cap = (end - o + 1 + 3) & ~3
    e = end
    while e - o < cap and pe.data[e] == 0:
        e += 1
    return min(e - o, cap)


def entries(exe_bytes):
    """-> list of dict(id, va, slot, renderer, note, text) for every translatable string."""
    pe = PE(exe_bytes)
    out = []
    for name, base, stride, count, rend, note in TABLES:
        for k in range(count):
            va = base + k * stride
            t = pe.cstr(va)
            if t:
                out.append(dict(id='%s/%03d' % (name, k), va=va, slot=stride, renderer=rend,
                                note=note, text=t))
    for va, rend, note in SINGLES:
        out.append(dict(id='misc/%06X' % va, va=va, slot=single_slot(pe, va), renderer=rend,
                        note=note, text=pe.cstr(va)))
    return out


def patch(exe_bytes, new_texts, name_bytes):
    """new_texts: dict id -> bytes (already encoded).  name_bytes: the player's name.
    Returns patched exe bytes; raises on any overflow."""
    pe = PE(exe_bytes)
    slots = {e['id']: e for e in entries(exe_bytes)}
    for k, b in new_texts.items():
        e = slots[k]
        if len(b) + 1 > e['slot']:
            raise ValueError('%s: %d bytes, slot holds %d' % (k, len(b), e['slot'] - 1))
        o = pe.off(e['va'])
        pe.data[o:o + e['slot']] = (b + b'\0').ljust(e['slot'], b'\0')
    # player name: the buffer, then a new default in .rdata slack
    va, size = NAME_BUFFER
    if len(name_bytes) + 1 > size:
        raise ValueError('player name too long')
    o = pe.off(va)
    pe.data[o:o + size] = (name_bytes + b'\0').ljust(size, b'\0')
    rd = [s for s in pe.sections if s['name'] == b'.rdata'][0]
    new_va = rd['va'] + ((rd['vsize'] + 15) & ~15)
    if new_va + len(name_bytes) + 1 > rd['va'] + rd['rsize']:
        raise ValueError('no room in .rdata for the default name')
    o = pe.off(new_va)
    if any(pe.data[o:o + len(name_bytes) + 1]):
        raise ValueError('.rdata slack is not empty')
    pe.data[o:o + len(name_bytes) + 1] = name_bytes + b'\0'
    po = pe.off(NAME_DEFAULT_PUSH)
    if struct.unpack_from('<I', pe.data, po)[0] != NAME_DEFAULT_VA:
        raise ValueError('unexpected code at the default-name push')
    struct.pack_into('<I', pe.data, po, new_va)
    struct.pack_into('<I', pe.data, rd['hdr'] + 8, rd['rsize'])     # map the slack
    return bytes(pe.data)
