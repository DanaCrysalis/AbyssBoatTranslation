# PROJECT.md — the project block

Everything in this suite that is specific to one game, engine, tool set, repository or language pair
lives here and nowhere else. `CLAUDE.md`, the `/translate` skill and the three agent definitions
refer to these sections by number and never repeat the values. **Nobody fills this file by hand.**
The setup skill (`.claude/skills/setup/SKILL.md`, run by `/translate` on first use) infers what the
repo can tell it, asks the human the rest in one batch, shows the completed block, and commits it on
confirmation. The runner's preflight refuses to start a wave while `grep -n '«FILL»' PROJECT.md`
prints anything.

Keep this file factual and short. Reasoning goes in `docs/`, `rulings.md` or `FLAGS.md`. After
setup, the only agent that edits it is the reviewer, and only to add a CHECK blind spot to §7. A
filled example is `docs/PROJECT.example.md`.

## 1. Identity

| Field | Value |
|---|---|
| Game | «FILL» <!-- title, developer, platform, product id, year --> |
| Source language → target language | «FILL» |
| GitHub owner / repo | «FILL» / «FILL» <!-- used by every GitHub MCP call and every PR --> |
| Integration branch | `main` — **not configurable** (CLAUDE.md Rule 3) |
| Model alias and effort | `opus` at `max` <!-- set in .claude/settings.json and in the frontmatter of the skill and the three agents; change all five together --> |
| What the human expects | «FILL» <!-- e.g. "fully unattended; I read HANDOFF.md once a day" --> |

## 2. Stores and units

One row per text store: a game file, or part of one, with its own dump, unit of work and hard limit.

| Store | Source dump | Unique-lines file | Unit of work | Unit file pattern | Hard limits | Unit file keeps source text? |
|---|---|---|---|---|---|---|
| «FILL» | `dumps/«FILL»` | `dumps/«FILL»` or n/a | «FILL» <!-- e.g. one whole chunk; 40–60 unique lines --> | `tl/«store»/«FILL»` | «FILL» <!-- bytes per slot; columns × rows --> | «yes / no» |

**"Keeps source text?" decides the duplicate-gate method** (CLAUDE.md §6 gate 6). A keyed file
(source in one column, target in another) is grepped. A file that replaces the source is paired
positionally against the dump, row by row, and the check must print how many pairs it compared.

| Field | Value |
|---|---|
| Unit order for dispatch | «FILL» <!-- e.g. chapter order, because voices and names accumulate --> |
| Batch rule for line-keyed stores | «FILL» <!-- e.g. 40–60 unique lines, highest occurrence count first, same scene together --> |
| `build/` outputs that are tracked in git | «FILL» <!-- e.g. the merged dumps, or "none" --> |
| Containers known to be tight (name · free bytes · date) | «FILL» <!-- from MEASURE's full table; keep current --> |

## 3. Commands

Run from the repo root. No game binaries needed except where marked human-only. The contract each
command must satisfy is `tools/README.md`.

| Abstract name | Concrete command | Notes |
|---|---|---|
| CHECK | `«FILL»` | must end `All checks passed`; non-zero exit otherwise |
| STATUS | `«FILL»` | |
| MERGE | `«FILL»` | writes under `build/`; refuses on any hard error |
| UNITCHECK (one unit) | `«FILL» <unit> <file>` | rows, columns, diff of movable codes vs. source |
| UNITCHECK (whole store) | `«FILL»` | after MERGE |
| MEASURE | `«FILL»` | container usage after MERGE; full table |
| QUEUE | `«FILL»` | planner; reads thresholds from §4, never its own source |
| EXTRACT | `«FILL» <unit>` | starts a unit file from the pristine dump |
| BUILD / REFRESH (human-only) | `«FILL»` | need the game files; agents never run them |

## 4. Budget

| Field | Value |
|---|---|
| Bytes per **source** character | «FILL» |
| Bytes per **target** character | «FILL» <!-- 2 if the target is written in a double-byte encoding (e.g. full-width Latin in Shift-JIS); 1 for a single-byte font. This halves or doubles every ratio below. --> |
| Bytes per control code · per argument byte | «FILL» |
| Slack floor per unit | «FILL» bytes <!-- e.g. ≥ 50, so a later one-character fix does not force a re-cut --> |
| Reserve kept per container | «FILL» bytes |

Ratio, per unit:

```
tag_bytes      = (SLOT − headroom) − BYTES_PER_SOURCE_CHAR × source_char_count
target_budget  = (SLOT − tag_bytes) ÷ BYTES_PER_TARGET_CHAR        # characters, not bytes
budget_ratio   = target_budget ÷ source_char_count
```

**Calibrate the tiers from the first unit, then fix them here.** Translate the first unit
literally and measure its ratio; apply the compression ladder and measure again. Those two numbers
set the bands. Do not copy another project's bands: they depend on the language pair and on the
bytes-per-character above.

| Tier | Ratio | What it demands of the first draft |
|---|---|---|
| blocked | < «FILL» | no faithful translation fits; needs an engine change; never dispatched |
| A | «FILL» – «FILL» | terse from the start, contractions mandatory, expect two re-cut passes |
| B | «FILL» – «FILL» | write tight from the first draft, expect one re-cut pass |
| C | «FILL» – «FILL» | translate literally; bytes rarely bind |
| D | > «FILL» | bytes never bind; geometry is the only constraint — do not relax |

| Measurement | Value |
|---|---|
| Natural literal draft ratio (unit, date) | «FILL» |
| Disciplined draft ratio (unit, date) | «FILL» |
| **Measured floor** — lowest ratio at which a faithful unit has fit | «FILL» <!-- QUEUE's blocked threshold equals this number and is updated here first --> |

## 5. Format

