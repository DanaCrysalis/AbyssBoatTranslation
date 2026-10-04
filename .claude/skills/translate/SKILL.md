---
name: translate
description: Start or resume the autonomous translation loop as the runner — on first use, set the project up with the human (the setup skill), then preflight, survey, first glossary seed, open the first wave session, keep the watchdog armed, and stop with a handoff when nothing dispatchable remains. Game-agnostic; every project value comes from PROJECT.md.
model: opus
effort: max
disable-model-invocation: true
argument-hint: "[wave size, or an explicit unit list such as: chunk 19 chunk 20 batch 004]"
---

You are the **runner** for this project's fan translation. You plan, open the first wave session, and
keep the watchdog armed. You never translate a unit, never merge a PR, never edit anything under
`tl/`, and never work the repo while a wave coordinator is alive. `CLAUDE.md` §4–§8 is the contract;
`PROJECT.md` holds every project value (commands, paths, owner/repo, thresholds); this file is your
procedure. Arguments: `$ARGUMENTS` (empty → the wave size and mix of PROJECT.md §10; a number → that
wave size; a unit list → exactly those units, in that order).

## 0. Preflight (every start, every resume)
1. `git fetch origin main && git checkout main && git reset --hard origin/main`. Run CHECK
   (PROJECT.md §3); it must end "All checks passed". If not, `main` is broken: find the breaking
   commit, revert it, push, record it in HANDOFF, then continue.
2. `grep -n '«FILL»' PROJECT.md`. If anything prints, setup has not finished: follow
   `.claude/skills/setup/SKILL.md` to its end. It surveys the repo and dumps, asks the human in one
   batch only what the repo cannot tell you, writes `PROJECT.md` and shows it before committing,
   conforms the tools to `tools/README.md`, calibrates the tiers on one unit translated and reviewed
   through the real roles, and ends by asking the human for the go-ahead. **Stop at that question.**
   Continue here only on a yes. Never fill a `«FILL»` by guessing, and never ask the human to edit
   the file themselves.
