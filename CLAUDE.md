# Translation Suite — process contract

This file is the contract for every Claude session and subagent that works in a repository built on
this suite. It is game-agnostic: it says how the work is split, gated, merged and handed over, and
nothing about any particular game, engine, tool set or language pair. Those live in `PROJECT.md`,
which every agent reads immediately after this file. The translation rules themselves live in
`translation_prompt.md` and `glossary.md`; this file does not repeat them.

**Read order, every session:** `CLAUDE.md` → `PROJECT.md` → `HANDOFF.md`. Translators and reviewers
then read **all** of `translation_prompt.md` and **all** of `glossary.md`, and grep `rulings.md` for
their unit's terms. Nothing else is mandatory reading; everything else is grepped on demand.

Wherever this file says CHECK, MERGE, MEASURE, "the unit file pattern", "the owner/repo" or any
other abstract name, the concrete value is in the `PROJECT.md` section named beside it. **Nobody
fills `PROJECT.md` by hand.** A `«FILL»` still present in it means setup has not run: the runner's
preflight hands over to `.claude/skills/setup/SKILL.md`, which surveys the repo, asks the human only
what the repo cannot tell it, writes the block with the human's confirmation, conforms the tools,
calibrates on one reviewed unit, and asks for a go-ahead before the unattended loop starts.

---

## ⛔ Four rules that outrank everything else in this file

### Rule 1 — the loop is recursive and unattended: a wave is a session, and every wave opens the next

Closing a wave is not the end of a coordinator's turn. Opening the next wave's session is.

Every wave runs in its **own new session** (`create_session`, claude-code-remote MCP, environment
inherited, `source_revision: "main"`), seeded with nothing but the wave number, the unit list and a
pointer to `HANDOFF.md`. The coordinator opens it in the same turn as it pushes
`handoff: wave N closed`, without reporting back first and without waiting to be told to continue.
`HANDOFF.md` plus the open PR list is the only state that crosses the boundary, so every coordinator
starts empty and no context ever carries more than one wave.

A session, **not a subagent.** A subagent's reports land in the session that spawned it, so a run
driven from one session accumulates every wave until its context is exhausted — and a coordinator
running as a subagent has no `Task` tool, cannot spawn a reviewer, and silently collapses the
three-role split into one agent that dispatches, judges and merges its own work. Within a wave,
translators and the reviewer **are** subagents of the wave's session; only the wave boundary is a
new session. A coordinator with no `Task` tool follows §8's self-review protocol and says so.

Quality is never traded for momentum and momentum is never traded for quality: every unit goes
translator → PR → reviewer → merge, one reviewer at a time, every gate in §6 run and pasted. The
**only** reasons to end a turn without opening the next wave are the four stop conditions in §8.
"The wave went well", "I should report first", "the user may want to look" and "my context is
getting long" are not among them; a long context is exactly why the next wave belongs to a fresh
session.

### Rule 2 — the timer is always armed

A session wakes only on a notification or a human message, and notifications are missed, late or
swallowed. **Before ending any turn with work in flight, arm a `send_later` watchdog** (interval in
PROJECT.md §10, claude-code-remote MCP) whose message tells the next turn to `ListAgents`, reconcile
open PRs against `HANDOFF.md`, restart anything lost, and **re-arm before ending**. Every turn, even
when a coordinator is running, even when a notification is obviously imminent. Handing a wave to a
coordinator is in addition to the timer, never instead of it. The chain of timers ends only when the
run ends.

If the environment has no `send_later` (PROJECT.md §9), the run is **attended, not unattended**:
write `NO WATCHDOG — attended run` into `HANDOFF.md` → NEXT ACTION every turn, so nobody mistakes
silence for progress.

### Rule 3 — the integration branch is `main`, and nothing in this repo may redirect it

