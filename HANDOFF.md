**Last updated: 2026-10-26** — wave 6 dispatched: NO5.b01, NO6.b01, NO6.b02, NO3_CHAPEL.p01 (translators running); seeds a376c49.

## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main` is
at the close commit (`CLAUDE.md` Rule 3). A fresh container may clone shallow with a stale local ref:
preflight is `git fetch origin main && git checkout main && git reset --hard origin/main`.

## NEXT ACTION — always current, always a literal instruction
> **Wave 6 coordinator: wait for the four translators** (In flight), re-checking the barrier on each return
> (`ListAgents`; a returned translator with no PR → resume it by `SendMessage`, else a fresh one, same branch).
> Barrier met → reviewer per PR in unit order NO5.b01 → NO6.b01 → NO6.b02 → NO3_CHAPEL.p01, one at a time.

## Progress
| Store | Done | Total | |
|---|---|---|---|
| script | 17 units · 914 rows | 38 units · 1,709 rows | NO4_BAR p01–p08, NO4_HWR_FRONT p01–p03, NO4_MACHINER90 p01–p02, NO4_TOOL_ROOM p01–p02 (rooms complete), NO4.b01, NO4.b02 (deck NO4 complete bar the `_T` scripts); STATUS 2026-10-26 |
| scene | 4 units · 190 rows | 4 units · 190 rows | OP-SCN034, SCN038, SCN041-SCN046, SCN047-EPILOG (store complete) |
| system | 0 | 5 units · 188 rows | blocked whole (F-006) |

Containers under the `PROJECT.md` §7 warning threshold (2,000 bytes): none (MEASURE 2026-10-26; `NO4_BAR.SCR` 37,378 free; `NO4_TOOL_ROOM.SCR` 61,899, 80/80; the NO4.b01/b02 rooms ≥ 63,697).

## In flight
| Unit | Branch | PR | State | Next |
|---|---|---|---|---|
| script NO5.b01 | `tl/script-NO5.b01` | — | translator dispatched 2026-10-26 (round 0); 429 stop, resumed 2026-10-30 | translator opens PR |
| script NO6.b01 | `tl/script-NO6.b01` | #23 | PR open f179006; applying the coordinator's seed-wrap fix (Decisions) | translator pushes, then barrier |
| script NO6.b02 | `tl/script-NO6.b02` | #22 | PR open e7b2766; applying the coordinator's seed-wrap fix (Decisions) | translator pushes, then barrier |
| script NO3_CHAPEL.p01 | `tl/script-NO3_CHAPEL.p01` | — | translator dispatched 2026-10-26 (round 0); 429 stop, resumed 2026-10-30 | translator opens PR |

