# PROJECT.md — the project block

Everything in this suite that is specific to one game, engine, tool set, repository or language pair
lives here and nowhere else. `CLAUDE.md`, the `/translate` skill and the three agent definitions
refer to these sections by number and never repeat the values. **Nobody fills this file by hand.**
The setup skill (`.claude/skills/setup/SKILL.md`, run by `/translate` on first use) infers what the
repo can tell it, asks the human the rest in one batch, shows the completed block, and commits it on
confirmation. The runner's preflight refuses to start a wave while any field still holds the fill
marker (the preflight greps for it; this paragraph deliberately does not spell it out).

Keep this file factual and short. Reasoning goes in `docs/`, `rulings.md` or `FLAGS.md`. After
setup, the only agent that edits it is the reviewer, and only to add a CHECK blind spot to §7. A
filled example is `docs/PROJECT.example.md`.

## 1. Identity

| Field | Value |
|---|---|
| Game | Abyss Boat (アビスボート), Leaf, Windows (DirectX 8), 2001 — retail CD `AB_01`, volume `ABYSS_BOAT` |
| Source language → target language | Japanese → English |
| GitHub owner / repo | DanaCrysalis / AbyssBoatTranslation |
| Integration branch | `main` — **not configurable** (CLAUDE.md Rule 3) |
| Model alias and effort | `opus` at `high` — lowered from `max` by the human on 2026-10-06 to save usage <!-- set in .claude/settings.json and in the frontmatter of the two skills and the three agents; change them together --> |
| What the human expects | Fully unattended, waves of 4; reads `HANDOFF.md` when they like. Wants `build/abyss_boat_script.ods` (every row, Japanese beside English) regenerated and committed at every wave close. Does in-game checks when HANDOFF → Blocked asks (F-001–F-003, F-010). The system store waits for an exe patch (F-006). |

## 2. Stores and units

| Store | Source dump | Unique-lines file | Unit of work | Unit file pattern | Hard limits | Unit file keeps source text? |
|---|---|---|---|---|---|---|
| script — `SCRIPT.PAK` room scripts (`*.SCR`), 1,709 rows | `dumps/script.tsv` | n/a | a big room's part of ≤ 60 messages (`NO4_BAR.p01`), or a per-deck bundle of whole small rooms, ≤ 60 messages (`NO2.b01`); the `_T` test scripts bundle apart (`NO4_T.b01`) — 38 units, `python3 tools/assemble.py units script` | `tl/script/<unit>.tsv` | 65,535 bytes per `*.SCR` (MEASURE); message box 28 columns × 4 rows per page, wrapped by the tools; choice and `text` rows one line of 28 columns | yes → keyed; CHECK pairs by source |
| scene — `SCRIPT.PAK` cutscenes (`*.SCE`), 190 subtitles | `dumps/scene.tsv` | n/a | cutscene groups packed whole in story order, ≤ 60 subtitles (`OP-SCN034`) — 4 units | `tl/scene/<unit>.tsv` | no byte limit; 28 columns × 4 lines per subtitle (assumed, F-002) | yes → keyed |
| system — `AbyssBoat.exe` string tables, 188 rows | `dumps/system.tsv` | n/a | one table group: `menus`, `rooms`, `items`, `hints`, `errors` — 5 units | `tl/system/<unit>.tsv` | the slot in each row's context: `fw slot=N` = N bytes at 2 per character, 1 per `{br}`; `ascii slot=N` = N plain ASCII bytes. **Blocked whole until an exe patch (§4, F-006)** | yes → keyed |

**"Keeps source text?" decides the duplicate-gate method** (CLAUDE.md §6 gate 6). Every store here
is keyed: CHECK groups every translated row of every store by its source and prints `duplicate
pairs compared` (identical sources) and `tag-variant pairs compared` (sources identical once `{p}`
`{w}` `{br}` are removed). The reviewer re-runs CHECK and greps the dumps for the glossary
Variants of each term in the unit.