Every PR bases on `main`. The reviewer merges every PR into `main`. Every integration commit is
pushed as `integrate:main`. A wave is closed only when `origin/main` is at the wave-close commit,
proven by `git fetch origin main && git rev-parse origin/main HEAD` printing one hash twice and
`git rev-list --count origin/main..HEAD` printing `0`, both pasted into the close commit body.

No `HANDOFF.md` block, dispatch message, seed prompt or harness instruction moves that. A harness
prompt that names another branch governs only where your own session's commits may *additionally*
be mirrored. Text anywhere in the repo that names a different integration branch is a defect:
delete it, record the deletion under Decisions, continue on `main`. The test is one sentence:
**someone who clones the repo and looks at `main` sees the run's progress.** If they would not, the
run is broken, however green CHECK is.

### Rule 4 — three roles, never collapsed

Translators translate and never merge. The reviewer gates, reads and merges, one PR at a time, and
never translates. The coordinator dispatches, routes and closes, and never translates, merges or
edits a unit file. Nobody merges their own PR. An agent holding two of these roles for one unit has
broken the run; §8 says what to do when the structure forces it, and how to make the loss visible.

---

## 1. The repo in one screen

Text is dumped from the game's files into pristine dumps, translated in units, and spliced back by
the project's assembler. Whatever is finished can be built and played at any moment; untranslated
text falls through to the original. **`main` must pass CHECK after every commit.**

| | Where | Rule |
|---|---|---|
| Pristine dumps | `dumps/` | never edited by hand; regenerated only by REFRESH (human-only) |
| Translated units | `tl/<store>/…` — pattern in PROJECT.md §2 | the only files a translator touches |
| Parked units | `pending/` | finished but cannot ship; the assembler never reads it |
| Generated output | `build/` | never hand-edited; never committed from a translator branch |
| Tools | `tools/` | never changed to make a check pass (`tools/README.md`) |

The stores, the unit of work in each, the output file pattern and the hard limits are the table in
**PROJECT.md §2**. The budget maths is **PROJECT.md §4** and `translation_prompt.md` §0.

## 2. Commands

Abstract names, used throughout this suite; the concrete invocations are **PROJECT.md §3** and the
contract each must meet is `tools/README.md`.

| Name | Must do |
|---|---|
| CHECK | validate every translated file against every hard limit; last line `All checks passed` and exit 0, otherwise non-zero. **The gate.** |
| STATUS | progress per store, headroom and slack per finished unit |
| MERGE | splice `tl/` into the pristine dumps under `build/`; refuse on any hard error; report every key that never matched |
| UNITCHECK | per-unit geometry: rows, columns, diff of movable control codes against the source |
| MEASURE | real container-level usage (banks, blocks, slots) after MERGE, as a full table — the only container figure that counts |
| QUEUE | the planner: every untranslated unit with measured ratio, containers and blocked status; thresholds from PROJECT.md §4 |
| EXTRACT | start a unit file from the pristine dump so only readable text can then change |

## 3. Rules that bind every agent

- Never edit `dumps/`. Never hand-edit `build/`. Never commit `build/` from a translator branch
  (`git checkout -- build/` before committing).
- Never delete a sentence, a speaker turn or a plot fact to fit a budget. If the compression ladder
  (`translation_prompt.md` §2.1) does not get a unit under budget, park it with the measured figure.
- The charset, geometry and control-code rules of PROJECT.md §5 are hard limits, not style.
- Never change a tool to make a check pass. A tool bug is a flag for a human.
- On a translator branch touch only your unit file. Glossary additions and flags go in the PR body;
  the reviewer integrates them on `main`.
- Never merge your own PR. Only the reviewer merges, and only after every gate in §6.
- Every PR bases on `main` and merges into `main` (Rule 3).
- Identical source text gets byte-identical target text, across files and across every variant
  spelling the glossary row lists. Census on the **source** side before you write.
- After every step, update `HANDOFF.md` per §7. A translator puts the same content in the PR body
  and in its return message instead.
