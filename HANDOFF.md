**Last updated: 2026-10-04** — setup committed locally (340f6d0 project block, dfc1e31 tools, 0795af0 flags/glossary/prompt); `git push` refused 403; calibration translator dispatched on NO4_BAR.p01.

## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main` is
at the close commit (`CLAUDE.md` Rule 3). A fresh container may clone shallow with a stale local ref:
preflight is `git fetch origin main && git checkout main && git reset --hard origin/main`.

## NEXT ACTION — always current, always a literal instruction
> **Setup in progress (attended, no watchdog).** Blocked on GitHub write access: `git push origin
> main` returns 403 ("Claude doesn't have GitHub access to DanaCrysalis/AbyssBoatTranslation"). The
> human gives the Claude GitHub App write access to the repo. Then: push local `main` (the three
> setup commits and this one), push `tl/script-NO4_BAR.p01`, open its PR, run the reviewer on it,
> fill PROJECT.md §4 tiers and `translation_prompt.md` §0.2/§5 from it, commit `setup:
> calibration`, ask the human for the go-ahead (setup SKILL §6).
> **If this container was lost:** the setup commits were never pushed — re-run `/translate`.

## Progress
| Store | Done | Total | |
|---|---|---|---|
| script | 0 | 38 units · 1,709 rows | from STATUS |
| scene | 0 | 4 units · 190 rows | from STATUS |
| system | 0 | 5 units · 188 rows | blocked whole (F-006) |

Containers under the `PROJECT.md` §7 warning threshold (2,000 bytes): none (MEASURE 2026-10-04; tightest `NO4_BAR.SCR` 42,096 free).

## In flight
| Unit | Branch | Agent | Round | PR | Last event | Next |
|---|---|---|---|---|---|---|
| script NO4_BAR.p01 (calibration) | `tl/script-NO4_BAR.p01` (local; push blocked) | translator | 0 | no PR yet | dispatched 2026-10-04 | translator commits locally → runner pushes and opens the PR → reviewer |

## Next up
Wave 1, if the calibration merges: script NO4_BAR.p02 (1,405 chars), NO4_BAR.p03 (1,307),
NO4_BAR.p04 (1,466) — all `NO4_BAR.SCR`, 42,096 free, tier D — plus scene OP-SCN034 (794 chars,
geom). Related shipped work: NO4_BAR.p01. NO4_BAR_T.p01 is a draft of the same scene with
`【Name】` speaker labels — use it to name speakers (F-009).

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
1. **GitHub write access** — `git push` → 403. Give the Claude GitHub App access to
   DanaCrysalis/AbyssBoatTranslation (https://github.com/apps/claude/installations/select_target),
   or reconnect GitHub at https://claude.ai/connect-github. Nothing can merge until then.
2. **System store** (5 units, 188 rows) — exe slots too short for English; you chose to wait for an
   exe patch that repoints the tables · F-006.
3. In-game checks: first built patch (F-001), subtitle width (F-002), choice width (F-003), box
   chains past 4 rows (F-010). Optional: font hack (F-004), text in images (F-005).

## Decisions this run
- Units bundled per deck (≤ 60 messages), `_T` test scripts last; scenes packed in story order — PROJECT.md §2, F-008.
- Dispatch in story order NO4 → NO5 → NO6 → NO3 → NO2 → NO1 → SPACESHIP — PROJECT.md §2.
- System store blocked whole until an exe patch — PROJECT.md §4, F-006.
- `spk=N` is not a speaker id; name speakers from content — PROJECT.md §5.3, F-009.
- `build/abyss_boat_script.ods` regenerated and committed at every wave close — PROJECT.md §2.
- Unattended, waves of 4 (3 script + 1 scene while scenes last) — PROJECT.md §10.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|

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