### 5.1 Charset — the permitted set, nothing outside it
«FILL» <!-- every permitted code-point range and punctuation mark; what is forbidden and what
replaces it (e.g. ellipsis → three stops with the source's count; ASCII apostrophe → ’; symbols with
no glyph → their spelled-out names) -->

### 5.2 Geometry
| Field | Value |
|---|---|
| Text box, columns × visible rows | «FILL» |
| Preferred width (one column of slack) | «FILL» |
| Column cost of each runtime insert (name, item, number) | «FILL» |
| Word wrap | «FILL» <!-- "none — every break is authored", or describe the engine's wrap --> |
| Boxes not yet widened / unknown row counts | «FILL» <!-- and the rule until confirmed --> |

### 5.3 Control codes
| Code | Meaning | May a translator move / add / remove it? |
|---|---|---|
| «FILL» | hard line break | move, add, remove — costs «n» bytes each |
| «FILL» | page break / clear | add when the target overruns the rows; keep existing ones |
| «FILL» | end of text, wait for input | keep; never add |
| «FILL» | end of message | keep; **always last** |
| «FILL» | speaker channel / portrait | keep; an alternation is a conversation — use it to keep voices straight |
| «FILL» | runtime inserts | move within its own sentence; never duplicate or drop |
| everything else | opaque | keep verbatim, in place |

Patterns that look like waste but must be preserved (e.g. a break immediately after a page clear):
«FILL»

### 5.4 Structural lines that must be byte-identical to the dump
«FILL» <!-- e.g. unit headers, padding markers, header blobs, # comments -->

## 6. Language-pair conventions
<!-- The policy translation_prompt.md §2 applies. Cover: how ambiguous name readings are chosen and
recorded; how honorifics and politeness levels are carried (register and word choice, not added
words); punctuation mapping; how menu-option gutters or fixed prefixes are preserved; case rules for
common vs. proper nouns; how verbal tics are fixed (the word is fixed, punctuation follows the
source); anything the target language needs that the source elides (pronouns, articles). -->
«FILL»

## 7. Gate specifics and evidence conventions

| Gate | Concrete check for this project |
|---|---|
| 4 — unit budget and geometry | «FILL» <!-- e.g. bytes ≤ slot with ≥ 50 slack; UNITCHECK shows no page over N rows the source did not exceed --> |
| 5 — container budget | «FILL» <!-- e.g. MEASURE: no container negative; any under 2,000 free named in the review --> |
| 8 — structure | «FILL» <!-- the literal list: terminator last, structural lines verbatim, gutters, repeat counts, forbidden glyphs --> |

**Known blind spots of CHECK** — things it does not verify, which the reviewer checks by hand in
every review. Add one the moment it is found (the reviewer may edit this list in an integration
commit); never remove one without a tool PR that closes it.
- «FILL» <!-- e.g. "the line-keyed store has no tag-parity check"; "the positional duplicate check pairs nothing when a file is misnumbered" -->

**Line-numbering convention for findings:** «FILL» <!-- exactly one, e.g. "the file line number as printed by grep -n on the unit file", and how it relates to any other index the tools print -->

## 8. Naming

| Thing | Pattern | Example |
|---|---|---|
| Translator branch | `tl/«store»-«id»` | «FILL» |
| Park branch | `park/«store»-«id»` | «FILL» |
| Commit and PR title, unit | `tl: «store» «id» — «measured figure»` | «FILL» <!-- e.g. "tl: chunk 019 — 7,912 / 8,192 (280 slack)"; "tl: batch 004 — shop lines, 52 lines / 410 instances" --> |
| Commit and PR title, park | `park: «store» «id» — «figure», floor «ratio»` | «FILL» |
| Integration commit | `integrate: «unit» — glossary, rulings, flags, handoff` | fixed |
| Handoff commits | `handoff: survey` · `handoff: dispatch wave N` · `handoff: PR #k opened` · `handoff: wave N closed` · `handoff: run complete` | fixed |
| Glossary seed commit | `glossary: provisional seeds for wave N` | fixed |
| Session title and tags | `«project» — wave N` · `["«project»-translation", "wave-N"]` | «FILL» |

## 9. Environment

| Question | Answer |
|---|---|
| Is `gh` installed? | «FILL» <!-- if no: every GitHub action uses the GitHub MCP tools with §1's owner/repo --> |
| Is the claude-code-remote MCP available (`create_session`, `send_later`, `ListAgents`)? | «FILL» |
| If not — fallback for the wave chain | an `orchestrator` subagent per wave, `run_in_background: true`; the run is then **attended** — a human restarts it when the session dies, and HANDOFF → NEXT ACTION says so |
| If not — fallback for the watchdog | none exists; write `NO WATCHDOG — attended run` into NEXT ACTION every turn |
| Is the scratchpad shared between parallel subagents? | «FILL» <!-- assume yes; namespace scratch files regardless --> |
| Does GitHub accept APPROVE / REQUEST_CHANGES from the bot account on its own PRs? | «FILL» <!-- if no: the reviewer posts a COMMENT review; the DECISION: first line is the decision --> |
| Does branch deletion succeed after merge? | «FILL» <!-- a 403 is not a merge signal; merged: true + the squash SHA is --> |
| Are the game files in the repo (split archives with pinned hashes) or human-only? | «FILL» |
| Worktree location for subagents | `.claude/worktrees/` (gitignored) |

## 10. Wave defaults

| Field | Value |
|---|---|
| Wave size and mix | «FILL» <!-- e.g. 4: three budgeted units in unit order plus one line-keyed batch --> |
| Re-dispatches per unit before parking | 2 |
| Rework rounds before PARK or a fresh translator | 3 |
| Watchdog interval | 10–15 minutes |
| HANDOFF line budget | 150 |