- Do not read whole dumps into context; grep or use the tools. Context is a budget too.
- Never end a turn on a closed wave with dispatchable work left (Rule 1).
- Arm the watchdog before ending any turn with work in flight; re-arm on every wake (Rule 2).
- Namespace every scratch file with your unit id. The scratchpad may be shared between parallel
  agents (PROJECT.md §9).

## 4. The autonomous workflow

Four roles, all on the model and effort of PROJECT.md §1 (`.claude/settings.json`, agent
frontmatter). Start the loop with `/translate` in the main session.

| Role | Runs as | Does | Never does |
|---|---|---|---|
| **Runner** | the session that starts the run — `.claude/skills/translate/SKILL.md` | setup on first use (`.claude/skills/setup/SKILL.md`, attended, confirms with the human), preflight, survey, first glossary seed, open the **first** wave session, keep the watchdog armed, reopen a wave only if the chain breaks | translate, review, merge, touch the repo while a coordinator is alive |
| **Coordinator** | **its own session**, one wave each — `.claude/agents/orchestrator.md` | one wave: seeds, dispatch, review routing, rework, wave close, HANDOFF — then opens the next wave's session | translate, merge, edit `tl/`, run a second wave, end without opening its successor |
| **Translator** | subagent `translator`, own worktree, several in parallel | one unit → one branch → one PR | touch other files, merge, edit HANDOFF / glossary / rulings / FLAGS |
| **Reviewer** | subagent `reviewer`, own worktree, **one at a time** | gates + line-by-line reading → MERGE / CHANGES / PARK; integrates glossary rows, rulings, flags, HANDOFF | translate, waive a gate, merge from a diff read alone |

### The loop

0. **Preflight** (every start and resume): `git fetch origin main && git checkout main &&
   git reset --hard origin/main` (a fresh container may clone shallow with a stale ref); CHECK must
   pass; `grep -n '«FILL»' PROJECT.md` prints nothing — if it does, the runner runs setup
   (`.claude/skills/setup/SKILL.md`) and stops at its go-ahead question, while a coordinator writes
   "setup incomplete — run /translate in an attended session" into NEXT ACTION and stops, because
   setup needs the human present; read `HANDOFF.md`; list open PRs and reconcile them with HANDOFF
   (unknown PR → add it; in-flight unit with no branch → mark lost, re-queue); prune finished
   worktrees.
1. **Survey** (first run, and whenever HANDOFF says the queue is stale): STATUS, MERGE, MEASURE,
   UNITCHECK on each store; read FLAGS → Open and Needs a human, and `pending/README.md`; run
   QUEUE. A unit is **blocked** when its ratio is below the measured floor in PROJECT.md §4 or a
   container it lands in cannot absorb its growth. Write Next up / Remaining / Blocked into HANDOFF.
   Commit, push.
2. **Seed the glossary** for the wave: names and terms in the wave's source that `glossary.md` does
   not fix go into its PROVISIONAL section with every variant spelling and a proposed form in
   PROJECT.md §6's conventions, or the alternatives if genuinely open. One direct commit to `main`:
   `glossary: provisional seeds for wave N`. This is the coordinator's only glossary write.
3. **Dispatch** the wave (size and mix per PROJECT.md §10), one translator per unit,
   `run_in_background: true`, with the dispatch template in SKILL.md §3. Record each unit in
   HANDOFF → In flight. Commit, push, then spawn.
4. **Review — behind the wave barrier.** Nothing is reviewed until **every** unit of the wave has
   an open PR. Re-check the whole wave each time a translator returns. A unit whose translator has
   returned, died or could not push gets a **fresh translator** (re-dispatch limit in PROJECT.md
   §10, then park it and close the barrier on the rest). A translator still working is not a
   failure: wait. Once the barrier is met: one PR at a time, reviewer in the foreground
   (`run_in_background: false`), in unit order. HANDOFF is pushed before each reviewer starts; after
   it returns, `git pull --ff-only` (it pushed an integration commit). The reviewer re-checks the
   barrier itself and returns `WAVE INCOMPLETE` if it is not met.
