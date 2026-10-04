"""Shared logic for MERGE, CHECK, UNITCHECK, MEASURE and BUILD.

Every row's final text is either its translation (word-wrapped by the tools) or its
untouched source.  Script containers (one per *.SCR) are sized with the same encoder
BUILD uses, from the numbers in dumps/layout.json, so MEASURE is exact without the game
files.
"""
import re
from collections import OrderedDict

from . import codec, scr
from .project import (BOX_COLS, BOX_ROWS, SCENE_COLS, SCENE_ROWS, CHOICE_COLS,
                      SCR_MAX_BYTES, SCR_MAX_TOKENS, read_dump, load_layout, translations)

KINSOKU = set('、。，．…？！゛゜ヽヾゝゞ々ー）］｝」』‼⁉')


def ctx_kind(ctx):
    return ctx.split(' ')[0]


def ctx_max(ctx):
    """System store: bytes available in the slot (excluding the NUL)."""
    m = re.search(r'slot=(\d+)', ctx)
    return int(m.group(1)) if m else None


def is_cont(ctx):
    return ctx.endswith(' +')


def store_width(store, ctx):
    if store == 'scene':
        return SCENE_COLS
    if store == 'script' and ctx_kind(ctx) == 'msg':
        return BOX_COLS
    return None


def ending(s):
    for t in ('{p}', '{br}', '{w}'):
        if s.endswith(t):
            return t
    return ''


def engine_pages(s, width, start_col=0):
    """Lay text out the way the renderer does (auto-wrap at `width`, kinsoku may
    overhang by one).  -> list of pages, each a list of line widths."""
    pages = [[start_col]]
    for kind, val in codec.tokens(s):
        if kind == 'tag':
            if val == '{br}':
                pages[-1].append(0)
            elif val in ('{p}', '{w}'):
                pages.append([0])
            else:
                pages[-1][-1] += codec.cols_of(val)
        elif kind == 'ch':
            line = pages[-1][-1]
            if line >= width and not (line == width and val in KINSOKU):
                pages[-1].append(0)
            pages[-1][-1] += 1
    return pages


class Final:
    """Final text for one row, with layout facts."""
    __slots__ = ('row', 'translated', 'text', 'too_long', 'start_col', 'end_col')


def finalize(store, rows, tl):
    """rows: dump rows of ONE file (script) or any rows (other stores), in order.
    tl: dict id -> target.  Returns list of Final."""
    out = []
    col = 0
    for r in rows:
        f = Final()
        f.row = r
        tgt = tl.get(r.id, '')
        f.translated = bool(tgt.strip())
        width = store_width(store, r.ctx)
        start = col if (store == 'script' and is_cont(r.ctx)) else 0
        f.start_col = start
        f.too_long = []
        if f.translated and width:
            f.text, f.too_long = codec.wrap(tgt, width, start)
        elif f.translated:
            f.text = tgt
        else:
            f.text = r.src
        if width:
            pages = engine_pages(f.text, width, start)
            last = pages[-1][-1]
            f.end_col = 0 if ending(f.text) in ('{br}', '{p}') else last
        else:
            f.end_col = 0
        col = f.end_col
        out.append(f)
    return out


def page_groups(finals):
    """Script store: rows of the message box per page, following '+' chains.
    -> list of (first_row, rows_on_page) for every page."""
    out = []
    cur_rows = 0
    cur_first = None
    for f in finals:
        if ctx_kind(f.row.ctx) != 'msg':
            continue
        pages = engine_pages(f.text, BOX_COLS, f.start_col)
        if not is_cont(f.row.ctx) or cur_first is None:
            if cur_first is not None:
                out.append((cur_first, cur_rows))
            cur_first, cur_rows = f, 0
        for k, pg in enumerate(pages):
            lines = len(pg)
            if pg[-1] == 0 and lines > 1:
                lines -= 1          # a trailing break does not show an empty line
            if k == 0:
                # continuing a chain: the first line may be the same as the last one
                cur_rows += lines - (1 if (is_cont(f.row.ctx) and f.start_col) else 0)
            else:
                out.append((cur_first, cur_rows))
                cur_first, cur_rows = f, lines
        if f.text.endswith('{p}') or f.text.endswith('{w}'):
            out.append((cur_first, cur_rows))
            cur_first, cur_rows = None, 0
    if cur_first is not None:
        out.append((cur_first, cur_rows))
    return [(f, n) for f, n in out if n]


def encode_final(store, f):
    """Final -> game bytes."""
    r = f.row
    if store == 'system':
        ascii_ok = ctx_kind(r.ctx) == 'ascii'
        if f.translated:
            return codec.encode_target(f.text, 'system', ascii_ok)
        return codec.encode_source(r.src, 'system')
    if f.translated:
        return codec.encode_target(f.text, store)
    return codec.encode_source(r.src, store)


def script_files(rows):
    byfile = OrderedDict()
    for r in rows:
        byfile.setdefault(r.file, []).append(r)
    return byfile


def container_usage(name, finals, layout):
    """Predict the rebuilt size of script `name`.  -> dict(bytes, tokens, error)."""
    lay = layout['scripts'][name]
    msgs = []
    strs = {}
    for f in finals:
        b = encode_final('script', f)
        kind = ctx_kind(f.row.ctx)
        if kind == 'msg':
            msgs.append(b)
        else:
            strs[int(f.row.id.split('/s')[1])] = b
    seed = [bytes.fromhex(w) for w in lay.get('seed', [])]
    chars, words = scr.build_dictionary(msgs, seed)
    enc = scr.encode_messages(msgs, chars, words)
    size = scr.predict_size(lay, chars, words, enc, list(strs.values()))
    return dict(bytes=size, tokens=len(chars) + len(words), limit=SCR_MAX_BYTES,
                token_limit=SCR_MAX_TOKENS)


def all_finals(store, tl=None):
    """-> OrderedDict file -> list of Final (script), or {'*': [...]} for other stores."""
    tl_all = translations() if tl is None else tl
    rows = read_dump(store)
    t = {k[1]: v for k, v in tl_all.items() if k[0] == store}
    if store == 'script':
        return OrderedDict((f, finalize(store, rs, t)) for f, rs in script_files(rows).items())
    if store == 'scene':
        return OrderedDict((f, finalize(store, rs, t)) for f, rs in script_files(rows).items())
    return OrderedDict([('*', finalize(store, rows, t))])
