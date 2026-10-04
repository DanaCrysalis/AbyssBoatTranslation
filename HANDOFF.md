**Last updated: «YYYY-MM-DD»** — «one line: what just happened, and the commit that did it».

## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main` is
at the close commit (`CLAUDE.md` Rule 3). A fresh container may clone shallow with a stale local ref:
preflight is `git fetch origin main && git checkout main && git reset --hard origin/main`.

## NEXT ACTION — always current, always a literal instruction
> **Run not started.** Run `/translate`. Because `PROJECT.md` still has `«FILL»` fields, it runs
> setup first (`.claude/skills/setup/SKILL.md`): surveys the repo and dumps, asks the human in one
> batch only what it cannot infer, writes `PROJECT.md` and shows it before committing, conforms the
> tools and proves CHECK fails on planted violations, translates and reviews one calibration unit
> through the real roles, then asks for the go-ahead before wave 1. Nothing is filled by hand.
>
> <!-- From then on this block holds exactly one of:
>   • the spawn to make — "open the wave N session with create_session; seed = SKILL.md §6a; units = Next up";
>   • the re-dispatch or review to run, with unit and round;
>   • the CLAUDE.md §8 stop condition that holds, named, with the measured reason;
>   • "NO WATCHDOG — attended run" when PROJECT.md §9 has no send_later (in addition to the above).
> A session that dies after writing this line and before acting on it resumes correctly. -->

## Progress
| Store | Done | Total | |
|---|---|---|---|
| «store» | 0 | «n» | from STATUS, never hand-counted |

Containers under the `PROJECT.md` §7 warning threshold: none yet measured. <!-- name · free bytes, from MEASURE's full table -->

## In flight
<!-- one row per dispatched unit: unit · branch · translator agent id · round · PR (or "no PR yet") ·
last event · who acts next. "Nothing." when empty — never leave it blank, blank is ambiguous. -->
Nothing.

## Next up
<!-- the next wave exactly as it will be dispatched: unit · source count · ratio / tier · containers
touched · related shipped work. Written by the survey or the previous wave's close. -->
Not yet surveyed.

## Remaining
<!-- everything dispatchable after Next up, in dispatch order, straight from QUEUE. Say when it was
generated; if the queue may be stale, say "STALE — re-survey" here so the next coordinator does. -->
Not yet surveyed.

## Blocked — needs a human
<!-- numbered. Each: what is blocked · the measured reason · exactly what the human does · pointer
(FLAGS id, spec file). Agents never loop on these. -->
None yet.

## Decisions this run
<!-- rulings that change how later units are translated or reviewed: one line each, with a pointer
into rulings.md or FLAGS.md. Not a diary; the reasoning lives at the pointer. -->

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|

## How to resume
1. Preflight per `CLAUDE.md` §4 step 0. CHECK must pass. A `«FILL»` in `PROJECT.md` means setup
   has not finished; `/translate` runs it, attended, and asks before wave 1.
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