| Field | Value |
|---|---|
| Unit order for dispatch | Story order, as QUEUE prints it (`DECK_ORDER` in `tools/abyss/project.py`). The ship is capsized and the party works down from the bar: script decks NO4 → NO5 → NO6 → NO3 → NO2 → NO1 → SPACESHIP, then the NO4 `_T` test scripts last (F-008); within a deck, big-room parts first, then bundles. Scenes: OP → SCN001 … SCN047 → EPILOG. |
| Batch rule for line-keyed stores | n/a — no line-keyed store |
| `build/` outputs that are tracked in git | `build/abyss_boat_script.ods` — `python3 tools/ods_export.py`, rerun and committed at every wave close |
| Containers known to be tight (name · free bytes · date) | None in script or scene: the largest, `NO4_BAR.SCR`, has 42,096 of 65,535 free untranslated, and English costs ≈ 1 byte per character after the script dictionary (2026-10-04). Exe slots are exact-fit (`camp/001`, `decks/001`, `decks/003`, `misc/45F1FF` have 0–1 bytes free), but the system store is blocked. |

## 3. Commands

Run from the repo root. Python 3 standard library only. No game binaries needed except where marked
human-only. The contract each command must satisfy is `tools/README.md`; `docs/TOOLS.md` documents
them.

| Abstract name | Concrete command | Notes |
|---|---|---|
| CHECK | `python3 tools/assemble.py check` | prints `examined:` counts; one `ERROR` line per problem; last line `All checks passed`, exit 0 — else exit 1 |
| STATUS | `python3 tools/assemble.py status` | per store: units, rows, source characters (tags excluded); per finished unit its slack |
| MERGE | `python3 tools/assemble.py merge` | runs CHECK first and refuses on any error; writes `build/<store>_merged.tsv`; reports keys that never matched |
| UNITCHECK (one unit) | `python3 tools/unitcheck.py <store>/<unit> [file]` | rows per page, columns per line after wrapping, long words, `{br}`/`{p}` diff vs source; exit 1 on a violation or on zero rows examined |
| UNITCHECK (whole store) | `python3 tools/unitcheck.py <store>` | every translated row of the store |
| MEASURE | `python3 tools/measure.py` | full table: every `*.SCR` (bytes, free, tokens), every exe slot (size, used, free), every `*.SCE` |
| QUEUE | `python3 tools/queue_plan.py [store]` | every unit not fully translated, in dispatch order: rows, characters, containers, free bytes, ratio, tier; thresholds and blocked stores read from §4 |
| EXTRACT | `python3 tools/assemble.py extract <store>/<unit>` | writes `tl/<store>/<unit>.tsv` from the dump, targets empty |
| ODS EXPORT | `python3 tools/ods_export.py` | writes `build/abyss_boat_script.ods`: every row of every store in one sheet; read-only |
| BUILD / REFRESH (human-only) | `python3 tools/assemble.py build` · `python3 tools/assemble.py refresh` | need `original/SCRIPT.PAK` and `original/AbyssBoat.exe`; agents never run them |

## 4. Budget