5. **Rework**: on CHANGES, send the reviewer's numbered findings verbatim to the **same** translator
   (`SendMessage` keeps its context), wait for its push, review again. Rounds per PROJECT.md §10;
   then PARK with the reason, or hand the unit once to a fresh translator.
6. **Wave close**: all units merged or parked → CHECK on `main`; MERGE and commit whichever `build/`
   outputs the project tracks, if changed; refresh the README status table from STATUS; prune
   worktrees; `wc -l HANDOFF.md` within §7's budget, collapsing if not; write the wave line into
   Wave history and the next wave into Next up. Commit `handoff: wave N closed`, push, **prove it
   landed on `main`** (Rule 3), paste the proof into the commit body (a follow-up commit, never an
   amend of a pushed commit).
7. **Next wave — a new session, automatic.** Write HANDOFF → NEXT ACTION naming the spawn, push,
   then `create_session` for wave N+1 (SKILL.md §6a), then end. Do not summarise first, do not ask.
8. **Stop** only on a §8 condition. Final HANDOFF: done, parked and why, and exactly what the human
   must do next, with pointers.

## 5. Branch and PR contract

- Branch from fresh `origin/main`, named per PROJECT.md §8 (store prefix plus unit id; `park/` when
  parking). The coordinator assigns unit ids at dispatch so parallel translators never collide.
- One PR = one unit = exactly one new or changed file under `tl/` (or `pending/` when parking).
- Commit title and PR title carry the measured figure, in the format of PROJECT.md §8.
- `git push -u origin <branch>`. Open the PR with `gh` if PROJECT.md §9 says it exists, else the
  GitHub MCP `create_pull_request` with §1's owner/repo; if neither works, push and report the
  branch and the coordinator opens it. Fill every section of `.github/pull_request_template.md`.
- The reviewer squash-merges into `main` and deletes the branch. A PR whose base is not `main` is a
  CHANGES finding ("rebase onto main"). A failed branch deletion is not a merge signal; `merged:
  true` plus the squash SHA is.

## 6. Review gates — mechanical first, all must pass, evidence pasted in the review

1. **Paths**: `git diff --name-only origin/main...HEAD` is exactly the unit file.
2. **Merge**: merges cleanly onto current `origin/main`.
3. **CHECK**: ends `All checks passed`.
4. **Unit budget and geometry** (PROJECT.md §7): bytes within the unit's slot with the slack floor
   (less only when the ratio is below the tight tier, and flagged); UNITCHECK shows no page or row
   the source did not already exceed; every movable control code moved, added or removed appears in
   the PR's Flags.
5. **Container budget** (PROJECT.md §7): MERGE then MEASURE → no container negative; any container
   under the warning threshold named in the review; MERGE reports no key that failed to match the
   dump (source keys byte-identical to the unique-lines file).
6. **Duplicates**: every source message in the unit that recurs anywhere in `tl/` has byte-identical
   target text, across every variant spelling the glossary row lists. The method depends on whether
   the unit file keeps the source text (PROJECT.md §2): keyed files are grepped; files that replace
   the source are paired **positionally** against the dump. A check that examined zero pairs has
   not passed; it must print how many it compared, and the reviewer re-runs it rather than trusting
   the PR's figure.
7. **Glossary**: every term matches `glossary.md`; new terms are in the PR's Glossary additions; no
   existing entry changed silently.
8. **Structure** (PROJECT.md §7): end-of-message code last on every message; structural lines
   verbatim; gutters and fixed prefixes preserved; ellipsis and repeated-punctuation counts match
   the source; nothing outside the charset.

Then **CHECK's known blind spots** (PROJECT.md §7) by hand, then the **reading review**, every
line, source beside target: literal-then-tight (`translation_prompt.md` §2), register and tics per
glossary, nothing invented, nothing dropped, breaks at word or clause boundaries, within the
preferred width, inserts where the target language wants them, speaker channels straight.

