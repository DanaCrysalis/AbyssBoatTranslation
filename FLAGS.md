# FLAGS — the open-issue list

<!-- Not a diary. One entry per issue, id F-NNN, never renumbered. The reviewer appends from PR Flags
in its integration commit; the coordinator moves closed entries to the Closed list at wave close
(one line each). Engine reverse-engineering notes belong in docs/, not here. -->

Entry format:
```
### F-NNN · YYYY-MM-DD · «area» · OPEN | HUMAN | CLOSED
What was observed · where (unit and line, PROJECT.md §7 numbering) · what would resolve it · pointer
```

## Needs a human
<!-- engine patches, binaries, in-game checks, anything that needs the disc or an emulator. Each
entry says exactly what the human does. HANDOFF.md → Blocked mirrors this list with pointers. -->

### F-001 · 2026-10-04 · engine · HUMAN
First in-game test of a built patch: does full-width English display correctly in the message
box, and does a rebuilt room script load and run? · any unit · BUILD with one translated room
(e.g. `script/NO1_CONTROLROOM`), copy `build/game/SCRIPT.PAK` and `build/game/AbyssBoat.exe`
over the installed game (back up first), open that room, examine things · `docs/ENGINE.md` §5.

### F-002 · 2026-10-04 · geometry · HUMAN
Subtitle box size is assumed 28 columns × 4 rows (`tools/abyss/project.py` SCENE_COLS/ROWS);
the Japanese source has a few subtitle lines of 30–51 columns, so the real box may be wider ·
scene store · watch a translated cutscene (SCN001 is short) and report how many full-width
columns fit on a line · `docs/ENGINE.md` §7.

### F-003 · 2026-10-04 · geometry · HUMAN
Choice options and inline lines (`choice`/`text` rows) are assumed to fit 28 columns
(CHOICE_COLS) · script store, e.g. NO2_CABIN_2001/s05 "通風孔に入る" · open a choice in game
with a long English option and report what fits.

### F-004 · 2026-10-04 · font · HUMAN
Full-width English is wide (28 characters a line). A font hack could double that: draw two
Latin letters per glyph in the Shift-JIS code points the translation frees up, or patch the
renderer (0x41F100 / 0x41F8E0) for half-width advance. Optional; changes the bytes-per-character
figure in PROJECT.md §4 if adopted · whole project.

### F-005 · 2026-10-04 · images · HUMAN
Text drawn into images is not in the dumps: `GPARTS.PAK` (camp menu, dialog buttons
DLG*.LGF, map labels) and `PICTDAT.PAK` `*.LGF`. Needs an LGF image extractor/inserter and
an image editor · not started.

### F-006 · 2026-10-04 · system · HUMAN
The executable's string tables are fixed-stride arrays: room names hold 14 full-width
characters, deck names 10, camp help 27, item text 43 (minus breaks). Several Japanese
entries already fill their slot (MEASURE: decks/001, camp/001, items/001). Expect
abbreviations; a code patch that repoints these tables to a larger area would lift the
limit · system store.


## Open
<!-- anything an agent could still act on: a suspected source typo to confirm, a reading to settle
when the other store is translated, a container approaching its threshold -->

### F-007 · 2026-10-04 · scene · OPEN
`SCN002OLD.SCE` looks like an unused older version of SCN002/SCN002A (its lines largely
repeat theirs). Translate it last; the duplicate gate keeps it consistent anyway.


## CHECK positive controls
<!-- One entry per kind of violation deliberately planted and caught by CHECK (tools/README.md rule 3).
A checker that has never failed has never been tested. -->

Planted 2026-10-04 while building the tools, each caught by `assemble.py check` (exit 1), then
removed: system slot overflow (rooms/000) · character outside the font (é) · word longer than a
line · missing ending `{p}` · removed `{w}` (NO3_NO4/0018) · key that matches nothing ·
source column edited · box page of 5 rows · same source with two different targets
(NO4_BAR/s24, s27) · `{br}` last in a menu string. Setup should repeat these on `main`.


## Closed
<!-- id · date · how it closed · pointer to rulings.md or the commit -->