| Field | Value |
|---|---|
| Bytes per **source** character | 2 (Shift-JIS) |
| Bytes per **target** character | 2 — English is written as full-width Latin in Shift-JIS; the font has no single-byte glyphs (`docs/ENGINE.md` §5). Inside a `*.SCR` the dictionary brings it to ≈ 1. The F-004 font hack would change this; not adopted. |
| Bytes per control code · per argument byte | 1 · 1 — `{p}` `{w}` `{br}` `{name}` 1 byte; `{pause:N}` `{num:N}` 2. In the system store `{br}` is `\`, 1 byte. |
| Slack floor per unit | 2,000 bytes free in each `*.SCR` the unit lands in, after MERGE (script); scene has no byte container |
| Reserve kept per container | 2,000 bytes per `*.SCR` |
| Stores blocked whole (engine work first) | system — F-006: the exe tables are fixed-stride and too short for English; an exe patch repointing them must come first |

Ratio, per unit:

```
tag_bytes      = (SLOT − headroom) − BYTES_PER_SOURCE_CHAR × source_char_count
target_budget  = (SLOT − tag_bytes) ÷ BYTES_PER_TARGET_CHAR        # characters, not bytes
budget_ratio   = target_budget ÷ source_char_count
```

For script, SLOT is the unit's `*.SCR` (65,535) and headroom its free bytes, so QUEUE's ratio is
`(free ÷ 2 + chars) ÷ chars`: 12.7 or more for every script unit (lowest: the NO4_BAR parts,
which share one container). That figure understates the room, since English costs ≈ 1 byte per
character after the dictionary; a simulated translation of every script row at 3× the source
length leaves `NO4_BAR.SCR` 32,933 bytes free (2026-10-04). Scenes have no byte limit (QUEUE
prints `geom`). Script and scene are therefore tier D: geometry is the only constraint. The tiers
bite only on the system store, which is blocked.

| Tier | Ratio | What it demands of the first draft |
|---|---|---|
| blocked | < 2.05 | no faithful translation fits; needs an engine change; never dispatched |
| A | 2.05 – 2.16 | terse from the start, contractions mandatory, expect two re-cut passes |
| B | 2.16 – 2.51 | write tight from the first draft, expect one re-cut pass |
| C | 2.51 – 5.02 | translate literally; bytes rarely bind |
| D | > 5.02 | bytes never bind; geometry is the only constraint — do not relax |

| Measurement | Value |
|---|---|
| Natural literal draft ratio (unit, date) | 2.51 — script NO4_BAR.p01, 2026-10-04 (4,525 target ÷ 1,803 source characters, tags excluded; 20 pages over 4 rows) |
| Disciplined draft ratio (unit, date) | 2.16 — script NO4_BAR.p01, 2026-10-04 (3,886 ÷ 1,803; shipped 3,882, 2.15) |
| **Measured floor** — lowest ratio at which a faithful unit has fit | 2.05 — provisional: the disciplined ratio less 5%. No unit has been byte-bound yet (script and scene are tier D); replace it the first time a unit ships below it |

## 5. Format

### 5.1 Charset — the permitted set, nothing outside it
Translators type plain ASCII English; the tools convert it to full-width Shift-JIS (one column, two
bytes per character, space → ideographic space). Permitted: ASCII letters, digits and punctuation;
`'` and `"`, which the tools turn into ‘ ’ and “ ” by context (the font has no straight quotes);
also `…` `‘` `’` `“` `”` `—` (drawn as ―) `‼` `⁉`, and any other character the Shift-JIS font
has. Forbidden: accented or other non-Shift-JIS letters (é → e), tabs, `{` `}` outside tags, raw
`{xNN}` tags. Counts follow the source: `…` glyph for glyph (`……` stays two), `‼` and `⁉` stay one
glyph each (never `!!`/`!?`), `──` → `——`. 「」 and 『』 → `"…"`; （） → `( )`, kept wherever the
source has them (inner thoughts). The system store's `ascii` slots take plain ASCII only, no tags.

### 5.2 Geometry
| Field | Value |
|---|---|
| Text box, columns × visible rows | message box 28 × 4 (verified, `docs/ENGINE.md` §7); subtitles 28 × 4 (assumed); choice options and inline `text` rows one line of 28 (assumed) |
| Preferred width (one column of slack) | 27 for choice and `text` rows and for any line ended by a deliberate `{br}`; messages are wrapped by the tools at 28 |
| Column cost of each runtime insert (name, item, number) | `{name}` 4 ("John"), `{num:N}` 5; both unused by the source |
| Word wrap | The engine breaks mid-word at column 28 (one closing punctuation mark may hang into column 29). The tools word-wrap every translated message and subtitle at spaces before building, so translators write no breaks for width; a `{br}` in a target is a deliberate break. Choice and `text` rows are not wrapped. |
| Boxes not yet widened / unknown row counts | Subtitles (F-002) and choices (F-003): translate to 28 until tested in game. Box chains the source already runs past 4 rows (F-010): add `{p}` so every page fits 4. |

### 5.3 Control codes
| Code | Meaning | May a translator move / add / remove it? |
|---|---|---|
| `{br}` (0x03) | hard line break | move, add, remove — 1 byte each; use it for a deliberate break (a new sentence on its own line where the source does that), never for width; must stay last where the source ends with it |
| `{p}` (0x01) | wait for a click, then clear the box | keep every one; add one at a clause boundary when a page would exceed 4 rows |
| `{w}` (0x02) | wait for a click, keep the box | keep, same count, same order; never last |
| end of message | none — the statement's 0x00 terminator is outside the text | every target ends with the same tag as its source: `{p}`, `{br}`, `{w}` or nothing |
| speaker | `spk=N` in the context column; `+` = continues the previous message's box | `spk=N` is **not** a character id (F-009): one value carries different speakers in one scene. Name the speaker from content and register, never from the slot. |
| `{name}` (0x04) · `{num:N}` (07 N) · `{pause:N}` (06 N) | player name · numeric variable · timed pause | unused by the source; never add |
| everything else | `{xNN}` raw bytes | none in the dumps; never allowed in a target |

