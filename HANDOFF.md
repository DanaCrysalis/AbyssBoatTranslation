**Last updated: 2026-10-25** — wave 3 dispatched: NO4_BAR.p08, NO4_HWR_FRONT.p01, p02, SCN041-SCN046 (wave 3 coordinator session).

## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main` is
at the close commit (`CLAUDE.md` Rule 3). A fresh container may clone shallow with a stale local ref:
preflight is `git fetch origin main && git checkout main && git reset --hard origin/main`.

## NEXT ACTION — always current, always a literal instruction
> **Wave 3 barrier met.** #13, #12, #10 merged. Review #11 (SCN041-SCN046) now, then close the wave. Session limit hit 2026-10-25 ~02:00, reset 06:00 UTC, resumed 06:50 on "continue".
> Translators that stop are resumed by `SendMessage` (same agent, worktree intact). Watchdog: 12-minute `send_later`.

## Progress
| Store | Done | Total | |
|---|---|---|---|
| script | 7 units · 433 rows | 38 units · 1,709 rows | p01–p07; UNITCHECK whole store 2026-10-25 |
| scene | 2 units · 98 rows | 4 units · 190 rows | OP-SCN034, SCN038; from STATUS 2026-10-25 |
| system | 0 | 5 units · 188 rows | blocked whole (F-006) |

Containers under the `PROJECT.md` §7 warning threshold (2,000 bytes): none (MEASURE 2026-10-25; tightest `NO4_BAR.SCR` 36,357 free with p01–p07).

## In flight
Wave 3, dispatched 2026-10-25, glossary seeds 1c36061 (§9, 15 rows). Base `main`.
| Unit | Branch | PR | State | Next |
|---|---|---|---|---|
| script NO4_BAR.p08 | `tl/script-NO4_BAR.p08` | #12 | **MERGED** — squash c39677d (round 0 CHANGES: 0441 なくていい as prohibition, 0424 `…、` ruling; round 1 MERGE); 52 rows, max 4 rows/page; NO4_BAR.SCR 37,378 free (485/485); CHECK 44 dup pairs; integration: this commit (glossary §2/§3/§6 +8 rows, rulings §11, F-019, F-020) | coordinator: wave close |
| script NO4_HWR_FRONT.p01 | `tl/script-NO4_HWR_FRONT.p01` | #13 | **MERGED** round 0, squash 28d44a9; 53 rows, max 4 rows/page, NO4_HWR_FRONT.SCR 55,011 free (p02 not merged), ratio 2.13; CHECK 38 + 2 pairs; 4 §9 seeds promoted (R §10); wave 4 p03 copies 0013's target at 0144 (R §10.4) | coordinator: wave close |
| script NO4_HWR_FRONT.p02 | `tl/script-NO4_HWR_FRONT.p02` | #10 | **MERGED** round 0, squash c755736; 51 rows, max 4 rows/page; NO4_HWR_FRONT.SCR 54,522 free with p01 (104/150), ratio 2.24; CHECK 46 + 2 pairs; integration: this commit (glossary §2 +8 rows, §6 と書かれている; rulings §12; F-021 room caps, F-022 indent; F-009/F-018 notes); p03 0102 takes `"Beer & Lagers," it reads.` (R §12.4) | coordinator: review #11, then wave close |
| scene SCN041-SCN046 | `tl/scene-SCN041-SCN046` | #11 | PR open, round 0; 52 subtitles, max 4 lines | reviewer, behind the barrier |

## Next up
Wave 4 (written at wave 3 close): from Remaining in QUEUE order — NO4_HWR_FRONT.p03, NO4_MACHINER90.p01,
p02, plus scene SCN047-EPILOG.

## Remaining
QUEUE order, generated 2026-10-06 (wave 3 units moved to Next up 2026-10-25) (source characters, tags excluded). Script: NO4_HWR_FRONT.p03 (759),
NO4_MACHINER90.p01 (1080), p02 (962), NO4_TOOL_ROOM.p01 (766), p02 (555), NO4.b01 (931),
NO4.b02 (1215), NO5.b01 (1144), NO6.b01 (839), NO6.b02 (495), NO3_CHAPEL.p01 (1068), p02 (1070),
p03 (1039), NO3_NO4.p01 (633), p02 (597), NO3.b01 (1105), NO3.b02 (502), NO2.b01 (1021),
NO2.b02 (829), NO1.b01 (151), SPACESHIP.b01 (159), then the `_T` test scripts (F-008):
NO4_BAR_T.p01 (1426), p02 (1251), p03 (1270), p04 (1189), NO4_T.b01 (607), b02 (735), b03 (414).
Scene (one per wave, wave 4): SCN047-EPILOG (793).

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
- Wave 2 stopped by the human ("stop for now", 2026-10-06 ~14:40 UTC) mid-review and resumed on "continue" 2026-10-25 01:05 UTC; translators resumed by `SendMessage` with worktrees intact.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| setup (calibration) | script NO4_BAR.p01 | 1 — PR #1, squash b1bba74 (round 0 CHANGES, round 1 MERGE) | 0 | script 1/38, scene 0/4, system blocked |
| 1 | script NO4_BAR.p02, p03, p04; scene OP-SCN034 | 4 — #5 c7e2986, #3 185beb6, #2 131288b (round 0); #4 42d2db9 (round 0 CHANGES ふん, round 1 MERGE) | 0 | script 4/38 (259 rows), scene 1/4 (39), system blocked; NO4_BAR.SCR 36,894 free. Two usage-limit stops (weekly, then 5-hour), resumed |
| 2 | script NO4_BAR.p05, p06, p07; scene SCN038 | 4 — #6 c6858ea (round 0); #9 1541592, #8 2a0b375, #7 8ffabc0 (round 0 CHANGES — lone-"a" / one-word wraps, battle-cry count — round 1 MERGE) | 0 | script 7/38 (433 rows), scene 2/4 (98), system blocked; NO4_BAR.SCR 36,357 free. Human stop 2026-10-06, resumed 2026-10-25 |

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
