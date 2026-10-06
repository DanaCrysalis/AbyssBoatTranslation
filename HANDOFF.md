**Last updated: 2026-10-06** — wave 2 dispatched: NO4_BAR.p05, p06, p07 and SCN038 (glossary seeds 9797991); coordinator session_018sADRqUwzYCcf65e1pUc63.

## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main` is
at the close commit (`CLAUDE.md` Rule 3). A fresh container may clone shallow with a stale local ref:
preflight is `git fetch origin main && git checkout main && git reset --hard origin/main`.

## NEXT ACTION — always current, always a literal instruction
> **Wave 2 barrier met (PRs #6 p05, #9 p06, #8 p07, #7 SCN038). Review in unit order, one reviewer
> at a time, foreground:** PR #6 (p05) now, then #9 (p06), #8 (p07), #7 (SCN038). `git pull --ff-only`
> after each reviewer. Coordinator session_018sADRqUwzYCcf65e1pUc63; 12-minute watchdog armed there.

## Progress
| Store | Done | Total | |
|---|---|---|---|
| script | 4 units · 259 rows | 38 units · 1,709 rows | from STATUS 2026-10-06 |
| scene | 1 unit · 39 rows | 4 units · 190 rows | from STATUS 2026-10-06 |
| system | 0 | 5 units · 188 rows | blocked whole (F-006) |

Containers under the `PROJECT.md` §7 warning threshold (2,000 bytes): none (MEASURE 2026-10-06; tightest `NO4_BAR.SCR` 36,894 free with p01–p04).

## In flight
| Unit | Branch | PR | State | Next |
|---|---|---|---|---|
| script NO4_BAR.p05 | `tl/script-NO4_BAR.p05` | #6 | PR open, d7386be; NO4_BAR.SCR 36,376 free, ratio 2.22 | reviewer, behind the barrier |
| script NO4_BAR.p06 | `tl/script-NO4_BAR.p06` | #9 | PR open, 3e49f41; NO4_BAR.SCR 36,314 free (alone), ratio 2.16 | reviewer, behind the barrier |
| script NO4_BAR.p07 | `tl/script-NO4_BAR.p07` | #8 | PR open; NO4_BAR.SCR 36,253 free (alone), ratio 2.20 | reviewer, behind the barrier |
| scene SCN038 | `tl/scene-SCN038` | #7 | PR open; max 3 lines/subtitle, ratio 2.05 | reviewer, behind the barrier |

## Next up
Wave 2 (QUEUE 2026-10-06): script NO4_BAR.p05 (58 rows, 1,208 chars, ratio 16.27), NO4_BAR.p06 (58,
1,384, 14.33), NO4_BAR.p07 (58, 1,556, 12.86) — all `NO4_BAR.SCR`, 36,894 free, tier D — plus scene
SCN038 (59 rows, 655 chars, geom, tier D). Glossary seeds: §9, wave 2 rows (9797991). Dispatched — see In flight.
Related shipped work: NO4_BAR.p01–p04, the same bar conversation (voices glossary §7; rulings R §1–§3,
§5); the save prompt is canonical (glossary §6, 19 later rows incl. 0239, 0242, 0341, 0377, 0397);
ふん → "Hmph, …". NO4_BAR_T drafts name speakers (F-009). CHECK blind spots F-012 (`+` glue) and
F-013 (`【Name】` copies unpaired) are new — PROJECT.md §7.

## Remaining
QUEUE order, generated 2026-10-06 (source characters, tags excluded). Script: NO4_BAR.p08 (1125),
NO4_HWR_FRONT.p01 (1088), p02 (1018), p03 (759),
NO4_MACHINER90.p01 (1080), p02 (962), NO4_TOOL_ROOM.p01 (766), p02 (555), NO4.b01 (931),
NO4.b02 (1215), NO5.b01 (1144), NO6.b01 (839), NO6.b02 (495), NO3_CHAPEL.p01 (1068), p02 (1070),
p03 (1039), NO3_NO4.p01 (633), p02 (597), NO3.b01 (1105), NO3.b02 (502), NO2.b01 (1021),
NO2.b02 (829), NO1.b01 (151), SPACESHIP.b01 (159), then the `_T` test scripts (F-008):
NO4_BAR_T.p01 (1426), p02 (1251), p03 (1270), p04 (1189), NO4_T.b01 (607), b02 (735), b03 (414).
Scene (one per wave, waves 3–4): SCN041-SCN046 (773), SCN047-EPILOG (793).

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
| 1 | script NO4_BAR.p02, p03, p04; scene OP-SCN034 | 4 — #5 c7e2986, #3 185beb6, #2 131288b (round 0); #4 42d2db9 (round 0 CHANGES ふん, round 1 MERGE) | 0 | script 4/38 (259 rows), scene 1/4 (39), system blocked; NO4_BAR.SCR 36,894 free. Two usage-limit stops (weekly, then 5-hour), resumed |

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
