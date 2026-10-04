#!/usr/bin/env python3
"""Abyss Boat translation assembler.

  python3 tools/assemble.py check            CHECK  - validate every file under tl/
  python3 tools/assemble.py status           STATUS - progress per store and unit
  python3 tools/assemble.py merge            MERGE  - splice tl/ into the dumps under build/
  python3 tools/assemble.py extract <store>/<unit>   EXTRACT - start a unit file
  python3 tools/assemble.py units [store]    list the units of a store
  python3 tools/assemble.py build            BUILD  (human-only: needs original/)
  python3 tools/assemble.py refresh          REFRESH (human-only: needs original/)

original/ must hold SCRIPT.PAK and AbyssBoat.exe from the disc (never committed).
Nothing here reads pending/.
"""
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abyss import codec, exe, lac, pipeline, sce, scr          # noqa: E402
from abyss.project import (STORES, ROOT, BOX_ROWS, SCENE_ROWS, CHOICE_COLS,  # noqa: E402
                           SCR_MAX_BYTES, SCR_MAX_TOKENS, LAYOUT_FILE, ORIGINALS_FILE, Row,
                           path, read_dump, write_dump, units, unit_path, unit_header,
                           read_unit_file, all_unit_files, translations, load_layout)

ORIGINAL = path('original')
BUILD = path('build')


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, '/')


# ================================================================ CHECK

def tag_multiset(s, names):
    return Counter(v for k, v in codec.tokens(s) if k == 'tag' and
                   any(v == '{%s}' % n or v.startswith('{%s:' % n) for n in names))


def check_row(store, r, problems, counts):
    """Per-row checks on a translated row.  Appends (row, message) to problems."""
    src, tgt, ctx = r.src, r.tgt, r.ctx
    kind = pipeline.ctx_kind(ctx)
    counts['translated rows'] += 1
    if tgt != tgt.strip():
        problems.append((r, 'target has leading or trailing whitespace'))
    if '\t' in tgt:
        problems.append((r, 'tab inside the target'))
    # charset / encoding
    ascii_ok = store == 'system' and kind == 'ascii'
    try:
        enc = codec.encode_target(tgt, 'system' if store == 'system' else store, ascii_ok)
    except codec.EncodeError as e:
        problems.append((r, 'charset: %s' % e))
        return
    counts['charset checks'] += 1
    # tags
    if store != 'system':
        fixed = ('name', 'num', 'pause', 'w')
        if tag_multiset(src, fixed) != tag_multiset(tgt, fixed):
            problems.append((r, 'tags {name}/{num:N}/{pause:N}/{w} differ from the source: '
                                'source %s, target %s' % (dict(tag_multiset(src, fixed)),
                                                          dict(tag_multiset(tgt, fixed)))))
        if tgt.count('{p}') < src.count('{p}'):
            problems.append((r, '{p} removed: source has %d, target %d'
                                % (src.count('{p}'), tgt.count('{p}'))))
        if pipeline.ending(src) != pipeline.ending(tgt):
            problems.append((r, 'must end like the source (%s), ends with %s'
                                % (pipeline.ending(src) or 'no tag', pipeline.ending(tgt) or 'no tag')))
        if tgt.endswith('{w}'):
            problems.append((r, '{w} may not be last'))
        counts['tag-parity checks'] += 1
    else:
        sp = sorted(codec.PRINTF_RE.findall(src))
        tp = sorted(codec.PRINTF_RE.findall(tgt))
        if sp != tp:
            problems.append((r, 'printf directives differ: source %s, target %s' % (sp, tp)))
        mx = pipeline.ctx_max(ctx)
        if mx is not None and len(enc) > mx:
            problems.append((r, 'slot: %d bytes, slot holds %d (2 per character, 1 per {br})'
                                % (len(enc), mx)))
        if not ascii_ok and (tgt.endswith('{br}') or '{br}{br}' in tgt):
            problems.append((r, '{br} may not be last or doubled (the menu renderer draws the '
                                'byte after it unconditionally)'))
        counts['slot checks'] += 1
    # widths for things that are not auto-wrapped
    if store == 'script' and kind in ('choice', 'text'):
        for line in tgt.split('{br}'):
            w = sum(codec.cols_of(v if k == 'tag' else v) for k, v in codec.tokens(line))
            if w > CHOICE_COLS:
                problems.append((r, 'line is %d columns, limit %d' % (w, CHOICE_COLS)))
        counts['width checks'] += 1


