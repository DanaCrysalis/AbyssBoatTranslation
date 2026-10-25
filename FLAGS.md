# FLAGS — the open-issue list

<!-- Not a diary. One entry per issue, id F-NNN, never renumbered. The reviewer appends from PR Flags
in its integration commit; the coordinator moves closed entries to the Closed list at wave close
(one line each). Engine reverse-engineering notes belong in docs/, not here. -->

Entry format:
```
### F-NNN · YYYY-MM-DD · «area» · OPEN | HUMAN | CLOSED
What was observed · where (unit and line, PROJECT.md §7 numbering) · what would resolve it · pointer
```

## Needs a human
<!-- engine patches, binaries, in-game checks, anything that needs the disc or an emulator. Each
entry says exactly what the human does. HANDOFF.md → Blocked mirrors this list with pointers. -->

### F-001 · 2026-10-04 · engine · HUMAN
First in-game test of a built patch: does full-width English display correctly in the message
box, and does a rebuilt room script load and run? · any unit · BUILD with one translated room
(e.g. `script/NO1_CONTROLROOM`), copy `build/game/SCRIPT.PAK` and `build/game/AbyssBoat.exe`
over the installed game (back up first), open that room, examine things · `docs/ENGINE.md` §5.
In the same session, watch the OP2 movie: OP-SCN034 (PR #2) renders OP2/01 待って、ジョン！捕まえて！ as
"Wait, John! Catch it!" because 捕まえて has no object. If what is being chased is a person, the
target becomes "him" or "her" (`tl/scene/OP-SCN034.tsv:4`; rulings R §4.3).

### F-002 · 2026-10-04 · geometry · HUMAN
Subtitle box size is assumed 28 columns × 4 rows (`tools/abyss/project.py` SCENE_COLS/ROWS);
the Japanese source has a few subtitle lines of 30–51 columns, so the real box may be wider ·
scene store · watch a translated cutscene (SCN001 is short) and report how many full-width
columns fit on a line · `docs/ENGINE.md` §7.
Also reading time: SCN002's subtitles last 40–50 frames (1.3–1.7 s) and the English runs about
twice the source's characters (SCN002/02: 95 characters in 50 frames, 4 lines). Report whether
SCN002 can be read at playback speed (OP-SCN034, PR #2 Flag 12).

### F-003 · 2026-10-04 · geometry · HUMAN
Choice options and inline lines (`choice`/`text` rows) are assumed to fit 28 columns
(CHOICE_COLS) · script store, e.g. NO2_CABIN_2001/s05 "通風孔に入る" · open a choice in game
with a long English option and report what fits.

### F-004 · 2026-10-04 · font · HUMAN
Full-width English is wide (28 characters a line). A font hack could double that: draw two
Latin letters per glyph in the Shift-JIS code points the translation frees up, or patch the
renderer (0x41F100 / 0x41F8E0) for half-width advance. Optional; changes the bytes-per-character
figure in PROJECT.md §4 if adopted · whole project.

### F-005 · 2026-10-04 · images · HUMAN
Text drawn into images is not in the dumps: `GPARTS.PAK` (camp menu, dialog buttons
DLG*.LGF, map labels) and `PICTDAT.PAK` `*.LGF`. Needs an LGF image extractor/inserter and
an image editor · not started.

### F-006 · 2026-10-04 · system · HUMAN
The executable's string tables are fixed-stride arrays: room names hold 14 full-width
characters, deck names 10, camp help 27, item text 43 (minus breaks). Several Japanese
entries already fill their slot (MEASURE: camp/001, decks/001, decks/003, misc/45F1FF).
The human chose (2026-10-04, setup) to wait for a code patch that repoints these tables to a
larger area rather than abbreviate: the whole system store is blocked (PROJECT.md §4 "Stores
blocked whole") and never dispatched until the patch exists and the slots in
`dumps/system.tsv` are regenerated · system store.

### F-010 · 2026-10-04 · geometry · HUMAN
Two `+` chains in the shipped scripts run past 4 rows between clicks when `{w}` counts as a page
end, as the tools model it: `NO4_BAR`/0090–0095 (Collison's story, 5 rows from 0092) and the
chain at `NO4_TOOL_ROOM`/0044 (5); also 15 chains in the `_T` test scripts (5–7). Whether the
engine scrolls, clears or overflows there is unknown, so CHECK holds every page to 4 rows and
translators add `{p}` · in game, play the bar conversation where Collison tells how the survivors
ran out of food and report whether a fifth line ever shows in one box · `docs/ENGINE.md` §7.
Also `NO4_BAR`/0053–0057, where Collison's story opens (shipped in NO4_BAR.p01, PR #1): it shows 5
rows between `{p}` clicks across two `{w}` in the source and 7 in the English, though each
`{w}`-page fits 4 as the tools model it. Check in the same session that the box scrolls or clears
there (rulings R §1.12).
NO4_BAR.p02 (PR #5, 2026-10-06) adds 9 `{p}` so every page of 0062–0119 fits 4 rows as the tools
model it, including the 5-row page from 0092 named above. Four of them open a `+` row straight
after a row ending in `{br}` (0066, 0083, 0089, 0099); the source never has `{br}` followed by `{p}`.
Check in the same session that the box clears cleanly there, with no blank first row (rulings R §2.4).


## Open
<!-- anything an agent could still act on: a suspected source typo to confirm, a reading to settle
when the other store is translated, a container approaching its threshold -->

### F-007 · 2026-10-04 · scene · OPEN
`SCN002OLD.SCE` looks like an unused older version of SCN002/SCN002A (its lines largely
repeat theirs). Since setup bundled the scene groups it sits in unit `OP-SCN034` beside
SCN002/SCN002A, where the duplicate gate keeps its repeated lines identical.
Shipped in OP-SCN034 (PR #2, 2026-10-06) with its `【Name】` labels translated and the words of
SCN002 after them. CHECK does not pair the labelled rows with SCN002/SCN002A (F-013); the review
checked all 8 by hand (rulings R §4.4).

### F-008 · 2026-10-04 · script · OPEN
The six `*_T` room scripts are prototypes or tests, probably never shown: `NO4_ROOM01_T` opens
"選択のテストをします" (testing choices), and `NO4_BAR_T`, `NO4_HWR_BACK_T`,
`NO4_HWR_FRONT_DOWN_T`, `NO4_HWR_FRONT_UP_T`, `NO4_MACHINE_T` are drafts of the shipped rooms
with `【Name】` speaker prefixes · units `NO4_BAR_T.p01`–`p04`, `NO4_T.b01`–`b03`, dispatched
last · resolved by a human checking whether any script or the exe references these names
(needs `original/`); if none does, they may be dropped from the queue.
`NO4_BAR_T`/0012–0089 draft the scene shipped in NO4_BAR.p01 (PR #1). CHECK pairs only its
identical rows (0078, 0079, 0082, 0084, 0085) and tag variants (0086, 0087, 0089). If these units
are kept, the `【Name】`-prefixed near-duplicates must reuse NO4_BAR.p01's wording too: T/0050 ↔
0032 "Old man, I have a question.", T/0063–0064 ↔ 0043, 虫の居所 "Foul mood?", 一匹 "a single
beast", 分身 "part of him" (PR #1 Flags 7; rulings R §1.5, §1.9).
`NO4_BAR_T`/0090–0148 likewise draft NO4_BAR.p02 (PR #5): 18 identical and 13 tag-variant rows,
which CHECK will pair; the exact ones carry p02's added `{p}` (T/0094, 0132, 0135, 0137). Its
rewritten or `【Name】` rows (e.g. T/0130, 0145–0154) reuse p02's wording by hand where the text
matches (rulings R §2.5).
`NO4_BAR_T`/0155–0168 draft NO4_BAR.p03 (PR #3) 0120–0134, all `【Name】`-prefixed, so CHECK
pairs none of them: reuse p03's wording by hand (T/0158 has 事故 for トラブル, T/0159 joins
0123–0124, T/0166 is reworded, T/0167 ふん → "Hmph,") (rulings R §3.6).
`NO4_HWR_BACK_T`/0001–0008 copy SCN002OLD/01–08 (OP-SCN034, PR #2): 0001–0003 and 0005–0008
are tag-variants CHECK pairs (reuse the target with `{p}` appended); 0004 has ⁉ for ！？ and is not
paired: `【Miller】Hide? How long are we meant to hide⁉{p}`. `NO4_MACHINE_T`/s06–s08 are
labelled `text` copies of SCN001/01–02: s06 `【Oakland】What are we to do?` (27); s07–s08 need
their own cut within one line (rulings R §4.5).

### F-009 · 2026-10-04 · speaker · OPEN
`spk=N` (first argument of statement 0xA9) is not a character id: `NO4_BAR`/0014–0018 put
William and Rob Collison on the same value, and Oakland is on it at 0002. `docs/ENGINE.md` §3
claimed a fixed slot per character and was corrected in setup. Every translator and reviewer
names speakers from content and register (PROJECT.md §5.3) · would resolve by identifying the
argument's real meaning in the exe (0x42BE28 handler table).
NO4_BAR.p04 (PR #4): NO4_BAR_T has no draft past T/0181, so 0178–0235 are named from content;
0178 (Oakland, Heming or Collison), 0179–0180 (probably Wolg) and 0181 (perhaps William) stay
uncertain and are rendered speaker-neutral; spk=6 carries a salvager and Collison (rulings R §5.3).
NO4_BAR.p05 (PR #6): 0236–0293 likewise from content; 0245, 0247, 0248, 0253, 0254, 0264, 0265,
0270, 0289 and 0290 stay uncertain (Oakland, William, Wolg, Heming or Miller) and are rendered
speaker-neutral; spk=4 carries Wolg (0249–0250), Miller (0251) and William (0255) (rulings R §6.2).
NO4_BAR.p06 (PR #9): 0294–0351 likewise from content; 0308 and 0311 (Oakland or Heming), 0313
(Wolg or Oakland), 0340 (probably Oakland), 0347 (Oakland or Heming), 0350 (Wolg or Heming) and
0349 (probably William: やがる, and NO4_BAR/0363 has them meet him in a corridor) stay uncertain and
are rendered speaker-neutral; spk=4 carries Wolg (0294), Oakland (0295) and Miller (0309), spk=5
Wolg (0320) and Oakland (0326) (rulings R §7.2).
NO4_BAR.p07 (PR #8): 0352–0409 likewise from content; 0365, 0378–0380, 0383, 0385, 0387, 0389,
0391, 0402, 0405, 0408 and 0409 stay uncertain and are rendered speaker-neutral; 0370, 0404, 0406
(probably Wolg), 0381, 0407 (probably Oakland) and 0403 (probably Heming) are likely but unconfirmed
(rulings R §8.2).
SCN038 (PR #7): scene subtitles carry no speaker code, so all 59 are named from content. These stay
uncertain and are rendered speaker-neutral:
- SCN038A/01–04 (Wolg / Oakland), A/05 and A/08 (Oakland or William).
- B/01 (William or Heming), B/04 and B/13 (Judy or Heming), B/06, B/08 and B/21 (probably Heming).
- D/02, 04, 05, 07–09 (Wolg or Oakland), D/12 (Wolg, Oakland or Heming).
The 5C1/5C2 speaker is the killer, except 5C1/01, 07 and 10 (Judy) (rulings R §9.2).
NO4_HWR_FRONT.p01 (PR #13): no `_T` draft exists, so speakers are named from content. Collison
(0011–0013) and William (0025, 0027, 0029, 0031, 0033, 0035, 0038–0039, 0042, 0044, 0046, 0048) are certain. John's partner (every other message row)
is not Oakland, whose 42 labelled rows use わし and never 俺, while the partner says 俺. He is Heming
(0004 on age, うむ, わっはっは) or Wolg (俺). Rendered speaker-neutral. 0023 is the partner's or John's.
spk=0/1/2 each carry the partner (rulings R §10.2).

### F-011 · 2026-10-04 · tools · OPEN
PR #1 (NO4_BAR.p01) found four things CHECK and UNITCHECK do not verify. Each was confirmed by a
plant in a scratch copy of the tree, which passed both (rulings R §1.13):
(a) a word-initial `'` after a space or at a segment start curls into an opening quote ‘
(`like 'em.` → `ｌｉｋｅ　‘ｅｍ．`);
(b) UNITCHECK's `codes:` lines diff the wrapped text, so wrap breaks the tools insert show as added
`{br}`;
(c) message lines ended by an authored `{br}` or `{w}` are held to 28, not the preferred 27;
(d) wrap points are not checked for sense: one-word last rows, a line ending in a lone "a" or "I",
a courtesy title split from its name.
All four are listed in PROJECT.md §7 and checked by hand in every review · would close with a tool
PR: map a word-initial `'` to ’ or reject it; add a `codes:` line on the authored text; warn at 28
on those lines; have UNITCHECK print the wrapped text and flag the three patterns in (d).


### F-012 · 2026-10-06 · tools · OPEN
A `+` message that follows a message with no ending tag continues on the same row with no
separator: Japanese needs none, English glues ("all along.She can't"). Found by PR #3 (Flag 3),
confirmed in PR #5's review by a plant in NO4_BAR.p02 (0113 without its leading `{br}`): CHECK
`All checks passed`, UNITCHECK 0 violations (0113's first line counted at 10 + 9 columns), MERGE
writes the glued text. 25 boundaries in the script dump: NO4_BAR 0113, 0115, 0149, 0315, 0338;
NO4_BAR_T 14; NO4_HWR_FRONT/0077; NO4_HWR_FRONT_DOWN_T/0005; NO4_HWR_FRONT_UP_T/0026, 0027;
NO5_ENTRANCEL/0005; NO6_BRIDGE/0002. Translators open the `+` target with `{br}` (flagged);
listed in PROJECT.md §7 and checked by hand · would close with a tool PR: CHECK errors when a
translated `+` target starts with text and the previous row's target ends in text, not a tag
(rulings R §2.3).


### F-013 · 2026-10-06 · tools · OPEN
CHECK's duplicate gate does not strip a leading `【Name】` label or equate `！？` with `⁉`, so
labelled copies of unlabelled rows are never compared: SCN002OLD ↔ SCN002/SCN002A,
NO4_MACHINE_T/s06–s08 ↔ SCN001/01–02, NO4_HWR_BACK_T/0004 ↔ SCN002OLD/04, and every `【Name】`
row of the `_T` scripts against its shipped room (F-008). Found by PR #2 (Flag 13), confirmed in
its review by a plant: a divergent target on SCN002OLD/01 passed CHECK (`All checks passed`).
Listed in PROJECT.md §7 and censused by hand · would close with a tool PR: a third pairing pass on
sources with the label stripped and final 。！？⁉ normalised, reported as warnings with a pair count
(rulings R §4.4).


### F-014 · 2026-10-06 · script · OPEN
Suspected source typo: `NO4_BAR/0218` もう一斑は社長とヘイミングだ has 一斑 ("a fleck"; 1 / 0 / 0,
only here) where the sense, after 二人ずつの二班, is 一班 ("the other team"; 0 rows). Shipped as
"the other pair" (`tl/script/NO4_BAR.p04.tsv:44 NO4_BAR/0218`, PR #4 Flag 7). Harmless; nothing
to change unless a later script or the `_T` drafts show a different reading · rulings R §5.5.


### F-015 · 2026-10-25 · script · OPEN
Suspected source typo: `NO4_BAR/0321` 正面から襲ってきたどうするつもりだ lacks the ら of the
conditional 襲ってきたら (てきたどう 1 / 0 / 0, only here; 襲ってきたらどう 0 rows). Shipped as the
conditional, "what will you do if he attacks from the front?" (`tl/script/NO4_BAR.p06.tsv:31
NO4_BAR/0321`, PR #9 Flag 7). Harmless; nothing to change unless the `_T` drafts show a different
reading · rulings R §7.3.


### F-016 · 2026-10-25 · script · OPEN
Suspected source typo: `NO4_BAR/0396` 捕まられなくてもかまわん has 捕まられ (passive of 捕まる, "be
caught", which makes no sense here) where the sense, after 0384's request to catch one, is the
potential 捕まえられなくても ("even if you can't catch one"; 捕まられ 1 / 0 / 0, only here). Shipped
as "No problem if you can't catch one." (`tl/script/NO4_BAR.p07.tsv:48 NO4_BAR/0396`, PR #8 Flag 9).
Harmless; nothing to change unless the `_T` drafts show a different reading · rulings R §8.3.


### F-017 · 2026-10-25 · script · OPEN
Suspected source typo: `NO4_BAR/0407` 無事に帰り着いてからいくらでも追求してやる has 追求 ("pursue a
goal"; 追求 1 / 0 / 0, 追及 0 rows) where the sense, blame for 0406's 俺の責任だ, is 追及 ("call to
account"). Shipped as "I'll
call you to account as much as I like!" (`tl/script/NO4_BAR.p07.tsv:59 NO4_BAR/0407`, PR #8
Flag 9). Harmless · rulings R §8.3.


### F-018 · 2026-10-25 · script · OPEN
The second victim at `NO4_BAR/0402` 二人目の犠牲者が出た…。俺たちの…仲間だ is unnamed. Probably
Miller: she has no line in 0410–0437, and at 0429 (わしはジュディと二人っきりか⁉) the speaker
expects to be left with Judy alone. Shipped
gender-neutral, "One of our… own" (`tl/script/NO4_BAR.p07.tsv:54`, PR #8 Flag 5), so nothing
shipped depends on it. The translator of NO4_BAR.p08 and later units confirms from content; if a line
names the victim, no p07 text changes · rulings R §8.2.
NO4_BAR.p08 (PR #12): no line in 0410–0461 names the victim and Miller has none; nothing changes
(rulings R §11.2).


### F-019 · 2026-10-25 · script · OPEN
Suspected source typo: `NO4_BAR/0412` 怪物は俺たちが動くのを待ってるんじないのか has じない where
the sense, a negative rhetorical question, is じゃない (んじない 1 / 0 / 0, only here; the other
じない hits are 信じない and 感じない). Shipped as "But isn't the monster waiting for us to move?"
(`tl/script/NO4_BAR.p08.tsv:6 NO4_BAR/0412`, PR #12 Flag 8). Harmless · rulings R §11.4.


### F-020 · 2026-10-25 · system · OPEN
The 倉庫 row's form for the room names `rooms/053`, `069`, `105` (第３/第４/第６デッキ倉庫),
"Deck 3 Storeroom", is 16 characters, over the 14-character room-name cap (glossary §8; exe slot 29
bytes). The system translator needs a shorter form (e.g. "Deck 3 Store", 12) once F-006 unblocks the
store; items/013 【第３デッキ倉庫の鍵】 has its own 43-character cap · PR #12 Flag 9 · rulings R §11.1.


## CHECK positive controls
<!-- One entry per kind of violation deliberately planted and caught by CHECK (tools/README.md rule 3).
A checker that has never failed has never been tested. -->

Planted 2026-10-04 while building the tools, each caught by `assemble.py check` (exit 1), then
removed: system slot overflow (rooms/000) · character outside the font (é) · word longer than a
line · missing ending `{p}` · removed `{w}` (NO3_NO4/0018) · key that matches nothing ·
source column edited · box page of 5 rows · same source with two different targets
(NO4_BAR/s24, s27) · `{br}` last in a menu string. Setup should repeat these on `main`.

Repeated 2026-10-04 in setup, on the setup tools (bundled units), in a scratch copy of the
tree, one plant at a time; every one exited 1 with the message shown, and a clean tree passed
afterwards: container over budget (`NO1_CONTROLROOM.SCR` 70,981 / 65,535 — a 72,000-character
target; 55,800 characters still fit, at ≈ 1 byte a character) · `é` → `charset` · 38-letter
word → `longer than a line` · ending `{p}` dropped → `must end like the source` · `{w}` dropped
(NO3_NO4/0018) → `tags … differ` · unknown key `NO1_CONTROLROOM/9999` → `matches nothing` ·
source column edited → `not byte-identical` · five `{br}`-lines → `box page has 5 rows` ·
NO3_CHAPEL/s09 vs s13 → `same source, different targets` · NO2_MAINSTORAGE/0023 vs
NO4_HWR_FRONT/0128 (`{p}` only differs) → `same text with different tags` · SCN038D/14 vs
NO4_HWR_FRONT/0023 → `same source, different targets` across stores · options/000 108 / 89
bytes → `slot:` · `{br}` last in options/000 → `may not be last or doubled` · OP2/01 in five
lines → `subtitle limit 4` · NO2_CABIN_2001/s05 at 32 columns → `limit 28` · `# rows:` edited →
`header lines differ` · a fifth column → `expected 4 tab-separated columns` · pre-bundling unit
name `NO1_CONTROLROOM.tsv` → `no unit`. Also: MERGE refused with a hard error (exit 1);
UNITCHECK on a unit with nothing translated → `nothing examined` (exit 1).


## Closed
<!-- id · date · how it closed · pointer to rulings.md or the commit -->
