# Rulings — the reviewer's integration log

<!-- Append-only. Grepped on demand, never read in full. One section per merged or parked PR, written
by the reviewer in its integration commit; nobody else writes here. glossary.md holds the WHAT (one
row per term); this file holds the WHY and the evidence. HANDOFF.md → Decisions points here. -->

Each ruling records: the source string(s) with every variant spelling; the target; the reasoning
with **source-side** evidence (grep counts per store, across every variant — a census on one spelling
or on the target side is not a census); the shipped lines it binds; and whether it adds or corrects a
`glossary.md` row. A correction to an existing row is written out here with every affected line, and
the row's Ruling column points back.

Format:

```
## Unit «store id» (PR #k, MERGED | PARKED, YYYY-MM-DD)
### k.1 «short title»
- Source: `…` (variants: `…`, `…`) — N instances: a in «store», b in «store»
- Target: `…` (c cols)
- Reasoning: …
- Binds: «file:line in PROJECT.md §7's numbering», …
- Glossary: «added §n row | corrected §n row — affected lines listed above | none»
```

A ruling that reverses an earlier one says so by number and says what changes in shipped files.

---

## Unit script NO4_BAR.p01 (PR #1, MERGED, 2026-10-04)

This was the calibration unit of setup.
- **Round 0** (b614f5f): CHANGES, for three one-word last rows (§1.12).
- **Round 1** (3bffa43): MERGE, decided by the reviewer on 2026-10-04. GitHub returned 403 at review time, so the runner squash-merges into `main` when access returns and cherry-picks this commit onto the squash.

Figures:
- NO4_BAR.SCR 25,770 / 65,535 bytes, 39,765 free: +2,331 bytes over the untranslated 42,096 free. Tokens 816 / 1,499.
- At most 4 rows per page.
- CHECK compared 22 duplicate pairs and 0 tag-variant pairs.

Census counts below are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-04. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_BAR.p01.tsv`.

### 1.1 Names of the cast
- Source and counts:

  | Name (variants) | Rows |
  |---|---|
  | ジュディ | 42 / 4 / 1 |
  | — full name ジュディ・アルセラ | 3 / 0 / 0 |
  | ロブ・コリスン (variant コリスン) | コリスン 42 / 1 / 0 |
  | — full name | 3 / 0 / 0 |
  | ビル・オークランド (variants オークランド, ビル) | オークランド 52 / 3 / 0 |
  | — full name | 3 / 0 / 0 |
  | — ビル alone (SCN046A2/01 「ビル…、ゲームオーバーだ。」) | 0 / 1 / 0 |
  | ウィリアム | 28 / 6 / 0 |
  | ジャック・ウォルグ (variant ウォルグ) | ウォルグ 60 / 5 / 0 |
  | — full name | 2 / 0 / 0 |
  | レベッカ・ミラー (variant ミラー) | ミラー 48 / 3 / 0 |
  | — full name | 2 / 0 / 0 |
- Target: Judy (4), Judy Arsela (11); Rob Collison (12), Collison (8); Bill Oakland (12), Oakland (7), Bill (4); William (7); Jack Wolg (9), Wolg (4); Rebecca Miller (14), Miller (6).
- Reasoning:
  - These are the natural English spellings of the katakana, as seeded in setup (PROJECT.md §6). Arsela beats Alsera and Arcella, and Wolg beats Walg and Volg, because each follows the katakana (ア/ル, ウォ) most directly.
  - The given names ロブ, ジャック, レベッカ and アルセラ occur only inside the full names (3, 2, 2 and 3 script rows), so they need no variant of their own. This corrects the round-0 review's note proposing to add them.
  - ビル does occur alone once, as "Bill".
- Binds: `tl/script/NO4_BAR.p01.tsv:4 NO4_BAR/0001` (Judy), `:30 0027` (Judy Arsela), `:22 0019` (Rob Collison), `:24 0021` (Bill Oakland), `:18 0015` and `:21 0018` (William), `:35 0032` (Jack Wolg), `:45 0042` (Rebecca Miller).
- Glossary: added §1 rows, promoted from §9.

### 1.2 さん → "Mr." / "Miss" (PR Flags 5c)
- Source:
  - コリスンさん 15 / 0 / 0; variant コリスンさんたち 3 / 0 / 0.
  - オークランドさん 7 / 0 / 0.
  - ミラーさん 2 / 0 / 0 (NO4_BAR/0043 and NO4_BAR_T/0064, both Collison).
  - 学者さん 2 / 0 / 0.
- Target:
  - Mr. Collison (12). コリスンさんたち → "Mr. Collison and the others" (27), or "your group, Mr. Collison" (24) in address.
  - Mr. Oakland (11); Miss Miller (11).
  - 学者さん → "scientist".
- Reasoning:
  - PROJECT.md §6's "never by added words" forbids romanised honorifics and padding ("-san", "honoured"). It does not forbid the English courtesy title, which is how English carries the politeness of a surname with さん. A bare "Collison" in polite address would misstate the register.
  - A bare surname in the source stays bare.
  - さん on a role noun is dropped and carried by tone.
  - "Miss" fits Collison's old-fashioned diction, and no other speaker uses ミラーさん.
  - The title stays on the same line as its name at every wrap (§1.13 d).
- Binds: `:26 NO4_BAR/0023` (Mr. Oakland); `:33 0030` (your group, Mr. Collison); `:43 0040`, `:49 0046`, `:54 0051` (Mr. Collison); `:46 0043` (Miss Miller; scientist).
- Glossary: added §1 rows コリスンさん, オークランドさん and ミラーさん; the §2 学者 row notes the dropped さん.

### 1.3 `…。` and `──。` — the 。 is absorbed (PR Flags 5a)
- Source: `…。` or `──。` at a sentence end. In this unit: 0001, 0005, 0008, 0018, and 0046 (`………。`).
- Target: the ellipsis or dash alone: `…`, `——`, `………`.
- Reasoning:
  - In English a sentence-final `…` or `——` ends the sentence; `….` and `——.` are not used.
  - Only 。 is absorbed. `？` `！` `‼` `⁉` after `…` or `──` are kept (`people…⁉`, 0001).
  - Glyph counts of `…` and `──` are unchanged (PROJECT.md §5.1).
- Binds: `:4 NO4_BAR/0001`, `:8 0005`, `:11 0008`, `:21 0018`, `:49 0046`.
- Glossary: none. This is a punctuation convention.

### 1.4 Numbers (PR Flags 5b)
- Source: １時間 (0010, 0011), ２時間 (0012), ３人 (0028, 0029), 二日目 (0054), ７月２５日 (0053).
- Target: "within the hour", "another hour", "Two hours", "three of you", "the three of us", "our second night"; "July 25".
- Reasoning:
  - In dialogue and narration, quantities and durations are spelled out.
  - Dates are the month name plus digits, with no ordinal suffix.
  - Identifiers such as deck and cabin numbers are names, and their own glossary rows decide them (§9 第Nデッキ proposes "Deck N").
- Binds: `:13 NO4_BAR/0010`, `:14 0011`, `:15 0012`, `:31 0028`, `:32 0029`, `:56 0053`, `:57 0054`.
- Glossary: none.

### 1.5 一匹 → "a single beast" (PR Flags 5d)
- Source: 一匹 6 / 1 / 0; variant １匹 2 / 0 / 0.
- Target: `a single beast` (14) at 0033 and `A single beast?` (15) at 0034. Elsewhere it is a plain number ("one").
- Reasoning:
  - Wolg asks 何人, the counter for people. Collison answers with 一匹, the counter for animals, and Wolg's echo 一匹？ reacts to that counter. Plain "one" would lose why he asks "What do you mean?".
  - The scope is only that exchange and its prototype copies NO4_BAR_T/0051–0052.
  - Miller's 一匹見かけた is a plain counter → "I saw one" (0042). NO4_BAR/0379, 0384 and SCN038_5C2/01 take "one" by context.
- Binds: `:36 NO4_BAR/0033`, `:37 0034`, `:45 0042`.
- Glossary: added a scoped §6 row.

### 1.6 部屋 → "room" (PR Flags 5e)
- Source: 部屋 41 / 3 / 0. For contrast, キャビン 3 / 0 / 15: signage at NO4_HWL_BACK/0016, NO4_HWL_BACK2/0012 and NO4_HWR_FRONT/0099, plus the blocked system store.
- Target: `room` (4).
- Reasoning: the source uses 部屋 for every kind of room (passenger cabins, storerooms, offices) and keeps キャビン for signage and room names. "room" preserves that distinction, and "cabin" is reserved for キャビン.
- Binds: `:60 NO4_BAR/0057`.
- Glossary: added a §6 row.

### 1.7 ヤツ → "he / him / his"
- Source: ヤツ 47 / 0 / 0. やつ (2) and 奴 (2) are other uses (a type of person, a small creature), not variants.
- Target: `he` / `him` / `his` (2 / 3 / 3) when it means the monster or the killer; never "it".
- Reasoning:
  - Collison names the monster with ヤツ, a word for persons, and keeps アレ for the impersonal ("that thing", 0037). "he" carries the source's own distinction.
  - NO4_BAR/0185–0187 equate ヤツ with 例の化け物.
  - Wolg's story uses ヤツ for the killer he hunted (NO3_NO4/0023–0042).
  - The "killer" of SCN002/06 and NO4_HWR_FRONT_UP_T/0004 is the same creature in the salvagers' early account, so one pronoun keeps that reading open.
  - As a common noun for a person it is translated in context and is not bound: わからんヤツだな (NO4_HWR_FRONT/0030), 世話の焼けるヤツだ (NO4_MACHINER90/0103), ウォルグのヤツ (NO3_CHAPEL/0112).
- Binds: `:36 NO4_BAR/0033` ("He's but a single beast."), `:46 0043` ("his young"), `:48 0045` ("part of him").
- Glossary: added a §6 row, promoted from §9, where the seed read "him (the killer)".

### 1.8 化け物 · 怪物 → "monster"
- Source: 怪物 21 / 0 / 0; 化け物 58 / 1 / 0. For reference, モンスター 8 / 0 / 1, not yet rendered.
- Target: `monster` (7) for both.
- Reasoning:
  - These are synonyms with one target, not spelling variants. Listing 怪物 as the row's variant makes the census pair lines that differ only in this word, which is the intent: the creature has one name.
  - 怪物 is rendered five times in this unit.
  - NO4_BAR/0083 has both in one sentence (化け物…そうと呼ぶしかない、おぞましく恐しい怪物じゃ). The p02 translator keeps "monster" for both, as an emphatic repetition.
  - モンスター is expected to be "monster" too when first rendered.
- Binds: `:38 NO4_BAR/0035`, `:43 0040`, `:49 0046`, `:50 0047`, `:54 0051`.
- Glossary: added a §6 row, promoted from §9.

### 1.9 Other terms promoted or added
Each row was rendered in this unit; counts are script / scene / system.
- **サルベージャー** 1 / 0 / 0 (variant サルベージ 3 / 0 / 0) → `salvagers` (9), singular `salvager` (8). サルベージ, the work, → "salvage". Binds `:5 NO4_BAR/0002`.
- **沈没船引き揚げ業者** (沈没船 8 / 0 / 0) → `shipwreck salvage firm` (22). The other phrasings, 沈没船のサルベージ業者 (NO4_BAR_T/0026) and 沈没船を引き上げる業者 (NO4_HWR_FRONT/0127), are rendered in context with "shipwreck salvage". Binds `:24 0021`.
- **責任者** 2 / 0 / 0 → `the one in charge` (17). William's echo 責任者？ needs the same words (`The one in charge?`, 18). Binds `:24 0021`, `:25 0022`.
- **学者** 6 / 0 / 0 (variant 学者さん) → `scientist` (9). Miller's 私は学者よ recurs at NO4_BAR/0225 and 0368. **海洋生物学者** 2 / 0 / 0 → `marine biologist` (16). Binds `:45 0042`, `:46 0043`.
- **フィラデルフィア** 2 / 0 / 0 → `Philadelphia` (12). Binds `:57 0054`.
- **潜水装備** 3 / 0 / 0 → `diving gear` (11); recurs at NO4_BAR/0248 and 0298. Binds `:7 0004`.
- **セーブする · セーブしない** 21 / 0 / 0 each → `Save` (4) · `Don't save` (10), cap 27 (choice rows). The exact recurrences are NO3_CHAPEL s09 s13 s19 s21 s23 s25 s32 s34 / s10 s14 s20 s22 s24 s26 s33 s35 and NO4_MACHINE s03 / s04. Binds `:65`–`:88 NO4_BAR/s24`–`s57`.
- **じいさん** 9 / 0 / 0 (variant 爺さん 1 / 0 / 0) → `old man` (7). Binds `:17 0014`, `:35 0032`, `:39 0036`, `:41 0038`.
- **お嬢さん** 2 / 0 / 0 → `young lady` (10). Binds `:44 0041`.
- **虫の居所が悪い** (variant 虫の居所, 6 / 0 / 0) → `in a foul mood` (14); William's echo is `Foul mood?` (10). Binds `:26 0023`, `:27 0024`.
- **分身** 2 / 0 / 0 → `part of him` (11): the young may be pieces of the monster itself. The alternative "his other selves" was not used. Binds `:48 0045`.
- Glossary: added §2, §3, §4 and §6 rows. The §9 seeds for サルベージャー, 責任者, じいさん, セーブする · セーブしない and フィラデルフィア are promoted.

### 1.10 Register per character (glossary §7)
- Source evidence:
  - Collison: じゃ/わし/おる/〜ん throughout.
  - Oakland: 我々/私 with strangers; わし to his crew (NO3_NO4/0002, NO4_BAR/0429).
  - William: ぜ/ねえ/よ and dropped subjects (0014, 0016, 0022, 0024, 0026).
  - Wolg: 俺, terse (0025, 0032–0038, 0047).
  - Miller: わ/かしら/のよ (0040–0048).
  - Heming: ませんかな (0051).
