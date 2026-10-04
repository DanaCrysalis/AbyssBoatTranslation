# Abyss Boat — English translation

Fan translation of **Abyss Boat** (アビスボート, Leaf, Windows, 2001) from Japanese to English,
run with the translation suite described below.

- **Text** — `dumps/`: `script.tsv` (room scripts, 1,709 rows), `scene.tsv` (cutscene
  subtitles, 190), `system.tsv` (UI strings in the executable, 188). Generated from the
  retail disc by `tools/assemble.py refresh`; never edited by hand.
- **Engine and formats** — `docs/ENGINE.md`. **Tools and the unit-file format** — `docs/TOOLS.md`.
- **Game files are never committed.** `original/` (git-ignored) holds `SCRIPT.PAK` and
  `AbyssBoat.exe` from the disc for the human-only BUILD and REFRESH steps.
- **To start**: open the repo in Claude Code and run `/translate`. On first use it runs
  setup, which completes `PROJECT.md` with you.

---

# translation-suite

A game-agnostic harness for running a fan translation of a tokenised game script as an unattended,
self-continuing loop of Claude Code agents: parallel translators, one reviewer that gates and merges,
a coordinator per wave that opens the next wave's session, a watchdog that never lets the chain die
silently, and a live board that lets any fresh session resume. Extracted from a completed PS1
project and generalised; the incidents behind each rule are in `docs/LESSONS.md`.

What it is **not**: a dumper, an inserter or a font hack. Those are per engine. `tools/README.md`
specifies the seven commands the suite needs from yours.

## Layout

| File | Role | Edited by |
|---|---|---|
| `CLAUDE.md` | the process contract — roles, waves, gates, board, stop rules | nobody, per project |
| `PROJECT.md` | every project-specific value, referenced by section number | setup, with the human's confirmation; the reviewer adds CHECK blind spots |
| `HANDOFF.md` | the live board | coordinator and reviewer |
| `translation_prompt.md` | how to translate under the budget | setup, from the calibration unit |
| `glossary.md` | fixed terms, one row each, read in full before every unit | the reviewer |
| `rulings.md` | the reasoning behind the terms, grepped on demand | the reviewer |
| `FLAGS.md` | open issues | the reviewer; collapsed by the coordinator |
| `pending/` | finished work that cannot ship | translators, via `park:` PRs |
| `tools/README.md` | the command contract the tools must meet | nobody, per project — setup conforms the tools to it |
| `docs/LESSONS.md` · `docs/PROJECT.example.md` | why each rule exists · a filled project block | optional reading |
| `.claude/` | the `/translate` and `setup` skills, the three agent roles, the permission allowlist | nobody, per project |
| `.github/pull_request_template.md` | the PR shape every translator fills | nobody, per project |

## Getting started

1. Copy this repo's contents into the root of your translation repo, next to your `dumps/` and
   `tools/`. Keep the file names: the agents refer to them.
2. Open the repo in Claude Code and run `/translate`.

That is the whole procedure. On first use `/translate` finds `PROJECT.md` unfilled and runs setup
(`.claude/skills/setup/SKILL.md`), which:

- surveys your dumps and tools and infers everything it can — tag syntax, the end-of-message code,
  the likely line break, owner and repo from the git remote, what the environment offers;
- asks you, once, in one batch, only what it cannot infer: the game, the target font's bytes per
  character, the box geometry, corrections to its tag guesses, what to do about missing tools;
- shows you the completed `PROJECT.md` before committing it;
- brings your tools up to `tools/README.md`'s contract, showing each change first, and proves
  CHECK fails on planted violations;
- translates one unit through the real translator → PR → reviewer → merge path, calibrates the
  budget tiers from it, and writes the prompt's worked examples;
- asks you once more before starting the unattended loop, and says what that loop will do.

From then on it runs on its own. Read `HANDOFF.md` whenever you want to know what is happening;
everything that needs you is under "Blocked — needs a human".

**What you need to have:** the game's text dumped under `dumps/`, and a way to put it back — a
dumper and an inserter for the engine. If you have those, setup adapts them to the contract. If you
do not, setup says so plainly and offers to build them with you from a format document, a community
tool or the binary. It will not pretend a translation can ship without a way to reinsert it.

## What stays fixed

The integration branch is `main` and is not a setting. The three roles never collapse into one. A
wave is a session and opens the next. The watchdog is armed before every turn ends. Those four are
`CLAUDE.md`'s banner; everything else is a parameter in `PROJECT.md`.

## Status
<!-- The coordinator refreshes this table from STATUS at every wave close. -->
| Store | Done | Total |
|---|---|---|
| «store» | 0 | «n» |
