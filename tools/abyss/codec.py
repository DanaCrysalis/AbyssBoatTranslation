"""Text codec: game bytes <-> tagged text, and English -> the game's full-width encoding.

The game draws every character from a Shift-JIS bitmap font (GPARTS.PAK MINCHO*.FNT,
double-byte glyphs only) and advances two bytes per character, so ALL displayed text
must be double-byte.  Translators write ordinary ASCII English; encode_target() maps it
to full-width Shift-JIS (A -> Ａ, space -> ideographic space, ' -> ’ ...).  One
character = one column = two bytes.

Tags (script and scene stores; the byte values are the renderer's control codes):
  {p}        0x01  wait for a click, then clear the box
  {w}        0x02  wait for a click, keep the box
  {br}       0x03  line break
  {name}     0x04  the player's name (John)
  {pause:N}  0x06 N  timed pause
  {num:N}    0x07 N  insert numeric variable N
System store (strings inside AbyssBoat.exe): {br} is the byte '\\' the menu renderer
treats as a line break; printf directives (%s, %d, %6d ...) are kept verbatim.

Glyph substitutions in this font: 0x8189 (♂ in Shift-JIS) is drawn as "!!" and
0x818A (♀) as "!?".  Dumps show them as ‼ and ⁉; translators may use ‼ and ⁉ too.
"""
import re

LEADS = set(range(0x81, 0xA0)) | set(range(0xE0, 0xEB))   # lead bytes with glyphs in the font

CTRL_TAG = {0x01: '{p}', 0x02: '{w}', 0x03: '{br}', 0x04: '{name}'}
TAG_CTRL = {v: k for k, v in CTRL_TAG.items()}
ARG_TAG = {0x06: 'pause', 0x07: 'num'}
TAG_ARG = {v: k for k, v in ARG_TAG.items()}

TAG_RE = re.compile(r'\{(p|w|br|name|pause:\d+|num:\d+)\}')
PRINTF_RE = re.compile(r'%[-+ 0#]*\d*(?:\.\d+)?[sdiuxXcf%]')

GLYPH_SUB = {'♂': '‼', '♀': '⁉'}           # how the font draws them
GLYPH_SUB_REV = {v: k for k, v in GLYPH_SUB.items()}

# ASCII -> full-width.  ' and " are handled contextually (curly quotes).
FW = {' ': '　', '-': '－', '~': '～', '`': '‘'}
for c in range(0x21, 0x7F):
    ch = chr(c)
    if ch not in FW and ch not in '\'"{}':
        FW[ch] = chr(0xFF00 + c - 0x20)
EXTRA_MAP = {'—': '―', '–': '－', '‐': '－', '‼': '♂', '⁉': '♀'}

NAME_TEXT = 'John'          # what {name} prints (exe string patched by BUILD)
NAME_COLS = len(NAME_TEXT)
NUM_COLS = 5                # widest value a {num:N} insert can print


class EncodeError(ValueError):
    pass


# ---------------------------------------------------------------- source side

def decode_game(b, store='script'):
    """Game bytes -> tagged text.  Lossless: encode_source(decode_game(b)) == b."""
    out = []
    i = 0
    while i < len(b):
        x = b[i]
        if store != 'system' and x in CTRL_TAG:
            out.append(CTRL_TAG[x])
            i += 1
        elif store != 'system' and x in ARG_TAG:
            out.append('{%s:%d}' % (ARG_TAG[x], b[i + 1]))
            i += 2
        elif 0x81 <= x <= 0x9F or 0xE0 <= x <= 0xFC:
            ch = b[i:i + 2].decode('cp932')
            out.append(GLYPH_SUB.get(ch, ch))
            i += 2
        elif store == 'system' and x == 0x5C:
            out.append('{br}')
            i += 1
        elif 0x20 <= x < 0x7F and chr(x) not in '{}':
            out.append(chr(x))
            i += 1
        else:
            out.append('{x%02X}' % x)
            i += 1
    return ''.join(out)


def encode_source(s, store='script'):
    """Inverse of decode_game (used by REFRESH to prove the dumps are lossless)."""
    out = bytearray()
    for kind, val in tokens(s):
        if kind == 'tag':
            out += tag_bytes(val, store)
        elif kind == 'raw':
            out.append(val)
        else:
            ch = GLYPH_SUB_REV.get(val, val)
            out += ch.encode('cp932')
    return bytes(out)


def tokens(s):
    """Yield ('tag', '{br}') / ('raw', byte) / ('ch', char) for a tagged string."""
    i = 0
    while i < len(s):
        if s[i] == '{':
            m = TAG_RE.match(s, i)
            if m:
                yield 'tag', m.group(0)
                i = m.end()
                continue
            m = re.match(r'\{x([0-9A-F]{2})\}', s[i:])
            if m:
                yield 'raw', int(m.group(1), 16)
                i += m.end()
                continue
            raise EncodeError('unknown tag at %r' % s[i:i + 12])
        if s[i] == '}':
            raise EncodeError('stray } in %r' % s)
        yield 'ch', s[i]
        i += 1