def run_check(verbose=True):
    """-> (problems list of strings, counts Counter)."""
    problems = []
    counts = Counter()
    dumps = {s: read_dump(s) for s in STORES}
    by_id = {s: {r.id: r for r in dumps[s]} for s in STORES}
    unit_rows = {s: units(s, dumps[s]) for s in STORES}
    seen_ids = defaultdict(dict)

    def err(where, msg):
        problems.append('%s: %s' % (where, msg))

    # the dumps themselves: unique ids, units partition the rows, layout covers every script
    layout = load_layout()
    for s in STORES:
        ids = [r.id for r in dumps[s]]
        if len(ids) != len(set(ids)):
            err('dumps/%s.tsv' % s, 'duplicate ids')
        covered = [r.id for rs in unit_rows[s].values() for r in rs]
        if sorted(covered) != sorted(ids):
            err('dumps/%s.tsv' % s, 'units do not cover every row exactly once')
        counts['dump rows verified'] += len(ids)
    for f in set(r.file for r in dumps['script']):
        lay = layout['scripts'].get(f)
        n = sum(1 for r in dumps['script'] if r.file == f and r.ctx.startswith('msg'))
        if lay is None or lay['messages'] != n:
            err('dumps/layout.json', '%s: layout missing or message count differs' % f)

    files = all_unit_files()
    for store, unit, p in files:
        counts['unit files'] += 1
        header, rows, probs = read_unit_file(p)
        for x in probs:
            err(rel(p), x)
        if unit not in unit_rows[store]:
            err(rel(p), 'no unit %s/%s (see `assemble.py units %s`)' % (store, unit, store))
            continue
        expect = unit_rows[store][unit]
        want_header = unit_header(store, unit, expect)
        if header[:len(want_header)] != want_header:
            err(rel(p), 'header lines differ from EXTRACT output')
        ids = [r.id for r in rows]
        if ids != [r.id for r in expect]:
            missing = set(r.id for r in expect) - set(ids)
            extra = [i for i in ids if i not in set(r.id for r in expect)]
            err(rel(p), 'rows differ from the unit: %d missing, %d unknown%s'
                % (len(missing), len(extra), (' e.g. ' + (extra or sorted(missing))[0]) if (missing or extra) else ' (order)'))
        for r in rows:
            counts['rows examined'] += 1
            d = by_id[store].get(r.id)
            if d is None:
                err('%s:%d' % (rel(p), r.line), 'key %s matches nothing in the dump' % r.id)
                continue
            if r.id in seen_ids[store]:
                err('%s:%d' % (rel(p), r.line), '%s also in %s' % (r.id, seen_ids[store][r.id]))
            seen_ids[store][r.id] = rel(p)
            if r.ctx != d.ctx or r.src != d.src:
                err('%s:%d' % (rel(p), r.line), 'context/source not byte-identical to the dump')
                continue
            if r.tgt.strip():
                rp = []
                check_row(store, r, rp, counts)
                for row, msg in rp:
                    err('%s:%d %s' % (rel(p), row.line, row.id), msg)

    # layout: geometry and containers on the merged result
    tl = translations()
    line_of = {}
    for store, unit, p in files:
        _, rows, _ = read_unit_file(p)
        for r in rows:
            line_of[(store, r.id)] = '%s:%d' % (rel(p), r.line)
    layout = load_layout()
    for store in ('script', 'scene'):
        for name, finals in pipeline.all_finals(store, tl).items():
            for f in finals:
                if not f.translated:
                    continue
                counts['geometry checks'] += 1
                for w in f.too_long:
                    err('%s %s' % (line_of.get((store, f.row.id), '?'), f.row.id),
                        'word "%s" is longer than a line' % w)
                if store == 'scene':
                    pages = pipeline.engine_pages(f.text, pipeline.SCENE_COLS)
                    for pg in pages:
                        n = len([x for x in pg if x]) or 0
                        if n > SCENE_ROWS:
                            err('%s %s' % (line_of.get((store, f.row.id), '?'), f.row.id),
                                '%d lines, subtitle limit %d' % (n, SCENE_ROWS))
            if store == 'script':
                for f, n in pipeline.page_groups(finals):
                    if n > BOX_ROWS and f.translated:
                        err('%s %s' % (line_of.get((store, f.row.id), '?'), f.row.id),
                            'box page has %d rows (limit %d) starting at this message'
                            % (n, BOX_ROWS))
                if any(f.translated for f in finals):
                    counts['containers measured'] += 1
                    try:
                        u = pipeline.container_usage(name, finals, layout)
                    except Exception as e:
                        err('%s.SCR' % name, 'cannot encode: %s' % e)
                        continue
                    if u['bytes'] > SCR_MAX_BYTES:
                        err('%s.SCR' % name, 'container over budget: %d bytes, limit %d'
                            % (u['bytes'], SCR_MAX_BYTES))
                    if u['tokens'] > SCR_MAX_TOKENS:
                        err('%s.SCR' % name, 'dictionary over budget: %d tokens, limit %d'
                            % (u['tokens'], SCR_MAX_TOKENS))
    # duplicates: identical source -> identical target, per store
    for store in STORES:
        by_src = defaultdict(set)
        for r in dumps[store]:
            t = tl.get((store, r.id))
            if t is not None:
                by_src[r.src].add((t, r.id))
        for src, ts in by_src.items():
            if len(ts) > 1:
                counts['duplicate pairs compared'] += len(ts) - 1
                if len(set(t for t, _ in ts)) > 1:
                    ids = sorted(i for _, i in ts)
                    err(line_of.get((store, ids[0]), store),
                        'same source, different targets: %s' % ', '.join(ids))
    return problems, counts


