#!/usr/bin/env python3
"""QUEUE - the planner: every untranslated unit with its measured budget.

  python3 tools/queue_plan.py [store]

For each unit not yet fully translated: source rows and characters, the containers it
lands in and their free bytes, the budget ratio, its tier and blocked status.

  ratio = target characters the unit may use / source characters
    script/scene: the box geometry binds, not bytes, unless the container is short:
                  (free bytes in the container / 2 + source characters) / source characters
    system:       the tightest row: characters the slot holds / source characters
Tier bands and the blocked floor are read from PROJECT.md section 4 every run; nothing
is hard-coded here.  While section 4 is unfilled the tier column says "uncalibrated".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abyss import codec, pipeline                                      # noqa: E402
from abyss.project import STORES, units, load_layout, read_project_numbers, translations  # noqa: E402


def tier_of(ratio, nums):
    tiers = nums.get('tiers', {})
    floor = nums.get('floor')
    if floor is not None and ratio < floor:
        return 'blocked'
    order = ['blocked', 'a', 'b', 'c', 'd']
    for name in order:
        band = tiers.get(name)
        if not band:
            continue
        if len(band) == 1:
            lo, hi = (band[0], float('inf')) if name == 'd' else (0, band[0])
        else:
            lo, hi = band[0], band[1]
        if lo <= ratio < hi:
            return name.upper() if name != 'blocked' else 'blocked'
    return 'uncalibrated' if not tiers else '?'


def main(argv):
    stores = [argv[0]] if argv else list(STORES)
    tl = translations()
    nums = read_project_numbers()
    layout = load_layout()
    usage = {}
    for name, finals in pipeline.all_finals('script', tl).items():
        usage[name] = pipeline.container_usage(name, finals, layout)
    print('thresholds from PROJECT.md section 4: floor=%s tiers=%s'
          % (nums.get('floor', 'unset'), nums.get('tiers') or 'unset'))
    n = 0
    for store in stores:
        print('\n%s' % store.upper())
        print('%-28s %5s %6s %-22s %8s %7s  %s' % ('unit', 'rows', 'chars', 'containers', 'free',
                                                   'ratio', 'tier'))
        for unit, rows in units(store).items():
            todo = [r for r in rows if (store, r.id) not in tl]
            if not todo:
                continue
            chars = sum(len(r.src) for r in rows)
            if store == 'script':
                conts = sorted(set(r.file for r in rows))
                free = min(usage[c]['limit'] - usage[c]['bytes'] for c in conts)
                ratio = (free / 2 + chars) / max(chars, 1)
                cname = ','.join(c + '.SCR' for c in conts)
            elif store == 'scene':
                free = None
                ratio = float('inf')
                cname = ','.join(sorted(set(r.file + '.SCE' for r in rows)))
            else:
                free = None
                ratio = min((pipeline.ctx_max(r.ctx) / (1 if r.ctx.startswith('ascii') else 2))
                            / max(codec.char_count(r.src), 1) for r in rows)
                cname = 'AbyssBoat.exe'
            t = tier_of(ratio, nums)
            print('%-28s %5d %6d %-22s %8s %7s  %s' % (
                unit, len(rows), chars, cname[:22], '-' if free is None else free,
                'geom' if ratio == float('inf') else '%.2f' % ratio, t))
            n += 1
    print('\n%d unit(s) not fully translated' % n)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
