#!/usr/bin/env python3
"""MEASURE - real container usage after MERGE, as a full table.

  python3 tools/measure.py

Containers:
  script  one per *.SCR: rebuilt size (limit 65,535 bytes, every header offset is u16)
          and dictionary tokens (limit 1,499).  Sized with the encoder BUILD uses, so
          the figure is exact.  Untouched files are listed with their rebuilt size too.
  system  one per exe string slot: size, used, free, for every slot.
  scene   subtitles have no byte container (the block is rebuilt); listed for completeness.
Every container is printed; there is no summary line that hides rows.  The warning
threshold is PROJECT.md section 4 "Reserve kept per container" when it is filled in.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abyss import pipeline                                             # noqa: E402
from abyss.project import load_layout, read_project_numbers, translations   # noqa: E402


def main():
    tl = translations()
    layout = load_layout()
    nums = read_project_numbers()
    reserve = nums.get('reserve')
    neg = 0
    warn = 0
    print('SCRIPT CONTAINERS (bytes used / 65535, free; tokens used / 1499)')
    print('%-26s %8s %8s %8s %8s  %s' % ('file', 'bytes', 'free', 'tokens', 'tok-free', 'translated'))
    for name, finals in pipeline.all_finals('script', tl).items():
        u = pipeline.container_usage(name, finals, layout)
        free = u['limit'] - u['bytes']
        tfree = u['token_limit'] - u['tokens']
        n_t = sum(1 for f in finals if f.translated)
        mark = ''
        if free < 0 or tfree < 0:
            mark = '  NEGATIVE'
            neg += 1
        elif reserve is not None and free < reserve:
            mark = '  under reserve'
            warn += 1
        print('%-26s %8d %8d %8d %8d  %d/%d%s' % (name + '.SCR', u['bytes'], free, u['tokens'], tfree,
                                                n_t, len(finals), mark))
    for alias, real in sorted(layout.get('aliases', {}).items()):
        print('%-26s (identical copy of %s; built from it)' % (alias + '.SCR', real + '.SCR'))
    print()
    print('SYSTEM SLOTS (every slot is its own container; full-width text costs 2 bytes per')
    print('character and 1 per {br}; ascii slots 1 per character)')
    print('%-16s %-6s %5s %5s %5s  %s' % ('slot', 'kind', 'size', 'used', 'free', 'state'))
    for f in pipeline.all_finals('system', tl)['*']:
        mx = pipeline.ctx_max(f.row.ctx)
        used = len(pipeline.encode_final('system', f))
        free = mx - used
        mark = '  NEGATIVE' if free < 0 else ''
        neg += free < 0
        print('%-16s %-6s %5d %5d %5d  %s%s' % (f.row.id, pipeline.ctx_kind(f.row.ctx), mx, used, free,
                                              'translated' if f.translated else 'source', mark))
    print()
    print('SCENE FILES (no byte limit; subtitle block is rebuilt)')
    for name, finals in pipeline.all_finals('scene', tl).items():
        n_t = sum(1 for f in finals if f.translated)
        print('%-26s subtitles %3d  translated %d' % (name + '.SCE', len(finals), n_t))
    print()
    print('containers negative: %d; under the reserve (%s): %d'
          % (neg, 'not set in PROJECT.md' if reserve is None else '%d bytes' % reserve, warn))
    return 1 if neg else 0


if __name__ == '__main__':
    sys.exit(main())