def cmd_check():
    problems, counts = run_check()
    for p in problems:
        print('ERROR ' + p)
    print('examined: ' + ', '.join('%s %d' % (k, v) for k, v in sorted(counts.items())))
    if not counts['unit files']:
        print('note: no unit files under tl/ yet; dumps and layout loaded and consistent')
    if problems:
        print('%d problem(s)' % len(problems))
        return 1
    print('All checks passed')
    return 0


# ================================================================ STATUS

def cmd_status():
    tl = translations()
    layout = load_layout()
    for store in STORES:
        us = units(store)
        done_units = 0
        rows_done = rows_total = ch_done = ch_total = 0
        lines = []
        for u, rows in us.items():
            n = sum(1 for r in rows if (store, r.id) in tl)
            c = sum(len(r.src) for r in rows)
            cd = sum(len(r.src) for r in rows if (store, r.id) in tl)
            rows_done += n
            rows_total += len(rows)
            ch_done += cd
            ch_total += c
            if n == len(rows):
                done_units += 1
                lines.append('  done  %-24s rows %4d  source chars %6d' % (u, len(rows), c))
            elif n:
                lines.append('  part  %-24s rows %4d/%-4d' % (u, n, len(rows)))
        print('%s: units %d/%d, rows %d/%d, source characters %d/%d'
              % (store, done_units, len(us), rows_done, rows_total, ch_done, ch_total))
        for x in lines:
            print(x)
        if store == 'script' and any(k[0] == 'script' for k in tl):
            print('  containers touched (bytes used / limit, free):')
            for name, finals in pipeline.all_finals('script', tl).items():
                if any(f.translated for f in finals):
                    u = pipeline.container_usage(name, finals, layout)
                    print('    %-24s %6d / %d  free %d' % (name, u['bytes'], u['limit'],
                                                         u['limit'] - u['bytes']))
    return 0


# ================================================================ MERGE

def cmd_merge():
    problems, counts = run_check()
    hard = [p for p in problems]
    if hard:
        for p in hard:
            print('ERROR ' + p)
        print('MERGE refused: %d hard error(s)' % len(hard))
        return 1
    tl = translations()
    os.makedirs(BUILD, exist_ok=True)
    dump_ids = {s: set(r.id for r in read_dump(s)) for s in STORES}
    unmatched = [k for k in tl if k[1] not in dump_ids[k[0]]]
    for store in STORES:
        out = os.path.join(BUILD, '%s_merged.tsv' % store)
        n_t = 0
        with open(out, 'w', encoding='utf-8', newline='\n') as f:
            f.write('# merged %s store: id <TAB> context <TAB> T|S <TAB> final text (wrapped)\n' % store)
            for name, finals in pipeline.all_finals(store, tl).items():
                for x in finals:
                    f.write('%s\t%s\t%s\t%s\n' % (x.row.id, x.row.ctx, 'T' if x.translated else 'S',
                                                 x.text))
                    n_t += x.translated
        print('wrote %s (%d translated rows)' % (rel(out), n_t))
    print('keys that never matched the dump: %d' % len(unmatched))
    for k in unmatched:
        print('  %s/%s' % k)
    return 1 if unmatched else 0