def tag_bytes(tag, store):
    if store == 'system':
        if tag == '{br}':
            return b'\\'
        raise EncodeError('tag %s not allowed in the system store' % tag)
    if tag in TAG_CTRL:
        return bytes([TAG_CTRL[tag]])
    name, n = tag[1:-1].split(':')
    n = int(n)
    if not 0 < n < 256:
        raise EncodeError('argument out of range in %s' % tag)
    return bytes([TAG_ARG[name], n])


# ---------------------------------------------------------------- target side

def fullwidth_char(ch, prev, nxt):
    """One target character -> its full-width Shift-JIS bytes, or EncodeError."""
    if ch == "'":
        ch = '‘' if (prev in ('', ' ', '"', '(', '{') and nxt.isalnum()) else '’'
    elif ch == '"':
        ch = '“' if prev in ('', ' ', '(', '　', '{', '}') else '”'
    elif ch in FW:
        ch = FW[ch]
    else:
        ch = EXTRA_MAP.get(ch, ch)
    try:
        b = ch.encode('cp932')
    except UnicodeEncodeError:
        raise EncodeError('character %r (U+%04X) has no glyph' % (ch, ord(ch)))
    if len(b) != 2 or b[0] not in LEADS:
        raise EncodeError('character %r has no glyph in the game font' % ch)
    return b


def encode_target(s, store='script', ascii_ok=False):
    """Translator text -> game bytes.  ascii_ok: plain ASCII (system MessageBox strings)."""
    if ascii_ok:
        try:
            b = s.encode('ascii')
        except UnicodeEncodeError as e:
            raise EncodeError('non-ASCII character %r in an ASCII-only string' % s[e.start])
        if b'{' in b or b'}' in b:
            raise EncodeError('tags are not allowed in an ASCII-only string')
        return b
    toks = list(tokens(s))
    out = bytearray()
    for k, (kind, val) in enumerate(toks):
        if kind == 'tag':
            out += tag_bytes(val, store)
        elif kind == 'raw':
            raise EncodeError('raw byte tags are not allowed in a translation')
        else:
            prev = toks[k - 1][1] if k and toks[k - 1][0] == 'ch' else ('{' if k else '')
            nxt = toks[k + 1][1] if k + 1 < len(toks) and toks[k + 1][0] == 'ch' else ''
            if store == 'system' and val == '%':
                pass
            out += fullwidth_char(val, prev, nxt)
    return bytes(out)


def char_count(s):
    """Characters in a tagged string, tags excluded."""
    return sum(1 for k, _ in tokens(s) if k != 'tag')


def cols_of(tag_or_char):
    if tag_or_char == '{name}':
        return NAME_COLS
    if tag_or_char.startswith('{num:'):
        return NUM_COLS
    if tag_or_char.startswith('{'):
        return 0
    return 1


def check_target_chars(s, store='script', ascii_ok=False):
    """Return a list of problems (empty if the text encodes)."""
    try:
        encode_target(s, store, ascii_ok)
        return []
    except EncodeError as e:
        return [str(e)]


# ---------------------------------------------------------------- layout

BREAKS = ('{br}',)
PAGE_ENDS = ('{p}', '{w}')


def wrap(s, width, start_col=0):
    """Word-wrap a target string: insert {br} at spaces so no line exceeds `width`
    columns.  Existing tags are kept; a space at a wrap point is consumed.
    start_col: column the text starts at (a message continuing a line).
    Returns (wrapped_text, list_of_words_longer_than_width)."""
    out = []
    col = start_col
    too_long = []
    # split into words while keeping tags as their own items
    items = []
    for kind, val in tokens(s):
        items.append(val if kind != 'raw' else '{x%02X}' % val)
    words = []      # list of lists of items; ' ' items separate words
    cur = []
    for it in items:
        if it == ' ':
            words.append(cur)
            words.append([' '])
            cur = []
        elif it in BREAKS or it in PAGE_ENDS:
            words.append(cur)
            words.append([it])
            cur = []
        else:
            cur.append(it)
    words.append(cur)
    pending_space = False
    for w in words:
        if not w:
            continue
        if w == [' ']:
            pending_space = True
            continue
        if len(w) == 1 and (w[0] in BREAKS or w[0] in PAGE_ENDS):
            out.append(w[0])
            col = 0
            pending_space = False
            continue
        wcols = sum(cols_of(x) for x in w)
        if wcols > width:
            too_long.append(''.join(w))
        need = wcols + (1 if pending_space and col else 0)
        if col and col + need > width:
            out.append('{br}')
            col = 0
            pending_space = False
        if pending_space and col:
            out.append(' ')
            col += 1
        pending_space = False
        out.extend(w)
        col += wcols
    if pending_space:
        out.append(' ')
    return ''.join(out), too_long


def lines_of(s):
    """Split wrapped text into pages of lines: [[line, ...], ...] where each line is
    its column count.  A page ends at {p} or {w}."""
    pages = [[0]]
    for kind, val in tokens(s):
        if kind == 'tag':
            if val == '{br}':
                pages[-1].append(0)
            elif val in PAGE_ENDS:
                pages.append([0])
            else:
                pages[-1][-1] += cols_of(val)
        elif kind == 'ch':
            pages[-1][-1] += 1
    return pages