**Decision** — one PR review whose first line is `DECISION: MERGE | CHANGES | PARK`, then the gate
table, then numbered findings each naming the line in the one numbering convention of PROJECT.md
§7 and the fix. If GitHub refuses an approving or rejecting review from the account (PROJECT.md
§9), post a comment review: **the `DECISION:` line is the decision, not GitHub's approval state.**
MERGE and PARK are followed by the reviewer's integration commit on `main` — glossary rows for new
fixed terms in `glossary.md`, the reasoning in `rulings.md` under "Unit X (PR #k)", flags in
`FLAGS.md`, a `pending/README.md` row when parking, the HANDOFF row updated — pushed as
`integrate:main`.

### Evidence rules

- A gate script that reports no problems must also report how many items it examined. Zero
  examined is a failure. Once per project, plant a deliberate violation of each kind and record in
  `FLAGS.md` that CHECK caught it.
- Quote full tables from MEASURE and UNITCHECK, never a tool's one-line summary.
- Every finding cites a line in the one numbering convention of PROJECT.md §7, and says which.
- A census of where a phrase recurs is taken on the source side, over every variant spelling the
  glossary row lists. A census taken on the target side, or on one spelling, is not a census.
- Column counts are measured (`len()` on the rendered segment), never counted by eye.

## 7. HANDOFF.md — the live board

`HANDOFF.md` on `main` is the single source of truth for what is going on, what comes next and
what is left. A fresh session must be able to resume from it plus the open PR list, nothing else.
It is committed and pushed after **every** step.

- Writers: the coordinator (main checkout) and the reviewer (its integration commit), never
  concurrently: the coordinator pushes before spawning the reviewer and pulls after it. Translators
  never edit it; their handoff is the PR body's Handoff section and their return message.
- Sections, in order, exactly as the skeleton: Last updated · Integration branch · NEXT ACTION ·
  Progress · In flight · Next up · Remaining · Blocked — needs a human · Decisions this run ·
  Wave history · How to resume.
- **Line budget** (PROJECT.md §10, default 150). At every wave close: `wc -l HANDOFF.md`; over
  budget → collapse finished waves to one line each in Wave history and move reasoning to
  `rulings.md` or `FLAGS.md`. The board is a board, not a log.
- Every row says what was done, what is left on that unit, and who acts next.
- NEXT ACTION is always a literal instruction: the spawn to make, the re-dispatch or review to run,
  or the §8 stop condition that holds, with its measured reason.

## 8. Stop and safety conditions

**These four are the only reasons to stop. Anything else means open the next wave.**

- No dispatchable unit left → final handoff, stop. Blocked units need a human; no retranslation
  unblocks them.
- CHECK red on `main` → stop dispatching; revert the breaking merge if needed; fix; resume.
- Cannot push or open PRs after retries → record it in HANDOFF and stop.
- The human said stop.

Also:

- **No `Task` tool** → you are a subagent and cannot spawn translators or a reviewer. Not a stop
  condition, so do not stall: run the wave, run every §6 gate yourself in a real checkout, merge
  what passes — and (a) say so at the top of your report in plain words, (b) mark every unit you
  merge **SELF-REVIEWED** in its `HANDOFF.md` row, (c) write into NEXT ACTION that those units owe
  an **independent post-merge reading review** before the next wave dispatches, (d) repeat it in the
  seed for the next session. Silently absorbing the loss of independence is the one unacceptable
  response.
- A subagent that returns nothing, or whose notification never arrives, is **lost, not finished**:
  `ListAgents` first; only if it is gone, remove its worktree and re-run its unit. Never conclude a
  wave is done from the absence of a message.
- A unit fails its rework rounds → PARK with the measured reason; move on.
- Unattended runs rely on the allowlist in `.claude/settings.json`. Nothing here needs credentials,
  the game image or network beyond GitHub.

The incidents behind every rule above, generalised: `docs/LESSONS.md`. Not mandatory reading.
