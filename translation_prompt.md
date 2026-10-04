# Translation prompt — Abyss Boat

<!-- Read in full by every translator and every reviewer before every unit, so keep it under ~350
lines: rules and worked examples only. Progress tables, schedules and engine history do not belong
here — STATUS prints progress, HANDOFF.md holds the schedule, docs/ holds history. Every «FILL» is
filled by the setup skill from PROJECT.md and the calibration unit, never by hand. A hand-kept table
in this file will go stale; when one disagrees with STATUS, STATUS is right. -->

## ROLE

You are translating the Japanese script of **Abyss Boat** into English for a fan
translation patch. The output is not prose for a reader. It is a **byte-exact replacement for a line
in a tokenised script dump** that the project's tools reinsert into the game binary. A translation
that reads beautifully but breaks the tag stream or overflows its slot is worthless.

The order of requirements is:

1. **Fits the byte budget.** A unit that overflows will not build.
2. **Format correctness.** Tags, charset, column and row limits.
3. **Translation quality.**

Requirement 1 is not a formality. Assume your first literal draft overflows. Budget first, then write.

---

## 0. BUDGET

### 0.1 The stores
The stores, units of work and hard limits are the table in `PROJECT.md` §2. Work in **whole units**:
a per-unit budget cannot be checked on a fragment. Line-keyed stores are worked in batches of unique
lines, highest occurrence count first, because one translated line propagates to every occurrence.

### 0.2 The ratio — the number that decides everything
```
tag_bytes      = (SLOT − headroom) − BYTES_PER_SOURCE_CHAR × source_char_count
target_budget  = (SLOT − tag_bytes) ÷ BYTES_PER_TARGET_CHAR        # characters, not bytes
budget_ratio   = target_budget ÷ source_char_count
```
`headroom` is what the dump header or STATUS prints for the unit; the source character count is the
dump line with every `{…}` tag stripped. Bytes per character are `PROJECT.md` §4. **If the target is
written in a double-byte encoding, every target character costs as much as a source character and
the budget is far tighter than the free space suggests.**

The tiers, and what each demands of your first draft, are `PROJECT.md` §4. Measured on this project
(NO4_BAR.p01): a natural literal draft runs about **2.5×** the source count; a disciplined one
(contractions, no filler, merged short lines) about **2.2×**. Script containers absorb either (≈ 1
byte per character after the dictionary). What binds is the 4-row page: the literal draft overran 4
rows on 20 pages, the disciplined one on none.

**Above the top tier the byte budget stops mattering and the box geometry takes over.** Do not relax
at a high ratio: draft straight to the geometry, count columns per segment as you write, and spend
the free bytes on line breaks rather than on longer words (§3.2).

### 0.3 Where the output goes
`PROJECT.md` §2 names the unit file pattern per store. A unit file is that unit exactly as it appears
in the dump — header, every body line in the same order and count, trailer — with only readable text
changed. Start it with EXTRACT, never by hand. Line-keyed stores use a TSV of
`<count>⇥<source line copied byte-for-byte>⇥<target>`; the source column is the lookup key and must
match the unique-lines file exactly, tags and all, or the line never propagates. `#` starts a comment.

**In this project** every store is keyed: `tl/<store>/<unit>.tsv` keeps the dump's id, context and
source columns byte for byte and you write only the fourth column, the target (`docs/TOOLS.md`). An
empty target falls through to the Japanese.

Never edit `dumps/`. Never hand-edit `build/`. Work that cannot fit goes under `pending/`, which the
assembler deliberately does not read, so the patch stays buildable with that unit falling through to
the source language.

### 0.4 Verifying — never from memory
CHECK **is** the self-check in §7. Run it before opening the PR, not after. If you are ever handed
the dumps without the repo, do not answer §7 from memory: reimplement the checks, plant a deliberate
violation to prove the checker fails, and flag that the real CHECK still has to run before merging.
A stand-in checker is evidence, not clearance.

---

## 1. INPUT FORMAT

Each line is one message: readable source text interleaved with tags in braces.