Patterns that look like waste but must be preserved: tag-only rows (`{p}`, `{br}`) — copy the tag
as the target so the unit counts as done; `{w}{br}` pairs inside narration; a message ending in
`{br}` followed by a `+` message (the box continues on a new line).

### 5.4 Structural lines that must be byte-identical to the dump
The three `#` header lines of every unit file (`# unit:`, `# rows:`, `# columns:`), and the id,
context and source columns of every row. Only the fourth (target) column is written.

## 6. Language-pair conventions
Katakana names take their natural English spelling, fixed in `glossary.md` (ジョン → John; the full
cast in §1 there). Honorifics and politeness levels are carried by register and word choice, never
by added words: Rob Collison's old-man じゃ/わし speech → old-fashioned diction, no dialect spelling;
William's rough speech → blunt, contracted. Punctuation: 。→ `.`, 、→ `,`, ？→ `?`, ！→ `!`;
counts of `…`, `‼`, `⁉`, `──` follow §5.1. Sentence case; proper nouns capitalised; room and place
names in dialogue are lowercase common nouns ("the bar", "the chapel") unless `glossary.md` scopes
them otherwise. Choice options are short imperatives within 27 columns. A tic's word is fixed in
`glossary.md` §5 and its punctuation follows the source. Supply the pronouns and articles the
source elides. In the `_T` test scripts, keep `【 】` around the speaker name and translate the name.

## 7. Gate specifics and evidence conventions

| Gate | Concrete check for this project |
|---|---|
| 4 — unit budget and geometry | CHECK and UNITCHECK: no page over 4 rows, no subtitle over 4 lines, no choice or `text` row over 28 columns, no word longer than a line. Every `{p}` added and every `{br}` moved, added or removed (UNITCHECK `codes:` lines) is listed in the PR's Flags. Each `*.SCR` the unit lands in keeps ≥ 2,000 bytes free (MEASURE). |
| 5 — container budget | MEASURE: no container negative; any `*.SCR` under 2,000 bytes free named in the review. MERGE: `keys that never matched the dump: 0`. |
| 8 — structure | every target ends like its source; `{w}` count and order unchanged and never last; no `{p}` removed (CHECK); `#` lines, ids, contexts and sources byte-identical (CHECK); `…`, `‼`, `⁉`, `──` counts match the source; `【 】` kept in `_T` files; nothing outside §5.1 (CHECK). |

**Known blind spots of CHECK** — things it does not verify, which the reviewer checks by hand in
every review. Add one the moment it is found (the reviewer may edit this list in an integration
commit); never remove one without a tool PR that closes it.
- Counts of `…`, `‼`, `⁉` and `──` are not compared with the source.
- Speakers: `spk=N` is not a character id (F-009); who speaks, and in what register, is a reading check.
- Glossary conformance (gate 7) is not machine-checked.
- Choice and `text` rows are checked against 28 columns only, not the preferred 27; subtitle and choice limits are assumed (F-002, F-003).
- CHECK does not know whether an added `{p}` or a moved `{br}` was flagged; compare UNITCHECK's `codes:` lines with the PR's Flags.
- Pages are modelled with `{w}` starting a new page; the real engine behaviour past 4 rows is untested (F-010).
- Duplicate pairing needs identical text once `{p}` `{w}` `{br}` are removed; spelling variants and source typos are not paired — census them by the glossary Variants.
- A tag-only row left empty counts as untranslated (STATUS shows `part`), not as an error.
- A word-initial apostrophe after a space or at a segment start ('em, 'cause, 'til, '70s) is curled into an opening quote ‘ by the codec, and CHECK passes it. Avoid the form, or type ’ (U+2019) directly (F-011, rulings R §1.13).
- UNITCHECK's `codes:` lines diff the wrapped text, so every wrap break the tools insert shows as an added `{br}`. Check the PR's Flags against a diff of the authored target's `{br}`/`{p}`/`{w}` sequence with the source's, plus the sentence each `{br}` follows, which catches a `{br}` moved within an unchanged sequence (F-011).
- Message lines ended by an authored `{br}` or by `{w}` are held to 28 by the wrap, not the preferred 27; measure them by hand (F-011).
- Wrap points are not checked for sense. A one-word last row, a line ending in a lone "a" or "I", or a courtesy title split from its name ("Mr. | Collison") passes CHECK and UNITCHECK, which prints column counts but not text. Read the wrapped lines in `build/script_merged.tsv` after MERGE (F-011, rulings R §1.12).

