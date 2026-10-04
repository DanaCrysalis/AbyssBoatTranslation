---
name: setup
description: Adopt the translation suite for a game — survey the repo and dumps, infer everything the repo can tell you, ask the human only what it cannot, write PROJECT.md with their confirmation, bring the tools up to tools/README.md's contract, calibrate the budget tiers on one unit translated and reviewed through the real roles, and ask for a go-ahead before the unattended loop starts. Runs automatically when /translate finds PROJECT.md incomplete.
model: opus
effort: max
argument-hint: "[nothing, or one of: project | tools | calibrate — to redo that step]"
---

You are setting this repository up to run the translation suite. The person who cloned this suite
does not fill a single field by hand: you infer what the repo can tell you, you ask for what it
cannot, you show every value before you write it, and you stop at the end for one explicit
go-ahead before the unattended loop starts. `CLAUDE.md` is the contract, `PROJECT.md` is the file
you are completing, `tools/README.md` is the contract the tools must meet, `docs/PROJECT.example.md`
shows a finished block.

Setup is **attended** by definition — the human is here — so this phase runs no watchdog, opens no
sessions, and spawns no subagents except the one calibration translator and its reviewer in §5.
Questions are batched; never ask one at a time across turns when you can ask them together.

## 0. Where things stand
`git fetch origin main && git checkout main && git reset --hard origin/main`. Then:
- `grep -n '«FILL»' PROJECT.md` → the fields still open. None left and `$ARGUMENTS` empty → setup is
  done; say so and stop. `PROJECT.md` missing → recreate the skeleton from git history
  (`git log --all --oneline -- PROJECT.md`) before anything else.
- `ls dumps/ tools/ tl/ pending/ build/` — what exists.
- `git remote -v` → owner and repo. Inferred, never asked.
- Environment probes, recorded for PROJECT.md §9: `command -v gh`; whether `create_session`,
  `send_later` and `ListAgents` are in your tool list; whether the Agent tool is (it must be — §5
  needs it). Scratchpad sharing: assume shared.

## 1. Survey the dumps and the tools — infer first, ask later
For each file under `dumps/`, with `head`, `grep -c`, `awk` or short Python — never a whole dump in
context:
- **Line shape.** One message per line? Which brackets delimit tags? Which tag is last on every
  message (the end-of-message code)? Which tag is the most frequent mid-line tag (the likely line
  break)? Which tags follow a page-level tag? Which lines are structural (`===`, `#`, padding,
  header blobs) and how many?
- **Script and encoding.** The source language from the characters present. A unique-lines file
  beside the full dump, and the duplication ratio. Counts: lines, unique lines, characters per unit.
- **Containers.** Headers that print a slot or bank size and headroom.
For each script under `tools/`: docstring and subcommands; whether anything ends with
`All checks passed`; whether thresholds are hardcoded; whether any checker prints an examined-count;
whether anything reads `pending/`. Map what you found onto the seven commands of `tools/README.md`
and write down every gap.

## 2. Ask the human — once, in one batch, only what the repo cannot tell you
Present your inferences as defaults to confirm or correct, and ask only what is genuinely unknown.
The usual batch:
1. Game identity, if no README names it: title, developer, platform, product id, year.
2. **Bytes per target character.** It depends on the font hack — is the target written in the
   game's native double-byte encoding, or in a single-byte font? This halves or doubles every
   budget; it is never guessed.
3. Text box geometry (columns × visible rows), whether the engine word-wraps, and the column cost of
   runtime inserts, if no tool or document states them.
4. Your tag assignments from §1 — line break, page break, wait, end-of-message, speaker channel,
   inserts — shown as guesses to correct, not as a blank list to fill.
5. The tool gaps from §1: does a dumper or inserter exist elsewhere; is there a format document or a
   community tool to build from.
6. Model alias (default `opus` at `max`) and what they expect of the run — fully unattended, or
   watched.
7. Whether the game files may be committed as split archives with pinned hashes, or stay human-only.

Use the AskUserQuestion tool if it is available, otherwise ask in chat, and **end the turn**. Do not
write `PROJECT.md` before the answers arrive.

