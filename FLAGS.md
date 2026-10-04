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
entries already fill their slot (MEASURE: camp/001, decks/001, decks/003, misc/45F1FF).
The human chose (2026-10-04, setup) to wait for a code patch that repoints these tables to a
larger area rather than abbreviate: the whole system store is blocked (PROJECT.md §4 "Stores
blocked whole") and never dispatched until the patch exists and the slots in
`dumps/system.tsv` are regenerated · system store.

### F-010 · 2026-10-04 · geometry · HUMAN
Two `+` chains in the shipped scripts run past 4 rows between clicks when `{w}` counts as a page
end, as the tools model it: `NO4_BAR`/0090–0095 (Collison's story, 5 rows from 0092) and the
chain at `NO4_TOOL_ROOM`/0044 (5); also 15 chains in the `_T` test scripts (5–7). Whether the
engine scrolls, clears or overflows there is unknown, so CHECK holds every page to 4 rows and
translators add `{p}` · in game, play the bar conversation where Collison tells how the survivors
ran out of food and report whether a fifth line ever shows in one box · `docs/ENGINE.md` §7.


## Open
<!-- anything an agent could still act on: a suspected source typo to confirm, a reading to settle
when the other store is translated, a container approaching its threshold -->

### F-007 · 2026-10-04 · scene · OPEN
`SCN002OLD.SCE` looks like an unused older version of SCN002/SCN002A (its lines largely
repeat theirs). Since setup bundled the scene groups it sits in unit `OP-SCN034` beside
SCN002/SCN002A, where the duplicate gate keeps its repeated lines identical.

### F-008 · 2026-10-04 · script · OPEN
The six `*_T` room scripts are prototypes or tests, probably never shown: `NO4_ROOM01_T` opens
"選択のテストをします" (testing choices), and `NO4_BAR_T`, `NO4_HWR_BACK_T`,
`NO4_HWR_FRONT_DOWN_T`, `NO4_HWR_FRONT_UP_T`, `NO4_MACHINE_T` are drafts of the shipped rooms
with `【Name】` speaker prefixes · units `NO4_BAR_T.p01`–`p04`, `NO4_T.b01`–`b03`, dispatched
last · resolved by a human checking whether any script or the exe references these names
(needs `original/`); if none does, they may be dropped from the queue.

### F-009 · 2026-10-04 · speaker · OPEN
`spk=N` (first argument of statement 0xA9) is not a character id: `NO4_BAR`/0014–0018 put
William and Rob Collison on the same value, and Oakland is on it at 0002. `docs/ENGINE.md` §3
claimed a fixed slot per character and was corrected in setup. Every translator and reviewer
names speakers from content and register (PROJECT.md §5.3) · would resolve by identifying the
argument's real meaning in the exe (0x42BE28 handler table).


## CHECK positive controls
<!-- One entry per kind of violation deliberately planted and caught by CHECK (tools/README.md rule 3).
A checker that has never failed has never been tested. -->

Planted 2026-10-04 while building the tools, each caught by `assemble.py check` (exit 1), then
removed: system slot overflow (rooms/000) · character outside the font (é) · word longer than a
line · missing ending `{p}` · removed `{w}` (NO3_NO4/0018) · key that matches nothing ·
source column edited · box page of 5 rows · same source with two different targets
(NO4_BAR/s24, s27) · `{br}` last in a menu string. Setup should repeat these on `main`.

Repeated 2026-10-04 in setup, on the setup tools (bundled units), in a scratch copy of the
tree, one plant at a time; every one exited 1 with the message shown, and a clean tree passed
afterwards: container over budget (`NO1_CONTROLROOM.SCR` 70,981 / 65,535 — a 72,000-character
target; 55,800 characters still fit, at ≈ 1 byte a character) · `é` → `charset` · 38-letter
word → `longer than a line` · ending `{p}` dropped → `must end like the source` · `{w}` dropped
(NO3_NO4/0018) → `tags … differ` · unknown key `NO1_CONTROLROOM/9999` → `matches nothing` ·
source column edited → `not byte-identical` · five `{br}`-lines → `box page has 5 rows` ·
NO3_CHAPEL/s09 vs s13 → `same source, different targets` · NO2_MAINSTORAGE/0023 vs
NO4_HWR_FRONT/0128 (`{p}` only differs) → `same text with different tags` · SCN038D/14 vs
NO4_HWR_FRONT/0023 → `same source, different targets` across stores · options/000 108 / 89
bytes → `slot:` · `{br}` last in options/000 → `may not be last or doubled` · OP2/01 in five
lines → `subtitle limit 4` · NO2_CABIN_2001/s05 at 32 columns → `limit 28` · `# rows:` edited →
`header lines differ` · a fifth column → `expected 4 tab-separated columns` · pre-bundling unit
name `NO1_CONTROLROOM.tsv` → `no unit`. Also: MERGE refused with a hard error (exit 1);
UNITCHECK on a unit with nothing translated → `nothing examined` (exit 1).


## Closed
<!-- id · date · how it closed · pointer to rulings.md or the commit -->
