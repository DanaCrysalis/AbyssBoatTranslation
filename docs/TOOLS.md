# Tools for this project

Python 3 standard library only; run from the repo root. They meet `tools/README.md`'s
contract; this page says how.

| Contract name | Command | Notes |
|---|---|---|
| CHECK | `python3 tools/assemble.py check` | every file under `tl/`; one line per problem; prints what it examined; last line `All checks passed`, exit 0 — else exit 1 |
| STATUS | `python3 tools/assemble.py status` | per store: units, rows, source characters done/total; finished units; script containers touched |
| MERGE | `python3 tools/assemble.py merge` | runs CHECK first and refuses on any error; writes `build/<store>_merged.tsv` (final wrapped text, `T`/`S` per row); reports keys that never matched |
| UNITCHECK (unit) | `python3 tools/unitcheck.py <store>/<unit> [file]` | lines and columns after wrapping, rows per box page (following `+` chains), long words, `{br}`/`{p}` diff vs source |
| UNITCHECK (store) | `python3 tools/unitcheck.py <store>` | every translated row of the store |
| MEASURE | `python3 tools/measure.py` | full table: every `*.SCR` (bytes / 65,535, tokens / 1,499), every exe table (tightest slot), every `*.SCE`; warns under PROJECT.md §4's reserve |
| QUEUE | `python3 tools/queue_plan.py [store]` | every unit not fully translated: rows, characters, containers, free bytes, ratio, tier; tiers and floor read from PROJECT.md §4 |
| EXTRACT | `python3 tools/assemble.py extract <store>/<unit>` | writes `tl/<store>/<unit>.tsv` from the dump, targets empty |
| (list units) | `python3 tools/assemble.py units [store]` | unit names, rows, characters |
| BUILD (human) | `python3 tools/assemble.py build` | needs `original/SCRIPT.PAK` and `original/AbyssBoat.exe` (hashes pinned in `dumps/originals.json`); writes `build/game/SCRIPT.PAK` and `build/game/AbyssBoat.exe` |
| REFRESH (human) | `python3 tools/assemble.py refresh` | regenerates `dumps/` from `original/`; reproduces them byte for byte |

The ONE layout table is `tools/abyss/project.py` (engine limits) plus `dumps/layout.json`
(per-script byte counts MEASURE needs). Policy thresholds are read from `PROJECT.md` §4.
No tool reads `pending/`.

## Unit files

`tl/<store>/<unit>.tsv`, UTF-8, LF, tab-separated, keeps the source:

```
# unit: script/NO1_CONTROLROOM
# rows: 4
# columns: id <TAB> context <TAB> source <TAB> target (empty target = untranslated)
NO1_CONTROLROOM/0003	msg spk=-	エンジンの制御装置のようだ。{br}なぜか正常に稼動しているようだ。{p}	Looks like the engine's control system.{br}For some reason, it's running normally.{p}
```

The three `#` lines, ids, contexts and sources must stay byte-identical to EXTRACT's output;
only the fourth column is written. An empty target falls through to the Japanese.

Units: `script` — one per room file, files over 60 messages split into `.pNN` parts at box
boundaries; `scene` — one per cutscene group (`SCN038` = SCN038A…D, 5C1, 5C2); `system` —
`menus`, `rooms`, `items`, `hints`, `errors`.

## Writing a target

- Type ordinary ASCII English. The tools convert to full-width (one column per character,
  two bytes). `'` and `"` become curly quotes automatically. Also allowed: … ‘ ’ “ ” — (em
  dash) ‼ ⁉ and any character the Shift-JIS font has. Not allowed: accented letters,
  tabs, `{` `}` outside tags.
- **Do not break lines for width.** The tools word-wrap at 28 columns. Use `{br}` only for a
  deliberate break (a new sentence on its own line, as the source does).
- End every target with the same tag as its source: `{p}`, `{br}`, `{w}`, or nothing.
- Keep every `{w}` (and any `{name}`, `{num:N}`, `{pause:N}`); `{p}` may be added to split an
  overfull box, never removed.
- A box page holds 4 rows. A message whose context ends in `+` continues the previous
  message's box: count them together (UNITCHECK does).
- System strings: `fw slot=N` = N bytes, 2 per character and 1 per `{br}` (`{br}` not last,
  not doubled); `ascii slot=N` = N plain ASCII bytes, no tags. Keep printf directives
  (`%s`, `%d`) exactly.
- ‼ and ⁉ are the font's "!!" and "!?" glyphs (Shift-JIS ♂/♀ in the source).
- `{name}` prints "John" (4 columns).
