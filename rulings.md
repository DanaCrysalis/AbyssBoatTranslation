# Rulings — the reviewer's integration log

<!-- Append-only. Grepped on demand, never read in full. One section per merged or parked PR, written
by the reviewer in its integration commit; nobody else writes here. glossary.md holds the WHAT (one
row per term); this file holds the WHY and the evidence. HANDOFF.md → Decisions points here. -->

Each ruling records: the source string(s) with every variant spelling; the target; the reasoning
with **source-side** evidence (grep counts per store, across every variant — a census on one spelling
or on the target side is not a census); the shipped lines it binds; and whether it adds or corrects a
`glossary.md` row. A correction to an existing row is written out here with every affected line, and
the row's Ruling column points back.

Format:

```
## Unit «store id» (PR #k, MERGED | PARKED, YYYY-MM-DD)
### k.1 «short title»
- Source: `…` (variants: `…`, `…`) — N instances: a in «store», b in «store»
- Target: `…` (c cols)
- Reasoning: …
- Binds: «file:line in PROJECT.md §7's numbering», …
- Glossary: «added §n row | corrected §n row — affected lines listed above | none»
```

A ruling that reverses an earlier one says so by number and says what changes in shipped files.

---