# ================================================================ EXTRACT

def cmd_extract(arg, force=False):
    if '/' not in arg:
        print('usage: assemble.py extract <store>/<unit>   (see `assemble.py units <store>`)')
        return 2
    store, unit = arg.split('/', 1)
    us = units(store)
    if unit not in us:
        print('no unit %s in store %s' % (unit, store))
        return 2
    p = unit_path(store, unit)
    if os.path.exists(p) and not force:
        print('%s exists; pass --force to overwrite' % rel(p))
        return 2
    os.makedirs(os.path.dirname(p), exist_ok=True)
    rows = us[unit]
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        for h in unit_header(store, unit, rows):
            f.write(h + '\n')
        for r in rows:
            f.write('%s\t%s\t%s\t\n' % (r.id, r.ctx, r.src))
    print('wrote %s (%d rows, %d source characters)' % (rel(p), len(rows),
                                                        sum(len(r.src) for r in rows)))
    return 0


def cmd_units(store=None):
    for s in ([store] if store else STORES):
        for u, rows in units(s).items():
            print('%s/%s\t%d rows\t%d chars' % (s, u, len(rows), sum(len(r.src) for r in rows)))
    return 0


# ================================================================ REFRESH / BUILD (human-only)

def sha256(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def need_originals():
    missing = [f for f in ('SCRIPT.PAK', 'AbyssBoat.exe') if not os.path.exists(os.path.join(ORIGINAL, f))]
    if missing:
        print('original/ is missing %s. Copy them from the game disc (human-only step).'
              % ', '.join(missing))
        sys.exit(2)


def cmd_refresh():
    need_originals()
    pak = os.path.join(ORIGINAL, 'SCRIPT.PAK')
    exe_path = os.path.join(ORIGINAL, 'AbyssBoat.exe')
    ents = lac.read(pak)
    order = sorted(ents, key=lambda e: (e[0].startswith('$'), e[0]))
    script_rows, scene_rows = [], []
    layout = {'scripts': {}, 'aliases': {}}
    seen = {}
    for name, data in order:
        base, ext = name.rsplit('.', 1)
        h = hashlib.sha1(data).hexdigest()
        if h in seen:
            layout['aliases'][base] = seen[h]
            continue
        seen[h] = base
        if ext == 'SCR':
            ex = scr.extract(data)
            if not ex:
                continue
            for e in ex:
                src = codec.decode_game(e['text'], 'script')
                assert codec.encode_source(src, 'script') == e['text'], name
                if e['kind'] == 'm':
                    rid = '%s/%04d' % (base, e['index'] + 1)
                    ctx = 'msg spk=%s%s' % ('-' if e['speaker'] is None else e['speaker'],
                                           ' +' if e['cont'] else '')
                else:
                    rid = '%s/s%02d' % (base, e['index'])
                    ctx = 'choice' if e['choice'] else 'text'
                script_rows.append(Row(rid, ctx, src))
            lay = scr.fixed_layout(data)
            s = scr.Script(data)
            lay['seed'] = [w.hex() for w in s.words if scr.is_japanese(w)]
            layout['scripts'][base] = lay
        elif ext == 'SCE':
            for k, sub in enumerate(sce.parse(data)['subs'], 1):
                src = codec.decode_game(sub['text'], 'scene')
                assert codec.encode_source(src, 'scene') == sub['text'], name
                scene_rows.append(Row('%s/%02d' % (base, k), 'sub %d-%d' % (sub['start'], sub['end']), src))
    sys_rows = []
    for e in exe.entries(open(exe_path, 'rb').read()):
        src = codec.decode_game(e['text'], 'system')
        assert codec.encode_source(src, 'system') == e['text'], e['id']
        sys_rows.append(Row(e['id'], '%s slot=%d' % (e['renderer'], e['slot'] - 1), src))
    write_dump('script', script_rows)
    write_dump('scene', scene_rows)
    write_dump('system', sys_rows)
    with open(LAYOUT_FILE, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(layout, f, indent=1, sort_keys=True)
        f.write('\n')
    with open(ORIGINALS_FILE, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'SCRIPT.PAK': sha256(pak), 'AbyssBoat.exe': sha256(exe_path)}, f, indent=1)
        f.write('\n')
    print('script %d rows, scene %d rows, system %d rows; layout for %d scripts'
          % (len(script_rows), len(scene_rows), len(sys_rows), len(layout['scripts'])))
    return 0


def cmd_build():
    need_originals()
    pins = json.load(open(ORIGINALS_FILE))
    for f, h in pins.items():
        if sha256(os.path.join(ORIGINAL, f)) != h:
            print('original/%s does not match dumps/originals.json; refusing to build' % f)
            return 2
    problems, _ = run_check()
    if problems:
        for p in problems:
            print('ERROR ' + p)
        print('BUILD refused: %d error(s)' % len(problems))
        return 1
    tl = translations()
    layout = load_layout()
    out_dir = os.path.join(BUILD, 'game')
    os.makedirs(out_dir, exist_ok=True)
    raw = lac.read_raw(os.path.join(ORIGINAL, 'SCRIPT.PAK'))
    data = dict(lac.read(os.path.join(ORIGINAL, 'SCRIPT.PAK')))
    script_f = pipeline.all_finals('script', tl)
    scene_f = pipeline.all_finals('scene', tl)
    alias_of = layout['aliases']
    new_entries = []
    changed = 0
    for name, comp, stored in raw:
        base, ext = name.rsplit('.', 1)
        key = alias_of.get(base, base)
        new = None
        if ext == 'SCR' and key in script_f and any(f.translated for f in script_f[key]):
            finals = script_f[key]
            msgs = [pipeline.encode_final('script', f) for f in finals
                    if pipeline.ctx_kind(f.row.ctx) == 'msg']
            strs = {int(f.row.id.split('/s')[1]): pipeline.encode_final('script', f)
                    for f in finals if pipeline.ctx_kind(f.row.ctx) != 'msg'}
            new, (chars, words, enc) = scr.rebuild(data[name], msgs, strs)
            pred = pipeline.container_usage(key, finals, layout)['bytes']
            if pred != len(new):
                raise SystemExit('internal: MEASURE predicted %d bytes for %s, BUILD made %d'
                                 % (pred, name, len(new)))
        elif ext == 'SCE' and key in scene_f and any(f.translated for f in scene_f[key]):
            new = sce.rebuild(data[name], [pipeline.encode_final('scene', f) for f in scene_f[key]])
        if new is None:
            new_entries.append((name, comp, stored))
        else:
            new_entries.append((name, 0, new))
            changed += 1
    lac.write(os.path.join(out_dir, 'SCRIPT.PAK'), new_entries)
    sys_f = pipeline.all_finals('system', tl)['*']
    texts = {f.row.id: pipeline.encode_final('system', f) for f in sys_f if f.translated}
    name_b = codec.encode_target(codec.NAME_TEXT)
    patched = exe.patch(open(os.path.join(ORIGINAL, 'AbyssBoat.exe'), 'rb').read(), texts, name_b)
    open(os.path.join(out_dir, 'AbyssBoat.exe'), 'wb').write(patched)
    print('build/game/SCRIPT.PAK: %d of %d files replaced' % (changed, len(raw)))
    print('build/game/AbyssBoat.exe: %d strings replaced, player name %s' % (len(texts), codec.NAME_TEXT))
    print('Copy both over the installed game (back up the originals first).')
    return 0


def main(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__)
        return 0
    cmd = argv[0]
    if cmd == 'check':
        return cmd_check()
    if cmd == 'status':
        return cmd_status()
    if cmd == 'merge':
        return cmd_merge()
    if cmd == 'extract':
        return cmd_extract(argv[1] if len(argv) > 1 else '', '--force' in argv)
    if cmd == 'units':
        return cmd_units(argv[1] if len(argv) > 1 else None)
    if cmd == 'refresh':
        return cmd_refresh()
    if cmd == 'build':
        return cmd_build()
    print('unknown command %s' % cmd)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
