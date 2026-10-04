#!/usr/bin/env python3
"""QUEUE - the planner: every untranslated unit with its measured budget.

  python3 tools/queue_plan.py [store]

For each unit not yet fully translated, in dispatch order (PROJECT.md section 2): source
rows and characters (tags excluded), the containers it lands in and their free bytes, the
budget ratio, its tier and blocked status.

  ratio = target characters the unit may use / source characters
    script/scene: the box geometry binds, not bytes, unless the container is short:
                  (free bytes in the container / 2 + source characters) / source characters
    system:       the tightest row: characters the slot holds / source characters
Tier bands, the blocked floor and the stores blocked whole (pending engine work) are read
from PROJECT.md section 4 every run; nothing is hard-coded here.  While the tiers are
unfilled the tier column says "uncalibrated".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abyss import codec, pipeline                                      # noqa: E402
from abyss.project import STORES, units, load_layout, read_project_numbers, translations  # noqa: E402


def tier_of(ratio, nums, store=None):
    if store in nums.get('blocked_stores', {}):
        return 'blocked (%s)' % nums['blocked_stores'][store]
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
        if lo <= ratio < hi or (hi == float('inf') and ratio >= lo):    # 'geom' units are inf
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
    print('thresholds from PROJECT.md section 4: floor=%s tiers=%s blocked stores=%s'
          % (nums.get('floor', 'unset'), nums.get('tiers') or 'unset',
             nums.get('blocked_stores') or 'none'))
    n = 0
    for store in stores:
        print('\n%s' % store.upper())
        print('%-20s %5s %6s %8s %8s  %-16s %s' % ('unit', 'rows', 'chars', 'free', 'ratio', 'tier',
                                                   'containers'))
        for unit, rows in units(store).items():
            todo = [r for r in rows if (store, r.id) not in tl]
            if not todo:
                continue
            chars = sum(codec.char_count(r.src) for r in rows)
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
            t = tier_of(ratio, nums, store)
            print('%-20s %5d %6d %8s %8s  %-16s %s' % (
                unit, len(rows), chars, '-' if free is None else free,
                'geom' if ratio == float('inf') else '%.2f' % ratio, t, cname))
            n += 1
    print('\n%d unit(s) not fully translated' % n)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