## 3. Write PROJECT.md — and show it before committing
Fill every section from §1's inferences and §2's answers. Leave `«FILL»` only in §4's measurement
and tier cells, which §5 fills. Show the completed file, or its diff, and ask for one confirmation.
On yes: commit `setup: project block`, push. On corrections: apply, show again.

## 4. Bring the tools up to the contract — and show each change before committing
For each of the seven commands in `tools/README.md`:
- **Exists and conforms** → record its invocation in PROJECT.md §3.
- **Exists but does not conform** — no `All checks passed` terminator, a hardcoded threshold, no
  examined-count, a summary line that drops rows, reads `pending/` — make the smallest change that
  conforms, show the diff, commit `setup: tools — <what>` on confirmation. Setup is the one time a
  tool change goes straight to `main`: there is no reviewer yet and nothing translated yet.
- **Missing but derivable** — STATUS, UNITCHECK, MEASURE, QUEUE and EXTRACT usually are, given a
  working dumper and inserter — write it, show it, commit on confirmation.
- **Missing and not derivable** — no dumper or inserter for the engine — **say so in plain words.**
  The suite cannot ship text it cannot put back. Offer to build one with the human from a format
  document, a community tool or the binary, and do not proceed to §5 until CHECK, MERGE and EXTRACT
  exist and pass.
Then the **positive controls**: plant one violation of each kind CHECK claims to catch — over
budget, outside the charset, over the width, a missing tag, a key that matches nothing — confirm
CHECK fails on each, remove the plants, and record each in `FLAGS.md` → CHECK positive controls.
Anything CHECK should catch and does not goes into PROJECT.md §7's blind-spot list now.

## 5. Calibrate on one unit — a real translation, through the real roles
Pick the first unit in PROJECT.md §2's order whose source count is near the store's median; a tiny
unit calibrates nothing. Seed `glossary.md` §9 PROVISIONAL with the names it and the dumps surface.
Dispatch **one** `translator` subagent with the dispatch template of
`.claude/skills/translate/SKILL.md` §3 plus one line:
`CALIBRATION: before any re-cut, measure and report the ratio of your first literal draft and of
your disciplined draft (contractions, no filler, merged short lines).`
When it returns, run the `reviewer` on its PR exactly as the loop would — one unit, one PR, the
barrier is met — and let it merge or request changes as the gates decide. Then:
- Fill PROJECT.md §4: the two measured ratios; starting bands — **A** from the provisional floor
  (the disciplined ratio less about five percent, the gain the rest of the ladder typically adds)
  up to the disciplined ratio, **B** from there to the natural ratio, **C** from the natural ratio
  to twice it, **D** above; and the floor, marked provisional. These are starting bands: the floor
  becomes measured the first time a unit ships below it, and §4 is updated before QUEUE reads it.
- Fill `translation_prompt.md`: §0.2's two ratios; §1's example line and tag table from the dump;
  §3.1's charset consequences from PROJECT.md §5.1; §5's worked examples from the unit's own lines,
  four to six, each showing one rule, one of them wrong-and-why; Appendix A's list of what CHECK
  verifies.
- Refresh the README status table from STATUS.
Show the human the tiers and the examples. On confirmation commit `setup: calibration`, push.

## 6. Hand over — and ask before the unattended loop starts
`grep -n '«FILL»' PROJECT.md` prints nothing; CHECK passes on `main`; `HANDOFF.md` → NEXT ACTION
reads `Setup complete. Awaiting the human's go-ahead to start wave 1.`; Progress, Next up and
Remaining are filled from STATUS and QUEUE. Commit `handoff: setup complete`, push.

Then ask the human **one question**: start the unattended run now? Say in two sentences what that
means — each wave opens the next wave's session, a watchdog fires every 10–15 minutes, PRs open and
merge into `main` without further confirmation until one of `CLAUDE.md` §8's stop conditions — and
stop. On yes, `/translate` continues from its preflight. On no, the repo is ready and waits; nothing
runs until someone says so.
