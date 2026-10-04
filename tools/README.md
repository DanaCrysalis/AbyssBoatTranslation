# tools/ — the interface the suite depends on

The suite never assumes a particular engine, so it cannot ship the tools. It ships the **contract**
the tools must meet. Build yours to it, name them in `PROJECT.md` §3, and the process files need no
other change.

## The seven commands

| Name | Must | Must not |
|---|---|---|
| **CHECK** | validate every file under `tl/` against every hard limit — unit bytes, container bytes, tag parity, charset, columns with inserts costed, rows; print one line per problem; end with `All checks passed` and exit 0 only when there are none | build anything; touch `dumps/`; pass on a fragment; read `pending/` |
| **STATUS** | print per-store progress (done / total, characters, instances) and per-unit headroom and slack for finished units | read anything outside `dumps/` and `tl/` |
| **MERGE** | splice every finished unit into the pristine dumps under `build/`; report every key that never matched the dump; refuse to write on any hard error | write outside `build/` |
| **UNITCHECK** | for one unit, or a whole store after MERGE: rows per page, columns per segment, and a per-line diff of the movable control codes against the source | |
| **MEASURE** | real container usage after MERGE, as a **full table** — every container, used, free | hide any row behind a "tightest" summary line |
| **QUEUE** | list every untranslated unit with source count, headroom, ratio, containers touched and blocked status | hardcode a threshold — it reads them from `PROJECT.md` §4 |
| **EXTRACT** | write a unit file from the pristine dump, byte-identical to the dump's unit | |

BUILD and REFRESH exist too, need the game files, and are human-only. REFRESH must reproduce
`dumps/` byte-for-byte from unchanged originals; if it ever does not, stop and look.

## Rules the tools must follow

1. **Every threshold lives in `PROJECT.md` §4, never in source.** A planner that hardcodes a
   blocked-ratio cutoff drifts from the measured floor and keeps printing "dispatchable" for units
   that cannot fit.
2. **Every checker prints how many items it examined.** "No problems" over zero items is a failure,
   not a pass. A duplicate check that paired nothing, a tag-parity check that compared no lines, a
   row check that found no pages — each must say so and exit non-zero.
3. **Positive control once per project.** Plant one violation of each kind, confirm CHECK catches it,
   record each in `FLAGS.md` → CHECK positive controls. A checker that has never failed has never
   been tested.
4. **Known blind spots are documented, not fixed silently.** Whatever CHECK does not verify goes in
   `PROJECT.md` §7 the day it is found, and the reviewer checks it by hand until a tool PR closes it.
   Common ones: a line-keyed store with no tag-parity check; insert column costs applied in one
   store's mode and not the other's; a summary line that drops rows.
5. **One numbering convention.** Every tool prints line references in the convention of
   `PROJECT.md` §7, or says which index it is printing. Three numberings in circulation produced a
   false "correction" of a correct citation once.
6. **Nobody edits a tool to make a check pass.** Tool changes are a PR like any other, reviewed by the
   reviewer, never merged from a translator branch or a coordinator's direct commit. The only
   direct-to-main exception is a read-only planning helper that CHECK does not depend on.
7. **Tools never read `pending/`.** That is what makes parking safe.
8. **One layout table.** Slot and container offsets live in one module shared by every tool, never
   in two copies that can drift.

## Suggested layout
```
tools/
  assemble.py      CHECK · STATUS · MERGE · EXTRACT · BUILD · REFRESH as subcommands
  unitcheck.py     UNITCHECK
  measure.py       MEASURE
  queue.py         QUEUE (read-only; thresholds from PROJECT.md §4)
  <store>.py       the extractor / inserter for each store
  layout.py        the ONE table of slots and containers
  unpack.py        rebuilds original/ from split archives against pinned hashes, if the project ships them
```
