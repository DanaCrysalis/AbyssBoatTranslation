"""LAFSCR room scripts (SCRIPT.PAK *.SCR): parse, extract text, rebuild.

File layout (all offsets u16, so a script can never exceed 65,535 bytes):
  0x00 "LAFSCR\\0\\x01"   0x08 u32 file size   0x0C u32 0
  0x10 u8 0x44, u8 NCH (characters in the character table)
  0x12 TA  label table (u16 code offsets, one per jump label)
  0x14 TB  word-offset table (u16 offsets into the text section)
  0x16 TX  text section: NCH x 2-byte characters, then NUL-terminated words
  0x18 END end of text; data[END:] is an opaque tail kept verbatim
  0x20 .. TA  bytecode
Text lives in the bytecode as `91 <tokens> 00` (statement 0x91).  A token is one byte
1..250 or a page prefix FB..FF plus one byte; token n (1-based) indexes the list
[characters..., words...]: 1..250 single byte, FB y = 250+y, FC y = 500+y, FD y = 750+y,
FE y = 1000+y, FF y = 1250+y  (decoder: AbyssBoat.exe 0x41E960).  Choice options and a
few speech-bubble lines are inline strings in expressions (`EB <bytes> 00`).
The parser mirrors the interpreter (statements 0x42A543, expressions 0x401000) so that
every message, inline string, label and `E9 hi lo` string reference is found exactly.
"""
import struct
from collections import Counter

MAX_TOKENS = 1499
MAX_FILE = 0xFFFF

# expression-argument count per statement opcode (handlers at AbyssBoat.exe 0x42BE28)
NARGS = {
    0x83: 0, 0x88: 1, 0x89: 1, 0x97: 0, 0x9a: 2, 0x9d: 0, 0x9e: 1, 0x9f: 1,
    0xa0: 1, 0xa1: 0, 0xa2: 0, 0xa7: 0, 0xa8: 1, 0xa9: 5, 0xaa: 2, 0xab: 1,
    0xac: 1, 0xad: 0, 0xae: 1, 0xaf: 1, 0xb0: 0, 0xb5: 1, 0xb8: 2, 0xb9: 1,
    0xba: 0, 0xbf: 2, 0xc0: 0, 0xc1: 4, 0xc2: 4, 0xc4: 2, 0xc5: 0, 0xc6: 0,
    0xc9: 1, 0xca: 1, 0xcb: 0, 0xcc: 1, 0xcd: 1, 0xcf: 0, 0xd0: 1, 0xd1: 0,
    0xd2: 3, 0xd3: 0, 0xd4: 1, 0xd5: 1, 0xd6: 1, 0xd7: 6, 0xd8: 3, 0xd9: 0,
    0xdb: 3, 0xdd: 7, 0xe0: 2, 0xe1: 1, 0xe2: 6, 0xe3: 5, 0xe4: 6, 0xe5: 1,
    0xe6: 1, 0xe7: 0,
}
HANDLED = set(NARGS) | {0x80, 0x81, 0x82, 0x84, 0x85, 0x86, 0x90, 0x91}
SPEAKER_OP = 0xa9


class ParseError(Exception):
    pass


def token_bytes(n):
    if 1 <= n <= 250:
        return bytes([n])
    page, y = divmod(n, 250)
    if not 1 <= page <= 5:
        raise ValueError('token %d out of range' % n)
    return bytes([0xfa + page, y])