**Line-numbering convention for findings:** the unit file's line number as printed by `grep -n` on
`tl/<store>/<unit>.tsv`, with the row id beside it (`tl/script/NO4_BAR.p01.tsv:12 NO4_BAR/0009`).
CHECK and UNITCHECK print the same numbering. Never cite `dumps/*.tsv` lines or worksheet rows.

## 8. Naming

| Thing | Pattern | Example |
|---|---|---|
| Translator branch | `tl/«store»-«id»` | `tl/script-NO4_BAR.p02` |
| Park branch | `park/«store»-«id»` | `park/script-NO4_BAR.p02` |
| Commit and PR title, unit | `tl: «store» «id» — «measured figure»` | `tl: script NO4_BAR.p02 — 58 rows, max 4 rows/page, NO4_BAR.SCR 40,112 free` · `tl: scene OP-SCN034 — 39 subtitles, max 3 lines` |
| Commit and PR title, park | `park: «store» «id» — «figure», floor «ratio»` | `park: script NO4_BAR.p02 — page of 5 rows at NO4_BAR/0092, floor n/a` |
| Integration commit | `integrate: «unit» — glossary, rulings, flags, handoff` | fixed |
| Handoff commits | `handoff: survey` · `handoff: dispatch wave N` · `handoff: PR #k opened` · `handoff: wave N closed` · `handoff: run complete` | fixed |
| Glossary seed commit | `glossary: provisional seeds for wave N` | fixed |
| Session title and tags | `«project» — wave N` · `["«project»-translation", "wave-N"]` | `Abyss Boat — wave 3` · `["abyssboat-translation", "wave-3"]` |

## 9. Environment

| Question | Answer |
|---|---|
| Is `gh` installed? | Installed, but its token is invalid: every GitHub action uses the GitHub MCP tools with §1's owner/repo. GitHub access has dropped mid-run before (2026-10-04, 403 on git and MCP): a 403 is a §8 stop, recorded in HANDOFF, never retried in a loop |
| Is the claude-code-remote MCP available (`create_session`, `send_later`, `ListAgents`)? | yes |
| If not — fallback for the wave chain | an `orchestrator` subagent per wave, `run_in_background: true`; the run is then **attended** — a human restarts it when the session dies, and HANDOFF → NEXT ACTION says so |
| If not — fallback for the watchdog | none exists; write `NO WATCHDOG — attended run` into NEXT ACTION every turn |
| Is the scratchpad shared between parallel subagents? | assume yes; namespace scratch files regardless |
| Does GitHub accept APPROVE / REQUEST_CHANGES from the bot account on its own PRs? | no — "Can not approve your own pull request" (PR #1, 2026-10-05): the reviewer posts a COMMENT review whose first line is `DECISION:` |
| Does branch deletion succeed after merge? | no — `git push origin --delete` returns 403 (PR #1, 2026-10-05); merged branches stay on origin. A 403 is not a merge signal — `merged: true` plus the squash SHA is |
| Are the game files in the repo (split archives with pinned hashes) or human-only? | human-only: `original/` is git-ignored; hashes pinned in `dumps/originals.json` |
| Worktree location for subagents | `.claude/worktrees/` (gitignored) |

## 10. Wave defaults

| Field | Value |
|---|---|
| Wave size and mix | 4: three script units in QUEUE order plus one scene unit while scene units remain, then four script units; the system store is never dispatched while blocked |
| Re-dispatches per unit before parking | 2 |
| Rework rounds before PARK or a fresh translator | 3 |
| Watchdog interval | 12 minutes for a wave coordinator; 30 minutes for the runner's backstop |
| Usage limits (human, 2026-10-06) | A session (5-hour) or weekly usage limit is a stop, like CLAUDE.md §8's "the human said stop". Whoever hits it records it in HANDOFF → NEXT ACTION with the reset time, deletes its own pending `send_later` watchdogs (`list_triggers` → `delete_trigger`), opens no session and stops. Nothing resumes by itself after the reset: the human restarts the run by telling the runner to continue. |
| HANDOFF line budget | 150 |