- Target: the six §7 rows, as the PR proposed them.
- Reasoning: PROJECT.md §6 governs: register and word choice, never dialect spelling. William's roughness is blunt syntax and standard contractions with no eye dialect ('em, ain't, gonna). That also keeps him clear of the word-initial-apostrophe blind spot (§1.13 a).
- Binds: every line of the unit.
- Glossary: added §7 rows; Heming's name stays in §9.

### 1.11 Speakers (PR Flags 4)
- Source: `spk=N` is ignored (F-009). Attributions come from content, register and the 【Name】 labels of NO4_BAR_T.
- Reasoning:
  - (a) 0006 and 0008 have no prototype counterpart. The attribution of record is Oakland, who carries 0002–0013; Wolg first speaks at 0025 and introduces himself at 0032. Both renderings are speaker-neutral, so a later correction changes no text.
  - (b) 0049 and 0051 are Heming, by NO4_BAR_T/0073 and 0076.
  - (c) 0050 is Oakland, by NO4_BAR_T/0075; his わしら fits his わし to his crew.
  - F-009 is confirmed again. spk=6 carries Oakland (0002), William (0016), Collison (0017–0020), Wolg (0032) and Miller (0040). spk=2 carries Collison (0003), Oakland (0010–0011), William (0014, 0022) and Heming (0051).
- Binds: `:9 NO4_BAR/0006`, `:11 0008`, `:52 0049`, `:53 0050`, `:54 0051`.
- Glossary: none.

### 1.12 Wrap points — a geometry precedent (round-0 findings 1–3)
- Source: the round-0 head left one-word last rows at 0007 ("escaped."), 0032 ("something.") and 0043 ("helpful."). Round 1 replaced them with `…we'd have stolen it and made our escape.`, `Old man, I have a question.` and `A scientist, eh? You'll be most helpful.`.
- Reasoning: the tools choose every wrap point, so translators control them only through wording, and the result shows only in the wrapped text (`build/script_merged.tsv` after MERGE).
  1. No one-word last row where an equally faithful rewording avoids it: a synonym, a word the source implies, an equivalent idiom. If none exists, keep the literal text and flag the orphan.
  2. No line ending in a lone "a" or "I", and never a courtesy title apart from its name. A function word ("to", "of", "the") at a wrap point is acceptable.
  3. Lines ended by an authored `{br}` or by `{w}` aim at 27 columns; 28 only when flagged with the reason. 0053 `It was the night of July 25.` (28 before `{w}{br}`) is accepted: it is a one-row page, and no 27-column wording keeps the sentence.
- Binds: `:10 NO4_BAR/0007`, `:35 0032`, `:46 0043`, `:56 0053`.
- Glossary: none.

### 1.13 CHECK and UNITCHECK blind spots (PR Flags 9, plus d)
- Evidence: each was planted, one at a time, in a scratch copy of the tree on 2026-10-04. Every plant exited 0 with `All checks passed` and gave UNITCHECK 0 violations.
  - (a) 0024 `like 'em.` encodes as `ｌｉｋｅ　‘ｅｍ．`, an opening quote. A typed `’` encodes as `’` and passes.
  - (b) UNITCHECK prints `line 7 NO4_BAR/0004 … codes: source - -> target {br} {br}` for a target with no authored `{br}`.
  - (c) 0005 with a 28-column first segment before its authored `{br}` passes.
  - (d) 0030 reworded so the wrap strands a title (`your own group, Mr. | Collison?`) passes, as did the round-0 one-word last rows.
- Ruling: all four are added to PROJECT.md §7 in this commit, and FLAGS F-011 records them for a tool PR.
- Glossary: none.

### 1.14 Calibration figures (for PROJECT.md §4 and translation_prompt.md §0.2)
Characters are counted with tags excluded (`codec.char_count`); the reviewer verified every figure.

| Draft | Target characters | Ratio | Messages only | Note |
|---|---|---|---|---|
| Literal | 4,525 / 1,803 | **2.51** | 4,357 / 1,671 = 2.61 | 20 pages over 4 rows |
| Disciplined | 3,886 / 1,803 | **2.16** | 3,718 / 1,671 = 2.23 | |
| Shipped | 3,882 / 1,803 | **2.15** | 3,714 / 1,671 = 2.22 | |

Bytes: the unit costs +2,331 in NO4_BAR.SCR (42,096 → 39,765 free), about 1.29 bytes per source character after the dictionary. No unit has been byte-bound, so the measured floor is n/a.

---

## Unit script NO4_BAR.p02 (PR #5, MERGED, 2026-10-06)

Collison's account of the sinking and the siege, then Wolg, Judy, Oakland and Collison reply. It continues NO4_BAR.p01 directly. Reviewed in one round: MERGE, squash c7e2986.

Figures:
- NO4_BAR.SCR 26,910 / 65,535 bytes, 38,625 free: +1,140 bytes over p01's 39,765 free. Tokens 814 / 1,499.
- At most 4 rows per page (UNITCHECK, 43 pages). 2,970 target characters ÷ 1,405 source = 2.11 (disciplined level).
- CHECK compared 22 duplicate pairs and 0 tag-variant pairs. The reviewer's positive control (NO4_BAR_T.p02 planted in scratch) gave 23 and 1, and failed on divergent targets.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-06. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_BAR.p02.tsv` (line = row number − 58).