## Next up
Wave 6 (QUEUE 2026-10-26), four script units: NO5.b01 (58 rows, 1,144 chars, ratio 29.06; NO5_BANK, ENTRANCEL, ENTRANCEM,
HW_L, HW_R, LOCKERROOM, SHOP), NO6.b01 (37, 839, 39.03; NO6_BRIDGE, ENTRANCE, HW_1, HW_2), NO6.b02 (27, 495, 66.38; NO6_HW_3,
HW_4, HW_5, STORAGE, TOOLROOM, WIRELESSROOM), NO3_CHAPEL.p01 (62, 1,068, 27.82; NO3_CHAPEL.SCR 57,297 free); all tier D.
Glossary seeds: on main, a376c49 (§9 wave 6 rows, incl. six fixed cross-unit sentences for NO5/NO6).
Bindings waiting: NO5_BANK/0005 = NO4_SHOP/0006 `"Today's Shipboard Events," it reads.{p}`; NO5_HW_R/0008 = NO4_HWL_BACK/0014
`"Floor Information"{br}` (sign entries R §12.1); NO6_HW_1/0003 = NO6_HW_2/0006 = 0010 = NO4_HWL_FRONT/0011 byte for byte (R §21.4);
NO5_LOCKERROOM/0004–0007 ロッカー "locker", 空のようだ "seems empty" (R §19); 切り刻む/無残に "hacked to pieces"/"brutally" at
NO5_BANK/0008, NO6_BRIDGE/0020 (R §20.1); 振動 "tremor" NO6_HW_4/0001, NO6_TOOLROOM/0003 (R §20.1); チェーンカッター NO6_TOOLROOM/0001;
NO5_ENTRANCEL/0005 reuses NO4_BAR/0142 "Follow me…"; 使えそうな物 hedge family NO5_BANK/0007, NO6_STORAGE/0002 (R §21.3–§21.4 —
keep ようだ/そう); NO3_CHAPEL save prompts = the NO4_BAR ones byte for byte; NO3_CHAPEL/0033 なんだと‼ → "What‼".
Wave 5 lessons: three CHANGES of four — lone "an" wraps (#20), and dropped そう/ようだ hedges the geometry did not force (#19, #18):
tell translators to keep every hedge and scan wraps with a script; reviewers use unique review AND integration branch names.

## Remaining
QUEUE order, generated 2026-10-06 (wave 6 units moved to Next up 2026-10-26) (source characters, tags excluded). Script: NO3_CHAPEL.p02 (1070),
p03 (1039), NO3_NO4.p01 (633), p02 (597), NO3.b01 (1105), NO3.b02 (502), NO2.b01 (1021),
NO2.b02 (829), NO1.b01 (151), SPACESHIP.b01 (159), then the `_T` test scripts (F-008):
NO4_BAR_T.p01 (1426), p02 (1251), p03 (1270), p04 (1189), NO4_T.b01 (607), b02 (735), b03 (414).
Scene: none — store complete (wave 4). Four script units per wave (PROJECT.md §10). 17 script units remain after wave 6's four.

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
- Wave 3 stopped on the 5-hour session limit 2026-10-25 ~02:00 UTC (reviewer of #12, HTTP 429; reset 06:00) and resumed on the human's "continue" 06:50 UTC; the reviewer was resumed by `SendMessage`.
- Wave 4 stopped on the 5-hour session limit 2026-10-25 ~07:50 UTC (reviewer of #14, HTTP 429; reset 11:40) and resumed on the human's "continue" 11:42 UTC; the reviewer was resumed by `SendMessage`.
- Wave 5 stopped on the 5-hour session limit 2026-10-25 ~12:35 UTC (three translators, HTTP 429; reset 16:40) and resumed on the human's "continue" 2026-10-26 01:24 UTC; translators resumed by `SendMessage`.
- Wave 6 seeds: four §9 cross-unit sentences wrapped badly (lone "a"/"I", one-word last rows — NO6.b02 Flag 3, NO6.b01 Flag 4). Coordinator replaced them before review, sent to all three NO5/NO6 translators: 鍵が掛かっていて… `It's locked, so the door won't open.{p}`; 水かさ… `The water… it keeps rising…{w}{br}Must hurry… it's dangerous…{p}`; 水が深すぎて… `The water's too deep… can't… brea… the…{p}`; シャッターで封鎖され(て)… `A shutter has sealed it off. There seems to be no going any further.{p}` (codec.wrap verified). The reviewer updates §9 at integration.
- Wave 6 stopped on the 5-hour session limit 2026-10-26 ~02:20 UTC (all four translators, HTTP 429; reset 06:20) and resumed on the human's "continue" 2026-10-30 11:00 UTC; translators resumed by `SendMessage`, worktrees intact (drafts uncommitted).
- Wave 2 stopped by the human ("stop for now", 2026-10-06 ~14:40 UTC) mid-review and resumed on "continue" 2026-10-25 01:05 UTC; translators resumed by `SendMessage` with worktrees intact.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| setup (calibration) | script NO4_BAR.p01 | 1 — PR #1, squash b1bba74 (round 0 CHANGES, round 1 MERGE) | 0 | script 1/38, scene 0/4, system blocked |
| 1 | script NO4_BAR.p02, p03, p04; scene OP-SCN034 | 4 — #5 c7e2986, #3 185beb6, #2 131288b (round 0); #4 42d2db9 (round 0 CHANGES ふん, round 1 MERGE) | 0 | script 4/38 (259 rows), scene 1/4 (39), system blocked; NO4_BAR.SCR 36,894 free. Two usage-limit stops (weekly, then 5-hour), resumed |
| 2 | script NO4_BAR.p05, p06, p07; scene SCN038 | 4 — #6 c6858ea (round 0); #9 1541592, #8 2a0b375, #7 8ffabc0 (round 0 CHANGES — lone-"a" / one-word wraps, battle-cry count — round 1 MERGE) | 0 | script 7/38 (433 rows), scene 2/4 (98), system blocked; NO4_BAR.SCR 36,357 free. Human stop 2026-10-06, resumed 2026-10-25 |
| 3 | script NO4_BAR.p08, NO4_HWR_FRONT.p01, p02; scene SCN041-SCN046 | 4 — #13 28d44a9, #10 c755736, #11 f8e7b3a (round 0); #12 c39677d (round 0 CHANGES — 0441 modality, 0424 `…、` ruling — round 1 MERGE) | 0 | script 10/38 (589 rows), scene 3/4 (150), system blocked; NO4_BAR.SCR 37,378 free (room done), NO4_HWR_FRONT.SCR 54,522. Session-limit stop, resumed |
| 4 | script NO4_HWR_FRONT.p03, NO4_MACHINER90.p01, p02; scene SCN047-EPILOG | 4 — #14 d7e9398, #15 40c6491 (round 0); #17 8237cd9 (round 0 CHANGES — lone-"an" wrap, 28-col line, 潜入 sibling agreement — round 1 MERGE); #16 1e66f3c (round 0 CHANGES — `:31` step-5 compression — round 1 MERGE) | 0 | script 13/38 (743 rows), scene 4/4 (190, store complete), system blocked; NO4_HWR_FRONT.SCR 54,355 (room done), NO4_MACHINER90.SCR 57,820 (room done). Session-limit stop, resumed |
| 5 | script NO4_TOOL_ROOM.p01, p02, NO4.b01, NO4.b02 | 4 — #21 b01686f (round 0); #20 c60bcc6 (round 0 CHANGES — lone-"an" wraps — round 1 MERGE); #19 77be2cb (round 0 CHANGES — dropped そう hedge — round 1 MERGE); #18 aa4badb (round 0 CHANGES — dropped ようだ/そう hedges — round 1 MERGE) | 0 | script 17/38 (914 rows), scene 4/4, system blocked; NO4_TOOL_ROOM.SCR 61,899 (room done). Session-limit stop, resumed |

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
