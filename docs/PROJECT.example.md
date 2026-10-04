# PROJECT.md — filled example

<!-- Abbreviated from the first project this suite ran, so an adopter can see what a completed block
looks like. Values are that game's; do not copy them into a new PROJECT.md. -->

## 1. Identity
| Field | Value |
|---|---|
| Game | Riot Stars (Hect, PlayStation, SLPS-00829, 1997) |
| Source language → target language | Japanese → English |
| GitHub owner / repo | ehekatlOf / RiotStarsTranslation |
| Integration branch | `main` — not configurable |
| Model alias and effort | `opus` at `max` |
| What the human expects | unattended; reads HANDOFF.md daily; does emulator tests when Blocked asks |

## 2. Stores and units
| Store | Source dump | Unique-lines file | Unit of work | Unit file pattern | Hard limits | Keeps source text? |
|---|---|---|---|---|---|---|
| battle (HEXMAP.BIN, 44 chunks) | `dumps/battle_dump.txt` | n/a | one whole chunk | `tl/battle/chunk_NNN.txt` | 8,192 bytes per chunk; 24 cols × 4 rows | **no** → positional pairing |
| script (SCRIPT.BIN, 44 banks) | `dumps/script_dump.txt` | `dumps/script_unique.txt` (1,430 lines) | 40–60 unique lines | `tl/script/batch_NNN.tsv` | 0xA000 per bank | **yes** → grep |

| Field | Value |
|---|---|
| Unit order | chunk number = chapter order; voices and names accumulate |
| Batch rule | highest occurrence count first, same scene (adjacent dump lines in one bank) together |
| Tracked `build/` outputs | `build/battle_dump_merged.txt`, `build/script_dump_merged.txt` |
| Tight containers | bank 40 · 75 free · bank 41 · 353 · bank 5 · 1,595 · bank 2 · 1,607 (2026-09-12) |

## 3. Commands
| Abstract | Concrete |
|---|---|
| CHECK | `python3 tools/assemble.py check` |
| STATUS | `python3 tools/assemble.py status` |
| MERGE | `python3 tools/assemble.py merge` |
| UNITCHECK (unit) | `python3 tools/rowcheck.py N tl/battle/chunk_NNN.txt` |
| UNITCHECK (store) | `python3 tools/rowcheck.py script` |
| MEASURE | `python3 tools/bankmeasure.py` |
| QUEUE | `python3 tools/queue.py battle` · `python3 tools/queue.py script` |
| EXTRACT | the Python one-liner in the project README (splits the dump, writes the chunk verbatim) |
| BUILD / REFRESH | `python3 tools/assemble.py build` · `refresh` — need `original/` |

## 4. Budget
| Field | Value |
|---|---|
| Bytes per source character | 2 (Shift-JIS) |
| Bytes per target character | **2** — English is written in full-width Latin, mapped by a font hook |
| Bytes per control code · argument byte | 2 · 1 |
| Slack floor | ≥ 50 bytes |
| Reserve per container | 500 bytes |

| Tier | Ratio | Demands |
|---|---|---|
| blocked | < 1.64 (measured floor) | slot extension needed |
| A | 1.64 – 1.7 | terse, contractions mandatory, two passes |
| B | 1.7 – 2.5 | tight first draft, one re-cut |
| C | 2.5 – 4.0 | literal |
| D | > 4.0 | geometry only |

Natural draft 2.1× · disciplined 1.7× (chunk 0, 2026-08) · floor 1.64× (chunk 0 shipped at 8,163 / 8,192).

## 5. Format
- **5.1 Charset:** full-width Latin, digits and the listed full-width punctuation only; `’` not `'`;
  `“ ”` for 『』; `．．．` for `・・・` with the source's dot count; `○□△×` → spelled button names;
  no ASCII anywhere (unmapped, renders as nothing).
- **5.2 Geometry:** 24 × 4 (battle box, widened); prefer 23; name insert costs 7 columns; no word
  wrap — every break is authored; the main-script box is not yet widened (translate to 24, flag).
- **5.3 Codes:** `{FFFE}` break (movable, 2 bytes); `{FCC0}` page clear (addable); `{FC30}` wait
  (keep); `{FFFF}` end (keep, last); `{FC50}`/`{FC51}` channels (keep; a borrow is marked by
  `{FB01}`); `{FC00}{=0000}` name insert, `{FFEC}{=00}{=0n}` item/number inserts (movable within
  sentence). Preserve the `{FCC0}{FFFE}` leading-blank pattern.
- **5.4 Structural:** `=== CHUNK n @ …`, `=== BANK n`, `{PAD n}`, `{PRE n}`, `{HDR:…}`, `#` lines.

## 6. Language-pair conventions
European readings for katakana names (Leon not Lion); `様` → Lady / Lord; politeness carried in
register not added words; menu options keep the leading full-width space (cursor gutter); common-noun
uses of a capitalised place name are lowercase; a tic's word is fixed, its punctuation follows the
source; supply pronouns the source elides.

## 7. Gate specifics
| Gate | Check |
|---|---|
| 4 | bytes ≤ 8,192 with ≥ 50 slack (less only below ratio 2.5, flagged); rowcheck: no page over 4 rows the source did not exceed |
| 5 | bankmeasure: no bank negative; any bank under 2,000 free named |
| 8 | `{FFFF}` last; `===` `{PAD}` `{HDR:}` verbatim; leading `　` on menu options; dot counts; no `…` `・` `○` or ASCII |

Blind spots of CHECK: the script store has **no tag-parity check** (a stray `{FCC0}` passes); a
positional duplicate script that pairs nothing passes; `bankmeasure`'s `tightest:` line hides a row.
Numbering: **the file line as printed by `grep -n` on the unit file**; `script_unique.txt` FILE =
DATA + 5 because of its header.

## 8. Naming
`tl/battle-019` · `park/battle-016` · `tl: battle chunk 019 — 7,912 / 8,192 (280 slack)` ·
`tl: script batch 004 — shop lines, 52 lines / 410 instances` · `park: battle chunk 016 — 8,6xx / 8,192, floor 1.6x` ·
session `Riot Stars — wave N`, tags `["riotstars-translation", "wave-N"]`.

## 9. Environment
`gh` absent → GitHub MCP. Remote MCP present (`create_session`, `send_later`). Scratchpad shared.
GitHub refuses APPROVE and REQUEST_CHANGES from the account → COMMENT reviews with `DECISION:`.
Branch deletion returns 403 → ignore. Game files on `main` as split archives with pinned hashes;
`tools/unpack.py` rebuilds `original/`.

## 10. Wave defaults
Wave of 4: three battle chunks in chunk order + one script batch. Re-dispatch 2. Rework 3.
Watchdog 10–15 min. HANDOFF 150 lines.
