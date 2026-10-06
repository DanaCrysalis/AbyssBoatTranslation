**Last updated: 2026-10-06** — wave 1 review 2 of 4 done: PR #3 (p03) MERGED, squash 185beb6; next review PR #4 (p04).

## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main` is
at the close commit (`CLAUDE.md` Rule 3). A fresh container may clone shallow with a stale local ref:
preflight is `git fetch origin main && git checkout main && git reset --hard origin/main`.

## NEXT ACTION — always current, always a literal instruction
> **Wave 1 barrier met** (PRs #5 p02, #3 p03, #4 p04, #2 OP-SCN034). #5 and #3 MERGED (reviews 1–2 of 4). Coordinator
> `git pull --ff-only`, then runs the `reviewer` subagent in the foreground on **PR #4**, then #2,
> `git pull --ff-only` after each. PR #4 was based before #5 and #3 merged: its review merges main in.
> Cross-PR forms fixed in the p03 review (rulings R §3.2): PR #4 0223/0232 ふん must read "Hmph, …" (not "Hmph.");
> PR #2 keeps "land-based equipment" (SCN011/04) and "the people up top" (SCN011/05). CHANGES → findings verbatim to the same translator (SendMessage), then review again.
> All merged or parked → wave close (orchestrator.md step 6), then open the wave 2 session.

## Progress
| Store | Done | Total | |
|---|---|---|---|
| script | 3 units · 201 rows | 38 units · 1,709 rows | from STATUS 2026-10-06 |
| scene | 0 | 4 units · 190 rows | from STATUS |
| system | 0 | 5 units · 188 rows | blocked whole (F-006) |

Containers under the `PROJECT.md` §7 warning threshold (2,000 bytes): none (MEASURE 2026-10-06; tightest `NO4_BAR.SCR` 37,487 free with p01–p03).

## In flight
| Unit | Branch | Round | State | Next |
|---|---|---|---|---|
| script NO4_BAR.p02 (0062–0119, 58 rows, 1,405 chars) | `tl/script-NO4_BAR.p02` at 14c6a42 | round 0 | **MERGED** PR #5, squash c7e2986; max 4 rows/page, NO4_BAR.SCR 38,625 free, 2.11; dupes grep + CHECK 22 pairs (control 23 + 1); new blind spot F-012 (`+` glue) in PROJECT.md §7; rulings R §2 | done — nothing left on the unit |
| script NO4_BAR.p03 (0120–0177, 58 rows, 1,307 chars) | `tl/script-NO4_BAR.p03` at aee58f8 | round 0 | **MERGED** PR #3, squash 185beb6; max 4 rows/page, NO4_BAR.SCR 37,487 free (p01–p03), 2.37; dupes grep 8,294 pairs + CHECK 23; save prompt canonical (21 rows); cross-PR forms ふん, 地上用の設備, 上の連中 fixed; rulings R §3 | done — nothing left on the unit |
| script NO4_BAR.p04 (0178–0235, 58 rows, 1,466 chars) | `tl/script-NO4_BAR.p04` at 5b9254c | dispatch 1, resumed | **PR #4 open**; max 4 rows/page, NO4_BAR.SCR 38,684 free, 3,023 ÷ 1,466 = 2.06; ふん → "Hmph." overlaps p03 0133 (Flag 10): ruled "Hmph," (R §3.2) | reviewer, next |
| scene OP-SCN034 (OP2/01 … SCN034/02, 39 rows, 794 chars) | `tl/scene-OP-SCN034` at 1862852 | dispatch 1 | **PR #2 open**, template filled; 39/39, max 4 lines, 1,900 ÷ 794 = 2.39 | reviewer, after the barrier |

## Next up
Wave 1 (QUEUE 2026-10-05): script NO4_BAR.p02 (58 rows, 1,405 chars, ratio 15.15), NO4_BAR.p03 (58,
1,307, 16.21), NO4_BAR.p04 (58, 1,466, 14.56) — all `NO4_BAR.SCR`, 39,765 free, tier D — plus scene
OP-SCN034 (39 rows, 794 chars, geom, tier D). Glossary seeds: §9 rows of wave 1 and the setup rows
still provisional (John, Heming, 社長, 殺人鬼, Deck N). Related shipped work: NO4_BAR.p01 — the same
conversation; read it first (voices in glossary §7, conventions in rulings R §1). NO4_BAR_T drafts
the bar scenes with `【Name】` speaker labels: use them to name speakers (F-009); its identical and
tag-variant rows must reuse the shipped wording (F-008).

## Remaining
QUEUE order, generated 2026-10-04 (source characters, tags excluded). Script: NO4_BAR.p05 (1208),
p06 (1384), p07 (1556), p08 (1125), NO4_HWR_FRONT.p01 (1088), p02 (1018), p03 (759),
NO4_MACHINER90.p01 (1080), p02 (962), NO4_TOOL_ROOM.p01 (766), p02 (555), NO4.b01 (931),
NO4.b02 (1215), NO5.b01 (1144), NO6.b01 (839), NO6.b02 (495), NO3_CHAPEL.p01 (1068), p02 (1070),
p03 (1039), NO3_NO4.p01 (633), p02 (597), NO3.b01 (1105), NO3.b02 (502), NO2.b01 (1021),
NO2.b02 (829), NO1.b01 (151), SPACESHIP.b01 (159), then the `_T` test scripts (F-008):
NO4_BAR_T.p01 (1426), p02 (1251), p03 (1270), p04 (1189), NO4_T.b01 (607), b02 (735), b03 (414).
Scene (one per wave, waves 2–4): SCN038 (655), SCN041-SCN046 (773), SCN047-EPILOG (793).

## Blocked — needs a human
1. **System store** (5 units, 188 rows) — exe slots too short for English; you chose to wait for an
   exe patch that repoints the tables · F-006.
2. In-game checks: first built patch (F-001), subtitle width (F-002), choice width (F-003), box
   chains past 4 rows (F-010). Optional: font hack (F-004), text in images (F-005).

## Decisions this run
- Units bundled per deck (≤ 60 messages), `_T` test scripts last; scenes packed in story order — PROJECT.md §2, F-008.
- Dispatch in story order NO4 → NO5 → NO6 → NO3 → NO2 → NO1 → SPACESHIP — PROJECT.md §2.
- System store blocked whole until an exe patch — PROJECT.md §4, F-006.
- `spk=N` is not a speaker id; name speakers from content — PROJECT.md §5.3, F-009.
- `build/abyss_boat_script.ods` regenerated and committed at every wave close — PROJECT.md §2.
- Unattended, waves of 4 (3 script + 1 scene while scenes last) — PROJECT.md §10.
- Calibration (NO4_BAR.p01): さん → "Mr."/"Miss"; `…。`/`──。` absorb the 。; numbers spelled out, dates in digits; no one-word last rows where a faithful rewording exists — rulings R §1.2–§1.12; four CHECK blind spots — PROJECT.md §7, F-011.
- Tiers: literal 2.51, disciplined 2.16, provisional floor 2.05; every script and scene unit is tier D — PROJECT.md §4.
- GitHub refused this repo 2026-10-04 → 05 (403); PR #1 was decided offline and merged when access returned. APPROVE is refused on the account's own PRs (COMMENT reviews) and branch deletion returns 403 — PROJECT.md §9.
- Go-ahead for the unattended run given by the human, 2026-10-05.
- Wave 1 stopped on the account's weekly usage limit 2026-10-05 22:42 UTC (all four translators, HTTP 429) and resumed 2026-10-06 07:27 UTC; stopped again on the 5-hour session limit at 07:41 UTC and resumed 09:05 UTC. The three without a PR were resumed by `SendMessage` (same agent, context and worktree intact), not re-dispatched: not counted against PROJECT.md §10's 2 re-dispatches.
- Effort lowered from `max` to `high` for every role, and a usage limit (session or weekly) is a stop that nothing resumes by itself — human, 2026-10-06 — PROJECT.md §1, §10.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| setup (calibration) | script NO4_BAR.p01 | 1 — PR #1, squash b1bba74 (round 0 CHANGES, round 1 MERGE) | 0 | script 1/38, scene 0/4, system blocked |

## How to resume
1. Preflight per `CLAUDE.md` §4 step 0. CHECK must pass. A fill marker left in `PROJECT.md` means
   setup has not finished; `/translate` runs it, attended, and asks before wave 1.
2. Read NEXT ACTION and do exactly that. If it names a spawn, make it. If it names a stop condition,
   verify the condition still holds before believing it.
3. Reconcile open PRs against In flight. Unknown PR → add it and queue it for review. In-flight unit
   with no branch on `origin` → lost; re-queue it.
4. `ListAgents` before declaring anything lost. Silence is not evidence; a subagent that returned
   nothing is lost, not finished.
5. Arm the watchdog before ending the turn (`CLAUDE.md` Rule 2).

<!-- Writing rules (CLAUDE.md §7): the coordinator and the reviewer write here, never concurrently —
the coordinator pushes before spawning the reviewer and pulls after it. Translators never write here;
their handoff is the PR body. Commit and push after every step. Line budget PROJECT.md §10, enforced
at every wave close: finished waves collapse to one line in Wave history; reasoning moves to
rulings.md or FLAGS.md. Section order is fixed; do not add sections, add rows. -->