```
NO1_CONTROLROOM/0003	msg spk=-	エンジンの制御装置のようだ。{br}なぜか正常に稼動しているようだ。{p}	Looks like the engine's control system.{br}For some reason, it's running normally.{p}
```
Columns: id · context (`msg`/`choice`/`text`, `spk=N`, a trailing `+` when the message continues
the previous one's box) · source · target. Plain ASCII in the target; the tools make it full-width.

**All tags are opaque binary. Never invent, delete, reorder or reformat one**, except the movable
codes `PROJECT.md` §5.3 names.

| Tag class | Form here | Rule |
|---|---|---|
| engine control code | `{p}` `{w}` `{br}`; `{name}` `{num:N}` `{pause:N}` exist but the source never uses them | keep verbatim unless §5.3 says movable |
| raw argument bytes | inside the tag (`{num:3}`); `{xNN}` raw bytes never appear | copy the form the source line uses |
| header / padding / structural | the three `#` lines; the id, context and source columns of every row | never touch |
| comments | `#` lines | never touch |

### Control codes you must reason about
`PROJECT.md` §5.3: the hard line break (movable, costs bytes — the engine has no word wrap unless
§5.2 says so, so every break is authored), the page break (addable when the target overruns the
rows), the wait-for-input and end-of-message codes (keep; end-of-message always last), the speaker
channels (keep; an alternation is a back-and-forth — use it to keep voices straight, and remember a
third party can borrow a channel mid-scene), and the runtime inserts. Patterns that look like waste
but must be preserved are listed in §5.3 too; do not "tidy" them.

### Runtime inserts are words in the sentence
A name, item or number insert is a word. You may **move an insert within its own sentence** to where
the target language wants it. You may not duplicate or drop it. If a sentence is only grammatical in
the source because of the insert's position, restructure the target around it rather than leaving a
stranded fragment. Each insert costs the columns in `PROJECT.md` §5.2 — budget for the longest value
it can take.

---

## 2. TRANSLATION POLICY — LITERAL, THEN TIGHT

**Default: translate literally.** Preserve sentence order, clause order, register and the speaker's
manner. Do not smooth, do not condense for taste, do not "improve", do not add explanation the source
does not contain, do not swap idioms for unrelated target-language idioms.

**Depart from literal only when** the literal rendering is not correct target-language text, or when
the byte budget forces it:
- ellipsis of subjects or objects that the target language requires → supply the pronoun;
- politeness levels and register with no lexical equivalent → carry them in **register and word
  choice**, not in added words (`PROJECT.md` §6);
- constructions that are ungrammatical if traced word for word;
- onomatopoeia and grunts with no target form → the fixed equivalent in `glossary.md` §6.

### 2.1 Compression, in the order you should reach for it
When a unit is over budget, cut in this order and stop as soon as you fit.
1. **Contractions.** Cost nothing in meaning; often suit the register better.
2. **Merge short lines**, deleting the break between them. The source was usually broken for a
   narrower box than yours (`PROJECT.md` §5.2).
3. **Drop redundant glosses** the source carries for its own reasons.
4. **Shorter synonym for a long word**, where the register survives.
5. **Implication instead of statement**, for a stated-but-obvious element. **Flag every one.**
6. **Reorder clauses** so the target fits the columns. Flag it.

Never cut by deleting a sentence, a speaker turn or a plot fact. If only that would work, the unit
is infeasible: park it with the measured figure and say so.

### 2.2 Voice
Voice must stay consistent per character across units and sessions; that is what `glossary.md` is
for. Two things depend on it:
- **Verbal tics** are characterisation, not noise. Each has **one fixed treatment**, recorded in
  `glossary.md` §5. Never mix treatments. What is fixed is the word; punctuation follows the source.
- **Duplicated lines.** Identical source text gets **byte-identical target text** every time, or
  propagation breaks and the game shows two renderings of one line. Before you write a line, census
  it on the **source** side across every variant spelling the glossary row lists, in `tl/` and in
  the dumps, by the method your dispatch names. Already translated → reuse byte for byte. Recurs
  untranslated → say so in Flags so the next translator reuses yours.

---

## 3. HARD FORMAT CONSTRAINTS

### 3.1 Charset
The permitted set is `PROJECT.md` §5.1, and nothing outside it. Consequences to internalise:
- Type `'` and `"` straight: the tools turn them into ‘ ’ and “ ” by context, because the font has
  no straight quotes. 「」 and 『』 become `"…"`.
- `…` is one glyph, one column. Copy the source's count (`……` stays `……`); never type `...`.
  `‼` and `⁉` are single glyphs too: keep them, never `!!` or `!?`. `──` → `——` (drawn as ――).
- Nothing outside Shift-JIS has a glyph: `café` fails CHECK — write `cafe`. No tabs, no `{` `}`
  outside tags.
- Every character costs one column and two bytes. Script containers are huge (PROJECT.md §4), so
  the limit you meet is the box, not the bytes.

### 3.2 Line and page geometry
The box is 28 × 4 (`PROJECT.md` §5.2). **The tools word-wrap every message and subtitle at 28
columns**, so you never break a line for width; a `{br}` you write is a deliberate break. Count
columns yourself only on choice and `text` rows (one line, never wrapped) and on lines you end with
a deliberate `{br}`.
- **≤ 28 characters between breaks** where you break by hand. Count characters, not bytes; an insert
  counts as its §5.2 cost.
- **≤ 4 rows per page.** A page is everything between clicks (`{p}` or `{w}`), following `+` chains
  across messages; UNITCHECK prints rows per page. If the target needs one more, insert a `{p}` at a
  clause boundary rather than cutting sense, and flag it.
- **Break at word boundaries**, preferably clause boundaries, so each line reads on its own.
- No line ending in a lone one- or two-letter word if it can be avoided.
- **Aim for 27** on hand-broken lines and choices. A line at the hard limit has no room for a later one-character fix — a
  changed name, an added apostrophe — without a re-flow.
- **Count as you draft, not afterwards.** The source's own break structure is usually close to right
  for your box; merge only where the source was split mid-clause for a narrower box, add a break
  where one clause will not fit (cheap at any ratio above the middle tier).

### 3.3 Byte budget
Per `PROJECT.md` §4: bytes per character, per control code, per argument byte; the slot per unit;
the slack floor. The inserter fails rather than overflow. Land with the slack floor wherever the
ratio allows, so a later fix does not force a full re-cut.

---

## 4. GLOSSARY PROTOCOL

Fixed terms live in **`glossary.md`** — short, one row per term, read in full before every unit. The
reasoning behind a term lives in **`rulings.md`**, grepped on demand. Rules:
1. **Check the glossary before rendering any name.** If it is there, use that form exactly.
2. **If it is not there, propose it** in your PR's Glossary additions: source form, every variant
   spelling seen, the chosen target, a one-line reason, the column count, any fixed-width cap. Never
   edit `glossary.md` from a translator branch.
3. **Never silently change an existing entry.** If a later line proves an earlier choice wrong (a
   character's gender, a "place" that is a person), say so explicitly in Flags, give the corrected
   entry, and list every shipped line that must change.
4. **Ambiguous readings**: pick the form the source most plausibly intended per `PROJECT.md` §6,
   note the alternative, and check the other store — a later role often fixes the reading.
5. **Length caps.** Terms destined for fixed-width tables carry their cap in the row and stay inside it.
6. **PROVISIONAL entries are not decisions.** Promote one the first time you render it, and say so.

---

## 5. WORKED EXAMPLES

<!-- From the calibration unit, script NO4_BAR.p01 (PR #1), each demonstrating one rule; the
reviewer may add more as rulings accrue. Keep them current — an example that contradicts a later
ruling is worse than none. Row counts were measured with the tools, not by eye. -->

**1. Merge short lines** (§2.1 step 2) — `NO4_BAR/0041`
```
知っておるのか？{br}お嬢さん。
You know of it, young lady?
```
The source gives the vocative a line of its own; English folds it into the question. `{br}`
removed (flagged), 2 rows → 1, one byte saved.

**2. Add `{p}` at a clause boundary when a page overflows** — `NO4_BAR/0060` (a `+` message)
```
ならばわしも見てみようと足を進めたとたん、ガクンと強い揺れが起こった。{br}
Thinking I'd have a look too, I stepped forward,{p}and that very instant, there was a strong jolt.{br}
```
Without the `{p}` the page opened by 0059's `{w}{br}` runs to 7 rows. The click goes at the comma
before the jolt, so it lands as a beat; the ending `{br}` stays. One byte spent, flagged.

**3. Keep `{w}` and hold the line to its row** — `NO4_BAR/0055` (a `+` message)
```
わしは奇妙な物音で目を覚ました。{w}{br}
I awoke to a strange noise.{w}{br}
```
`{w}{br}` stays exactly where it is. UNITCHECK counts the page that 0053's `{w}{br}` opens at one
row, and 0054 takes two, so this line must fit one: "I was woken up by a strange noise." wraps and
makes the page 5 rows.

**4. Name the speaker from content, not from `spk=N`** — `NO4_BAR/0016`, `0017`
```
最終的に助からなかったら意味ないね。   (spk=6)
まったく、なんという言いぐさじゃ。     (spk=6)
Means nothing if we're not saved in the end.
Really, what a thing to say.
```
One `spk` value, two speakers (F-009): William, blunt, subject dropped; then Rob Collison,
old-fashioned diction with no dialect spelling.

**5. Glyph counts follow the source** — `NO4_BAR/0005`
```
なんとっ⁉{br}それはいったい誰が…。
What⁉{br}Who on earth did that…
```
`⁉` stays one glyph (never `!?`), one `…` stays one `…`, and the 。 after `…` is absorbed.

**Wrong, and why** — `NO4_BAR/0024`
```
虫の居所？{br}そうじゃない。気に入らねえんだよ。{br}こんな非常識な場所にノコノコやってくる連中がよ。
WRONG:   Foul mood?{br}That's not it. I just don't like 'em.{br}People who come waltzing into an insane place like this.
CORRECT: Foul mood? That's not it.{br}I just don't like them.{br}Guys who come waltzing into a crazy place like this.
```
- Keeping the source's first `{br}` after "Foul mood?" makes the page 6 rows: CHECK fails it.
- `'em` after a space is drawn as an opening quote, `‘em`, and CHECK does not catch it (PROJECT.md
  §7). Write "them", or type `’` yourself.
- "People … an insane place" wraps to three rows where William's "Guys … a crazy place" takes two.

The correct version keeps both `{br}`, the first moved one sentence later (flagged), in 4 rows.

---

## 6. OUTPUT FORMAT

For each unit, deliver exactly:
1. **The translated file**, saved at its `PROJECT.md` §2 path, every non-text line reproduced
   unchanged.
2. **`GLOSSARY ADDITIONS`** — a table of new or corrected entries (source · variants · target · cols
   · cap · note). `(none)` if empty.
3. **`FLAGS`** — numbered. The first flag on a unit is always **the measured figure**: script
   `unit «id»: «file».SCR «used» / 65,535 — «free» free (MEASURE); max «r» rows/page (UNITCHECK)`;
   scene `unit «id»: max «n» lines per subtitle (UNITCHECK)`. Then: §2.1 step 5–6 deviations; every movable code
   moved, added or removed, per line, before → after; ambiguous referents or speakers; names with
   more than one defensible reading; added page breaks; anything still over the width; any tag whose
   meaning you guessed in order to place text around it; suspected typos in the source.

In a PR these are the template's sections. No commentary outside them.

---

## 7. SELF-CHECK BEFORE SENDING

Run CHECK. Do not answer these from memory.
- [ ] Bytes within the slot, figure stated in Flags.
- [ ] Every tag from the source in the output, same count, spelling and order — except the movable
      codes I deliberately re-flowed and the inserts I deliberately repositioned.
- [ ] Nothing outside the charset. No forbidden glyph. No ASCII where the font has none.
- [ ] No segment over the width, inserts counted at their cost. No page over the rows.
- [ ] Repeated-punctuation and ellipsis counts match the source.
- [ ] Every proper noun matches `glossary.md` exactly, including case and scope.
- [ ] Identical source lines produced identical output — **census it on the source side across
      variant spellings, count the hits, print the pair count.** Repeats cross unit boundaries.
- [ ] Gutters and fixed prefixes preserved (`PROJECT.md` §6).
- [ ] Every new name checked against the other store too.
- [ ] End-of-message code last on every line. Structural lines byte-identical to the input.
- [ ] CHECK ends `All checks passed`; UNITCHECK shows nothing non-inherited over the rows.
- [ ] `git checkout -- build/` done before committing.

---

## APPENDIX A — what CHECK verifies, and what it does not

CHECK performs, for every translated file, all as errors: unit structure (the `#` lines, row ids
and their order, contexts and sources byte-identical to the dump; unknown keys; a row in two files);
charset (every character has a glyph; `ascii` slots pure ASCII); tag parity in script and scene
(`{w}` `{name}` `{num:N}` `{pause:N}` as in the source, no `{p}` removed, the same ending tag, `{w}`
never last); system slots in bytes, printf directives, `{br}` never last or doubled; geometry after
the tools' word wrap (no word longer than a line, box pages ≤ 4 rows following `+` chains,
subtitles ≤ 4 lines, choice and `text` rows ≤ 28 columns, inserts costed); every `*.SCR` within
65,535 bytes and 1,499 dictionary tokens; duplicates across files and stores (identical sources,
and sources identical once `{p}` `{w}` `{br}` are removed, must have identical targets, tags
aside), printing how many pairs it compared. MERGE re-runs all of it and refuses to write on any hard error, so a broken unit cannot
reach a build by accident.

**Known blind spots** are listed in `PROJECT.md` §7 and are checked by hand in every review. If you
find a new one, say so in your PR's Flags; the reviewer adds it to §7 in the integration commit.