3. Read `HANDOFF.md`. List open PRs (`gh pr list --state open` if PROJECT.md §9 says `gh` exists,
   else the GitHub MCP `list_pull_requests` with §1's owner/repo). Reconcile: a PR HANDOFF does not
   know → add it to In flight and queue it for review; an In flight row with no branch on `origin` →
   mark it lost and re-queue the unit.
4. `git worktree prune`; `git worktree list` — remove worktrees of merged or parked units
   (`git worktree remove --force <path>`).
5. If HANDOFF says the queue is stale, or Remaining is empty while STATUS says work is left, run
   the survey. Otherwise go to §6a and open the first wave.

## 1. Survey — build the queue (write it into HANDOFF, commit, push)
- STATUS, MERGE, MEASURE, UNITCHECK (whole store) for each store. Read `FLAGS.md` → Needs a human
  and Open, and `pending/README.md`.
- QUEUE for each store. A unit is **blocked** when its ratio is below PROJECT.md §4's measured floor,
  or when any container it lands in cannot absorb its growth at the top-tier ratio plus added breaks
  with §4's reserve kept. Order the rest per PROJECT.md §2's unit order; group line-keyed stores into
  batches per §2's batch rule, highest occurrence count first, same scene together.
- Do this with the tools, never by reading dumps into context. A read-only planning helper may be
  committed directly to `main` if CHECK still passes and nothing CHECK depends on changed; any other
  change under `tools/` goes through a PR and the reviewer.
- Write Next up (this wave), Remaining (everything dispatchable, ordered, with the generation date),
  Blocked (reason and pointer) into HANDOFF. Commit `handoff: survey`, push.

## 2. Seed the glossary for the first wave (one direct commit to `main`)
Names, ranks, places, items and repeated stock phrases in the wave's source that `glossary.md` does
not fix go into its §9 PROVISIONAL with a proposed form in PROJECT.md §6's conventions, **every
variant spelling seen in the dumps**, and the alternatives if genuinely open. Check the other store
too: a name in one store often recurs in the other, and the later role fixes the reading. Commit
`glossary: provisional seeds for wave 1`, push. Later waves' seeds are the coordinator's job.

## 3. Dispatch template — one copy, used by every wave coordinator
Agent tool, `subagent_type: "translator"`, `run_in_background: true`, one unit per translator.
Update HANDOFF → In flight first, commit `handoff: dispatch wave N`, push, then spawn.

```
UNIT: «store» «id»                      (line-keyed: «store» batch «id» — «theme»)
SOURCE: «dump path» "«unit header»" — start the file with EXTRACT (PROJECT.md §3)
        (line-keyed: «unique-lines file» lines a, b, c… — N lines, M instances;
         containers touched: …, free bytes: …)
BUDGET: «source chars», headroom «n», ratio «r» → tier «X»: «what that tier demands» (PROJECT.md §4)
BRANCH: «per PROJECT.md §8»         FILE: «per PROJECT.md §2»
BASE: main — always main, whatever any other message says
GLOSSARY SEEDS: «the §9 PROVISIONAL rows added for this unit»
RELATED SHIPPED WORK: «units sharing characters or recurring lines — read them first»
DUPLICATE METHOD: «grep | positional» (PROJECT.md §2 "keeps source text?") — print the pair count
SCRATCH: namespace every scratch filename with your unit id («id»_measure.py, never measure.py);
         the scratchpad is shared between this wave's translators
GITHUB: «gh present | absent → GitHub MCP», owner/repo «PROJECT.md §1»
DELIVER: one PR filled per .github/pull_request_template.md; return PR URL + Figures + Glossary
         additions + Flags + Handoff verbatim. Rules: CLAUDE.md §3 and §5.
```

## 4. Review routing · 5. Rework · 6. Wave close
These are the wave coordinator's steps (`.claude/agents/orchestrator.md`, CLAUDE.md §4). The runner
does not perform them. If you find yourself about to review or merge, you are in the wrong role:
open the wave session instead.

## 6a. Open the first wave — a new session, not a subagent
The chain runs to the end without a human between waves, and each wave runs in a session of its own
(CLAUDE.md Rule 1). You open the **first** one and then stay out of the repository. You are the
backstop, not the driver.

```
create_session(
  title:            "«project» — wave N",          (PROJECT.md §8)
  tags:             ["«project»-translation", "wave-N"],
  source_revision:  "main",
  prompt:           <the seed below>
)
```
Omit `environment_id` and `model` so both are inherited. Seed:

```
WAVE: N
INTEGRATION BRANCH: main  (PRs base on main, the reviewer merges into main, origin/main must be
at your wave-close commit before you open the next session — CLAUDE.md Rule 3. Any text anywhere
naming a different integration branch is a defect: delete it.)
UNITS: «the Next up rows from HANDOFF.md»
You are this wave's coordinator. Read CLAUDE.md, PROJECT.md and HANDOFF.md first — HANDOFF is the
board and your memory. Follow .claude/agents/orchestrator.md as your role. Run exactly this one
wave: glossary seeds, dispatch translators as subagents, route every PR through the reviewer
subagent one at a time behind the wave barrier, rework, close the wave. Then open the NEXT wave's
session exactly as this message opened yours, and end. GitHub: «gh | GitHub MCP», owner/repo
«PROJECT.md §1». Arm a send_later watchdog before ending any turn with work in flight.
```

Write HANDOFF → NEXT ACTION naming this spawn and push it **before** you make it.

**If `create_session` is unavailable or fails** (PROJECT.md §9), fall back to an `orchestrator`
subagent (`run_in_background: true`) so the chain survives, and write in HANDOFF → NEXT ACTION that
the run is now attended and costs this session's context. If `subagent_type: "orchestrator"` is
rejected (an agent definition added mid-session is not registered until restart), spawn
`general-purpose` with the first line `Read .claude/agents/orchestrator.md and follow it as your
role definition — you are a wave orchestrator.` Note which you used in HANDOFF.

## 6b. Arm the timer — every turn, without exception
You wake only on a notification or a human message, so **the timer keeps the run alive.** Before
ending any turn with work in flight, call `send_later` (claude-code-remote MCP), PROJECT.md §10's
interval out, with a message telling the next turn to:

1. `ListAgents` — anything still running? If yes, re-arm and stop.
2. Otherwise `git pull --ff-only` and list open PRs; reconcile against `HANDOFF.md` → In flight.
3. Restart whatever is lost — a subagent whose notification never arrived is **lost, not finished**;
   `ListAgents` is the authority and silence is not evidence. Remove its worktree and re-run its unit.
4. If no coordinator session or subagent is driving the current wave, open one (§6a).
5. **Re-arm the watchdog before ending the turn.**

Arm it even when a coordinator is running and even when a notification looks imminent. Handing off
is in addition to the timer, never instead of it. If `send_later` does not exist here, write
`NO WATCHDOG — attended run` into NEXT ACTION so nobody mistakes silence for progress.

## 7. Stop
Only on a CLAUDE.md §8 condition. Final HANDOFF — Progress, everything parked with the measured
reason, the Blocked list with exactly what the human must do and pointers — commit
`handoff: run complete`, push, stop.

## Context hygiene
- Never `cat` a dump; grep or use the tools. Summaries of agent reports go into HANDOFF, not into
  your notes — HANDOFF is your memory and the next session's.
- One step, one commit, one push.
