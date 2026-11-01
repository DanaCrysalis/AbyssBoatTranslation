**Last updated: 2026-11-01** — **run complete.** Wave 11 closed: NO4_T.b03 merged (#42 e909403, 26/27), then F-030 filled NO4_MACHINE_T/s11 by re-cutting shipped NO4_HWR_BACK_T/0010 (#43 83d5b51) and filling s11 (#44 1a7061a), all round 0. Script 38/38 units, 1,709/1,709 rows; scene 4/4, 190/190; system 0/5, blocked (F-006). No dispatchable unit remains.

## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main` is
at the close commit (`CLAUDE.md` Rule 3). A fresh container may clone shallow with a stale local ref:
preflight is `git fetch origin main && git checkout main && git reset --hard origin/main`.

## NEXT ACTION — always current, always a literal instruction
> **Run complete — stop condition holds (CLAUDE.md §8: no dispatchable unit left).** Script and scene stores are 100% translated;
> the system store (5 units, 188 rows) is blocked until an exe patch repoints its tables (F-006). No session opens a wave 12.
> **The human acts next:** (1) build the patch (`python3 tools/assemble.py build`, needs `original/`) and play-test per Blocked
> item 2 (F-001, F-002, F-003, F-010 — four `text` rows sit at exactly 28 columns, F-003); (2) decide on the exe patch for the
> system store (F-006); then `/translate` resumes with a survey (QUEUE) if new work is unblocked.

## Progress
| Store | Done | Total | |
|---|---|---|---|
| script | 38 units · 1,709 rows | 38 units · 1,709 rows | NO4_BAR p01–p08, NO4_HWR_FRONT p01–p03, NO4_MACHINER90 p01–p02, NO4_TOOL_ROOM p01–p02 (rooms complete), NO4.b01, NO4.b02 (deck NO4 complete bar the `_T` scripts); NO5.b01 (deck NO5 complete); NO6.b01, NO6.b02 (deck NO6 complete); NO3_CHAPEL.p01–p03 (room complete, 150/150); NO3_NO4.p01–p02 (room complete, 61/61); NO3.b01, NO3.b02, NO2.b01, NO2.b02 (decks NO3, NO2 complete); SPACESHIP.b01 (deck SPACESHIP complete); NO1.b01 (deck NO1 complete); NO4_BAR_T.p01–p04 (room complete, 181/181); NO4_T.b01 (NO4_HWR_BACK_T 16/16, NO4_HWR_FRONT_DOWN_T 9/9); NO4_T.b02 (NO4_HWR_FRONT_UP_T 39/39); NO4_T.b03 (NO4_ROOM01_T 14/14, NO4_MACHINE_T 13/13; s11 #44, F-030 closed) (store complete); STATUS 2026-11-01 |
| scene | 4 units · 190 rows | 4 units · 190 rows | OP-SCN034, SCN038, SCN041-SCN046, SCN047-EPILOG (store complete) |
| system | 0 | 5 units · 188 rows | blocked whole (F-006) |

Containers under the `PROJECT.md` §7 warning threshold (2,000 bytes): none (MEASURE 2026-10-31; the NO3/NO2 bundle rooms ≥ 62,822 (NO2_MAINSTORAGE); `NO4_BAR.SCR` 37,378 free; `NO4_TOOL_ROOM.SCR` 61,899, 80/80; the NO4.b01/b02 rooms ≥ 63,697; the NO5 rooms ≥ 63,950; NO6_BRIDGE 63,400, the other NO6 rooms ≥ 64,242; NO3_CHAPEL.SCR 55,247, 150/150; NO3_NO4.SCR 60,727, 61/61; SPACESHIP.SCR 64,874, SPACESHIP_HW.SCR 64,841, 8/8; NO4_BAR_T.SCR 55,244, 181/181 (MEASURE 2026-11-01, after #40); NO4_HWR_BACK_T.SCR 64,023, 16/16 (after #43), NO4_HWR_FRONT_DOWN_T.SCR 64,297, 9/9 (after #39); NO4_HWR_FRONT_UP_T.SCR 63,183, 39/39 (after #38); NO1_CONTROLROOM 64,880, NO1_ENGINEROOM 64,564, NO1_STORAGE 65,180, 8/8; NO4_MACHINE_T.SCR 64,088, 13/13 (after #44), NO4_ROOM01_T.SCR 64,898, 14/14 (MEASURE 2026-11-01, after #42)).

## In flight
Nothing. Wave 11's three PRs are merged: #42 (NO4_T.b03), #43 (NO4_T.b01 0010 re-cut), #44 (NO4_T.b03 s11); rulings R §42–§44.

## Next up
None. Every script and scene unit is merged; the system store is blocked (F-006). A new wave needs the exe patch first.

## Remaining
None. F-030 is done: #43 (0010 re-cut, 83d5b51) and #44 (s11 fill, 1a7061a). Scene: none, store complete (wave 4). No dispatchable unit remains: the run is complete bar the blocked system store (F-006), and wave 11's coordinator writes the final handoff (`handoff: run complete`) instead of opening a wave 12 session.

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
- Wave 7 stopped on the 5-hour session limit 2026-10-30 ~12:00 UTC (all four translators, HTTP 429, mid-draft; reset 15:50) and resumed on the human's "continue" 19:57 UTC; translators resumed by `SendMessage`, worktrees intact (drafts uncommitted).
- Wave 8 stopped on the 5-hour session limit 2026-10-30 ~20:50 UTC (all four translators, HTTP 429, early in drafting; reset 00:50) and resumed on the human's "continue" 2026-10-31 16:44 UTC; translators resumed by `SendMessage` ("continue from the file on disk"), worktrees intact.
- Wave 8 stopped again on the 5-hour session limit 2026-10-31 ~21:05 UTC (reviewer of #31 round 1 and translator of #33 round 1, HTTP 429; reset 21:10) and resumed on the human's "continue" 21:11 UTC; both resumed by `SendMessage`.
- Wave 9 stopped on the 5-hour session limit 2026-10-31 ~23:45 UTC (reviewer of #36, HTTP 429, after the squash-merge 8a1e7ab and before its integration commit; reset 02:10) and resumed on the human's "continue" (relayed by the runner) 2026-11-01 02:12 UTC; the reviewer resumed by `SendMessage` to finish #36's integration.
- Wave 10 stopped on the 5-hour session limit 2026-11-01 ~03:00 UTC (reviewer of #40, HTTP 429, mid-review, before any merge; reset 07:10) and resumed on the human's "continue" (relayed by the runner) 07:12 UTC; the reviewer resumed by `SendMessage`.
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
| 6 | script NO5.b01, NO6.b01, NO6.b02, NO3_CHAPEL.p01 | 4 — #25 4a6819e, #23 388bb77, #22 47b3edc, #24 6fe71ae (all round 0; seeded cross-unit sentences re-cut for wraps before review) | 0 | script 21/38 (1,098 rows), scene 4/4, system blocked; decks NO5, NO6 complete; NO3_CHAPEL.SCR 55,976 (62/150). Session-limit stop, resumed |
| 7 | script NO3_CHAPEL.p02, p03, NO3_NO4.p01, p02 | 4 — #26 56e2531, #29 e6a9aa1, #27 62509c4 (round 0); #28 f45c28a (round 0 CHANGES — 0128 authored-`{br}` line at 28 — round 1 MERGE) | 0 | script 25/38 (1,247 rows), scene 4/4, system blocked; rooms NO3_CHAPEL (55,247 free, 150/150) and NO3_NO4 (60,727, 61/61) complete; F-026 mid-row `{w}` found and fixed. Session-limit stop, resumed |
| 8 | script NO3.b01, NO3.b02, NO2.b01, NO2.b02 | 4 — #32 4ed66e9 (round 0); #30 0a3bbec (round 0 CHANGES — dropped "looks", body "it", 操作パネル phrase — round 1 MERGE); #31 028dcdf (round 0 CHANGES — locker "looks", body "it" — round 1 MERGE); #33 b7e0ea2 (round 0 CHANGES — passive 〜されたのだろうか — round 1 MERGE) | 0 | script 29/38 (1,421 rows), scene 4/4, system blocked; decks NO3 and NO2 complete (rooms ≥ 62,822 free). Two session-limit stops, resumed. Lineage limit: no successor session |
| 9 | script NO1.b01, SPACESHIP.b01, NO4_BAR_T.p01, p02 | 4 — #35 e967004, #36 8a1e7ab (round 0); #34 c5f8a29 (round 0 CHANGES — 知らせる "tell" vs 報告 "report" — round 1 MERGE); #37 baa917b (round 0 CHANGES — 0081 shipped words, 0059 label `{br}` — round 1 MERGE) | 0 | script 33/38 (1,531 rows), scene 4/4, system blocked; decks NO1 and SPACESHIP complete; NO4_BAR_T.SCR 55,261 (94/181). Session-limit stop, resumed |
| 10 | script NO4_BAR_T.p03, p04, NO4_T.b01, b02 | 4 — #41 a64d635, #38 a21408b (round 0); #40 2edb846 (round 0 CHANGES — 0166 からな, 0172 subject — round 1 MERGE); #39 b76838f (round 0 CHANGES — 0002 だろう hedge — round 1 MERGE) | 0 | script 37/38 (1,682 rows), scene 4/4, system blocked; NO4_BAR_T.SCR 55,244 (181/181), NO4_HWR_BACK_T 64,005, NO4_HWR_FRONT_DOWN_T 64,297, NO4_HWR_FRONT_UP_T 63,183. Session-limit stop, resumed |
| 11 | script NO4_T.b03 (+ F-030 follow-up: NO4_T.b01 0010 re-cut) | 3 PRs — #42 e909403 (26/27, s11 bound to shipped 0010 by CHECK, R §42); #43 83d5b51 (0010 → `【Oakland】What, scared?{p}`); #44 1a7061a (s11 filled; F-030 closed) — all round 0 | 0 | **run complete:** script 38/38 (1,709 rows), scene 4/4 (190), system blocked (F-006); NO4_MACHINE_T 64,088 free (13/13), NO4_ROOM01_T 64,898 (14/14), NO4_HWR_BACK_T 64,023 |

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
