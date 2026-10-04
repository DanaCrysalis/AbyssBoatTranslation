#!/usr/bin/env python3
"""UNITCHECK - geometry of one unit, or of a whole store after MERGE.

  python3 tools/unitcheck.py <store>/<unit> [unit-file]   one unit (file defaults to tl/<store>/<unit>.tsv)
  python3 tools/unitcheck.py <store>                       every translated row of a store

For every translated row: the wrapped text's lines and their column counts, rows per
box page (following "+" chains), words longer than a line, and the diff of the movable
codes ({br}, {p}) against the source.  Line numbers are the unit file's line numbers
(`grep -n` numbering).  Prints how many rows it examined; exits 1 on any violation or
when it examined nothing.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abyss import codec, pipeline                                      # noqa: E402
from abyss.project import (BOX_COLS, BOX_ROWS, SCENE_COLS, SCENE_ROWS, CHOICE_COLS,  # noqa: E402
                           STORES, read_dump, units, unit_path, read_unit_file, translations)


def movable(s):
    return [v for k, v in codec.tokens(s) if k == 'tag' and v in ('{br}', '{p}')]


def report(store, rows_with_lines, tl):
    """rows_with_lines: list of (Row-from-dump, file_line or None)."""
    bad = 0
    examined = 0
    line_of = {r.id: ln for r, ln in rows_with_lines}
    wanted = set(line_of)
    if store == 'system':
        finals = pipeline.all_finals('system', tl)['*']
        groups = {'*': finals}
    else:
        groups = pipeline.all_finals(store, tl)
    for name, finals in groups.items():
        finals_in = [f for f in finals if f.row.id in wanted]
        if not finals_in:
            continue
        for f in finals_in:
            if not f.translated:
                continue
            examined += 1
            r = f.row
            kind = pipeline.ctx_kind(r.ctx)
            ln = line_of[r.id]
            where = 'line %s %s' % (ln if ln else '-', r.id)
            if store == 'system':
                mx = pipeline.ctx_max(r.ctx)
                n = len(pipeline.encode_final('system', f))
                lines = f.text.split('{br}')
                print('%s  bytes %d/%d  chars/line %s' % (where, n, mx,
                                                          [codec.char_count(x) for x in lines]))
                if n > mx:
                    print('  VIOLATION: over the slot')
                    bad += 1
                continue
            width = SCENE_COLS if store == 'scene' else (BOX_COLS if kind == 'msg' else CHOICE_COLS)
            pages = pipeline.engine_pages(f.text, width, f.start_col)
            print('%s  pages %d  rows/page %s  cols/line %s' % (
                where, len(pages), [len(p) for p in pages], [p for p in pages]))
            for pg in pages:
                for c in pg:
                    if c > width:
                        print('  VIOLATION: line of %d columns (limit %d)' % (c, width))
                        bad += 1
                if store == 'scene' and len([c for c in pg if c]) > SCENE_ROWS:
                    print('  VIOLATION: %d lines (limit %d)' % (len(pg), SCENE_ROWS))
                    bad += 1
            for w in f.too_long:
                print('  VIOLATION: word longer than a line: %s' % w)
                bad += 1
            ms, mt = movable(r.src), movable(f.text)
            if ms != mt:
                print('  codes: source %s -> target %s' % (' '.join(ms) or '-', ' '.join(mt) or '-'))
        if store == 'script':
            for f, n in pipeline.page_groups(finals):
                if f.row.id in wanted and f.translated:
                    flag = '  VIOLATION' if n > BOX_ROWS else ''
                    if n > BOX_ROWS:
                        bad += 1
                    print('page from %s: %d rows (limit %d)%s' % (f.row.id, n, BOX_ROWS, flag))
    return examined, bad


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    arg = argv[0]
    tl = translations()
    if '/' in arg:
        store, unit = arg.split('/', 1)
        us = units(store)
        if unit not in us:
            print('no unit %s' % arg)
            return 2
        p = argv[1] if len(argv) > 1 else unit_path(store, unit)
        _, rows, probs = read_unit_file(p)
        for x in probs:
            print('ERROR ' + x)
        mine = {r.id: r for r in rows}
        for r in rows:
            if r.tgt.strip():
                tl[(store, r.id)] = r.tgt
            else:
                tl.pop((store, r.id), None)
        pairs = [(d, mine[d.id].line if d.id in mine else None) for d in us[unit]]
    elif arg in STORES:
        store = arg
        pairs = [(d, None) for d in read_dump(store)]
    else:
        print(__doc__)
        return 2
    examined, bad = report(store, pairs, tl)
    print('examined %d translated rows, %d violation(s)' % (examined, bad))
    if examined == 0:
        print('nothing examined: no translated rows')
        return 1
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