class Script:
    def __init__(self, data):
        if data[:8] != b'LAFSCR\0\x01':
            raise ParseError('not a LAFSCR file')
        self.data = data
        hdr = struct.unpack_from('<8H', data, 0x10)
        self.nch = hdr[0] >> 8
        self.ta, self.tb, self.tx, self.end = hdr[1:5]
        self.code = data[0x20:self.ta]
        self.labels = list(struct.unpack_from('<%dH' % ((self.tb - self.ta) // 2), data, self.ta))
        offs = struct.unpack_from('<%dH' % ((self.tx - self.tb) // 2), data, self.tb)
        text = data[self.tx:self.end]
        self.chars = [text[i * 2:i * 2 + 2] for i in range(self.nch)]
        self.words = [text[o:text.index(b'\0', o)] for o in offs]
        self.tail = data[self.end:]

    def token(self, n):
        if 1 <= n <= self.nch:
            return self.chars[n - 1]
        k = n - self.nch - 1
        if 0 <= k < len(self.words):
            return self.words[k]
        raise ParseError('token %d out of range' % n)

    def decode_text(self, pos):
        """Mirror of 0x41E960: (text bytes, position after the terminator)."""
        c = self.code
        out = bytearray()
        i = pos
        while c[i] != 0:
            x = c[i]
            if x <= 0xfa:
                n = x
                i += 1
            else:
                n = (x - 0xfa) * 250 + c[i + 1]
                i += 2
            t = self.token(n)
            if n <= self.nch and t[0] <= 4:
                t = t[:1]        # 0x41EB50 copies one byte for control codes 1-4
            out += t
        return bytes(out), i + 1


class Parser:
    """Walk the bytecode; record statements, messages, inline strings, E9 refs."""

    def __init__(self, s):
        self.s = s
        self.c = s.code
        self.pc = 0
        self.flag = 0
        self.depth = 0
        self.stmts = []       # (pos, op)
        self.messages = []    # (op_pos, token_start, terminator_pos)
        self.strings = []     # (start, nul_pos, opcode) of EB inline strings
        self.cur_op = None
        self.e9refs = []      # (operand_pos, target_offset)
        self.speaker = {}     # message index -> speaker slot of the latest 0xA9

    def byte(self, k=0):
        if self.pc + k >= len(self.c):
            raise ParseError('ran off the end of the code at %#x' % (self.pc + k))
        return self.c[self.pc + k]

    # --- expressions (0x401620 read_tok, 0x4013D0 primary, precedence levels)
    def read_tok(self):
        if self.flag:
            self.flag = 0
            return 0x80
        al = self.byte()
        if al >= 0xec:
            self.pc += 1
        if 0x38 <= al < 0x80:
            self.pc += 1
        if al in (0xfd, 0xff):
            if self.depth > 0:
                if al == 0xfd:
                    self.flag = 1
                self.depth -= 1
                return al
            raise ParseError('unbalanced close at %#x' % (self.pc - 1))
        if al == 0xfe:
            if self.depth < 0:
                return al
            self.depth += 1
            self.lvl_or()
            al = self.byte()
            if al >= 0xec:
                self.pc += 1
            return al
        if al == 0xfc:
            if self.depth < 0:
                return al
            self.depth += 1
            return self.lvl_or()
        return al

    def primary(self):
        al = self.read_tok()
        if al == 0x60:
            self.pc += 2
            self.lvl_or()
            return self.read_tok()
        if al == 0x67 or al & 0xf8 == 0x68:
            self.pc += 1
            return self.read_tok()
        if al & 0xe0 == 0x40 or al & 0xf8 in (0x38, 0x70):
            return self.read_tok()
        if al & 0xe0 == 0x00 or al & 0xf8 == 0x20:
            self.pc += 2
            return self.read_tok()
        if al in (0xec, 0xed, 0xee):
            self.pc += {0xec: 4, 0xed: 1, 0xee: 2}[al]
            return self.read_tok()
        return al

    def lvl_mul(self):
        bl = self.primary()
        while bl in (0xfa, 0xfb, 0xef):
            bl = self.lvl_mul()
        return bl

    def lvl_add(self):
        bl = self.lvl_mul()
        while bl in (0xf8, 0xf9):
            bl = self.lvl_mul()
        return bl

    def lvl_cmp(self):
        bl = self.lvl_add()
        if 0xf2 <= bl <= 0xf7:
            bl = self.lvl_add()
        return bl

    def lvl_or(self):
        bl = self.lvl_cmp()
        while bl in (0xf0, 0xf1):
            bl = self.lvl_cmp()
        return bl

    def expr(self):
        """Mirror of 0x401000.  Returns the constant value when the expression is a
        single small constant (used to read the speaker slot), else None."""
        self.flag = 0
        self.depth = 0
        b = self.byte()
        if b == 0xeb:
            start = self.pc + 1
            end = self.c.index(b'\0', start)
            self.strings.append((start, end, self.cur_op))
            self.pc = end + 1
            return None
        if b == 0xe9:
            self.e9refs.append((self.pc + 1, (self.c[self.pc + 1] << 8) | self.c[self.pc + 2]))
            self.pc += 3
            return None
        start = self.pc
        self.lvl_or()
        if self.depth > 0:
            raise ParseError('unclosed parenthesis before %#x' % self.pc)
        val = None
        body = self.c[start:self.pc]
        if len(body) == 1 and 0x38 <= body[0] <= 0x3f:
            val = body[0] - 0x38
        elif len(body) == 2 and body[0] == 0xed:
            val = body[1]
        if self.pc < len(self.c) and self.c[self.pc] == 0xea:
            self.pc += 1
        return val

    @staticmethod
    def is_expr_start(b):
        return b <= 0x27 or 0x38 <= b <= 0x77 or b in (0xe9, 0xeb, 0xec, 0xed, 0xee, 0xfc, 0xfe)

    # --- statements (0x42A543)
    def run(self):
        c = self.c
        speaker = None
        while self.pc < len(c):
            pos = self.pc
            op = c[pos]
            self.cur_op = op
            self.stmts.append((pos, op))
            if op & 0xf8 == 0x28:            # if !expr goto label
                self.pc += 2
                self.expr()
            elif op & 0xf8 == 0x30:          # goto label
                self.pc += 2
            elif op == 0x80:
                self.pc += 2
                self.expr()
            elif op in (0x81, 0x82):         # goto / gosub label
                self.pc += 2
            elif op == 0x84:                 # call: count, label, count exprs
                n = c[pos + 1]
                self.pc += 3
                for _ in range(n):
                    self.expr()
            elif op == 0x85:
                self.pc += 1
                self.expr()
                self.pc += 1
            elif op == 0x86:                 # choice menu: count x (condition, text)
                n = c[pos + 1]
                self.pc += 2
                for _ in range(2 * n):
                    self.expr()
            elif op == 0x90:                 # assignment
                self.pc += 1
                lv = c[self.pc]
                if lv == 0x60:
                    self.pc += 3
                    self.expr()
                    self.expr()
                elif lv == 0x67:
                    self.pc += 2
                    self.expr()
                elif lv & 0xe0 == 0x40 or lv & 0xf8 == 0x70:
                    self.pc += 1
                    self.expr()
                elif lv & 0xe0 == 0 or lv & 0xf8 in (0x20, 0x68):
                    self.pc += 2
                    self.expr()
                else:
                    raise ParseError('bad assignment target %#x at %#x' % (lv, self.pc))
            elif op == 0x91:                 # text
                _, after = self.s.decode_text(pos + 1)
                self.speaker[len(self.messages)] = speaker
                self.messages.append((pos, pos + 1, after - 1))
                self.pc = after
            elif op in NARGS:
                self.pc += 1
                vals = [self.expr() for _ in range(NARGS[op])]
                if op == SPEAKER_OP:
                    speaker = vals[0]
            elif 0x80 <= op <= 0xe7:         # no handler: the engine yields
                self.pc += 1
                while self.pc < len(c) and self.is_expr_start(c[self.pc]) and any(c[self.pc:]):
                    self.expr()
            elif op == 0 and not any(c[pos:]):
                self.stmts.pop()
                self.code_end = pos          # alignment padding follows
                self.pc = len(c)
            else:
                raise ParseError('bad opcode %#x at %#x' % (op, pos))
        if self.pc != len(c):
            raise ParseError('overran the code section')
        if not hasattr(self, 'code_end'):
            self.code_end = len(c)
        return self


# ---------------------------------------------------------------- text units

def is_japanese(b):
    return any(x >= 0x80 for x in b)


def extract(data):
    """-> list of entries: dict(kind='m'|'s', index, text_bytes, speaker, cont)
    'm' = message (statement 0x91), 's' = inline string containing Japanese."""
    s = Script(data)
    p = Parser(s).run()
    out = []
    prev_end = None
    prev_stmt_was_msg = False
    stmt_index = {pos: k for k, (pos, _) in enumerate(p.stmts)}
    for i, (pos, a, end) in enumerate(p.messages):
        text, _ = s.decode_text(a)
        k = stmt_index[pos]
        cont = k > 0 and p.stmts[k - 1][1] == 0x91 and not prev_end
        out.append(dict(kind='m', index=i, text=text, speaker=p.speaker.get(i), cont=cont))
        prev_end = text[-1:] == b'\x01'
    for j, (a, b, op) in enumerate(p.strings):
        t = s.code[a:b]
        if is_japanese(t):
            out.append(dict(kind='s', index=j, text=t, speaker=None, cont=False,
                            choice=(op == 0x86)))
    return out


# ---------------------------------------------------------------- encoder

def _atom_len(b, i):
    x = b[i]
    if x in (0x05, 0x06, 0x07) or 0x81 <= x <= 0x9f or 0xe0 <= x <= 0xfc:
        return 2
    return 1


def atoms(b):
    """Split text bytes into indivisible units for tokenising.  The word copier
    (0x41EAE0) copies 02 together with the byte after it, so {w} is glued to the unit
    that follows it: a word may then never end in 02 and run past its terminator."""
    out = []
    i = 0
    while i < len(b):
        n = _atom_len(b, i)
        if b[i] == 0x02 and i + 1 < len(b):
            n = 1 + _atom_len(b, i + 1)
        out.append(b[i:i + n])
        i += n
    return out


SPACE = '　'.encode('cp932')


def _chunks(at):
    """Candidate multi-atom words: runs between spaces/controls, with trailing space."""
    cur = []
    for a in at:
        if a == SPACE or a[0] < 0x20:
            if cur:
                yield tuple(cur + [a])
                yield tuple(cur)
            cur = []
        else:
            cur.append(a)
    if cur:
        yield tuple(cur)


def build_dictionary(messages, seed_words=()):
    """Choose characters and words for a set of message byte strings.
    Returns (chars, words): chars are 2-byte glyph atoms (single-byte indices),
    words are byte strings.  seed_words: extra candidates (the original Japanese words,
    so untranslated messages still compress)."""
    msg_atoms = [atoms(m) for m in messages]
    atom_freq = Counter(a for at in msg_atoms for a in at)
    cand = Counter()
    for at in msg_atoms:
        for ch in _chunks(at):
            if len(ch) > 1:
                cand[ch] += 1
    for w in seed_words:
        aw = tuple(atoms(w))
        if len(aw) > 1:
            cand[aw] += 0           # present as a candidate; usage decides
    # count seed-word usage roughly (substring occurrences in Japanese messages)
    joined = [b''.join(at) for at in msg_atoms]
    for w in seed_words:
        aw = tuple(atoms(w))
        if len(aw) > 1 and aw in cand:
            cand[aw] = sum(m.count(w) for m in joined)
    capacity = MAX_TOKENS - len(atom_freq)
    if capacity < 0:
        raise ValueError('more distinct characters (%d) than tokens' % len(atom_freq))

    def saving(item):
        w, f = item
        nbytes = sum(len(a) for a in w)
        return f * (len(w) - 1.5) - (nbytes + 3)
    picked = [w for w, f in sorted(cand.items(), key=saving, reverse=True)
              if saving((w, f)) > 0][:capacity]
    vocab = [tuple([a]) for a in atom_freq] + picked

    # first pass: segment with uniform cost to get usage counts
    usage = Counter()
    by_first = _index(vocab)
    for at in msg_atoms:
        for tok in _segment(at, by_first, lambda t: 1):
            usage[tok] += 1
    # drop words nobody uses; keep every atom (needed for coverage)
    vocab = [t for t in vocab if len(t) == 1 or usage[t]]
    ranked = sorted(vocab, key=lambda t: (-usage[t], len(t), t))
    single = ranked[:250]
    chars = [t[0] for t in single if len(t) == 1 and len(t[0]) == 2 and t[0][0] >= 0x80]
    single_words = [t for t in single if not (len(t) == 1 and len(t[0]) == 2 and t[0][0] >= 0x80)]
    rest = [t for t in ranked[250:]]
    words = [b''.join(t) for t in single_words + rest]
    if len(chars) + len(words) > MAX_TOKENS:
        raise ValueError('dictionary overflow')
    return chars, words


def _index(vocab):
    by_first = {}
    for t in vocab:
        by_first.setdefault(t[0], []).append(t)
    return by_first


def _segment(at, by_first, cost):
    """Minimum-cost segmentation of an atom list into vocabulary tokens."""
    n = len(at)
    best = [0] + [None] * n
    back = [None] * (n + 1)
    for i in range(n):
        if best[i] is None:
            continue
        for t in by_first.get(at[i], ()):
            j = i + len(t)
            if j <= n and tuple(at[i:j]) == t:
                c = best[i] + cost(t)
                if best[j] is None or c < best[j]:
                    best[j] = c
                    back[j] = t
    if best[n] is None:
        raise ValueError('text cannot be tokenised')
    out = []
    j = n
    while j:
        t = back[j]
        out.append(t)
        j -= len(t)
    return out[::-1]


def encode_messages(messages, chars, words):
    """-> list of token byte strings (without the 00 terminator)."""
    index = {}
    for k, c in enumerate(chars):
        index[(c,)] = k + 1
    for k, w in enumerate(words):
        index.setdefault(tuple(atoms(w)), len(chars) + k + 1)
    by_first = _index(list(index))
    out = []
    for m in messages:
        toks = _segment(atoms(m), by_first, lambda t: 1 if index[t] <= 250 else 2)
        out.append(b''.join(token_bytes(index[t]) for t in toks))
    return out


# ---------------------------------------------------------------- rebuild

def fixed_layout(data):
    """Numbers MEASURE needs to predict a rebuilt file's size without the game data."""
    s = Script(data)
    p = Parser(s).run()
    msg_tok = sum(end - a for _, a, end in p.messages)
    jp_str = sum(b - a for a, b, _ in p.strings if is_japanese(s.code[a:b]))
    return dict(fixed_code=p.code_end - msg_tok - jp_str, labels=len(s.labels),
                tail=len(s.tail), messages=len(p.messages))


def predict_size(layout, chars, words, enc_msgs, new_strs):
    code = layout['fixed_code'] + sum(len(m) for m in enc_msgs) + sum(len(x) for x in new_strs)
    code += code & 1
    return (0x20 + code + 2 * layout['labels'] + 2 * len(words) + 2 * len(chars)
            + sum(len(w) + 1 for w in words) + layout['tail'])


def rebuild(data, msg_texts, str_texts):
    """msg_texts: list (one per message, in order) of text bytes.
    str_texts: dict string_index -> new bytes for Japanese inline strings.
    Returns the new file bytes."""
    s = Script(data)
    p = Parser(s).run()
    if len(msg_texts) != len(p.messages):
        raise ValueError('message count mismatch')
    seed = [w for w in s.words if is_japanese(w)]
    chars, words = build_dictionary(msg_texts, seed)
    enc = encode_messages(msg_texts, chars, words)

    edits = []      # (old_start, old_end, new_bytes) -- regions replaced in the code
    for (pos, a, end), e in zip(p.messages, enc):
        edits.append((a, end, e))
    for j, (a, b, _) in enumerate(p.strings):
        if j in str_texts:
            if b'\0' in str_texts[j]:
                raise ValueError('NUL in inline string')
            edits.append((a, b, str_texts[j]))
    edits.sort()
    code = bytearray()
    shifts = []     # (old_pos, cumulative delta after this edit)
    last = 0
    delta = 0
    old = s.code[:p.code_end]
    for a, b, new in edits:
        code += old[last:a] + new
        delta += len(new) - (b - a)
        shifts.append((b, delta, a))
        last = b
    code += old[last:]

    def move(x):
        d = 0
        for b, dl, a in shifts:
            if x >= b:
                d = dl
            elif x > a:
                raise ValueError('reference into an edited region at %#x' % x)
        return x + d

    for opos, target in p.e9refs:
        nt = move(target)
        npos = move(opos)
        if nt > 0xffff:
            raise ValueError('code too large for an E9 reference')
        code[npos:npos + 2] = bytes([nt >> 8, nt & 0xff])
    if len(code) & 1:
        code += b'\0'
    labels = [move(x) for x in s.labels]

    ta = 0x20 + len(code)
    tb = ta + 2 * len(labels)
    tx = tb + 2 * len(words)
    text = bytearray(b''.join(chars))
    offs = []
    for w in words:
        offs.append(len(text))
        text += w + b'\0'
    end = tx + len(text)
    total = end + len(s.tail)
    if total > MAX_FILE:
        raise ValueError('rebuilt script is %d bytes (limit %d)' % (total, MAX_FILE))
    if max(offs or [0]) > 0xffff or max(labels or [0]) > 0xffff:
        raise ValueError('offset overflow')
    out = bytearray(data[:0x10])
    struct.pack_into('<I', out, 8, total)
    out += struct.pack('<8H', 0x44 | (len(chars) << 8), ta, tb, tx, end, 0, 0, 0)
    out += code
    out += struct.pack('<%dH' % len(labels), *labels)
    out += struct.pack('<%dH' % len(offs), *offs)
    out += text
    out += s.tail
    return bytes(out), (chars, words, enc)