### 2.1 Terms promoted or added
- **食料庫** 11 / 0 / 2 → `the food storeroom` (18). Promoted from §9. NO4_BAR/0418–0446 send the party there, so the phrase recurs heavily in this room; the room name (rooms/044) waits for the system store. Binds `:36 NO4_BAR/0094`, `:45 0103`.
- **下層** 4 / 0 / 0 → `the lower decks` (15). Promoted from §9. The ship's own lower decks, which lie above the party now the ship is capsized. Binds `:36 0094`, `:38 0096`.
- **フロア** 22 / 0 / 0, including variant **フロアー** 5 / 0 / 0 → `floor` (5). Promoted from §9. 下層のフロア → "a floor on the lower decks". Binds `:36 0094`.
- **ホール** 6 / 0 / 0 alone → `the hall` (8), lowercase per PROJECT.md §6. Promoted from §9. **エントランスホール** (6 / 0 / 2) is a separate compound, not a spelling variant; it is not rendered here, so it stays in §9 as its own row with "entrance hall" proposed. Binds `:9 0067`, `:30 0088`.
- **甲板** 3 / 0 / 0 → `deck`, "on deck" (4). New. It means the ship's open deck. Keep it apart from デッキ (25 / 0 / 31), whose 第Nデッキ → "Deck N" is still in §9. NO4_BAR/0366 (甲板より上、つまりここから下のデッキ) puts both in one sentence, so the distinction matters. Binds `:14 0072`.
- **大部屋** 2 / 0 / 0 → `large room` (10). New. 部屋 → room per R §1.6. Recurs inside the merged T/0130. Binds `:31 0089`.
- Not given rows: **怪音** (2 / 0 / 0, "that strange noise", echoing p01 0055's 物音 "a strange noise"), **悪魔** (2 / 0 / 0, "a devil") and **狩り場** (2 / 0 / 0, `"hunting ground"`). Each occurs in one line here, and the line's only recurrence is its NO4_BAR_T copy (T/0100, T/0126, T/0137). That copy is an exact or tag-variant duplicate, which CHECK binds byte for byte. A glossary row would add nothing, so the glossary stays short.
- Glossary: added §2 rows 食料庫, 下層, フロア, ホール, 甲板 and the §6 row 大部屋. §9 drops 食料庫, 下層 and フロア, and splits ホール so that エントランスホール keeps its own provisional row. PR #4 (p04) proposes the same forms for 食料庫 and フロア.

### 2.2 Speakers (PR Flag 7)
- `spk=N` is ignored (F-009). Speakers come from the NO4_BAR_T `【Name】` labels:
  - 0108 Wolg (T/0149)
  - 0109–0110 Collison (T/0150)
  - 0111 Judy (T/0151)
  - 0114–0115 Oakland (T/0152)
  - 0116–0117 Collison (T/0153)
  - 0118–0119 Oakland (T/0154)
- 0112–0113 have no prototype line. They are Collison by じゃ and by この子, his word for Judy in 0109.
- F-009 again: spk=6 carries Collison (0062–0107), Wolg (0108), Judy (0111) and Oakland (0114, 0118); spk=1 carries Collison (0112).
- Binds `:50`–`:61`.
- Glossary: none.

### 2.3 `+` after a message with no ending tag: open the target with `{br}` (PR Flag 3; new CHECK blind spot)
- Source: there are 25 such boundaries in the script dump and none in scene. Japanese needs no separator; English glues the last word of one message to the first of the next.
- Target: the `+` target opens with `{br}`, at a sentence or phrase boundary. Trailing or leading spaces fail CHECK, so `{br}` is the only separator available. Flag each one as an added `{br}`.
- Evidence: the reviewer removed the leading `{br}` from 0113 in a scratch state. CHECK still printed `All checks passed`, and UNITCHECK reported 0 violations, counting 0113's first row as 10 + 9 columns. MERGE wrote "all along." followed directly by "She can't". This is now listed in PROJECT.md §7, with F-012 open for a tool fix.
- How p02 handles each boundary:
  - 0112→0113: 皆と moves into 0113 ("with others"), so the `{br}` falls between two sentences. Accepted as a step-6 reorder, as flagged.
  - 0114→0115: the subject "this monster you speak of" ends 0114 and the predicate opens 0115, as in the source. The source's internal `{br}` in 0115 now opens the row, and a `{p}` takes its place at the sentence boundary, because the page would otherwise run to 5 rows.
- Binds `:55 NO4_BAR/0113`, `:57 0115`.
- Glossary: none.

### 2.4 Leading `{p}` on a `+` row after a `{br}`-ended row (PR Flag 11)
- Rows 0066, 0083, 0089 and 0099. Without the `{p}`, their pages run to 7, 5, 5 and 6 rows in the tool model.
- Each `{p}` sits at a sentence boundary. The alternative, `{p}` before the previous row's ending `{br}`, would open the next page on a blank row.
- The tool counts the `{br}` cursor row on the earlier page. That page then holds 4, 3, 4 and 3 rows, so the conservative count costs nothing.
- The source has no `{br}` directly followed by `{p}` (0 rows), so the in-game check joins F-010.
- The other five `{p}` (0091, 0094, 0096, 0112, 0115) are mid-row at a sentence end. Each is needed by the same count. The `{p}` in 0094 also clears the source's own 5-row page from 0092 (F-010). The PR credited 0096 with this, but 0096 had no such page in the source.
- Binds `:8`, `:25`, `:31`, `:41`, `:33`, `:36`, `:38`, `:54`, `:57`.
- Glossary: none.

### 2.5 Recurrences left for NO4_BAR_T (PR Flag 9)
- The reviewer's census matched the PR's: 18 exact recurrences and 13 tag variants, all in NO4_BAR_T/0090–0148. There are none in shipped work or in sibling PRs #3 and #4.
- The exact ones must copy p02's target byte for byte, including the `{p}` added at 0066, 0091, 0094 and 0096 (T/0094, 0132, 0135, 0137).
- Recorded under F-008.

### 2.6 Accepted readings (non-blocking review notes)
- `:10 0068`: the conjectural ろう is dropped ("no one could be at ease"), as flagged. The reading is accepted as the idiomatic equivalent of narrative ろう. "surely no one was at ease" also fits two rows if a later edit wants the hedge.
- `:13 0071` and `:27 0085` each must fit one row, on the pages from 0069 and 0084. "in vain" carries どこにも見あたらない, and "We saw many killed." carries 目の前で何人も殺された.
- `:52 0110` is read in the third person ("She's merely been lucky…"), keeping 0109's topic.
- `:47 0105` お蔭で → "thanks to them", meaning the men who went.
- `:58 0116` "kidding you" is a shade casual for Collison; "pulling your leg" would sit closer to glossary §7. Not a fidelity error.

---

## Unit script NO4_BAR.p03 (PR #3, MERGED, 2026-10-06)

The end of the bar conversation, the surface crew's card game, the longwave radio attempt and the first two save prompts. It continues NO4_BAR.p02 directly. Reviewed in one round: MERGE, squash 185beb6.

Figures:
- With p01, p02 and p03 merged: NO4_BAR.SCR 28,048 / 65,535 bytes, 37,487 free. p03 costs +1,138 bytes over p02's 38,625. Tokens 803 / 1,499.
- At most 4 rows per page (UNITCHECK, 56 pages). 3,104 target characters ÷ 1,307 source = 2.37.
- CHECK compared 23 duplicate pairs (22 + 0170/0173) and 0 tag-variant pairs. The reviewer's grep compared 8,294 pairs against `tl/` (0 hits) and made 117,682 source-side comparisons against the dumps.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-06. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_BAR.p03.tsv` (line = row number − 116).

### 3.1 Terms promoted or added
- **ジョン** 86 / 8 / 1 → `John` (4). Promoted from §9. The player and Oakland's son (NO3_NO4/0043, NO6_BRIDGE/0008). PRs #2 and #4 agree. Binds `:52 0168`, `:55 0171`.
- **ヘイミング** 33 / 2 / 0 → `Heming` (6). Promoted from §9; glossary §7 drops "(name still §9)". PRs #2 and #4 agree. Binds `:56 0172`.
- **社長** 12 / 1 / 0 → `the boss` (8); "boss" in direct address (PR #4 0209). Promoted from §9. Binds `:24 0140`.
- **海上** 3 / 0 / 0 → `the surface` (11). Promoted from §9. p01's 0009 "up on the surface" agrees. Binds `:36 0152`.
- **電波** 2 / 0 / 0 → `radio waves` (11). Promoted from §9. ＶＬＦ帯の電波 → "VLF-band radio waves". Binds `:37 0153`, `:46 0162`.
- **超音波** 3 / 0 / 0 → `ultrasound` (10). Promoted from §9. It recurs at NO4_HWR_FRONT/0070. Binds `:40 0156`, `:41 0157`.
- **長波** 2 / 0 / 0 → `longwave` (8). Promoted from §9. Binds `:44 0160`, `:45 0161`.
- **無線装置** 3 / 0 / 0 → `radio equipment` (15). New. Its relatives are not rendered here, so they go to §9 as proposals:
  - 無線機 (1 / 0 / 0, NO4_HWR_FRONT/0103) → "the radio" (9)
  - 無線室 (2 / 0 / 4, including rooms/107) → "the radio room" (14, inside the room-name cap)
  - 装置 (10 / 0 / 0) and 設備 (3 / 1 / 0) on their own are **not** fixed. Their senses vary: 制御装置 "control system", 0158 装置 "device", 0155 通信設備 "communications equipment", 0162 船の設備 "this ship's equipment".
  - Binds `:55 0171`.
- **潜水艇** 2 / 0 / 0 → `submersible` (11). New. 潜水艦 "submarine" has 0 rows. It recurs at NO4_BAR_T/0108. Binds `:42 0158`.
- **回転** 5 / 0 / 0 → `roll over`, noun `roll`. New. Every row is the capsized ship turning on its long axis: NO4_HWL_BACK/0007, NO4_HWL_BACK2/0005, NO4_SHOP/0005, NO6_TOOLROOM/0003. Binds `:8 0124`.
- Not given rows:
  - 二重遭難 (2 / 0 / 0; its other row, T/0159, is a draft of 0123–0124) → "the rescuers could become victims too".
  - 下の連中 (2 / 0 / 0): the divers at 0138, the lower-deck survivors at NO4_BAR/0421.
  - 使用人 → "hired hands" and スタッフ → "staff" (2 / 0 / 0 each; the other rows are T copies).
- Glossary: added §1 ジョン, ヘイミング; §2 社長, 上の連中 (§3.2), 海上; §3 電波, 超音波, 長波, 無線装置, 潜水艇, 地上用の設備 (§3.2), 回転. §9 drops the promoted rows and gains 無線機 and 無線室.

### 3.2 Cross-PR decisions (binding on the reviews of PR #4 and PR #2)
- **ふん** — 5 / 0 / 0 as an interjection, every one `ふん、`: NO4_BAR/0133, 0223, 0232, 0247 and T/0167. The sixth grep hit, NO4_TOOL_ROOM/0070 段階をふんで, is the verb 踏む, not the interjection.
  - Target: `Hmph` (4). Punctuation follows the source (PROJECT.md §6: 、 → `,`), so the form is "Hmph, …".
  - The shipped form is p03's `:17 0133` "Hmph, if such a thing really shows up, …".
  - **PR #4 renders 0223 and 0232 as "Hmph." and must change both to "Hmph, …"** in its review.
  - Glossary: added §6 row.
- **地上用の設備** — 1 / 1 / 0: NO4_BAR/0175 and SCN011/04.
  - Target: `land-based equipment` (20).
  - PR #2's SCN011/04 already reads "Using land-based equipment underwater, unmodified, …"; its review holds it.
  - Binds `:59 0175`. Glossary: added §3 row.
- **上の連中** — 4 / 1 / 0: NO3_CHAPEL/0017, NO4_BAR/0151, 0177, 0289 and SCN011/05.
  - Target: `the people up top` (17).
  - PR #2's SCN011/05 already reads "the people up top"; its review holds it.
  - Binds `:35 0151`, `:61 0177`. Glossary: added §2 row, promoted from §9.

### 3.3 じいさん row: Variants extended (PR Flag 8)
- Source:
  - 爺 not followed by さん: 1 / 0 / 0, NO4_BAR/0142 強欲爺 (a surface crewman about Oakland).
  - じじい: 1 / 0 / 0, NO4_BAR/0259 (p05, William to Collison, うるせえ、じじいっ！).
  - ジジイ: 0.
- Target: `old man`, as the row already says. The pejorative edge is carried by the words around it ("greedy old man").
- This changes the row: its Variants grow from 爺さん to 爺さん · 爺 · じじい. No shipped line changes. The rows already bound by R §1.9 (p01 :17, :35, :39, :41) are じいさん and keep their text. The new binding is `:26 0142` "What's the greedy old man putting on airs for?"
- Glossary: §6 じいさん row, Variants extended, Ruling column → R §1.9, §3.3.

### 3.4 The save prompt (PR Flag 5)
- Source: ここまでの状況をセーブできます。セーブしますか？ — 21 / 0 / 0, every row a standalone `msg` with no `+` and no tags:
  - NO3_CHAPEL 0039 0049 0070 0079 0111 0114 0129 0130
  - NO4_BAR 0170 0173 0239 0242 0341 0377 0397 0401 0440 0443 0460 0461
  - NO4_MACHINE/0001
- Target: `You can save your progress so far. Do you want to save?` (55). It wraps 26 + 28 in 2 rows, so it fits every occurrence. It is followed by the §4 choice pair Save · Don't save.
- CHECK pairs every later occurrence byte for byte.
- Binds `:54 0170`, `:57 0173`. Glossary: added §6 row.

### 3.5 Speakers (PR Flag 4)
- `spk=N` is ignored (F-009). From the NO4_BAR_T labels:
  - Collison: 0120 (T/0155)
  - Oakland: 0121–0122, 0125, 0127, 0131, 0133 (T/0156, 0158, 0160, 0162, 0165, 0167)
  - Heming: 0123–0124, 0126, 0128 (T/0159, 0161, 0163)
  - Wolg: 0129–0130, 0132, 0134 (T/0164, 0166, 0168)
- From content:
  - the surface crew, two or three unnamed men: 0135–0147
  - Oakland, the impatient boss: 0148–0149, 0151–0152, 0154, 0157, 0159, 0161, 0163, 0171–0172, 0174, 0176
  - Wolg (俺): 0150, 0167
  - Heming, who goes to test the radio (0172): 0153, 0155, 0158, 0160, 0162, 0164, 0166, 0169, 0175
  - Miller: 0156, 0177
  - Collison: 0165
- 0168 is Heming by the flow: he asks for company at 0166, and 0169 answers John's assent. The text ("Right.{br}John, will you lend a hand?") works for Wolg as well, so a later correction changes no text.
- F-009 again: spk=5 carries Heming, Oakland, Collison, Wolg, Miller and the save prompt.
- Binds `:4`–`:61`. Glossary: none.

### 3.6 Recurrences and near-duplicates (PR Flags 5–6)
- **Exact recurrences, untranslated; CHECK will pair them:**
  - 0139 さあな。 "Who knows." ↔ NO4_MACHINER90/0021
  - 0164 わかった。 "All right." ↔ NO3_CHAPEL/0104
- **Near-duplicate, reused by hand:** 0171 "Are you done checking the radio equipment?" ↔ NO4_HWR_FRONT/0103 (無線機の調査は済んだのか) and 0145 (無線装置の調査).
- **NO4_BAR_T copies:** T/0155–0168 draft 0120–0134 with `【Name】` prefixes, so CHECK does not pair them. If kept, they reuse p03's wording (F-008):
  - T/0158 has 事故 for トラブル.
  - T/0159 joins 0123–0124.
  - T/0166 is reworded.
  - T/0167 ふん is "Hmph,".

### 3.7 Accepted readings (non-blocking review notes)
- `:8 0124` "rolls over again" and `:46 0162` "They carry well underwater.": §2.1 step-5 implications, flagged and accepted.
- `:33 0149`: the leading `{br}` separates the `+` row from 0148 at a sentence boundary (R §2.3, F-012). The page is 4 rows.
- `:9 0125` 言ったつもりだぞ → "I'm sure I told them".
- `:14 0130` drops the hedge in 味方では無いだろう; "they're hardly on our side" would keep it.
- `:50 0166` `……Then, someone come along.`: the comma is optional, and "come with me" would sit closer to 付き合ってくれ.
- None of these is a fidelity error.

---

## Unit scene OP-SCN034 (PR #2, MERGED, 2026-10-06)

The first scene unit: OP2, SCN001, SCN002 / SCN002A / SCN002OLD (one exchange in three layouts), SCN011 (Heming's radio attempt, the counterpart of NO4_BAR/0175), SCN021, SCN029, SCN034. Reviewed in one round: MERGE, squash 131288b.

Figures:
- 39 subtitles, every one 1 page, at most 4 lines (UNITCHECK, 0 violations). 1,900 target characters ÷ 794 source = 2.39. No byte container (scene); script containers unchanged (NO4_BAR.SCR 37,487 free).
- CHECK compared 26 duplicate pairs (main's 23 + SCN002/01, /05, /08 = SCN002A) and 2 tag-variant pairs (SCN002/02, /03 ~ SCN002A). The reviewer's source-side script made 162,708 comparisons (exact and tag-variant, then label-stripped with final 。！？⁉ normalised): no recurrence in shipped `tl/` or in open PR #4.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-06. Line citations use PROJECT.md §7's numbering in `tl/scene/OP-SCN034.tsv` (line = row index + 3).

### 4.1 Terms promoted or added
- **殺人鬼** 5 / 2 / 0 → `the killer` (10). Promoted from §9 (R §1.7). Rows: SCN002/06, SCN002OLD/06, NO3_NO4/0018 and 0024 (いかれた殺人鬼, Wolg's police story: "a crazed killer"), NO4_BAR_T/0164, NO4_HWR_BACK_T/0006 (copy of SCN002OLD/06), NO4_HWR_FRONT_UP_T/0004 (殺人鬼？…たしかに鬼ね, a pun on 鬼, rendered in context). Binds `:12 SCN002/06`, `:28 SCN002OLD/06`. Glossary: §6 row, §9 row removed.
- **弾切れ** 0 / 2 / 1 → `out of ammo` (11). New. SCN029/02, SCN046A1/07 (弾切れ⁉), items/000 (system, blocked; 弾切れに注意 in context). Binds `:39 SCN029/02`. Glossary: §3 row.
- **くっ** 1 / 1 / 0 → `Ngh` (3). New. SCN029/02 くっ、 and NO4_BAR_T/0072 【ウォルグ】くっ…！ → "Ngh…!". Binds `:39`. Glossary: §6 row.
- **くそ** 0 / 4 / 0 as the curse (the 1 script hit, NO4_BAR/0305 ともかくそんな, is not it): SCN011/02 くそ！, SCN038A/02 くそおおおっ‼, SCN046A1/03 くそっ‼, SCN047B3/01 くそっ…. Not proposed by the PR; added by the reviewer from `:32 SCN011/02` "Damn!" so the three later scene rows reuse the word. Elongation stretches the vowel, in context. Glossary: §6 row.
- **きゃあ…っ** 0 / 1 / 0 (the 3 script hits for きゃ are なきゃ / やらなきゃ): SCN034/02 きゃ + あ×10 + っ‼ → `Aaaaaaaaaaah‼` (13). A one-off, kept as a §6 treatment because it gives the rule (A for きゃ, one a per あ, h for っ) a later scream reuses. Binds `:42`.
- **ジョン**, **ヘイミング**: already promoted in R §3.1; this unit agrees (`:4`, `:40`, `:41`; 【Heming】 at `:25`).
- Not given rows: 安全な場所 "a safe place" (SCN001/02, SCN002/01; NO4_HWR_FRONT_DOWN_T/0003, NO4_MACHINER90/0107 near-parallels), 得体の知れない "strange" (SCN002A/04), さあ → "All right," (SCN002/08, SCN011/06). Context words; later units should reuse where the line matches (PR Flag 9).

### 4.2 上 alone → "the people up top" (PR Flag 6)
- Source: １時間で戻らなければ上も異常に気付く — SCN002/05, SCN002A/05, SCN002OLD/05, NO4_HWR_BACK_T/0005 (0 / 3 / 0 plus the T copy). 上 alone is a common word and not a Variant; here its referent is the surface crew of 上の連中 (R §3.2).
- Target: "If we're not back within the hour, the people up top will notice something's wrong." も dropped ("too" has nothing to attach to). Not identical to NO4_BAR/0010 (１時間たって戻らなければ、我々の事故に気付く → "If we don't return within the hour, …"); different source, no pairing.
- Binds `:11`, `:19`, `:27`. Glossary: §2 上の連中 row note extended (scope note, no target change, no shipped line changes).

### 4.3 Speakers and readings (PR Flags 3–5, 7, 10)
- SCN002 / SCN002A named from the SCN002OLD labels: 01 Oakland, 02 Wolg, 03 Heming, 04 Miller, 05 Oakland, 06 Miller, 07 Wolg, 08 Oakland; SCN002A/04, /06 Miller by content; SCN002A/07 unlabelled, rendered speaker-neutral. SCN001/01 Oakland, /02 Wolg (NO4_MACHINE_T/s06–s08). SCN011/01–06 Heming (NO4_BAR/0158–0175). SCN021, SCN029 unnamed (SCN029 probably Wolg, armed); SCN034/01 a woman (わね), Miller or Judy. Every line is worded so a corrected attribution changes no text.
- `:4 OP2/01` 捕まえて has no object: "Catch it!" held until someone watches the OP2 movie (FLAGS F-001).
- Punctuation: `:5 SCN001/01` 。 → `?` (English question); `:20 SCN002A/06` keeps ！ ("what then!"); SCN002OLD/02, 03, 05–08 have no final 。 in the source and no final period in English; `:26 SCN002OLD/04` ！？ (two glyphs) → `!?` (two glyphs), SCN002/04's ⁉ stays ⁉.
- Stutters take the English hyphen on the first English word (`H-help`, `Wh-what`, `J-John`); `:37 SCN021/01` た、助けてく──！ → "H-help m——!" mirrors the cut-off.
- Accepted, non-blocking: `:13 SCN002/07` やられん → "we're" (could be "I'm"); `:20` "what then!" as the source's exclamation.

### 4.4 New CHECK blind spot: labelled copies (PR Flag 13)
- CHECK groups rows by source and by source with `{p}` `{w}` `{br}` removed (`tools/assemble.py`, duplicates block); it never strips a leading `【Name】` and never equates `！？` with `⁉`.
- Evidence: a planted divergent target on SCN002OLD/01 (`【Oakland】Is anywhere safe at all?`) in the review checkout passed CHECK (`All checks passed`).
- Affected now: SCN002OLD ↔ SCN002 / SCN002A (8 rows, checked by hand: identical words after the label), NO4_MACHINE_T/s06–s08 ↔ SCN001/01–02, NO4_HWR_BACK_T/0004 ↔ SCN002OLD/04, and every `【Name】` row of the `_T` scripts against its shipped room (F-008).
- Ruling: added to PROJECT.md §7 in this commit; FLAGS F-013 records it for a tool PR.

### 4.5 Recurrences left for NO4_T (PR Flag 8)
- NO4_HWR_BACK_T/0001–0003, 0005–0008 (NO4_T.b01) are tag-variants of SCN002OLD/01–03, 05–08: CHECK pairs them. Reuse each SCN002OLD target with `{p}` appended.
- NO4_HWR_BACK_T/0004 (⁉, not ！？) is not paired: `【Miller】Hide? How long are we meant to hide⁉{p}`.
- NO4_MACHINE_T/s06 `【Oakland】What are we to do?` (27 columns, one `text` line); s07–s08 split SCN001/02 and need their own cut within 28 (27 preferred), keeping its words where they fit.

---

## Unit script NO4_BAR.p04 (PR #4, MERGED, 2026-10-06)

The bar conversation after the radio attempt. The survivors argue about food and the monster, then Wolg forms the search teams and sends them out. It continues NO4_BAR.p03 directly. Reviewed in two rounds:
- **Round 0** (5b9254c): CHANGES. Every mechanical gate passed; the three findings were all ふん (§5.2).
- **Round 1** (86d0b84): MERGE, squash 42d2db9. Only 0223 and 0232 changed.

Figures:
- With p01–p04 merged: NO4_BAR.SCR 28,641 / 65,535 bytes, 36,894 free; tokens 788 / 1,499 (MEASURE). p04 costs +593 bytes over p03's 37,487.
- At most 4 rows per page (UNITCHECK, 52 pages, 0 violations). About 3,023 target characters ÷ 1,466 source = 2.06.
- CHECK compared 26 duplicate pairs and 2 tag-variant pairs, the same as main without p04: no source in the unit recurs in a translated row.
- The reviewer's grep made 110,084 source-side comparisons (58 rows × 1,898 other script and scene dump rows) at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped with punctuation normalised. The only recurrence is 0201 (§5.6).

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-06. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_BAR.p04.tsv` (line = row number − 174).

### 5.1 Terms promoted or added
- **第Nデッキ** → `Deck N` (6), e.g. "Deck 4". 15 / 0 / 29 rows, decks ２–６ only. Promoted from §9.
  - Capitalised, with an Arabic numeral, like a name.
  - デッキ alone (このデッキ, 下のデッキ; 25 script rows contain デッキ) is not fixed: lowercase "deck" in context.
  - The system deck-name cap of 10 (F-006) applies when that store unblocks.
  - Binds `:58 0232`. Glossary: §2 row added; §9 row removed.
- **ウォルグさん** → `Mr. Wolg` (8). 1 / 0 / 0. New. Surname + さん → title + surname, as コリスンさん (R §1.2). Collison is the speaker. Never split from the name at a wrap: 0195 wraps "Let us pray Mr. Wolg brings | him down…".
  - Binds `:21 0195`. Glossary: §1 row added.
- **元警官** → `ex-policeman` (12). 3 / 0 / 0: NO4_BAR/0190, NO3_NO4/0014, NO3_CHAPEL/0089. New. It matches glossary §7's Wolg row.
  - 警官 (5 / 0 / 0, including the 3 元警官 rows) is not fixed on its own. 0231 renders it "cop" (Miller's sarcasm: 警官続けてれば → "if you'd stayed a cop").
  - Binds `:16 0190`. Glossary: §2 row added.
- **生き残り** → `survivor(s)` (8 / 9); **生き残りグループ** → `survivor group` (14). 22 / 0 / 0, including 1 グループ row. New.
  - Binds `:37 0211` ("other survivors") and `:59 0233` ("another survivor group"). Glossary: §2 row added.
- **薬品** → `medicine` (8). 2 / 0 / 0: NO4_BAR/0226, NO3_MEDICALROOM/0002. New.
  - Binds `:52 0226`. Glossary: §3 row added.
- **ヘイミングたち** → in context. 1 / 1 / 0: NO4_BAR/0232 "Heming's team" (Heming paired with Miller at 0224), and SCN038A/07 射軸にヘイミングたちがいる, untranslated.
  - The ヘイミング row gains the Variant and a scope note; its target "Heming" is unchanged and no shipped line changes.
  - Binds `:58 0232`. Glossary: §1 ヘイミング row, Variants extended, Ruling column → R §3.1, §5.1.
- Conforming, already fixed:
  - ヤツ → he/him (0185–0187, 0195, 0197–0199, 0204, 0206, 0208)
  - 化け物 → monster (0186, 0198)
  - 食料庫 → the food storeroom (0183, 0188)
  - コリスンさん → Mr. Collison (0189)
  - じいさん → old man (0205)
  - 社長 → "boss" in address (0209), "the boss" otherwise (0218)
  - フロア → floor (0220)
  - 部屋 → room (0196)
  - 学者 → scientist (0225)
  - 装備 → "whoever destroyed our gear" (0212), as p03 0129
- PR #4 also proposed 食料庫, フロア, ジョン, ヘイミング and 社長 as promotions; R §2.1 and R §3.1 had already promoted them.

### 5.2 ふん applied (round-0 findings 1–3; R §3.2)
- Round 0 rendered 0223 and 0232 as "Hmph." against the §6 row (ふん、 → "Hmph,"). Round 1 shipped `:49 0223` `Hmph, then you can command.` (27) and `:58 0232` `Hmph, talk all you like.{br}…` (first line 24).
- With 0133 in p03, three of the five interjection rows are now shipped. NO4_BAR/0247 (p05) and NO4_BAR_T/0167 remain, both ふん、 → "Hmph,".
- The PR's "Hmph." glossary proposal was withdrawn. Glossary: none.

### 5.3 Speakers (PR Flag 5)
- NO4_BAR_T ends at T/0181 and has no draft of this scene, so every speaker comes from content (F-009).
- Oakland: 0189–0190, 0196, 0210, 0213, 0215, 0217, 0219, 0222, 0235.
- Collison: 0183, 0185, 0187–0188, 0191, 0195, 0197, 0199, 0201, 0204, 0206, 0208.
- Wolg: 0182, 0184, 0186, 0192–0194, 0198, 0200, 0202–0203, 0205, 0207, 0209, 0211–0212, 0214, 0216, 0218, 0220–0221, 0223–0224, 0226–0227, 0229–0230, 0232–0234.
- Miller: 0225, 0228, 0231.
- Uncertain:
  - 0178 is Oakland, Heming or Collison.
  - 0179–0180 are probably Wolg.
  - 0181 is perhaps William.
  - All four are rendered speaker-neutral, so a corrected attribution changes no text.
- F-009 again: spk=6 carries a salvager (0182, 0184, 0186) and Collison (0187–0188).

### 5.4 Movable codes and geometry (PR Flag 2)
- `:16 0190`, a `+` message: the source `{br}` → `{p}` at the sentence boundary. Without it, the page that 0189 opens runs to 5–6 rows; with it, the pages are 3 and 2 rows. This is the only change to the authored `{br}`/`{p}`/`{w}` sequence.
- 39 lines end at an authored `{br}`. Measured with `len()` on the wrapped build row, the longest is 27 (0218, 0229, 0231, 0233).
- No `+` row follows an untagged message, so there is no F-012 glue.

### 5.5 Suspected source typo: 0218 一斑 → 一班 (PR Flag 7)
- Source: `二人ずつの二班に分かれる。{br}俺とジョン、もう一斑は社長とヘイミングだ。` 一斑 ("a spot, a fleck") occurs only here, 1 / 0 / 0; 一班 has 0 rows. 班 alone appears in the same row's 二班 and in NO4_HWR_FRONT/0068 and 0074. The intended word is 一班, "the other team".
- Target: `John and me; the other pair is the boss and Heming.` ("pair" follows 二人ずつ). Binds `:44 0218`.
- FLAGS F-014. Glossary: none.

### 5.6 Recurrences (PR Flag 8)
- 0201 `………。` → `………`, the same form as p01 `:49 0046` (R §1.3). It recurs untranslated:
  - 8 exact rows: NO3_NO4/0007, 0061; NO4_BAR/0265, 0430; NO4_HWR_FRONT/0057, 0092; SCN038_5C1/10, SCN046B1/01.
  - 3 tag-variant rows: NO4_MACHINER90/0108, NO4_TOOL_ROOM/0025, 0060.
  - CHECK pairs all 11 once they are translated.
- Echoes for later units (PR Flag 9):
  - 0212 "whoever destroyed our gear" (also NO4_BAR/0254, 0298).
  - 0217 "That's true, but…" (= p01 0008).
  - 0227 and 0230: 長居する可能性が高い → "A long stay here is likely" / "…gets even more likely".
  - 0225 私は学者よ → "I'm a scientist" (recurs at NO4_BAR/0368).

### 5.7 Accepted readings (non-blocking review notes)
- `:59 0233`: 発見しても → the question-form conditional "Find another survivor group? Don't rush to make contact." It adds a `?` the source lacks. This is a §2.1 step-6 reordering, flagged: it keeps 生き残り and グループ in a 4-row page without a second `{p}`.
- `:16 0190`: このウォルグ → "Wolg", dropping the deictic "here" to avoid a lone "an" at a wrap and a one-word last row. A §2.1 step-3 gloss drop, flagged.
- `:53 0227` and `:59 0233` drop からな's "since". Both pages are already 4 rows.
- `:31 0205` "the old man's stories" reads as a dismissive third person. "your stories, old man" would sit closer, if a later edit wants it.
- `:57 0231`: 警官 → "cop" (§5.1).
- Stutters take a hyphen on the first English word: `:36 0210` "Y-yes.", `:45 0219` "Wh-what…⁉", `:51 0225` "M-me⁉". The same treatment as p03 0163 "R-right" and R §4.3.
- `:12 0186` puts the mentioned pronoun in quotation marks (`"he,"` → “he,”).
- `:48 0222` keeps the source's 。 and renders the rhetorical question as a statement.
- None of these is a fidelity error.

---

## Unit script NO4_BAR.p05 (PR #6, MERGED, 2026-10-06)

The bar after the search: Wolg's report (the culprit is human; one body was shot), William walks out, the surface crew loses the ship on the sonar, the party beds down, and Collison is attacked. It continues NO4_BAR.p04 directly. Reviewed once:
- **Round 0** (d7386be): MERGE, squash c6858ea. Every gate passed; no finding.

Figures:
- With p01–p05 merged: NO4_BAR.SCR 29,159 / 65,535 bytes, 36,376 free; tokens 777 / 1,499 (MEASURE). p05 costs +518 bytes over p04's 36,894.
- At most 4 rows per page (UNITCHECK, 58 pages, 0 violations). 2,679 target characters ÷ 1,208 source = 2.22.
- CHECK compared 29 duplicate pairs (main's 26 + 0239, 0242, 0265) and 2 tag-variant pairs.
- The reviewer's census made 110,084 source-side comparisons (58 rows × 1,898 other script and scene dump rows) at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped with final punctuation normalised. Hits are in §6.4.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-06. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_BAR.p05.tsv` (line = row number − 232).

### 6.1 Terms promoted from §9
- **客船** → `passenger ship` (14). 4 / 0 / 0: NO4_BAR/0182 (p04, shipped "passenger ship"), 0277, 0279, NO4_HWR_FRONT/0007. 例の客船 → "That passenger ship" (0279).
  - Binds `:45 0277`, `:47 0279`. Glossary: §2 row added.
- **便所** → `the toilet` (10). 2 / 0 / 0: NO4_BAR/0292, NO4_HWR_FRONT/0011, both Collison (わし). "the head" was the alternative; "toilet" is the plain word and needs no nautical gloss.
  - Binds `:60 0292`. Glossary: §2 row added.
- **ソナー** → `the sonar` (9). 5 / 0 / 0: NO4_BAR/0272, 0279, 0282, NO4_HWR_FRONT/0064, 0069. ソナーの反応が消えてしまった → "The contact's vanished from the sonar." (0272); the HWR_FRONT rows ソナーに反応が無い take "no contact on the sonar" in context.
  - Binds `:40 0272`, `:47 0279`, `:50 0282`. Glossary: §3 row added.
- **死体** → `body` (4). 23 / 0 / 0 (listed in the §6 row's census). Only the 死体 part of the §9 seed is promoted: 死骸 (2 / 0 / 0: NO4_BAR/0387, 0455) and 遺体 (1 / 0 / 0: NO4_BAR/0294) are rendered by p07 and p06 and stay in §9 until those reviews. The §9 row is narrowed to 死骸 · 遺体, its targets unchanged.
  - Binds `:18 0250`, `:19 0251`, `:20 0252`. Glossary: §6 row added; §9 row narrowed.
- **見張り** → `watch` (5): "stand watch", "keep watch", "change of watch". 7 / 0 / 0: NO3_CHAPEL/0061, 0097 (見張りの順番, added to the Variants), NO4_BAR/0288, 0322, 0339, 0400, NO4_HWR_FRONT/0143. 交代で見張りを立てて → "take turns standing watch". Open PRs #9 (0322 "stand watch", 0339 "change of watch") and #8 (0400 "keep watch") already conform.
  - Binds `:56 0288`. Glossary: §6 row added; §9 row removed.

### 6.2 Speakers (PR Flag 4)
- NO4_BAR_T has no draft past T/0181, so every speaker comes from content (F-009).
  - Collison: 0236–0237, 0258, 0260, 0262, 0292. Wolg: 0238, 0244, 0246, 0249–0250, 0252, 0256, 0267, 0269, 0287–0288, 0293. Oakland: 0240–0241, 0243, 0263, 0266, 0268. Miller: 0251, 0291. William: 0255, 0257, 0259, 0261.
  - Surface crew (0271–0286): crewman A 0271, 0273, 0275, 0277; the sonar operator 0272, 0274, 0276, 0279, 0281, 0283, 0285; their superior 0278, 0280, 0282, 0284, 0286.
- Uncertain, every one rendered speaker-neutral, so a corrected attribution changes no text: 0245, 0247, 0248, 0253 (Oakland or William; 0247's ふん、 plus the skeptic's line echoes Oakland's p03 0133, and 0248's food and diving gear fit him); 0254 (Oakland's 我々, or Wolg); 0264 (Wolg or Oakland); 0265 (anyone); 0270 (Oakland or Heming); 0289 (Miller, Heming or Oakland); 0290 (Oakland or Heming, 出来ん).
- Binds `:4`–`:61`. Glossary: none.

### 6.3 Movable codes and readings (PR Flags 2, 3, 5)
- `:18 0250`: the source `{br}` before そうだろ、ミラー is removed, `{br} {p}` → `{p}`. With it the page is 5 rows; joined, the last row reads "weapon. Right, Miller?" (22).
- `:30 0262`: 申し訳ない。{br}オークランドさん。 → "My apologies, Mr. Oakland." (26), the vocative merged as translation_prompt §5 example 1.
- These are the only differences in the authored `{br}`/`{p}`/`{w}` sequence. No `{p}` added, no `{w}`, no `+` rows (F-012 n/a). Lines ended by an authored `{br}` measure 27 at most (0276).
- `:23 0255` お前らが作ったんだろ⁉ has no stated object. Read as the shot body ("You did it yourselves, didn't you⁉"), which 0257 この、人殺しめ…‼ "Why, you murderers…‼" follows. The alternative, "You made it up", is noted; the English covers both loosely.
- `:22 0254` 我々の装備を破壊した輩 → "whoever destroyed our gear", as p04 0212. PR #9's 0298 潜水装備を破壊した輩 → "whoever destroyed our diving gear" keeps the same frame.
- `:38 0270` 上からの助け → "help from the people up top" (上 alone, R §4.2). `:54 0286` 非常招集 → "Emergency muster".
- Step-5/6 departures, flagged and accepted: `:50 0282` clause reorder "What were you watching, if not the sonar?"; `:12 0244` "We know …" supplies the verb from 0243's わかったか; `:9 0241` 一刻も早く → "without delay"; `:15 0247` など → "simply".
- Glossary: none.

### 6.4 Recurrences (PR Flag 6)
- 0239 and 0242: the save prompt (R §3.4), byte-identical to 0170 and 0173.
- 0265 `………。` → `………` = 0201 (R §5.6). Its remaining recurrences are as R §5.6 lists them; the `【Name】`/unlabelled ……… rows (NO4_BAR_T/0010, 0068, 0151; NO4_HWR_FRONT/0033, 0123, 0129; NO4_HWR_FRONT_UP_T/0022, 0024, 0028; NO4_MACHINER90/0010) take `………` with their own ending tag.
- **Untranslated exact recurrences; CHECK pairs them when translated:**
  - 0245 なんだと⁉ → "What⁉" ↔ NO4_HWL_BACK/0008 (after 船体が回転し始めるぞ; the reading fits).
  - 0263 いいや。 → "Not at all." ↔ NO4_BAR/0432 (p08; the reply to なにか文句でもあるのか).
- **Not paired by CHECK:** NO3_CHAPEL/0033 なんだと‼ (‼ for ⁉) should take "What‼".
- Glossary: none.

### 6.5 Accepted readings (non-blocking review notes)
- `:61 0293` "attacked by the monster": "a monster" would mark the surprise after 0246's "The culprit is human"; both read.
- `:53 0285` "Cards with this guy…" is elliptical for "Playing cards with this guy…", as the source's カードを… is.
- `:60 0292` wraps "I'm off to the toilet. Will | you come along?": acceptable under R §1.12 (no lone "a"/"I", no orphan).
- `:28 0260` おい → "Here," keeps Collison's old-fashioned diction (glossary §7).
- None of these is a fidelity error.

## Unit script NO4_BAR.p06 (PR #9, MERGED, 2026-10-25)

The bar after Collison is lost into the air vent: the survivors argue over the vents, Miller and Judy move to the small room, Wolg sets two rules, and after the save prompt Wolg reports the first handgun encounter and the spider comparison follows. It continues NO4_BAR.p05 directly. Reviewed twice:
- **Round 0** (3e49f41, 2026-10-06): CHANGES. Four wraps left a line ending in a lone "a" (0298, 0312, 0330, 0335; R §1.12 rule 2), 0335 also read as innuendo ("get it up"), and 怪物 was dropped at 0351. The PR body's figures were stale.
- **Round 1** (3471e2d, after the run's pause 2026-10-06 → 2026-10-25): MERGE, squash 1541592. Exactly those five rows changed, each to the reviewer's wording; the merge of `origin/main` left the unit file untouched.

Figures:
- With p01–p06 merged: NO4_BAR.SCR 29,361 / 65,535 bytes, 36,174 free; tokens 730 / 1,499 (MEASURE). p06 costs +202 bytes over p05's 36,376.
- At most 4 rows per page (UNITCHECK, 58 rows, 55 pages, 0 violations). 2,983 target characters ÷ 1,384 source = 2.16.
- CHECK compared 30 duplicate pairs (main's 29 + 0341) and 2 tag-variant pairs.
- The reviewer's census made 120,988 source-side comparisons (58 rows × 2,086 other script, scene and system dump rows) at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped with ！？ → ⁉ and final punctuation normalised. Hits are in §7.4.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_BAR.p06.tsv` (line = row number − 290).

### 7.1 Terms promoted from §9, and one added
- **通風孔** → `air vent` (8), then `vent` / `vents`. 20 / 0 / 0: NO4_BAR/0294, 0302, 0307, 0311, 0321; NO2_CABIN_2001/0001, s05; NO2_SUBSTORAGE/0002, 0009, s06; NO2_TOFE_ROOM/0001, 0003, 0004; NO3_CABIN_3003/0002, s06; NO3_CABIN_3105/0001, 0003, 0004, 0005, s07. The full form at the scene's first mention (0294 "dragged deep into the air vent"), the short form after (0302 "the room's vent", 0307 "a vent in here", 0311 "a room with no vents", 0321 "without vents"). The room scripts of NO2/NO3 are examine texts, each a fresh first mention: "air vent".
  - Binds `:4 0294`, `:12 0302`, `:17 0307`, `:21 0311`, `:31 0321`. Glossary: §2 row added; §9 row removed.
- **中央ダクト** → `the central duct` (16). 1 / 0 / 0: NO4_BAR/0302 only.
  - Binds `:12 0302`. Glossary: §2 row added.
- **遺体** → `remains` (7). 1 / 0 / 0: NO4_BAR/0294 遺体は見つからなかった → "We found no remains". Only the 遺体 part of the §9 row is promoted; 死骸 (2 / 0 / 0: NO4_BAR/0387, 0455) is rendered by p07 (PR #8, still open) and stays in §9.
  - Binds `:4 0294`. Glossary: §6 row added; §9 row narrowed to 死骸.
- **ハンドガン** → `handgun` (7). 3 / 0 / 2: NO4_BAR/0343, NO4_MACHINER90/0004, 0012; equip/000, items/000 (system, blocked). ハンドガン程度の銃弾 → "Bullets from a mere handgun" (程度 as "mere").
  - Binds `:53 0343`. Glossary: §3 row added; §9 row removed.
- **蜘蛛 · クモ** → `spider` (6). 蜘蛛 4 / 0 / 0 (NO4_BAR/0349, 0350, 0352, NO5_BANK/0006) + クモ 2 / 0 / 0 (NO4_BAR/0040, NO4_BAR_T/0059) = 6. p01's 0040 クモのような形 shipped "spider-shaped" and agrees; PR #8 renders 0352 "spiders".
  - Binds `:59 0349`, `:60 0350`. Glossary: §6 row added; §9 row removed.
- **昆虫** → `insect` (6). 12 / 0 / 0, of which 昆虫採集 1 / 0 / 0 (NO4_BAR/0389, p07's "bug collecting"). 昆虫がでかくなった怪物 → "an overgrown insect monster" (0351, round-0 finding 5). Only 昆虫 alone is promoted; 昆虫採集 and the 節足動物門鋏角亜門 note stay in §9 for PR #8.
  - Binds `:60 0350`, `:61 0351`. Glossary: §6 row added; §9 row narrowed to 昆虫採集.
- **フッ** (new) → `Heh` (3), punctuation per source. 2 / 1 / 0: NO4_BAR/0299 フッ…そんなものがあればだがな → "Heh… if any exist, that is."; NO3_NO4/0017 フッ、どうやら知らないようだな (Wolg, his police past) → "Heh, …". The scene hit is グフッ‼ (SCN038B/17, a grunt as someone is struck), not this scoff.
  - Binds `:9 0299`. Glossary: §6 row added.

### 7.2 Speakers (PR Flag 6)
- NO4_BAR_T has no draft of this scene, so every speaker comes from content (F-009).
  - Wolg: 0294, 0298–0299, 0301–0302, 0304–0306, 0318, 0320, 0322, 0324, 0327, 0329, 0331, 0333, 0335, 0337–0339, 0342–0343, 0345, 0348.
  - Oakland: 0295, 0297, 0300, 0303, 0319, 0321, 0323, 0325–0326, 0328, 0330, 0332, 0334, 0336, 0344, 0351.
  - Miller: 0296, 0307, 0309–0310, 0312, 0314–0317, 0346.
- Uncertain, every one rendered speaker-neutral, so a corrected attribution changes no text: 0308 and 0311 (Oakland or Heming); 0313 (Wolg or Oakland); 0340 (probably Oakland); 0347 (Oakland or Heming); 0350 (Wolg or Heming); 0349 (probably William: やがる, and NO4_BAR/0363 says they met him in a corridor).
- spk=4 carries Wolg (0294), Oakland (0295) and Miller (0309); spk=5 carries Wolg (0320) and Oakland (0326). spk=N is not a character id.
- Glossary: none.

### 7.3 Movable codes and readings (PR Flags 2–5, 7, 9)
- Authored `{br}`/`{p}`/`{w}` diff against the source, exactly as flagged: 0294 `{p}` → `{p} {p}` (a click after "…into the air vent."; pages 2 + 3); 0315 `-` → `{br}` (F-012, sentence boundary after the untagged 0314); 0338 `{br}` → `{br} {p}` (leading `{br}` after the untagged 0337 at "If you run into him," / "don't try to fight; run."; the source's internal `{br}` becomes a `{p}` before "Keep to these two rules."); 0349 `{br} {br}` → `{br}` (§2.1 step 2, "Not so." runs on). No `{w}` in the unit. Lines ended by an authored `{br}` measure 27 at most (0307, 0309, 0327, 0348).
- Round-0 wrap fixes (R §1.12): 0298 "a real monster is aboard too…" (28 / 23 / 22); 0312 "I'd had enough of" for いい加減うんざりしてた (21 / 24 / 26 / 15); 0330 "What's the difference?" for どう違うというんだ (27 / 26 / 24); 0335 "I'll raise it to one hundred percent" for １００％まで…引き上げる, literal and free of the innuendo (23 / 20 / 27 / 28). The F-011 scan of all 375 translated script rows now finds no line ending in a lone "a", "I" or "an".
- The monster takes he/him/his wherever an elided subject or object means it (0301, 0302, 0321, 0326, 0328, 0330, 0344, 0345, 0348, 0349, 0351), and 0337 ヤツ → "him" (glossary §6, R §1.7; p04 0198).
- Step-5 implications, flagged and accepted: `:55 0345` 効かないと決まったわけじゃない → "That's not certain." (points back to 0344); `:47 0337` 部屋の外へは → "go outside"; `:58 0348` 動きが思ったより鈍い → "he's slower than we thought"; `:5 0295` → "Can such nonsense be true⁉".
- 0321 正面から襲ってきたどうする is read as the conditional 襲ってきたら (suspected source typo, F-015).
- Readings: 0331 算数の勝負 → "a math contest"; 0299 化け物用の対策 → "anti-monster measures"; 0320 女性専用 → "ladies-only"; 0296 また一人、減った → "We've lost another one."; 0317 護衛 → "escort".
- Glossary: none.

### 7.4 Recurrences (PR Flag 8)
- 0341: the save prompt (R §3.4), ×20 exact in the dumps; byte-identical to 0170, 0173, 0239, 0242.
- 0298 輩 → "whoever destroyed our diving gear", the frame of p04 0212 and p05 0254 (R §6.3).
- 0336 頼んだぞ。 → "I'm counting on you." as p04 0235; NO3_NO4/0010 should reuse it.
- 0325 どうすればいいんだ…？ ("What should we do…?") matches SCN001/01 and NO4_MACHINE_T/s06 どうすればいいんだ。 only with final punctuation normalised, so it is not a duplicate; SCN001/01 shipped "What are we to do?" (Oakland). Left as written; the round-0 note offering "What are we to do…?" was optional.
- Glossary: none.

### 7.5 Accepted readings (non-blocking review notes)
- `:12 0302` "he reached for the room's vent" can read as grabbing the vent itself; "reached in through the room's vent" was offered in round 0 and not required.
- None of these is a fidelity error.

## Unit script NO4_BAR.p07 (PR #8, MERGED, 2026-10-25)

The bar conversation goes on. It covers the spider/insect exchange, Wolg's three search teams, the report on the small monsters and the live sample, and then the second victim. It continues NO4_BAR.p06 directly. Reviewed twice:
- **Round 0** (7977ba8, 2026-10-06): CHANGES.
  - 0383 wrapped to a line ending in a lone "a" (R §1.12 rule 2).
  - 0378 left a one-word row, "everywhere.", before an authored `{br}` (R §1.12 rule 1).
  - The PR body's wrap claim was untrue, and its figures were measured without p05.
- **Round 1** (860c462): MERGE, squash 2a0b375.
  - Exactly those two rows changed, each to the reviewer's wording.
  - The merge of `origin/main` left every other row untouched (`git diff 7977ba8 860c462`).

Figures:
- **Container**, with p01–p07 merged: NO4_BAR.SCR 29,178 / 65,535 bytes, 36,357 free; tokens 621 / 1,499 (MEASURE).
  - Against p06's 36,174 free, p07 *frees* 183 bytes, because the script dictionary rebuilds over the English text (tokens 730 → 621).
  - The PR body's 36,053 was measured before p06 landed.
- **Pages**: at most 4 rows per page (UNITCHECK, 58 rows, 59 pages, 0 violations).
- **Ratio**: 3,423 target characters ÷ 1,556 source characters = 2.20.
- **Duplicates**: CHECK compared 33 duplicate pairs (main's 30, plus 0377, 0397 and 0401) and 2 tag-variant pairs.
  - The reviewer's census made 120,988 source-side comparisons: 58 rows × 2,086 other script, scene and system dump rows.
  - It ran at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped with ！？ → ⁉ and final punctuation normalised.
  - It found 67 hits, of which 21 are translated pairs, with 0 mismatches. The hits are in §8.4.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_BAR.p07.tsv` (line = row number − 348).

### 8.1 Terms promoted from §9
- **モンスター** → `monster`; the small kind → `small monster(s)` (13 (14)).
  - Census: 8 / 0 / 1. Script: NO4_BAR/0378 小さいタイプのモンスター, 0384 小さなモンスター, 0398 小型モンスター, NO3_NO4/0053, NO4_TOOL_ROOM/0039, NO5_BANK/0001 小さいモンスター, NO5_HW_R/0006, SPACESHIP/0001. System: hints/005 小モンスター (blocked).
  - It is a synonym of 化け物 (58 / 1 / 0) and 怪物 (21 / 0 / 0) and takes the same target (R §1.8). "creature" was the alternative. It is rejected because Miller already uses "creature" freely (p01 0040, p07 0354), so it is not a fixed term.
  - Every 小-variant is now listed in the row, so the duplicate census can pair them.
  - Binds `:30 0378` "Small monsters", `:36 0384` "one small monster", `:50 0398` "a sample of the small monsters".
  - Glossary: §6 row added; §9 row removed.
- **死骸** → `carcass` (7).
  - Census: 2 / 0 / 0, NO4_BAR/0387 and 0455 (p08, 化け物の死骸, where "the monster's carcass" is expected).
  - It is a creature's dead body, kept apart from 死体 "body" (R §6.1) and 遺体 "remains" (R §7.1). The alternative "corpse" is rejected because it reads as human.
  - Binds `:39 0387` "Will a carcass do?".
  - Glossary: §6 row added; §9 row removed. The 遺体 row's note pointer "死骸 is §9" now reads "死骸 'carcass'", and its Ruling column adds §8.1. This changes the pointer only, not the target.
- **鞄 · カバン · 旅行鞄** → `bag`; 旅行鞄 → `suitcase` (3; 8).
  - Census: 鞄 3 / 0 / 0 (NO4_BAR/0392, 0393 in 旅行鞄, 0394), カバン 1 / 0 / 0 (NO4_TOOL_ROOM/0003), 旅行鞄 1 / 0 / 0 (0393).
  - The plural follows the line: 0393 "plenty of passengers' suitcases".
  - Binds `:44 0392` "Stuff it in a bag?", `:45 0393`, `:46 0394` "Take a bag each".
  - Glossary: §3 row added; §9 row removed.
- **昆虫採集** → `bug collecting` (14).
  - Census: 1 / 0 / 0, NO4_BAR/0389 "No time for bug collecting.".
  - Binds `:41 0389`.
  - Glossary: §6 row added; §9 row removed. The 昆虫 row's note pointer "(§9, …)" now reads "is its own row", and its Ruling column adds §8.1. This changes the pointer only.
- **節足動物門鋏角亜門** → `phylum Arthropoda, subphylum Chelicerata` (40).
  - Census: 1 / 0 / 0, NO4_BAR/0352 only. It is the standard zoological naming: lowercase ranks, capitalised taxa.
  - The wrap separates "phylum | Arthropoda". That is accepted, because it is not a courtesy title.
  - Binds `:4 0352`.
  - Glossary: §6 row added.
- The PR also listed 蜘蛛, 昆虫, 死体 and 見張り. These were promoted earlier (R §6.1, §7.1), and p07 conforms: 0352 "spiders aren't insects", 0378/0380 "bodies", 0400 "keep watch".

### 8.2 Speakers (PR Flag 5)
- NO4_BAR_T has no draft of this scene, so every speaker comes from content (F-009). The attributions are:
  - Miller: 0352, 0354, 0368–0369, 0371, 0384, 0386, 0388, 0390, 0393.
  - Oakland: 0353, 0355, 0357, 0359, 0361; probably also 0381 and 0407.
  - Wolg: 0356, 0358, 0360, 0362–0364, 0366–0367, 0372, 0374–0376, 0382, 0392, 0394–0396, 0398–0400; probably also 0370, 0404 and 0406.
  - Judy: 0373.
  - Heming: probably 0403.
- These are uncertain, and every one is rendered speaker-neutral, so a corrected attribution changes no text: 0365, 0378–0380, 0383, 0385, 0387, 0389, 0391, 0402, 0405, 0408, 0409.
- The second victim (0402 二人目の犠牲者…俺たちの…仲間だ) is unnamed. Miller is probably the victim: she is absent from 0410–0437, and at 0429 the speaker expects to be left alone with Judy. 0402 "One of our… own" is gender-neutral, so nothing shipped depends on it (F-018).
- The pronoun for the monster is he/him/his, consistent with R §7.3:
  - 0353 "how to handle him", 0355 "his weakness", 0408 ヤツ → "him".
  - 0354 "the creature" supplies an object the source does not state.
  - 0371 "see it‼" is Miller's, as in her p01 0040 "Might it be spider-shaped?". p06 gives her no pronoun for the monster. Accepted.
- Glossary: none.

### 8.3 Movable codes, wraps and readings (PR Flags 2–4, 6–9)
- **Authored codes.** The authored `{br}`/`{p}`/`{w}` diff against the source matches the flags exactly:
  - 0352 `{br} {br}` → `{br} {p}`: a click before "Taxonomy puts them…", giving pages of 2 + 3 rows.
  - 0363 (the only `+` row) `{p}` → `{p} {p}`: a leading `{p}` after 0362's `{br}`, per R §2.4. The pages are 3 + the cursor row, then 3 rows. F-012: no glue.
  - There is no `{w}` in the unit.
- **Lines ended by an authored `{br}`** measure 27 at most: 0365, 0367, 0374, 0389, 0399 (29 lines, `len()`).
- **F-011 scan.** The reviewer scanned the 148 wrapped lines of the unit in `build/script_merged.tsv`. It found no lone "a", "I" or "an" at a line end and no split courtesy title. The only one-word line is 0386 "Yes.", which is the source's authored ええ。{br}.
- **Round-1 wraps** (R §1.12):
  - 0378 "Small monsters are all over the place." (27 / 10) for そこらじゅうにいる.
  - 0383 "Now we'll have to figure out how to escape on our own…" (28 / 25) for 考えないと.
- **Step-6 restructure, flagged and accepted.** 0367 and 0374 use colon lists ("This deck: Heming, William." / "Below it: John, Miller."; "Bottom deck: I'll go alone.") to keep the authored lines within 27.
- **Readings:**
  - 0366 甲板より上、つまりここから下のデッキ → "above the deck, that is, the decks below us": the capsized ship (R §2.1).
  - 0358 社長のあんたは → "Boss, …" (the §2 row in address).
  - 0396 チビ → "the runts", in context.
  - 0395 小さいヤツ → "the small ones", the parasites (a type, R §1.7).
  - 0384 １匹 → "one" (R §1.5).
- **Suspected source typos**, read as the sense requires:
  - 0396 捕まられなくても → 捕まえられなくても, "No problem if you can't catch one." (F-016).
  - 0407 追求 → 追及, "I'll call you to account" (F-017).
- Glossary: none.

### 8.4 Recurrences (PR Flag 10)
- 0377, 0397 and 0401 are the save prompt (R §3.4). They are byte-identical to 0170, 0173, 0239, 0242 and 0341. CHECK pairs them.
- Untranslated exact recurrence: 0373 …かまわないわ。 → "…I don't mind." ↔ NO3_NO4/0009. CHECK pairs it when that row is translated.
- Tag variants: 0391 `……。` → `……` ↔ NO2_THIRDSTORAGE/0006 and NO4_MACHINER90/0034. CHECK pairs these too.
- Not duplicates: ……？ and ……⁉ (NO4_HWR_FRONT/0034, NO4_MACHINER90/0093, SCN038B/04, /12) match 0391 only after punctuation is normalised.
- Glossary: none.

### 8.5 Accepted readings (non-blocking review notes, round 0)
- `:19 0367` "This deck: Heming, William." could be read as one name in surname-first order. The parallel "Below it: John, Miller." disambiguates it.
- `:12 0360` "enough to go on to talk big" is slightly clumsy. "Right now I just lack the material to talk big." was offered and not required.
- `:6 0354` "the creature" could be "him" (the he/him used at 0353 and 0355). This was not required.
- None of these is a fidelity error.

## Unit scene SCN038 (PR #7, MERGED, 2026-10-25)

The second scene unit covers five groups:
- SCN038A, SCN038B, SCN038D: the monster in the corridor, and William's sacrifice and death.
- SCN038_5C1, SCN038_5C2: the killer's first encounter with Judy.

Reviewed twice:
- **Round 0** (f6853ac): CHANGES.
  - `:22 SCN038B/10` had 12 "a" for the source's 11 お.
  - The PR body's figures were taken before p05 merged.
- **Round 1** (103d60b, with `origin/main` 38fe648 merged in): MERGE, squash 8ffabc0.
  - `git diff f6853ac 103d60b -- tl/` changes exactly one row, line 22.
  - The reviewer re-ran every gate on 103d60b merged with `origin/main` 3b33b87 (p06 and p07 in).

Figures:
- **Subtitles**: 59, every one 1 page, at most 3 lines (UNITCHECK, 0 violations).
- **Ratio**: 1,344 target characters ÷ 655 source = 2.05 (tags excluded).
- **Containers**: no byte container (scene). Script containers are unchanged: NO4_BAR.SCR 36,357 free.
- **Duplicates**: CHECK compared 34 duplicate pairs (main's 33, plus SCN038_5C1/10 in the `………。` group) and 2 tag-variant pairs.
  - The reviewer's source-side census made 369,196 comparisons: 59 rows × every other script, scene and system dump row.
  - It ran at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped, with ！？ → ⁉ and final punctuation normalised.
  - It found 35 hits. Two are translated true duplicates, both byte-identical. There are 0 divergences. See §9.4.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/scene/SCN038.tsv` (line = row index + 3).

### 9.1 Terms promoted or added
- **The killer's laugh: クッ · ククッ · クカカカカカカッ** → `Heh` · `Heh-heh` · `Kahahahahaha` (3 · 7 · 12). Run together it is `Heh, heh-heh, kahahahahaha.` (27). Punctuation follows the source.
  - Census: rows with クッ 6 / 7 / 0; ククッ 6 / 6 / 0; クカカカカカカッ 4 / 5 / 0.
  - Every クカ…ッ in the dumps has exactly 6 カ. "Kahahahahaha" gives one syllable per カ (Ka + ha × 5).
  - Rows: NO2_MAINSTORAGE/0001, 0002, 0004, 0005, 0008, 0012; SCN038_5C1/02–04, SCN038_5C2/02, SCN046B1/02, 04, 06, SCN046B2/08.
  - SCN046B2/08 クッ、ククッ、クカカカカカカッ。 should read exactly `Heh, heh-heh, kahahahahaha.`, like `:62` line 2.
  - It is distinct from くっ (`Ngh`, R §4.1). It is also distinct from Wolg's scoff フッ (`Heh`, R §7.1): the two words coincide in English, the speakers do not.
  - Binds `:52`, `:53`, `:54`, `:62`.
  - Glossary: §6 row added.
- **うおおおっ (battle cry)** → "R" for う, one "a" per お, "h" for っ.
  - Census: 0 / 1 / 0 (おおおっ 0 / 2 / 0: the other row is SCN038A/02 くそおおおっ‼, the くそ row's elongation).
  - SCN038B/10 う + お × 11 + っ‼ → `Raaaaaaaaaaah‼` (14; `.count('a')` = 11). This follows the きゃあ…っ pattern of R §4.1.
  - Binds `:22`.
  - Glossary: §6 row added.
- **～ (long-vowel mark)** → repeat the vowel once per ～; a final っ after a word is dropped (as in `Daaaamn‼`, `:5`).
  - Census: 0 / 2 / 0. SCN038B/11 いまだ！{br}行け～～～っ。 → `Now!{br}Goooo.` (Go + 3 o). SCN046A3/01 ヘイミン～～～～～～～グ‼ is in context: the stretch falls inside the name.
  - Binds `:23`.
  - Glossary: §6 row added.
- **グフッ** → `Guh` (3).
  - Census: 0 / 1 / 0. SCN038B/17 早く行けって――グフッ‼ → `Hurry up and go——Guh‼` is William struck mid-sentence. It is not フッ.
  - Binds `:29`.
  - Glossary: §6 row added.
- **«Name»たち** → "«Name» and the others".
  - Census of katakana name + たち: ウォルグたち 0 / 1 / 0 (SCN038B/07); ヘイミングたち 1 / 1 / 0 (NO4_BAR/0232, SCN038A/07); ジョンたち 2 / 0 / 0 (NO3_CHAPEL/0050, NO4_BAR/0444, untranslated). コリスンさんたち 3 / 0 / 0 keeps its own §1 row (R §1.2).
  - Binds `:10 SCN038A/07` "Heming and the others are in the line of fire." and `:19 SCN038B/07` "…run toward Wolg and the others."
  - NO4_BAR/0232 "Heming's team" (p04, `tl/script/NO4_BAR.p04.tsv:58`) stands in its context: Wolg is assigning teams. No shipped line changes.
  - Glossary: new §1 row.
  - The §1 ヘイミング row's たち target was "in context". It now reads "Heming and the others", with 0232's "Heming's team" in context, and its note's "SCN038A/07 open" is closed. The open question is answered here, and no shipped target changes.
- **俺様** → no fixed word: the killer's swagger is carried by register. Promoted from §9 as proposed.
  - Census: 3 / 4 / 0. Rows: NO2_MAINSTORAGE/0002–0004, SCN038_5C1/06, SCN046B1/11, SCN046B2/03, 04.
  - SCN038_5C1/06 俺様の……。 → `My very own……` (13). 。 is absorbed after `……` (R §1.3).
  - NO2_MAINSTORAGE/0003 その俺様の女神 should echo it as "my very own goddess".
  - The killer's voice in this unit is mock courtesy: "No, no, my apologies.", "have the pleasure of meeting you". Later killer units (NO2_MAINSTORAGE, SCN046B1/B2) should keep it.
  - Binds `:56`.
  - Glossary: §6 row added; §9 row removed.

### 9.2 Speakers (PR Flag 4)
- Every speaker is named from content (F-009): scene subtitles carry no speaker code at all.
  - A: 01–04 are the lead pair (Wolg / Oakland); 05 and 08 Oakland (or William); 06, 07 and 09 Wolg.
  - B: 03, 05, 07, 09–11, 14, 16–18 and 20 are William; 02, 12, 15 and 19 Judy; 06, 08 and 21 probably Heming; 01 William or Heming; 04 and 13 Judy or Heming.
  - D: 01, 11, 13, 15 and 17 are William; 03, 06, 10, 14 and 16 Judy; 02, 04, 05 and 07–09 Wolg or Oakland; 12 Wolg, Oakland or Heming.
  - 5C1/01, 07 and 10 are Judy. The rest of 5C1, and 5C2, is the killer.
- Geography: Wolg and the man urging him to shoot are on one side of the monster. Heming, William, Judy and John are on the other (A/07, B/07).
- Every line is speaker-neutral in English, so a corrected attribution changes no text.
- William's 帰れる…妹のところへ (`:48`, `:50`) → "I can go back… / To my sister…" points to his dead sister (NO4_HWR_FRONT/0075–0082).
- Glossary: none.

### 9.3 Movable codes and readings (PR Flags 2, 3, 5)
- **Authored codes.** Diffing the authored `{br}`/`{p}`/`{w}` sequence against the source over 59 rows gives one difference: `:48 SCN038D/15` gains `{br}` ("It's fine, now…{br}I can go back…", 15 + 14). Without it the wrap leaves a one-word last row, `back…`.
- Lines ended by an authored `{br}` are all ≤ 27 (`len()`): `:23` 4, `:40` 26, `:48` 15, `:51` 17, `:58` 21, `:61` 14, `:62` 10.
- **F-011 scan** over every wrapped line: 0 lone "a"/"I", 0 split titles, 0 word-initial apostrophes. The one one-word row, `:23` "Goooo.", follows the source's own `{br}`.
- **Step-6 reorder, flagged.** `:59 SCN038_5C1/09` moves のでね ("You see,") to the front. In final position the wrap left "…meeting you in a | place…".
- **Readings, accepted:**
  - `:33` さあ、行くんだ → "Come on, go." さあ stays a context word: "All right," where it opens a "let's" (R §4.1); "Come on," to a reluctant listener.
  - `:28–32` the 早く行け near-repeats are kept consistent ("Hurry up and go", "Go, I'm telling you‼").
  - `:41` 命 → "yours".
  - `:61` もう一匹 → "another one" (R §1.5) and ただの…… → "just a……".
  - `:39` and `:43` place the ellipsis by English word order, with the count kept.
  - `:5` くそおおおっ‼ → `Daaaamn‼` (the §6 くそ row, 1 + 3 a).
  - `:14` "At this rate…… we all die." keeps one row; "we'll all die" would orphan "die.".
- Stutters are hyphenated per R §4.3 (`:44` "H-hurry up‼", `:46` "N-not yet‼").
- Glossary: none.

### 9.4 Recurrences (PR Flag 7)
- **Translated, identical**: `:60 SCN038_5C1/10` `………。` → `………` = NO4_BAR/0201 (p04) and NO4_BAR/0265 (p05). CHECK pairs them.
- **Untranslated exact repeats**, for the next translators:
  - D/12 すまん…。 = SCN046A1/11 → `Sorry…`.
  - D/14 ウィリアムっ‼ = NO4_HWR_FRONT/0023 → `William‼`.
  - B/04 ……？ = NO4_HWR_FRONT/0034 (exact) and NO4_MACHINER90/0093 (tag-variant) → `……?`.
  - 5C1/10 `………。` = the R §5.6 list. The labelled `_T` `【Name】………` rows are covered by R §6.4.
- **Not duplicates**: B/04 ……？ and B/12 ……⁉ match NO4_BAR/0391 ……。 only once final punctuation is normalised (R §8.4).
- **Echo**: SCN046B1/04 俺もまさか、こんな場所でお前に会えるとは思ってなかったぜ echoes `:59`, and can reuse its wording.
- Glossary: none.

## Unit script NO4_HWR_FRONT.p01 (PR #13, MERGED, 2026-10-25)

The starboard front corridor, from John and his partner's patrol to Collison's death and William's return. The partner is skeptical of the monster. Collison explains the toilet arrangement and goes off. After his death, William accuses the salvagers of making the monster. A monster attack follows (`Retry?`, Yes/No), and then William agrees to come back. Reviewed once:
- **Round 0** (fce14fa): MERGE, squash 28d44a9. Every gate passed, and there were no findings.

Figures:
- **Container.** With p01 merged: NO4_HWR_FRONT.SCR 10,524 / 65,535 bytes, 55,011 free; tokens 377 / 1,499 (MEASURE). p01 costs +1,174 bytes over the untranslated 56,185 free. NO4_HWR_FRONT.p02 (PR #10) lands in the same container.
- **Pages.** At most 4 rows per page (UNITCHECK, 53 rows, 0 violations).
- **Ratio.** 2,321 target characters ÷ 1,088 source characters = 2.13, re-measured with `codec.char_count`.
- **Duplicates.** CHECK compared 38 duplicate pairs (main's 34 + s11/s17, s12/s18, 0023, 0034) and 2 tag-variant pairs.
  - The reviewer's census made 110,558 source-side comparisons: 53 rows × every other script, scene and system dump row, with the sibling heads #10, #11 and #12 counted as translated.
  - It ran at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped, with ！？ → ⁉ and final punctuation normalised.
  - It found 59 hits, 15 of them translated pairs, with 0 divergences. The two "different" hits differ in final punctuation only (§10.4).

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_HWR_FRONT.p01.tsv` (line = row number + 3; choices s11 s12 s17 s18 are lines 53–56).

### 10.1 Terms promoted from §9
- **マガジン** → `magazine` (8); 予備のマガジン / マガジンの予備 → "spare magazine(s)".
  - Census: 2 / 0 / 0, NO4_HWR_FRONT/0020 and NO3_NO4/0010 (一応マガジンの予備を渡しておく, which should take "spare magazine").
  - "clip" was the alternative. It is rejected: a handgun takes a magazine.
  - Binds `:23 0020` "I'll share my spare magazines with you.".
  - Glossary: §3 row added; §9 row removed.
- **Ｒｅｔｒｙ？** → `Retry?` (6).
  - Census: 2 / 0 / 0, NO4_HWR_FRONT/0036 and NO2_MAINSTORAGE/0007, both the game-over prompt.
  - It is the source's own English. Typed ASCII, `encode_target('Retry?')` equals `encode_source('Ｒｅｔｒｙ？')` byte for byte (`827182858294829282998148`, checked by the reviewer).
  - Binds `:39 0036`.
  - Glossary: §4 row added; §9 row removed.
- **はい · いいえ (choice)** → `Yes` · `No` (3 · 2), cap 27.
  - Census: as exact `choice` rows, 8 / 0 / 0 each: NO2_HW_3 s05/s06, NO2_MAINSTORAGE s03/s04, NO2_TOFE_ROOM s08/s09, NO3_CABIN_3002 s03/s04, NO3_CABIN_3003 s03/s04, NO3_MACHINE s03/s04, NO4_HWR_FRONT s11/s12, s17/s18.
  - The row's scope is `choice` rows. はい inside dialogue is translated in context.
  - Binds `:53`–`:56`.
  - Glossary: §4 row added; §9 row removed.
- **妹 · 妹さん** → `sister`: "my sister" / "his sister"; the echo 妹？ → "Sister?" (6).
  - Census: 妹 5 / 1 / 0, of which 妹さん is 2 / 0 / 0. The rows are NO4_HWR_FRONT/0031, 0032, 0075 (妹さん), 0080 (妹さん), 0082, and SCN038D/17.
  - Every row means William's dead sister.
  - さん is dropped, as for a role noun (R §1.2), and carried by tone.
  - Already consistent:
    - "little sister" was not used; the shipped SCN038D/17 says "To my sister…" (R §9.2).
    - Sibling PR #10 renders 0075 "His sister…", 0080 "his sister's death" and 0082 "his sister's death". That conforms; the row binds both units.
  - Binds `:34 0031` "Give my sister back!" and `:35 0032` "Sister?{br}What are you talking about?".
  - Glossary: §6 row added; §9 row removed.

### 10.2 Speakers (PR Flag 4; points decided in review)
- There is no `_T` draft of this scene, so speakers are named from content (F-009).
  - Collison: 0011–0013 (わし/おる/じゃ).
  - William: 0025, 0027, 0029, 0031, 0033, 0035, 0038–0039, 0042, 0044, 0046, 0048.
  - John's partner: every other message row.
  - 0023 ウィリアムっ‼ is the partner's, or John's.
  - 0036 is the game-over prompt.
- **John's partner is not Oakland.**
  - Oakland's 42 `【オークランド】` rows in the dump contain わし 5 times and 俺 0 times (NO4_BAR_T/0075, 0158, 0160, 0165; NO4_HWR_FRONT_DOWN_T/0002). His unlabelled わし lines agree (NO3_NO4/0002, NO4_BAR/0429).
  - The partner says 俺 throughout (0002, 0003, 0006, 0007, 0008, 0020).
  - He is Heming or Wolg:
    - For Heming: 0004 (人間、歳をとると頭が固くなる, self-deprecating about age), うむ (0007) and わっはっは (0008) fit the older salvager.
    - For Wolg: 俺 (NO4_BAR_T/0050, 0055), and his "the culprit is human" report (NO4_BAR/0246).
  - Heming has no labelled line with a first-person pronoun, so the evidence cannot settle it.
  - Every line is speaker-neutral, so a corrected attribution changes no text. Recorded in F-009.
- **0018 まだ中にいるかもしれん → "He may still be in there."** The supplied subject is the monster's "he" (R §1.7, §7.3), for three reasons:
  - 気をつけろよ makes the subject a danger.
  - 0016 has just accepted John's report that there really was a monster, and 0015 that Collison was its victim.
  - 0026 states that Collison is dead.
  Reading "he" as Collison is not supported. "The monster may still be in there." wraps to a one-word row (R §1.12 rule 1). Accepted.
- spk=0, 1 and 2 each carry the partner, as well as William (spk=1) and Collison (spk=2). spk=N is not a character id.
- Glossary: none.

### 10.3 Movable codes, wraps and readings (PR Flags 2, 3, 6, 7)
- **Authored codes.** The authored `{br}`/`{p}`/`{w}` sequence differs from the source in one row: `:22 0019` `{br} {br}` → `{p} {br}`.
  - Without the click, the page opened by 0019 and its `+` row 0020 has 5 rows. With it, the pages have 1 and 4 rows.
  - The click falls at a sentence boundary. The source's page there is 3 rows, so this is not inherited (F-010 n/a).
  - There is no `{w}`.
  - F-012: the `+` rows 0020, 0039 and 0041 each follow a `{br}`-ended row, so nothing is glued. None of the 25 dump boundaries is in this unit.
- **Glyph counts.** `…` `‼` `⁉` `──` counts match the source on every row.
- **Wraps** (F-011 scan of `build/script_merged.tsv`, 115 wrapped lines):
  - 0 lines end in a lone "a", "I" or "an".
  - 0 split titles: "Mr. Collison" stays on one line at 0001, 0002, 0027 and 0044.
  - 0 word-initial apostrophes.
  - The one-word rows 0027 `…What⁉` and 0032 `Sister?` are the source's own authored breaks.
  - Lines ended by an authored `{br}` are 27 or fewer (`len()`): 0006 line 1 and 0040 are 27.
- **0035 お、お前らが作ったんだろ…？ → "Y-you made that thing, didn't you…?"**
  - The supplied object is the monster, for three reasons:
    - The topic is 0028–0029: the monster killed Collison, and William replies "You guys killed him!".
    - 俺たちを選んだ "why did you choose us" makes the salvagers the monster's masters.
    - 0038–0039 何故、怪物がお前たちも狙うんだ / けしかけた and 0046 あいつ continue the same belief.
  - NO4_BAR/0255 (p05) お前らが作ったんだろ⁉ → "You did it yourselves, didn't you⁉" stays as shipped (R §6.3):
    - Its context is the shot body and "whoever destroyed our gear".
    - Its source differs (⁉ for …？, a different following line), and the two rows do not pair.
  - This unit does show that William's belief is "you made the monster". A later pass that wants p05 to match could use "You made it, didn't you⁉". That would be optional, not a fidelity fix.
- **Step-5/6 departures, flagged and accepted:**
  - `:10 0007` reorder: "given the tech to submerge a passenger ship" carries といい.
  - `:11 0008` 組織 implied: "What kind, I couldn't say.".
  - `:42 0039` "set him on us": the object is supplied.
  - `:44 0041` "We nearly got killed‼": the elided subject is read as the patrol attacked together.
  - `:49 0046` あいつ → "that thing".
- **Readings:**
  - 0002 どうも → "can't quite".
  - 0004 頭が固くなる → "hard-headed".
  - 0006 ハハッ → "Ha-ha,"; 0008 わっはっは → "ha-ha-ha.".
  - 0011 ４１０１号室 → "room 4101" (R §1.4); 便所 → "The toilet's" (§2 row).
  - 0012 あいつ (the monster) → "He".
  - 0013 済ませてくる → "I'll go and attend to it", Collison's diction.
  - 0026 それはそっちのセリフだ → "I should be asking you that.".
  - 0030 わからんヤツだな → "You just don't get it." (ヤツ as a person, R §1.7).
  - Stutters hyphenated (R §4.3).
- **Non-blocking:** 0005 なんだろうな。 → "…, I wonder?" puts a question mark on a sentence that ends in 。 in the source. That is acceptable English, and `?` is not a counted glyph.
- Glossary: none.

### 10.4 Recurrences (PR Flag 5)
- **Translated, identical:**
  - 0023 `William‼` = SCN038D/14.
  - 0034 `……?` = SCN038B/04.
  - s11 = s17 `Yes`, s12 = s18 `No`.
  - 0033 `………` = NO4_BAR/0201, 0265, SCN038_5C1/10, and the sibling heads p02 0057 and 0092, p08 0430 and SCN046B1/01.
  - 0009 is 0006's second sentence, byte for byte.
- **Untranslated exact recurrences, which CHECK pairs once translated:**
  - **0013 = NO4_HWR_FRONT/0144** (p03, wave 4): `Thank you. I'll go and attend to it.{br}Wait here a moment for me.`. The wave-4 translator copies it byte for byte. 0144 is spk=1 in a different scene, but the sentence is identical, so the target is too.
  - 0036 = NO2_MAINSTORAGE/0007 `Retry?`.
  - 0048 = NO3_NO4/0003 `…All right.`.
  - s11/s17 and s12/s18 = the six NO2/NO3 Yes/No pairs (§10.1).
- **Not duplicates:** 0034 `……?` against NO4_BAR/0391 `……` and SCN038B/12 `……⁉` (R §8.4).
- The #12 review's `…、` ruling does not apply: the unit has no `…、` (0 rows).
- Glossary: none.

## Unit script NO4_BAR.p08 (PR #12, MERGED, 2026-10-25)

The end of the bar scenes. Three days without food; Wolg's plan to break the barricade on the stairs to the food storeroom (Deck 3, one deck up in the capsized ship); the search teams; Judy volunteers; the chain cutter is brought back; the move to a room near the storeroom; Oakland's bag with the monster's carcass. NO4_BAR.SCR is now fully translated (485/485). Reviewed twice:
- **Round 0** (23bdaac): CHANGES.
  - 0441: 帰ってこなくていい was rendered as a prohibition, an unflagged departure from a literal that fits.
  - 0424: `…、` was followed by a capital (§11.3).
- **Round 1** (280748e): MERGE, squash c39677d. Exactly those two rows changed (`git diff 23bdaac 280748e -- tl/`), each to the reviewer's wording.

Figures:
- **Container.** With p01–p08 merged and NO4_HWR_FRONT.p01: NO4_BAR.SCR 28,157 / 65,535 bytes, 37,378 free; tokens 419 / 1,499 (MEASURE). Against p07's 36,357 free, p08 *frees* 1,021 bytes, because the script dictionary rebuilds over the English text (tokens 621 → 419).
- **Pages.** At most 4 rows per page (UNITCHECK, 52 rows, 0 violations).
- **Ratio.** 2,529 target characters ÷ 1,125 source characters = 2.25 (round 0, from the PR; round 1 changes are ± 5 characters).
- **Duplicates.** CHECK compared 44 duplicate pairs (main's 38 + 0430, 0432, 0440, 0443, 0460, 0461) and 2 tag-variant pairs.
  - The reviewer's census made 108,472 source-side comparisons: 52 rows × 2,086 other script, scene and system dump rows.
  - It ran at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped with ！？ → ⁉ and final punctuation normalised.
  - It found 92 hits, 48 of them translated pairs, with 0 mismatches. The hits are in §11.5.
- **F-011 wrap scan**, run by the reviewer on `build/script_merged.tsv` (110 lines): no lone "a", "I" or "an" and no split title. Four lines end in "the" (0426, 0428, 0447, 0448; allowed, R §1.12 rule 2). The one-word rows are whole messages (0430 `………`, 0435 "What?") or the source's authored なんだと⁉{br} (0447 "What⁉"). Authored-`{br}` lines measure 27 at most.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_BAR.p08.tsv` (line = row number − 406).

### 11.1 Terms promoted from §9, and three added
- **操舵室** → `the wheelhouse`; 操舵室のデッキ → `the wheelhouse deck` (14; 19).
  - Census: 2 / 0 / 0, NO4_BAR/0428, 0437. ブリッジ is "the bridge" (rooms/108), so the two stay apart. "the helm" was the alternative; rejected, since a helm is the wheel itself, not a room.
  - Binds `:22 0428` "Heming and John take the wheelhouse deck.", `:31 0437`.
  - Glossary: §2 row added; §9 row removed.
- **倉庫** (variant 第Nデッキ倉庫) → `storeroom` (9).
  - Census: 1 / 0 / 4. Script: NO4_BAR/0424. System: rooms/053, 069, 105, items/013 (blocked).
  - Kept apart from 食料庫 "the food storeroom" (R §2.1) by the modifier only; one noun for both reads naturally.
  - The room-name form "Deck 3 Storeroom" is 16 characters, over the 14-character cap: F-020 (PR Flag 9).
  - Binds `:18 0424` "they're all in the storeroom".
  - Glossary: §2 row added, cap 14 and the F-020 pointer in the row; §9 row removed.
- **バリケード** → `barricade`; the verb where the line wants it (9).
  - Census: 5 / 0 / 0, NO4_BAR/0421, 0422, 0444, NO4_HWL_KAIDAN/0005, 0006.
  - 0421 バリケードを作っている → "barricaded the stairs" (step-6 restructure, flagged, keeps the page at 4 rows). 撤去 → "clear" (0444); NO4_HWL_KAIDAN/0006 バリケードを撤去する takes the same verb.
  - Binds `:15 0421`, `:16 0422` "that barricade", `:38 0444` "the barricade".
  - Glossary: §3 row added; §9 row removed.
- **チェーンカッター** → `chain cutter` (12).
  - Census: 2 / 0 / 1, NO4_BAR/0444, NO6_TOOLROOM/0001, hints/006 (blocked, cap 39). "bolt cutters" rejected: the source names a chain cutter, one tool.
  - Binds `:38 0444`.
  - Glossary: §3 row added; §9 row removed.
- **工具** → `tools` (5).
  - Census: 2 / 0 / 0, NO4_BAR/0423, 0424. 道具 (2 / 1 / 1: NO4_BAR/0441, NO4_HWL_KAIDAN/0006, SCN047C1/05, items/009) is not fixed; 0441 "a tool" in context.
  - Binds `:17 0423`, `:18 0424`.
  - Glossary: §3 row added; §9 row removed.
- **刃物** (variant 鋭利な刃物) → `blade`; `a sharp blade` (5; 13). New.
  - Census: 3 / 0 / 0, NO4_BAR/0439, NO4_4102/0001 and NO6_BRIDGE/0020 (both 鋭利な刃物, wound descriptions).
  - Binds `:33 0439` "bring back every blade you find".
  - Glossary: §3 row added.
- **親玉** → `the big one` (11). New.
  - Census: 1 / 0 / 0, NO4_BAR/0438. The parent monster against 小さいの "small ones". Never "boss", which is 社長 (R §3.1).
  - Binds `:32 0438`.
  - Glossary: §6 row added.
- **巣** (variant 化け物の巣) → `nest`; `the monster's nest` (4; 18). New.
  - Census: 4 / 0 / 0, NO4_BAR/0368 (shipped "a monster's nest", Miller's generic), 0447, 0448, NO5_BANK/0006 (蜘蛛の巣 "web" and 化け物の巣 in one row; the second takes this row).
  - The article follows the line: generic "a" (0368), the known monster "the" (0447, 0448).
  - Binds `:41 0447`, `:42 0448`.
  - Glossary: §6 row added.
- **バッグ** 0454 → "bag", conforming to the 鞄 row (R §8.1). PR #11 proposes バッグ as a Variant of that row (its SCN046A1/01 "The bag‼"); that review decides the row, and this line needs no change either way.

### 11.2 Speakers (PR Flag 3)
- No `_T` draft of this scene exists, so speakers come from content (F-009).
  - Wolg (the PR's attribution): 0413, 0415, 0417, 0420, 0422–0423, 0425–0426, 0428, 0430, 0432, 0435, 0437–0439, 0444–0446, 0448, 0450, 0452, 0454, 0456, 0458; he calls Oakland "boss" at 0454 (社長 row).
  - Oakland: 0414 and 0429 (わし to his crew, R §1.10), 0431, 0447, 0449, 0451, 0453, 0455, 0457.
  - William: 0419, 0421, 0424, 0427 (0418 addresses him; he knows the ship). Judy: 0434, 0436.
- Uncertain, each rendered speaker-neutral so a corrected attribution changes no text: 0410–0411 (Wolg or Heming), 0412 (probably William), 0416 and 0418 (Oakland or Heming), 0433 (probably Wolg), 0441–0442 (Oakland or Wolg). 0430 and 0432 could equally be Heming, whom 0429 names; both are neutral. Accepted.
- F-009 confirmed again: spk=4 carries William, Oakland, Judy and Wolg here.
- F-018: no line names the second victim; Miller has no line in 0410–0461. Nothing shipped changes.
- Glossary: none.

### 11.3 `…、` → `…`, lowercase continuation (round-0 finding 2; PR Flag 6)
- Source: `…、` mid-sentence, 4 / 2 / 0: NO4_BAR/0424, NO4_BAR_T/0130, NO2_MAINSTORAGE/0027, NO2_TOFE_ROOM/0003 (`……、`), SCN046A2/01, SCN047B3/01.
- Target: the ellipsis alone, with the same glyph count; the 、 is absorbed, as 。 is after `…` (R §1.3). Because 、 continues the sentence, the next word is lowercase (a proper noun or "I" keeps its capital).
- Reasoning: shipped mid-sentence `…` continues lowercase (NO4_BAR/0299 "Heh… if any exist", 0350 "A spider… an insect?", SCN038_5C2/01 "Oho…… don't tell me"), while `…。` starts a new sentence (0281, 0339, 0402, 0408). `…,` is not used in English.
- Binds `:18 0424` "Tools… if any, they're all in the storeroom." PR #11 SCN046A2/01 "Bill… it's game over." already conforms.
- Glossary: none. This is a punctuation convention.

### 11.4 Movable codes and readings (PR Flags 2, 5–8; round-0 finding 1)
- **Authored codes.** The authored `{br}`/`{p}`/`{w}` diff against the source matches Flag 2 exactly: leading `{p}` on the `+` rows 0411 (`-` → `{p}`), 0426 (`-` → `{p}`) and 0445 (`{p}` → `{p} {p}`), each after a `{br}`-ended row and at a sentence boundary (R §2.4). Without them the pages run to 5, 5 and 7 rows. Every other `{br}` follows the same sentence as in the source. F-012: all four `+` rows follow a `{br}`, so nothing glues. No `{w}` in the unit.
- **0441** 帰ってこなくていい → "No need to come back here until you've found a tool." The round-0 "Don't come back here…" turned permission into prohibition; the literal is correct English with the same wraps (25 / 26), so literal-first (translation_prompt.md §2) applies.
- **Step-5/6 departures, flagged and accepted:** 0455 化け物の死骸が入っている → "It's the monster's carcass." (the contents implied by 0454's question; holds the authored line at 27); 0421 noun → verb (§11.1); 0422 the topic phrase folded into "Trouble is, …"; 0424 あるとしたら → "If any"; 0418 "located" to avoid the one-word row "storeroom?".
- **Punctuation:** 。 → `?` on three rhetorical questions (0442, 0454, 0457), accepted.
- **Readings:** 0420 １つ上 → "one deck up" (capsized ship, R §2.1); 0421 下の連中 → "the lower-deck guys" (the lower-deck survivors; 下の連中 not fixed, R §3.2); 0441 期待しているぞ → "I'll be expecting results." (頼んだぞ is "I'm counting on you.", R §6.4); 0449 しかしだなっ → "But see here."; 0450 この部屋 → "here" (keeps the page at 4 rows).
- **Suspected source typo:** 0412 じない → じゃない, read as the sense requires (F-019).
- Glossary: none.

### 11.5 Recurrences (PR Flag 10)
- 0440, 0443, 0460, 0461: the save prompt (R §3.4), byte-identical to 0170, 0173, 0239, 0242, 0341, 0377, 0397, 0401. Untranslated: NO3_CHAPEL/0039, 0049, 0070, 0079, 0111, 0114, 0129, 0130, NO4_MACHINE/0001.
- 0430 `………。` → `………` = 0201, 0265, SCN038_5C1/10. Untranslated exact: NO3_NO4/0007, 0061, NO4_HWR_FRONT/0057, 0092, SCN046B1/01; tag variants NO4_MACHINER90/0108, NO4_TOOL_ROOM/0025, 0060.
- 0432 いいや。 → "Not at all." = 0263 (R §6.4).
- 0447 opens with なんだと⁉ → "What⁉", as 0245; not a duplicate row (0447 continues).
- In context, not duplicates: NO4_HWL_KAIDAN/0005–0006 バリケード, NO6_TOOLROOM/0001 チェーンカッター.
- Glossary: none.
