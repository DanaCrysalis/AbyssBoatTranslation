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

## Unit script NO4_HWR_FRONT.p02 (PR #10, MERGED, 2026-10-25)

The starboard front corridor after Miller's death. Judy comforts John. A man tells Judy that John blames himself and will draw his gun next time ("the sanctity of life"). The surface crew is still searching for the ship on sonar. Judy tells John about William's sister. Wolg gives the marching order, and the starboard search begins at the deck sign. Reviewed once:
- **Round 0** (968ac4c, merged with main 964d3c5 for review): MERGE, squash c755736. Every gate passed, and there were no must-change findings.

Figures:
- **Container.** With p01 and p02 merged: NO4_HWR_FRONT.SCR 11,013 / 65,535 bytes, 54,522 free; tokens 291 / 1,499 (MEASURE).
  - p02 costs 489 bytes over p01's 55,011 free.
  - The PR measured 1,004 bytes without p01. The dictionary rebuilds over both parts.
  - 104 / 150 rows are translated; p03 (0101–0150) is wave 4.
- **Pages.** At most 4 rows per page (UNITCHECK, 51 rows, 0 violations). The whole store: 589 rows, 0 violations.
- **Ratio.** 2,281 target ÷ 1,018 source characters = 2.24 (`codec.char_count`).
- **Duplicates.** CHECK compared 46 duplicate pairs (main's 44 + 0057, 0092) and 2 tag-variant pairs.
  - The reviewer's census made 106,386 source-side comparisons: 51 rows × every other script, scene and system dump row.
  - It ran at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped, with ！？ → ⁉ and final punctuation normalised.
  - It found 51 hits, 12 of them translated pairs, with 0 divergences (§12.4).
- **F-011 wrap scan.** The reviewer's own scan of `build/script_merged.tsv` aligned the wrapped text token for token with the authored target, and examined 106 lines.
  - No lone "a", "I" or "an"; no split title; no wrap-made one-word row; no word-initial apostrophe.
  - Three lines end in "the" (0062, 0077, 0085), which is allowed (R §1.12 rule 2).
  - Lines ended by an authored `{br}` are 27 at most (`len()`).

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_HWR_FRONT.p02.tsv` (line = row number − 46).

### 12.1 Terms promoted from §9, the deck sign, and one stock phrase
- **右舷 · 左舷** → `starboard` · `port` (9 · 4), lowercase in dialogue.
  - Census: 右舷 1 / 0 / 9, 左舷 1 / 0 / 5. The one script row is NO4_HWR_FRONT/0096.
  - The system rows are the corridor room names 第Nデッキ右舷廊下 / 左舷廊下 (rooms/000, 020, 028, 043, 046, 060, 067, 070, 081, 087, 100, 101, 103 …).
  - "Deck 4 Starboard Corridor" is 25 characters. Even "Deck 4" + "Starboard" is 16, over the 14-character room cap, so the system translator needs an abbreviation (F-021).
  - Binds `:50 0096` "We search port once we've finished with starboard.".
  - Glossary: §2 row added; §9 row removed.
- **エントランスホール** → `entrance hall` (13).
  - It is lowercase in dialogue and narration (NO4_4102/0001, NO4_STORAGE/0002), and capitalised `Entrance Hall` on a sign (0100, NO4_HWL_BACK/0017, NO4_HWL_BACK2/0013, NO5_HW_R/0009) and as a room name (rooms/066, 084; 13 ≤ 14).
  - Census: 6 / 0 / 2. "lobby" was the alternative; it is rejected because the source names a hall.
  - Binds `:54 0100`.
  - Glossary: §2 row added; §9 row removed.
  - The §2 ホール row's pointer "(§9)" now reads "(§2)". This is a pointer change only: no target changes, and no shipped line is affected.
- **The deck sign** 『フロアーインフォメーション』 / パーサーオフィス／メインダイニング / ラウンジ／ビアー＆ラガーズ／キャビン / エントランスホール.
  - Source: NO4_HWR_FRONT/0097–0100 = NO4_HWL_BACK/0014–0017 = NO4_HWL_BACK2/0010–0013, byte-identical in the source column. NO4_HWR_FRONT/0097 = NO5_HW_R/0008, whose sign then lists different entries (0009–0011).
  - Census: フロアーインフォメーション 4 / 0 / 0; パーサー 3 / 0 / 1 (rooms/065); メインダイニング, ラウンジ 3 / 0 / 0 each; ビアー＆ラガーズ 4 / 0 / 0 (with NO4_HWR_FRONT/0102); キャビン 3 / 0 / 15 (room names, R §1.6).
  - Target, as shipped:
    ```
    "Floor Information"{br}
    Purser's Office/Main Dining{br}
    Lounge/Beer & Lagers/Cabins{br}
    Entrance Hall, it reads.{p}
    ```
    - Measured with `len()`, the rows are 19, 27, 27 and 24. The page is 4 rows.
  - Reasoning:
    - 『』 → `"…"` (PROJECT.md §5.1).
    - The entries are capitalised, as signage.
    - The source's ／ is unspaced, and so is the `/`. Spaced, the first entry row is 31 and wraps.
    - キャビン → "Cabins" keeps "cabin" for キャビン (R §1.6).
    - The leading full-width indent of rows 2–4 is dropped. `assemble.py` rejects a target where `tgt != tgt.strip()`, and Python's `strip()` removes U+3000, so the indent cannot be authored. This is a tool limit recorded in F-022, not a blind spot.
  - The three copies are bound byte for byte, and CHECK pairs them when NO4_HWL_BACK and NO4_HWL_BACK2 are translated.
  - "Purser's Office" (15) is over the rooms/065 cap of 14 (F-021). The sign keeps it, and the room name is decided with the system store.
  - Binds `:51 0097` – `:54 0100`.
  - Glossary: §2 rows added for フロアーインフォメーション, パーサーオフィス, メインダイニング, ラウンジ, ビアー＆ラガーズ and キャビン; §9 row removed.
- **と書かれている** → `it reads` (8).
  - Census: 7 / 0 / 0: NO4_HWL_BACK/0017, NO4_HWL_BACK2/0013, NO4_HWR_FRONT/0100, 0102, NO4_SHOP/0006, NO5_BANK/0005, NO5_HW_R/0011.
  - Pattern: `"«text»," it reads.` for a quoted 『』 text (0102 `"Beer & Lagers," it reads.`; NO4_SHOP/0006 and NO5_BANK/0005 `『本日の船内イベント案内』と書かれている`). After the last entry of a multi-row sign: `«last entry», it reads.` (0100).
  - NO5_HW_R/0011 has the phrase alone on its row after a sign, and is rendered in context.
  - Binds `:54 0100`.
  - Glossary: §6 row added.
- **妹 · 妹さん** (R §10.1): 0075 "His sister…", 0080 "his sister's death" and 0082 "his sister's death" conform to the row promoted by #13. No change.

### 12.2 Speakers (PR Flag 4; points decided in review)
- There is no `_T` draft of this scene, so speakers are named from content (F-009).
  - Judy: 0050–0054, 0057, 0061, 0063, 0075–0086 (the よ/わ endings), 0095.
  - Wolg: 0087–0089, 0091, 0093.
  - William: 0090 (かよ). 0092 is probably William.
  - Narration: 0097–0100.
- **0055–0056, 0058–0060, 0062**, the man who tells Judy about John:
  - He uses **no first-person pronoun**, so #13's 俺-against-わし test (R §10.2) cannot be applied.
  - His one marked form, 君 (0056), occurs in 1 script row, this one. It appears in 0 of Oakland's 42 labelled rows and 0 of Wolg's 29.
  - His knowledge of John's inner state fits Oakland, John's father, but the evidence cannot settle it: Oakland or Wolg.
- **0064–0074**: the surface crew. A sonar operator, a crewman, and a superior who orders the dives.
  - 見失ってからもう何日経ってる counts the days since they lost the ship, so this may be the present, not a flashback. The English tenses read either way.
- **0094 まっ、待つんだ、ウォルグ！**: William or Oakland. **0096**: Oakland or Wolg.
- Every uncertain line is speaker-neutral, so a corrected attribution changes no text. Recorded in F-009.
- **F-018.** 0082 ミラーの時 and 0052–0054 (あの人の油断が招いた結果, 彼女は戻らない) establish that Miller has died and that John blames himself. This agrees with F-018's reading of NO4_BAR/0402, and nothing shipped changes.
- Glossary: none.

### 12.3 Movable codes and readings (PR Flags 2, 3, 6)
- **Authored codes.** The authored `{br}`/`{p}`/`{w}` diff against the source matches Flag 2 exactly:
  - `:31 0077` `{p}` → `{br} {p}`: a leading `{br}` on the unit's only F-012 boundary (after the untagged 0076), at a sentence boundary.
  - `:32 0078` `{br} {br}` → `{p} {br}`: an added `{p}`. Without it, the page 0078 + 0079 is 5 rows. The source's page there is 3 rows, so the overflow is not inherited.
    - The click follows "She hadn't long to live……". The English makes the から clause its own sentence, and the causal link is carried by juxtaposition.
  - Every other `{br}` follows the same sentence as in the source. There is no `{w}`.
- **Glyphs.** `…` `‼` `⁉` `──` `！？` counts match on all 51 rows. The unit has no `…、`, so R §11.3 does not apply.
  - Mid-sentence `…` continues in lowercase (0056, 0058, 0075, 0084).
  - 0086 ごめんなさい…行きましょう is two sentences, so "Let's" keeps its capital.
- **Step-5/6 departures and readings (PR Flag 6), accepted:**
  - 0052 招いた結果 → "brought it on".
  - 0062 / 0063 生命の尊さ → "the sanctity of life". The halting echo "The sanctity, of life…?" moves the pause from after 生命の to after "sanctity". It still reads as halting.
  - 0061 the noun echo of 0058.
  - 0068 午後一番 → "first thing this afternoon"; numbers spelled out (R §1.4).
  - 0070 潮目 → "a current boundary", 目視 → "by eye".
  - 0074 救護班 → "the rescue team", フロート → "floats".
  - 0075 殺された → "was murdered, they say".
  - 0078 って → "he said".
  - 0087 一定間隔をとって → "at intervals", meaning spaced.
  - 0089 かまわず → "don't stop for anything".
  - 0091 いくらか → "somewhat".
- **Non-blocking:**
  - 0067 じゃあ、どうしろってんだ‼ → "Then what should we do‼" loses the retort in って. "Then what do you want us to do‼" would be closer.
  - 0082 "Just as you felt it, when Miller died……" could be smoother as "just as you did when Miller died".
  - Neither change is required.
- Glossary: none.

### 12.4 Recurrences (PR Flag 7)
- **Translated, identical:** 0057 = 0092 `………` = NO4_BAR/0201, 0265, 0430, SCN038_5C1/10. NO4_HWR_FRONT/0033 matches at the normalised level. Sibling PR #11's head renders SCN046B1/01 `………`, the same.
- **Untranslated exact twins, which CHECK pairs once translated:**
  - 0057 / 0092 = NO3_NO4/0007, 0061.
  - The sign 0097–0100 = NO4_HWL_BACK/0014–0017 = NO4_HWL_BACK2/0010–0013.
  - 0097 = NO5_HW_R/0008.
- **For later units:**
  - NO4_HWR_FRONT/0102 (p03, wave 4) `『ビアー＆ラガーズ』と書かれている。{p}` → `"Beer & Lagers," it reads.{p}`.
  - NO5_HW_R/0009 starts with `Entrance Hall` and uses unspaced `/` like this sign.
  - The other normalised hits are the labelled `_T` rows and tag variants, as R §5.6 and §11.5 list them.
- Glossary: none.

## Unit scene SCN041-SCN046 (PR #11, MERGED, 2026-10-25)

The third scene unit:
- SCN041 / SCN041_B: Judy, hurt shielding John, puzzles over why she did it.
- SCN046 / AMO1 / AMO2 / B: Wolg's vote prompts.
- SCN046A1–A3: Oakland's sacrifice, and Heming ("Clyde") turning on him.
- SCN046B1–B3: Wolg faces the killer, Jake Norman.
- SCN046_VALVE: the fuel valve.

Reviewed once:
- **Round 0** (fb26b1b, merged with `origin/main` 2f4949e for review): MERGE, squash f8e7b3a. Every gate passed, and there were no must-change findings.

Figures:
- **Subtitles.** 52, every one 1 page, at most 4 lines (`:44 SCN046B1/11`, `:49 SCN046B2/05`; UNITCHECK, 0 violations). The scene store has 150 rows, 0 violations.
- **Ratio.** 1,642 target characters ÷ 773 source = 2.12 (tags excluded).
- **Containers.** No byte container (scene). Script containers are unchanged: NO4_BAR.SCR 37,378 free, NO4_HWR_FRONT.SCR 54,522.
- **Duplicates.** CHECK compared 54 duplicate pairs (main's 46 + 8) and 2 tag-variant pairs. The +8 are 3 + 3 in the two vote-prompt groups, 1 in `すまん…。` and 1 in `………。`.
  - The reviewer's source-side census made 108,472 comparisons: 52 rows × every other script, scene and system dump row.
  - It ran at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped, with ！？ → ⁉ and final punctuation normalised.
  - It found 46 hits, 32 of them translated pairs, with 0 divergences (§13.4).
- **F-011 wrap scan.** The reviewer's own scan of `build/scene_merged.tsv` examined 52 subtitles and 84 wrapped lines. It was proved first on four planted violations.
  - It reported one problem: `:15 SCN046A1/04` "Go! | Wolg!". That row follows the source's authored 行けっ！{br}ウォルグ！, as SCN038B/11 does.
  - Lines ended by an authored `{br}` are ≤ 27 (`len()`).

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/scene/SCN041-SCN046.tsv` (line = row index + 3).

### 13.1 Terms promoted from §9, added, and one row extended
- **クライド** → `Clyde` (5).
  - Census: 0 / 1 / 0. Oakland says it to the man who betrays him (`:24 SCN046A2/02` "Clyde, you…"), and Heming answers as "Bill" (`:23`).
  - It is read as Heming's given name, by content. No row names Heming's given name otherwise.
  - Binds `:24`.
  - Glossary: §1 row added; §9 row removed.
- **ジェイク・ノーマン** → `Jake Norman` (11).
  - Census: 0 / 1 / 0. ジェイク and ノーマン occur only in the full name. Wolg names the killer at `:36 SCN046B1/03` "Jake Norman‼".
  - Binds `:36`.
  - Glossary: §1 row added; §9 row removed.
- **ウスノロ** → `dimwit` (6).
  - Census: 0 / 3 / 0. Rows: `:35` 親愛なるウスノロ "my dear dimwit", `:50` てめえらウスノロ "you dimwits", `:51` そのウスノロ "those dimwits".
  - "slowpoke" (the §9 alternative) loses the insult.
  - Glossary: §6 row added; §9 row removed.
- **メス** → `bitch` (5). The article is in context (あのメス → "that bitch").
  - Census: 0 / 2 / 0 (`:43`, `:44`). The killer means Judy.
  - "female" (the §9 alternative) keeps the animal sense but not the crude register (てめぇ, ねえ, やがる) of these lines.
  - Glossary: §6 row added; §9 row removed.
- **売女** → `whore` (5).
  - Census: 0 / 1 / 0 (`:51` "Your whore, too‼"). The killer means Wolg's murdered wife (NO3_NO4/0030–0037).
  - Glossary: §6 row added; §9 row removed.
- **神** → `god`, lowercase (3).
  - Census: 1 / 4 / 0 for 神 outside 女神. The scene rows are `:46`, `:47`, `:48`, `:49`. The script row is NO4_BAR_T/0144 神は──主は, a test-script line, in context. 女神 is 3 / 0 / 0 and stays the 俺様 row's "goddess".
  - Glossary: §6 row added; §9 row removed.
- **生肝** → `raw liver` (9). Census: 0 / 1 / 0 (`:48`). Glossary: §6 row added; §9 row removed.
- **シャッター** (variant 防水シャッター) → `shutter`; `watertight shutter` (7; 18). New.
  - Census: 31 / 1 / 1. 防水シャッター is 3 / 0 / 0 (the control panels NO3_MACHINE/0002, 0004, NO6_BRIDGE/0012); hints/011 is blocked, cap 39.
  - Lowercase. Binds `:4 SCN041/01`.
  - Glossary: §3 row added.
- **ゲームオーバー** → `game over` (9). New.
  - Census: 0 / 1 / 0. It occurs in dialogue only, `:23` "Bill… it's game over."; the system store has no ゲームオーバー row.
  - Glossary: §6 row added.
- **バッグ** joins the §3 鞄 · カバン row as a Variant, with the same target `bag`.
  - Census: 1 / 1 / 0. Rows: NO4_BAR/0454 "What's that bag, boss?" (shipped, #12) and `:12 SCN046A1/01` "The bag‼". It is the same bag, Oakland's, holding the carcass (NO4_BAR/0455).
  - The row's Variants and Note are extended. The target does not change, and no shipped line changes.
- **～ row note** (R §9.1). It read "SCN046A3/01 in context". It now records the decided form.
  - Rule: after ン, the stretched syllable's vowel is repeated once per ～: `:27` ヘイミン～～～～～～～グ‼ → `Hemiiiiiiiing‼` (Hemi + 7 i, 14).
  - The literal-nasal alternative `Heminnnnnnnng‼` is rejected. The row says "repeat the vowel", ン has none, and English stretches a shouted name on its vowel.
  - Only this row is affected, and it is the row's only open case. No shipped line changes.
- **Elongation, checked.** `:21` 行けえええええええっ‼ (7 え) → `Goooooooo‼` (G + 8 o = Go + 7). This follows the ～ row and the くそおおおっ → Daaaamn precedent (R §4.1, §9.1).
- **Applied, unchanged:** the killer's laugh (R §9.1: `:35`, `:52` "Heh, heh-heh, kahahahahaha."; `:37` "Heh, heh-heh."; `:39` "Heh-heh, kahahahahaha."); くそっ → `Damn‼`; 弾切れ → out of ammo; 社長 → the boss; ビル alone → Bill; ウォルグ → Wolg.

### 13.2 Speakers (PR Flag 4)
- Subtitles carry no speaker code, so every speaker is named from content (F-009).
- **The vote prompts** (`:10`/`:11` and their copies) are Wolg's. NO3_CHAPEL/0120–0122 (spk=2, 俺) has him set up the vote: hold a round in your right hand if you are for stopping the engine. "AMO" is ammo.
- **SCN041/02, SCN041_B** are Judy (わ, かしら). SCN041/01 is Judy or John.
- **SCN046B1–B2:**
  - The killer: B1/02, 04, 06, 07, 09–11 and B2/03, 04, 06–08.
  - Wolg: B1/03, 05, 08 and B2/01, 02, 05.
  - B1/01 and B3/01–02 are probably Wolg.
- **The killer's register in SCN046 is crude** (てめぇ, ねえ, しらねー, やがる), unlike the mock courtesy he uses with Judy in SCN038_5C1. R §9.1's note that later killer units "should keep" the courtesy is superseded for SCN046 by the source's own register. NO2_MAINSTORAGE is still to be judged from its source.
- **SCN046A1–A2** speakers stay partly uncertain (F-009). Every line is speaker-neutral in English, so a corrected attribution changes no text.
- **SCN046_VALVE** is a female voice (わよ), probably Judy.
- Glossary: none.

### 13.3 Movable codes and readings (PR Flags 2, 3, 5–8)
- **Authored codes.** The reviewer's diff of the authored `{br}`/`{p}`/`{w}` sequence against the source, over 52 rows, finds 3 differences, matching Flag 2 exactly.
  - `:44` `{br}{br}{br}` → `{br}{br}`: the removed `{br}` split 消えていく{br}姿.
  - `:49` the same: it split 殺したと{br}思ってる.
  - `:50` `{br}{br}` → `{br}`: it split なんて、{br}数えてる.
  - Each removed `{br}` fell mid-clause, and keeping it gives 5 lines or a broken clause.
  - No `{p}` or `{w}`. `…`, `‼`, `⁉` and `──` counts match on all 52 rows. ・ and ～ are not counted glyphs: the name ジェイク・ノーマン drops its ・, and the ～ are rendered as an elongation.
- **`:40 SCN046B1/07`** 見つけた / いやがった with no object → "found it" / "The damn thing's for real".
  - Accepted over "her". The source withholds the referent: Wolg asks 何を言っている at `:41`, and the killer later calls her アレ (`:48`) and "not human" (`:44`).
  - "damn" carries やがる. "her" first appears at `:42`, where the killer starts to explain.
- **`:55 SCN046_VALVE/01`** ト・マ・ラ・ナ・イ・ワ・ヨ…… → `It・will・not・stop……` (18). Accepted.
  - ・ is in the font, and CHECK passes it.
  - It keeps the halting, mora-by-mora delivery as word-by-word. "will not", uncontracted, carries わよ.
  - "It" is the engine at the fuel valve (NO3_CHAPEL/0126). The `……` count is kept.
  - In-game appearance noted under F-002.
- **`:8 SCN041_B/03`** "I wonder why I shielded you?" Accepted.
  - The ？ follows the source's かしら？ (PROJECT.md §6: punctuation follows the source).
  - The reorder (step 6, flagged) avoids "wonder?" alone on a line. It is 28 on one wrapped line.
- **`:23 SCN046A2/01`** "Bill… it's game over." conforms to R §11.3: 、 is absorbed after `…`, with a lowercase continuation.
- **`:37 SCN046B1/04`** echoes SCN038_5C1/09's frame ("I never dreamed I'd … meet you in a place like this"), crude here, and "either" carries 俺も (R §9.4).
- **Step-5/6 departures, flagged and accepted:**
  - `:46` お得意の神 → "that god of yours".
  - `:48` となる → "I become".
  - `:36` 逃がさん → "You'll never escape again" (an agency shift; "I won't let you get away again" is 30 on an authored-`{br}` line).
  - `:54` やるべきこと → "work to do".
  - `:35` 久しぶりだな。 → "Long time,".
- **Non-blocking:** each of these carries register by word choice (translation_prompt.md §2), and none changes sense.
  - `:44` "with my own eyes" carries 俺様は…んだよ.
  - `:39` "Pure chance" carries だよ.
  - `:49` drops と思ってるんだ, which is idiomatic in the accusation and needed to hold 4 lines.
- Glossary: the ～ row note (§13.1).

### 13.4 Recurrences (PR Flag 9)
- **Translated, identical:**
  - The vote prompts ×4 are byte-identical: `When you're ready, raise your right hand.` / `Open your hand.`
  - `:22` すまん…。 = SCN038D/12 `Sorry…`.
  - `:34` `………。` → `………` = NO4_BAR/0201, 0265, 0430, NO4_HWR_FRONT/0057, 0092, SCN038_5C1/10. NO4_HWR_FRONT/0033 `………` matches at the normalised level, with the same target.
- **Untranslated twins**, which CHECK pairs once translated:
  - `………。`: NO3_NO4/0007, 0061 (exact); NO4_MACHINER90/0108, NO4_TOOL_ROOM/0025, 0060 (tag variants).
  - The labelled `_T` hits are covered by R §5.6 and §6.4.
- **For later units:**
  - NO3_CHAPEL/0122 右手に握れ should match the prompt's "right hand" wording.
  - NO2_MAINSTORAGE/0003, 0009, 0012 女神 → "goddess" (俺様 row).
- Glossary: none.

## Unit script NO4_HWR_FRONT.p03 (PR #14, MERGED, 2026-10-25)

The starboard front corridor before Miller's death: the schedule board and the bar sign, Oakland sending John after Heming, the unnamed woman (Judy) questioning John, the party finding her, Miller introducing the salvagers, and the patrol and escort lines (0139–0146). Reviewed once:
- **Round 0** (e424309, merged with main f54819c for review): MERGE, squash d7e9398. Every gate passed, and there were no must-change findings.

Figures:
- **Container.** NO4_HWR_FRONT.SCR 11,180 / 65,535 bytes, 54,355 free; tokens 136 / 1,499 (MEASURE). p03 costs 167 bytes over p02's 54,522. The room is complete, 150 / 150.
- **Pages.** At most 4 rows per page (UNITCHECK, 46 rows, 0 violations). The whole store: 635 rows, 0 violations.
- **Ratio.** 1,838 target ÷ 759 source characters = 2.42 (PR figure, `codec.char_count`).
- **Duplicates.** CHECK compared 56 duplicate pairs (main's 54 + 0123 = 0129, 0144 = 0013) and 2 tag-variant pairs.
  - The reviewer's census made 95,956 source-side comparisons: 46 rows × every other script, scene and system dump row, at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？ dropped).
  - It found 60 hits, 19 of them translated pairs, with 0 divergences. The label-stripped `………` hits (0123/0129 ↔ NO4_BAR/0201, 0265, 0430, NO4_HWR_FRONT/0033, 0057, 0092, SCN038_5C1/10, SCN046B1/01) agree once 【Woman】 is stripped; sibling heads #17 NO4_MACHINER90/0010 and #15 0108 render `………{p}` too.
- **F-011 wrap scan.** The reviewer's script over `build/script_merged.tsv` aligned every wrapped line with its authored segment, after a planted copy proved it catches a lone "a", a split "Mr. | Oakland", a wrap-made one-word row, `'em`, an authored-`{br}` line over 27 and a glued `+` boundary. Result: 46 rows, 86 wrapped lines, 0 problems. 0139 wraps "shows | up" (a phrasal verb across a row), which reads.
- **F-012.** The one `+` row, 0128, follows 0127 ending `{br}`; nothing glued. None of the dump's 25 boundaries is in this unit.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_HWR_FRONT.p03.tsv` (line = row number − 97).

### 14.1 Terms promoted from §9, and one added
- **【女】 (label in a message)** → `【Woman】` (7).
  - Census: 16 / 0 / 0. Two are in a shipped room, NO4_HWR_FRONT/0123 and 0129 (`【女】………。{p}`); the other 14 are in the `_T` drafts (UP_T/0001–0008, 0022, 0024, 0028, 0030, 0035, 0037).
  - The translator's question, whether the label stays in a non-`_T` message, is ruled **yes**: the shipped source prints the label inside the message, so dropping it would delete source text (CLAUDE.md §3). It is translated and bracketed as PROJECT.md §6 does for the `_T` files.
  - "Woman", not "Girl" (the §9 alternative): 0121 女じゃないか → "Why, it's a woman." uses the same word for the same person. Miller's この子 (0126) is carried by "she".
  - `【Woman】………{p}` and the unlabelled `………` rows differ by the label only; that is not a divergence.
  - Binds `:26 0123`, `:32 0129`; UP_T/0022, 0024, 0028 (`【女】………{p}`) take `【Woman】………{p}`.
  - Glossary: §1 row added; §9 row removed.
- **乗客** → `passenger(s)` (10 (9)).
  - Census: 15 / 0 / 0. Shipped as "passenger(s)" at NO4_BAR/0028, 0094, 0191, 0198, 0393; no other rendering exists.
  - Binds `:25 0122` "Are you a passenger on board this ship?" (UP_T/0021 is its labelled copy).
  - Glossary: §2 row added; §9 row removed.
- **無線機** → `the radio` (9).
  - Census: 1 / 0 / 0, 0103 only. 無線装置 (3 / 0 / 0) stays "radio equipment" (`:48 0145`, NO4_BAR/0171). "the radio set" was the alternative; "the radio" keeps 0103 parallel to NO4_BAR/0171 (R §3.6) where the source agrees.
  - Binds `:6 0103` "What is it, John? Are you done checking the radio?".
  - Glossary: §3 row added; §9 row removed. The §3 無線装置 row's Note now reads "無線機 is its own row; 無線室 is a §9 row" — a pointer change only, no target changes, no shipped line affected.
- **ボンベ** → `air tank(s)` (9 (8)).
  - Census: 3 / 0 / 0: NO4_HWR_FRONT/0124, NO4_MACHINE/0002 (何者かによって破壊されたボンベ), NO4_MACHINE_T/0001 (壊れたボンベの破片). All are the party's diving tanks someone smashed. "oxygen tanks" is rejected: the source does not name the gas.
  - Binds `:27 0124` "You're the one who wrecked the air tanks, aren't you⁉".
  - Glossary: §3 row added; §9 row removed.
- **船内イベント** → `shipboard events` (16), new.
  - Census: 7 / 0 / 0. Five identical rows もう起こることの無い、船内イベントのスケジュール表が張ってある。{p} (NO4_HWR_FRONT/0101, NO4_HWL_FRONT/0011, NO6_HW_1/0003, NO6_HW_2/0006, 0010), which CHECK pairs once translated, and 『本日の船内イベント案内』と書かれている (NO4_SHOP/0006, NO5_BANK/0005), which takes the と書かれている pattern (R §12.1).
  - Binds `:4 0101` "A schedule of shipboard events that will never take place now is posted here.{p}".
  - Glossary: §6 row added.
- The other wave-4 §9 rows (ブリッジ, 船体, 装備, 虫, 生き物, 雇い主, 人間, 実験…, 処分) are left for the sibling reviews (#15, #16, #17).

### 14.2 Speakers (PR Flag 3)
- Checked against the `NO4_HWR_FRONT_UP_T` draft (F-009):
  - Oakland: 0113–0114 (T/0011), 0118 (T/0016), 0121 (T/0020), 0130 (T/0029), 0132 (T/0031), 0134 (T/0033), 0137 (T/0036); 0103–0104 by the NO4_BAR/0171–0172 parallel.
  - Wolg: 0119–0120 (T/0017, 0019), 0122 (T/0021), 0133 (T/0032), 0135 (T/0034). Heming: 0115 (T/0013). Miller: 0116 (T/0012), 0126–0128 (T/0025–0027).
  - The woman (Judy): 0105–0112, 0123, 0129, 0131, 0136, 0138.
  - Collison: 0144 (おって), a different scene; the text is bound to 0013.
- The shipped scene rewrites the draft at 0124–0125: T/0023 他の乗客はどうした (Oakland) becomes ボンベを壊したのはお前だな⁉ and 待て。その話は後回しだ, and Miller's 待って二人とも becomes そうよ. So 0124 is an accuser (probably William, or Wolg) and 0125 the man who defers it (Oakland or Wolg). Uncertain, speaker-neutral.
- 0117 (Wolg or William), 0139–0143 and 0146 (0143 and 0146 say 俺, so not Oakland) stay uncertain and are rendered speaker-neutral. Recorded in F-009.
- Registers fit: Oakland's 我々 → "In any case, we want to know how things stand on board."; Wolg terse ("Depends on the situation. Right, Mr. Oakland?").
- Glossary: none.

### 14.3 Movable codes and readings (PR Flags 2, 4–6, 8)
- **Authored codes.** The authored `{br}`/`{p}`/`{w}` sequence equals the source's on all 46 rows; no `{p}` added; no `{w}` in the unit. Glyph counts (`…` `‼` `⁉` `──`/`——` `【】`) match on all 46 rows (reviewer's script).
- **Modality** (the wave-3 lesson): the unit has no permissive or prohibitive construction. 0140 うろうろしてないで → "Quit wandering around", 0143 大人しくしておけ → "sit tight" and 0109 調べることなんかない → "there's anything to look into" are literal.
- **Step-5/6 departures, flagged and accepted:** 0117 って言うんだ → "Where'd you say they were⁉"; 0122 "on board this ship"; 0127 発見した → "came across"; 0134 現状 / この船 → "how things stand on board"; 0140 くれよ → "already"; 0104 サポートに行ってやれ → "go back him up"; 0118 "they"; 0131 "us" supplied; 0128 あなたは？ → "What about you?" (also fits its tag-variant twin NO2_MAINSTORAGE/0023).
- **？ for 。** (R §10.3): 0103 (as p01 0014 どうした、ジョン？ "What is it, John?"), 0126, 0145. Accepted.
- **Punctuation:** `【女】………。` and `それは──。` absorb the 。 (R §1.3); 0134 "Mm… Y-yes" (うむ a standalone interjection); 0141 "but… let's" continues in lowercase (mid-sentence `…`). No `…、` in the unit.
- **Non-blocking:** 0104 "Hurry and go back him up." is idiomatic (go + bare verb) though "go back" can garden-path; 0141 "anyway, just in case" carries 一応 twice ("let's check it, just in case" would be tighter); 0134 そ、そうだな → "Th-that's right." would mirror the stutter more exactly. None is a fidelity error.
- Glossary: none.

### 14.4 Recurrences (PR Flag 7)
- **Translated, identical:** 0144 = NO4_HWR_FRONT/0013 byte for byte (R §10.4); 0123 = 0129 `【Woman】………{p}`; 0102 = `"Beer & Lagers," it reads.{p}` (R §12.4).
- **Near-duplicate, aligned by hand:** 0103 ↔ NO4_BAR/0171 ("What is it, John… Are you done checking the radio…"); the `{br}`, ⁉ and 無線装置 of 0171 are not in 0103's source. 0145 keeps "checking the radio equipment".
- **Untranslated twins, which CHECK pairs once translated:** 0101 = NO4_HWL_FRONT/0011, NO6_HW_1/0003, NO6_HW_2/0006, 0010; 0128 (tag variant) = NO2_MAINSTORAGE/0023.
- **For later units, by hand:** NO5_ENTRANCEL/0005 寄り道せずについて来いよ (ついて for 付いて) reuses 0142's "Follow me, and no detours."; UP_T/0016–0037 are labelled copies of 0118–0138 (F-008, F-013) and reuse this unit's wording.
- Glossary: none.

## Unit script NO4_MACHINER90.p02 (PR #15, MERGED, 2026-10-25)

The salvagers' first entry into the ship, told in flashback: Wolg feels eyes on them in the hall, Miller wants to take the creature back, they find their gear smashed, the hull lurches, Miller faints, and they look for somewhere safe. Reviewed once:
- **Round 0** (93a0d5a, merged with main 8f330ba for review): MERGE, squash 40c6491. Every gate passed, and there were no must-change findings.

Figures:
- **Container.** NO4_MACHINER90.SCR 7,227 / 65,535 bytes, 58,308 free; tokens 271 / 1,499 (MEASURE). That is 54 / 108 rows; p01 (#17) shares the container and is in rework.
- **Pages.** At most 4 rows per page (UNITCHECK, 54 rows, 0 violations). The whole store: 689 rows, 0 violations.
- **Ratio.** 2,288 target ÷ 962 source characters = 2.38 (PR figure).
- **Duplicates.** CHECK compared 56 duplicate pairs and 4 tag-variant pairs.
  - The reviewer's census made 112,644 comparisons (54 rows × every other dump row, at three levels: exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？ dropped).
  - It found 27 hits, 13 of them translated pairs, with 0 divergences: 0093 `……?` and 0108 `………` (§15.4).
- **F-011 wrap scan.** 112 wrapped lines: no lone "a"/"I"/"an", no split title, and every authored-`{br}` line ≤ 27. One wrap-made one-word last row (0096, §15.3).
- **F-012.** Both `+` rows (0061, 0086) follow `{br}`-ended rows; nothing glued.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_MACHINER90.p02.tsv` (line = row number − 51).

### 15.1 Terms promoted from §9, and one added
- **生き物** → `creature` (8).
  - Census: 9 / 0 / 0, with no variant. Shipped as "creature" at NO4_BAR/0040.
  - Binds `:13 0064` "It's odd, this creature……", `:21 0072` "this creature's value"; NO4_TOOL_ROOM ×5 follow.
  - Glossary: §6 row added (beside 昆虫); §9 row removed.
- **船体** → `the hull` (8).
  - Census: 5 / 1 / 0. Sibling p01 0022 船体の中央 → "the middle of the hull" agrees.
  - 0098 repeats 船体 in one sentence (船体が動き始めてる……船体の角度が変わるぞ‼). The second is "it": "the hull's going to tilt" wraps to 5 rows with an orphaned "tilt‼".
  - NO4_BAR_T/0180, the `_T` draft of this moment, has 船が──船体が傾いているぞっ (傾く, "tilt"), which supports 0098's verb.
  - SCN047C1/05 (the alien vessel) is rendered in context. 船 alone stays "the ship".
  - Binds `:47 0098`; p01 `:25 0022` (#17).
  - Glossary: §2 row added; §9 row removed.
- **装備** → `gear` (4).
  - Census: 16 / 0 / 6, including 3 rows of 潜水装備, which is its own row ("diving gear").
  - Shipped as "gear" at NO4_BAR/0129, 0212, 0254, 0305. "equipment" (the §9 alternative) is rejected because it would split the four shipped rows.
  - The system rows (equip/000–003 を装備しました, camp/001, items/000 標準装備) use the verb or a compound, and are rendered in context once F-006 unblocks them.
  - Binds `:33 0084` "Our gear's been destroyed‼"; p01 `:19 0016` "this cumbersome gear" (#17).
  - Glossary: §3 row added; §9 row removed.
- **潜入 (する)** → `come aboard` (11), new.
  - Census: 2 / 0 / 0 (NO4_MACHINER90/0011, 0089). Both are the salvagers entering the wreck.
  - "infiltrate" and "sneak in" are rejected: the party is not hiding from anyone it knows of.
  - The binding from #17's round-0 review: p01 0011 changes to "come aboard".
  - Binds `:38 0089` "did we even need to come aboard?"; p01 `:14 0011` (#17 round 1).
  - Glossary: §6 row added.
- Left for the sibling merges: ブリッジ, 雇い主, 虫, 処分, 無茶を言う (#17); 人間, 実験 · 検体 · フェーズ２ (#16).

### 15.2 Speakers (PR Flag 5)
- These are named from content, ignoring spk=N (F-009). In this scene spk=2 mostly carries Oakland, spk=3 Miller, spk=4 Wolg and spk=5 Heming, with borrowings: Miller on spk=2 (0062, 0088) and spk=4 (0068), Oakland on spk=4 (0082), Wolg on spk=3 (0090).
  - Heming: 0069, 0073–0074, 0076, 0078, 0096, 0098, 0102–0103. 0097 "Heming, what's gotten into you" confirms 0096.
  - Wolg: 0055, 0057, 0059, 0081, 0083–0084, 0090, 0092, 0100 (社長 address), 0104, 0106.
  - Oakland: 0056, 0082 ("What is it, Wolg!"), 0079 (answering Heming's そうだろ？), 0097, 0101 (answering 0100).
  - Miller: 0062, 0064, 0068, 0070, 0072, 0075, 0077, 0080, 0085–0086, 0088–0089, 0091, 0107.
- 0063 is Oakland, by its labelled twin NO4_HWR_FRONT_DOWN_T/0001 【オークランド】なんだ？.
- These are probable, not confirmed: the spk=2 rows 0058, 0060–0061, 0065–0067, 0071, 0094–0095 and 0105 (Oakland); 0099 (Wolg or Oakland); 0093 and 0108 (unattributed).
- **0087 ミラー、少し黙れ (spk=3)** is uncertain. Two points favour Oakland:
  - Miller's 0086 (連れて来といて, "you dragged me here") is addressed to her employer.
  - So is 0089 (潜入する必要があったの？, "did we even need to come aboard?").
  - Wolg is also possible, being terse and taking 0090 静かにしろ‼.
  - All of these are speaker-neutral and recorded in F-009.
- Registers fit:
  - Oakland is plain and measured ("Quit joking.", "Of course. Let's get a move on.").
  - Heming is calm, mildly old-fashioned ("Not that I can't understand how you feel, but I'm afraid that's not possible.").
  - Miller is assertive, with かしら carried by "could" (0107).
- Glossary: none.

### 15.3 Movable codes, wraps and readings (PR Flags 2–4)
- **Authored codes.** Only two rows differ from the source, and both are in Flag 2:
  - `:8 0059` `{br} {br} {p}` → `{br} {p} {p}`, at the sentence boundary after 何か危険な感じがする。 The pages are 4 rows, then 2.
  - `:35 0086` gains a leading `{p}` on the `+` row after 0085's `{br}` (R §2.4). The pages are 4 (3 rows plus the cursor row), then 4. Added to F-010's in-game check.
  - The unit has no `{w}`. Glyph counts match on all 54 rows.
- **0096 one-word last row** (R §1.12 rule 1). The reviewer measured each candidate with `len()` and `codec.wrap(…, 28)`:
  - "Everyone, grab onto something‼" 30, "…hold onto something‼" 30, "…hold on to something‼" 31, "…grab hold of something‼" 33: each orphans "something‼".
  - "Grab onto something, all of you‼" 32 orphans "you‼".
  - "Grab onto something, everyone‼" 30 orphans "everyone‼".
  - Within 28, "Everyone, grab something‼" (25) loses つかまる's hold-on-for-support sense (it reads as つかむ, and can mean "pick something up"). "…hold on tight‼" (24) drops 何かに. "…brace yourselves‼" (27) is an idiom swap.
  - None of these is equally faithful, so the literal stands, flagged (rule 1, last sentence).
- **0078 "Right?"** is the source's own そうだろ？ line after an authored `{br}`, a whole sentence and not a wrap orphan, so it stands.
- **Readings accepted (Flag 3):**
  - 0098 角度が変わる → "tilt": a one-verb synonym (step 4; see 船体, §15.1). It is not 回転 "roll over".
  - 0058 でもそれなら → "So": the literal "But then why don't they come out?" orphans "out?".
  - 0072 それ以上 → "even more".
  - 0076 無茶苦茶言うやつ → "You say the wildest things." and 0103 世話の焼けるヤツ → "What a handful she is.": type-of-person readings (R §1.7). 無茶苦茶 is not 無茶を言う (#17's row).
  - 0088 黙れですって？ → "Shut up, you say?": the SCN002A/04 precedent "Wait…… you say?".
  - 0107 得体の知れない → "strange", as SCN002A/04.
- **Modality** (the wave-3 lesson) is literal: 0073 わからんでもない, 0075 できればやってる, 0089 必要があったの.
- Glossary: none.

### 15.4 Recurrences (PR Flag 6)
- **Translated, identical:**
  - 0093 `……?` = NO4_HWR_FRONT/0034, SCN038B/04.
  - 0108 `………` = NO4_BAR/0201, 0265, 0430, NO4_HWR_FRONT/0033, 0057, 0092, SCN038_5C1/10, SCN046B1/01, and 0123/0129 once the label is stripped. Sibling p01 0010 `………{p}` (#17) agrees.
- **Untranslated twins, which CHECK pairs once translated:** 0108 = NO3_NO4/0007, 0061, NO4_TOOL_ROOM/0025 (`………。{p}`), 0060 (`………。{w}{br}`).
- **Labelled twins, which CHECK does not pair (F-008, F-013); reuse by hand:**
  - 0063 なんだ？{p} = NO4_HWR_FRONT_DOWN_T/0001 【オークランド】なんだ？{p} → `【Oakland】What is it?{p}`. This also confirms 0063's speaker.
  - 0108 = NO4_BAR_T/0010 【男】, 0068 【ミラー】, 0151 【ジュディ】, NO4_HWR_FRONT_UP_T/0022, 0024, 0028 【女】 (R §14.4): `………`, with the translated label.
- **Near-duplicate for a later unit, by hand:** NO4_HWL_BACK/0007 みんな何かにつかまれ！{br}船が、船体が回転し始めるぞ！ The first sentence reuses 0096's words with the source's `!`: "Everyone, grab onto something!". 船体 → "the hull", and 回転 → "roll over" (glossary §3).
- **Agreement:** 0068 ちょっと待って！ "Wait a minute!" agrees with NO4_BAR/0368 ちょっと待ってよ！.
- Glossary: none.

## Unit script NO4_MACHINER90.p01 (PR #17, MERGED, 2026-10-25)

The salvagers' first entry into the capsized ship, told in flashback. Wolg hands out the weapons, Miller refuses one, Heming gives a handgun to John, and Oakland orders everyone to the bridge. Miller is held to the group as the team's doctor. Wolg checks the doors, they find the bodies, and Miller is drawn to an unknown bug. Reviewed twice:
- **Round 0** (5840b2d, merged with main b1e5067 for review): CHANGES. Every mechanical gate passed; there were three findings:
  - 1: `:28 0025` the wrap left a row ending in a lone "an" (R §1.12 rule 2).
  - 2: `:48 0045` an authored-`{br}` line was 28 columns, over the preferred 27.
  - 3: `:14 0011` 潜入 was "get inside", against #15's "come aboard".
- **Round 1** (4b8964e, merged with main 0c81906, which has #15, for review): MERGE, squash 8237cd9. `git diff 5840b2d 4b8964e` changes exactly the three rows.

Figures:
- **Container.** NO4_MACHINER90.SCR 7,715 / 65,535 bytes, 57,820 free; tokens 115 / 1,499 (MEASURE, with p02). The room is complete, 108 / 108. p01 alone cost 1,073 bytes over the untranslated 59,419 free.
- **Pages.** At most 4 rows per page (UNITCHECK, 54 rows, 0 violations). The whole store: 743 rows, 0 violations.
- **Ratio.** About 2,400 target ÷ 1,080 source characters ≈ 2.2 (PR figure).
- **Duplicates.** CHECK compared 57 duplicate pairs and 6 tag-variant pairs.
  - The reviewer's census made 112,644 comparisons: 54 rows × every other dump row, at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？ dropped).
  - It found 27 hits, 16 of them translated pairs, with 0 divergences (§16.4).
- **F-011 wrap scan.** 114 wrapped lines, 0 problems in round 1. Every authored-`{br}` line is ≤ 27.
- **F-012.** The one `+` row, 0046, follows 0045 ending `{br}`; nothing glued.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_MACHINER90.p01.tsv` (line = row number + 3).

### 16.1 Terms promoted from §9, and one added
- **ブリッジ** → `the bridge` (10); as a room name, `Bridge` (6, cap 14).
  - Census: 5 / 0 / 1 — NO4_MACHINER90/0019, 0020, 0028, 0029, NO6_BRIDGE/0017; rooms/108 (blocked, F-006).
  - Lowercase in dialogue (PROJECT.md §6). 操舵室 stays "the wheelhouse" (R §11.1).
  - Binds `:22 0019` "We aim for the bridge first.", `:23 0020`, `:31 0028`, `:32 0029`.
  - Glossary: §2 row added; §9 row removed.
- **雇い主** → `employer` (8).
  - Census: 3 / 0 / 0. Shipped as "employer" at NO4_BAR/0127; NO4_BAR_T/0162 is its labelled copy.
  - Binds `:39 0036` "But I'm your employer, so be ready for the consequences.".
  - Glossary: §2 row added; §9 row removed.
- **虫** → `bug` (3).
  - Census, 虫 alone: 3 / 0 / 0 — NO4_HWL_FRONT/0002 俺は虫は苦手でな, NO4_MACHINER90/0050, 0052.
  - The seed's 24 counted every row containing 虫: 昆虫 ×12 (its own row, "insect"), 虫の居所 ×6 (§6), 成虫 ×2 (NO4_TOOL_ROOM/0070, 0075) and 虫かご ×1 (NO3_CHAPEL/0023). The last two are other words, rendered in context.
  - "bug" over "insect": Heming's plain word, while Miller's 昆虫 keeps "insect". NO4_BAR/0389's "bug collecting" is the same register.
  - Binds `:53 0050` "that creepy bug", `:55 0052` "a bug like it".
  - Glossary: §6 row added; §9 row removed.
- **処分** → `dispose of` (10); それなりの処分 in context.
  - Census: 1 / 2 / 0 — SCN047A/03 検体の処分を行え, SCN047C1/05 道具は処分する必要がある (#16, both "dispose of" in its head), NO4_MACHINER90/0036.
  - 0036 is disciplinary: それなりの処分は覚悟しろ → "be ready for the consequences". "dispose of" would be wrong there.
  - #16's reviewer conforms to this row at its merge.
  - Binds `:39 0036`; SCN047A/03, C1/05 (#16).
  - Glossary: §6 row added; §9 row removed.
- **無茶を言う** → in context, new (PR Flag 5).
  - Census across every variant: 無茶を言 6 / 0 / 0 (無茶を言うな ×4, 無茶を言わないで ×1, 無茶を言ってる ×1); 無茶言 0. 無茶 appears in 9 / 0 / 0 rows in all.
  - The shipped rows answer requests: NO4_BAR/0155 (to call for help) and 0352, 0389 (to catch the spider). They take "Don't ask the impossible".
  - p01's rows answer a stance, not a request: 0024 answers "I'll wait here", 0031 answers "I'll be heading back". "ask the impossible" would misread them. "don't be absurd" fits, and Miller's echo 0032 無茶を言ってるのはあなたよ takes the same word: "You're the one being absurd".
  - 無茶 alone is "That's absurd." (NO4_HWR_FRONT/0071) and "hopeless" (NO4_BAR/0175). 無茶苦茶言うやつ (NO4_MACHINER90/0076, #15) is a different word, "You say the wildest things." Neither is fixed.
  - The rows are different messages, so no duplicate is split; no shipped line changes.
  - Binds `:27 0024`, `:34 0031`, `:35 0032`.
  - Glossary: §6 row added.
- **Conformance with #15's rows** (R §15.1): 潜入 `:14 0011` "the moment we come aboard" (round-0 finding 3); 装備 `:19 0016` "this cumbersome gear"; 船体 `:25 0022` "the middle of the hull".

### 16.2 Speakers (PR Flag 6)
- Named from content (F-009). spk=4 carries Wolg and Miller, spk=3 Miller and the men, spk=5 Heming and Miller (0047), spk=2 Oakland and Miller (0044).
  - Wolg: 0003–0004 (こいつは俺が持つ), 0006, 0008, 0015 (the safety warning NO4_MACHINE_T/s15 gives as 【ウォルグ】), 0016, 0022, 0026, 0039–0040, 0042.
  - Miller: 0005, 0007, 0009, 0020, 0023, 0025, 0027, 0029–0030, 0032, 0034, 0037, 0044, 0047, 0049, 0051, 0053.
  - Heming: 0002, 0012–0014 (俺, so not Oakland, whose わし is plain), 0017–0018, 0045–0046, 0048, 0050, 0052.
  - Oakland: 0019, 0031, 0033, 0035–0036 (雇い主はわしだ), 0038, 0041, 0043, 0054.
- Uncertain and rendered speaker-neutral: 0001 (Wolg or Oakland), 0011 (Heming or Oakland; a peacemaker line like NO4_BAR/0049), 0021, 0024, 0028 (Oakland or Wolg; male, not Miller), 0010 (unattributed).
- Registers fit: Oakland is plain with his crew ("That's why I brought you."); Wolg terse ("Any guarantee there isn't?"); Miller assertive, with かしら and のよ carried by tone ("And any guarantee there is?").
- Glossary: none.

### 16.3 Movable codes, wraps and readings (PR Flags 2–4, 7)
- **Authored codes.** Exactly four rows differ from the source, all in Flag 2:
  - `:18 0015` `{br} {br} {p}` → `{br} {p} {p}`: an added `{p}` at the sentence boundary after 弾はでない。 It gives pages of 3 + 3, where 6 rows would otherwise go on one page.
  - `:25 0022` loses the source's mid-sentence `{br}` (階段がある|はずだ), which broke for a narrower box: 4 rows.
  - `:29 0026` gets the same treatment as 0015 after 判かっていない。: pages of 3 + 2.
  - `:49 0046` gains a leading `{p}` on the `+` row after 0045's `{br}` ending (R §2.4): pages of 4 + 2. Added to F-010's in-game check.
  - The unit has no `{w}`. Glyph counts match on all 54 rows.
- **Round-0 findings, fixed in round 1:**
  - `:28 0025`: "I didn't come for an | obstacle course." became "I didn't come along to run an obstacle course." (26 / 26 / 19). "an" at a wrap counts as "a" under R §1.12 rule 2, as reviews have applied it since wave 2.
  - `:48 0045`: "I'd braced for no survivors," (28) became "I braced for no survivors," (26). It keeps 覚悟 and the comma. An authored-`{br}` line at 28 has not been accepted where a 27-or-less faithful wording exists (PROJECT.md §5.2).
- **Step-5/6 departures, flagged and accepted:**
  - 0015 reorders the reason clause after the verb (step 6); in source order, "recklessly." would be a one-word last row.
  - 0027 いつ安全だとわかる → "when will we know that?" (step 5; "it's safe" orphans "safe?").
  - 0028 → "We'll know at the bridge." (same reason).
- **Readings accepted:**
  - 0025 アスレチック → "obstacle course" (field athletics; "athletics" would be a false friend). 医者 → "doctor": she came as the team's doctor (0033 手当て), as the source says, though NO4_BAR/0042 calls her a marine biologist.
  - 0036 処分 → "the consequences" (§16.1). 0044 この死体 → "these bodies". 0046 のか… → "Perhaps…", musing, no ？. 0047 冗談じゃないわ → "No way.".
  - 0053 待ってと言った is kept literal, though Miller said どいて at 0049 (a source inconsistency).
- **Modality** (the wave-3 lesson) is literal: 0005 要らない "I don't need one."; 0014 しまっておけばいい "just keep it stowed" (permissive); 0015 控えろ "refrain from".
- **Non-blocking:** 0025 のよ？ "right?" asks where Miller insists ("remember?" would be closer). 0052 wraps "like | it.". Neither is a fidelity error.
- Glossary: none.

### 16.4 Recurrences (PR Flag 8)
- **Translated, identical:**
  - 0021 = NO4_BAR/0139 "Who knows.".
  - 0010 `………{p}` = NO4_HWR_FRONT/0033 (tag variant), NO4_BAR/0201, 0265, 0430, NO4_HWR_FRONT/0057, 0092, SCN038_5C1/10, SCN046B1/01, sibling 0108 `………{p}`, and 0123/0129 once 【Woman】 is stripped.
  - 0034 `……{p}` = NO4_BAR/0391 (tag variant). Sibling 0093 `……?{p}` and NO4_HWR_FRONT/0034 have ？, a different source.
- **Untranslated twins, which CHECK pairs once translated:** NO2_THIRDSTORAGE/0006 `……。{p}` (exact twin of 0034) → `……{p}`; 0010's twins NO3_NO4/0007, 0061, NO4_TOOL_ROOM/0025, 0060.
- **Labelled twins (F-013), by hand:** NO4_BAR_T/0010, 0068, 0151, NO4_HWR_FRONT_UP_T/0022, 0024, 0028 → `………` after the translated label (R §14.4, §15.4).
- **Near-parallels, not paired:** NO4_BAR/0049 仲間割れは困る "infighting" (0011 "Falling out", a different sentence); 保証 → "guarantee", as NO4_BAR/0132.
- Glossary: none.

## Unit scene SCN047-EPILOG (PR #16, MERGED, 2026-10-25)

The last scene unit. Its scenes, with speakers named from content (F-009):
- SCN047A: the alien command ends the experiment, and Judy, who now knows what she is, sends John away.
- SCN047B2–B3: the dying Wolg holds the aliens off so that John can go after Judy.
- SCN047C1: the alien voice explains the experiment.
- SCN047C2: Judy declares herself human.
- EPILOG, EPILOG0: the survivors' afterword and the aliens' "Phase 2".

Reviewed twice:
- **Round 0** (210d59b, merged with main b3a9fc2): CHANGES, one finding. `:31 C1/03` "is beyond our senses" was a step-5 departure the geometry did not force. In English it reads as "imperceptible", and it dropped 理解できない.
- **Round 1** (8bc8f6a, merged with main bcb6360): MERGE, squash 1e66f3c. `git diff 210d59b 8bc8f6a` is that one line, now "makes no sense to us".

Figures:
- **Subtitles.** 40, every one 1 page, at most 4 lines (`:4`, `:31`, `:33`, `:43`; UNITCHECK, 0 violations). The scene store is complete: 190 / 190 rows, 0 violations.
- **Ratio.** 1,589 target ÷ 793 source characters = 2.00 (PR figure).
- **Containers.** None for scene. MEASURE: 0 containers negative and 0 under the reserve.
- **Duplicates.** CHECK compared 58 duplicate pairs and 6 tag-variant pairs.
  - The reviewer's census made 83,440 comparisons: 40 rows × every other dump row, at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？ dropped).
  - It found 2 hits, the ハイ。 pair A/02 ↔ A/04 in each direction, both `Yes.`, with 0 divergences.
- **F-011 wrap scan.** 78 wrapped lines: no lone a/an/I, no apostrophe, and glyph counts match on all 40 rows. One wrap-made one-word last row, `:28` (§17.3). Every authored-`{br}` line is ≤ 27.
- **F-012.** There are no `+` rows in the unit.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-25. Line citations use PROJECT.md §7's numbering in `tl/scene/SCN047-EPILOG.tsv` (line = row index + 3).

### 17.1 Terms promoted from §9, added, and one note corrected
- **人間** → `human(s)`; `people` where the line is general (5 (6)).
  - Census: 21 / 5 / 0.
  - "human(s)" is shipped at NO4_BAR/0035, 0132, 0199 ("us humans"), 0246, 0333, NO4_HWR_FRONT/0003, 0005, SCN046B1/11 and B2/01. "people" is shipped at NO4_BAR/0310 and NO4_HWR_FRONT/0004 (人間、歳をとると, a general statement). 外の人間 (NO4_BAR/0003, "from outside") is in context.
  - Binds `:28` (elongated, `humaaaaaaaaaaaans`), `:38`, `:39`.
  - Glossary: §6 row added; §9 row removed.
- **実験 · 検体 · フェーズ２** → `experiment` · `specimen` · `Phase 2` (10 · 8 · 7).
  - Census: 0 / 3 / 0 · 0 / 1 / 0 · 0 / 1 / 0.
  - "specimen" is preferred to "test subject" (the §9 alternative): the aliens speak of John as material, and the word is shorter.
  - フェーズ２ takes an Arabic digit, as a label.
  - Binds `:4`, `:6`, `:31`, `:42`.
  - Glossary: §6 row added; §9 row removed.
- **処分** conforms to the §6 row #17's integration wrote (R §16.1): `:6` "Dispose of the specimen.", `:33` "must be disposed of". No second row is added; the row's Note now says the #16 lines are shipped.
- **自己犠牲** → `self-sacrifice` (14), new. Census: 0 / 1 / 0. Binds `:31`. Glossary: §6 row added.
- **ハイ** (katakana) → `Yes` (3), new.
  - Census: 0 / 2 / 0. `:5` and `:7` are byte-identical `Yes.`, and CHECK pairs them.
  - Hiragana はい in dialogue stays in context (EPILOG/03 "Yes…… understood."). The choice row is §4.
  - Glossary: §6 row added.
- **うう** → `Uuh` (3), new: one "u" per う, with an "h" closing it, as in the きゃあ…っ pattern.
  - Census: 0 / 1 / 0 for うう proper. The one script hit is NO3_CHAPEL/0119 ううむ, another word, in context.
  - Binds `:8` うう…。 → "Uuh…".
  - Glossary: §6 row added.
- **船体, a note correction** (the §2 row, R §15.1). The target is unchanged and no shipped line changes.
  - The note read "SCN047C1/05 (the alien vessel) in context". It now reads "SCN047C1/05 'the vessel' in context, referent left open".
  - At `:33`, 使った道具は処分する…いまから船体は軌道上で分解、投棄する may mean the alien ship. It may also mean the passenger ship, as the experiment's "tool". The source does not say which.
  - "the vessel" covers both readings. "the hull" would favour the second.
  - Binds `:33`.
  - Glossary: §2 row note corrected; Ruling column now R §15.1, §17.1.

### 17.2 Speakers (PR Flag 6)
- Subtitles carry no speaker code. Every speaker is named from content, and every line is speaker-neutral in English.
- **SCN047A:**
  - 01 and 03 are the alien command.
  - 02 and 04 (ハイ) are probably Judy taking the orders: `:15` "I was told to kill you". An alien subordinate is possible.
  - 05–15 are Judy.
- **SCN047B2–B3** are the dying Wolg.
- **SCN047C1:**
  - `:29` C1/01 "John, why……" is Judy: it echoes A/15 "Goodbye…… John". The dispatch had named the alien voice.
  - 02–06 are the alien voice.
- **SCN047C2:**
  - 01, 02, 04 and 05 are Judy (わ, のよ).
  - `:37` C2/03 ば、馬鹿な‼ → "A-absurd‼" is the alien, reacting to C2/02. The stutter is hyphenated on the first English word (R §4.3), and the cold register suits "absurd" over "impossible".
- **EPILOG and EPILOG0:**
  - EPILOG/01–02 and EPILOG0 are a survivor's inner thoughts in （ ）, probably John's.
  - EPILOG/03 is an unidentified agent reporting to the aliens.
- Recorded under F-009.
- Glossary: none.

### 17.3 Movable codes, wraps and readings (PR Flags 2–5, 7, 8)
- **Authored codes.** The reviewer's diff over 40 rows finds exactly one difference, `:31` `{br} {br}` → `{br}` (Flag 2).
  - Keeping both `{br}`s needs 5 or more lines.
  - Round 1's line 31 wraps 28 / 26 / 26 / 27.
  - The unit has no `{p}` or `{w}`.
- **`:31`, losses accepted.**
  - 今回の実験も同じ結果だった → "This experiment ended the same.": も is carried by "the same". Every "too" variant measured 29 or more on the authored-`{br}` line, or added lines.
  - 理解不能なデータの蓄積に終わった → "More data we cannot fathom.": 蓄積 is carried by "More", and 終わった by the preceding "ended".
- **`:28` elongation** 人間をなめんなああああああぁぁぁぁぁっ！ → `Don't underestimate humaaaaaaaaaaaans!`
  - The word has a×12 = 1 + あ×6 + ぁ×5; small ぁ counts like あ. The final っ is dropped and the single ！ kept.
  - This follows the ～ row and R §13.1 (`Goooooooo`, `Daaaamn`): the stretch moves to the English last word's vowel.
  - "underestimate" is the literal sense of なめる ("take lightly"). "mess with" (provoke) changes the sense, and Wolg's register (glossary §7) is serious, not crude.
  - The one-word last row cannot be avoided: an 18-column word leaves 10 columns, and "Don't mess with | humaaaaaaaaaaaans!" orphans too. It stands, flagged under R §1.12 rule 1, like SCN046A1/04 "Go! | Wolg!".
- **`:27` B3/01** "draw them off… you get Judy…" conforms to R §11.3.
- **Step-4/5/6 departures, flagged and accepted:**
  - `:43` 助かった → "lived": the reviewer measured "survived" at 5 lines with a lone "a".
  - `:19` ここ → "this".
  - `:21` reordered "So this is… what he… meant…".
  - `:25` "You're determined… to go?".
  - `:4` "we" supplied.
- **Readings accepted:**
  - あいつら `:19` → "those people" (the aliens look human).
  - あいつ `:21` → "he" (the killer, SCN046B1/11).
  - C2/04–05 なんだって continue C2/01's 気が付いた ("That …").
  - こそ → "above all".
  - EPILOG0 keeps the source's missing final 。.
  - Numbers: １月 → "a month", ２人 → "the two of us", フェーズ２ → "Phase 2".
- **Modality** (the wave-3 lesson) is literal: さわらないで, 殺したくない, 死なせたくない.
- Glossary: none.

### 17.4 Recurrences (PR Flag 9)
- **Translated, identical:** ハイ。 A/02 = A/04 `Yes.`
- **Echoes, not duplicates:**
  - SPACESHIP_HW/0001 今戻るのは危険すぎる… (untranslated) shares 危険すぎる with `:24` "…It's too dangerous."; reuse "too dangerous".
  - NO3_NO4/0053 バカな、閉じ込めたはず‼ is a different line (馬鹿な here is the alien's).
  - NO4_MACHINER90/0081 これはいったい⁉ "What on earth is this⁉" agrees with `:19`.
- Glossary: none.

## Unit script NO4_TOOL_ROOM.p01 (PR #21, MERGED, 2026-10-26)

Miller shows John the drowned sample. Then comes the 【Miller】/【Judy】 exchange: the creature combines the advantages of insects and mammals. The sibling NO4_TOOL_ROOM.p02 (#20) continues the conversation.
- **Round 0** (210d4d1, merged with main 02a7bbd for review): MERGE, squash b01686f. No findings.

Figures:
- **Container.** NO4_TOOL_ROOM.SCR 3,394 / 65,535 bytes, 62,141 free; tokens 227 / 1,499 (MEASURE). That is +902 bytes over the untranslated 63,043 free; 42 / 80 rows translated.
- **Pages.** At most 4 rows per page (UNITCHECK, 42 rows, 0 violations). The whole store: 785 rows, 0 violations.
- **Ratio.** 1,871 ÷ 766 = 2.44 (PR figure).
- **Duplicates.** CHECK compared 70 duplicate pairs and 6 tag-variant pairs.
  - The reviewer's census made 87,612 comparisons: 42 rows × 2,086 other dump rows, at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？ dropped).
  - It found 178 hits, almost all label rows, with 0 divergences (§18.4).
- **F-011 wrap scan.** 107 wrapped lines and 0 problems. Every `{w}`- or authored-`{br}`-ended line is ≤ 27 (`len()`).
- **F-012.** Every `+` row follows a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-26. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_TOOL_ROOM.p01.tsv` (line = row number + 3).

### 18.1 Terms promoted from §9, and rows added
- **哺乳類** → `mammal(s)` (7 / 6).
  - Census: 9 / 0 / 0 — NO4_TOOL_ROOM/0017, 0019, 0022, 0029, 0031, 0033, 0034, 0037 (p01) and 0064 (p02 "mammals", #20 head fae16dc).
  - Glossary: §6 row added; §9 row removed.
- **感覚器官** → `sensory organs` (14); the seed's alternative "sense organs" was not taken.
  - Census: 2 / 0 / 0 — 0035 "keen sensory organs", 0037 "their sensory organs bring".
  - Glossary: §6 row added; §9 row removed.
- **解剖** → `dissect / dissection` (7 / 10).
  - Census: 2 / 0 / 0. The two uses: `:14 0011` 解剖してみないと → "without dissecting it", and NO4_HWL_FRONT/0001 怪物の解剖 → "the monster's dissection" (#18 head 0e3bb89).
  - The two units agree. "autopsy" is wrong for a creature.
  - Glossary: §6 row added; §9 row removed.
- **生物** (variant 全生物) → `organism(s)`; 全生物 → "all organisms".
  - Census: 生物 11 / 0 / 0, of which 2 are 海洋生物学者 (NO4_BAR/0042, NO4_BAR_T/0062; §2 row). That leaves 9: NO4_BAR/0457 and NO4_TOOL_ROOM/0016, 0017, 0021, 0023, 0042, 0047, 0048, 0055.
  - Miller's scientific word, kept apart from 生き物 "creature" (§6, R §15.1). The same speaker uses both in one scene: 0006 不思議な生き物 vs 0016 この生物.
  - In context:
    - Shipped NO4_BAR/0457 新種の生物だぞ⁉ → "This is a new species⁉" (Oakland). No change.
    - `:24 0021` 生物としての観点から言えば → "Biologically," (§18.3).
  - Binds `:19 0016`, `:20 0017`, `:26 0023`, `:45 0042`; p02 0047, 0048, 0055 agree.
  - Glossary: §6 row added.
- **生命 · 生命体**, as an organism → `life form` (9), with no hyphen, so the wrap cannot strand "life-form.".
  - Census: 生命体 1 / 0 / 0 (0041). 生命 7 / 1 / 0: as an organism only at 0033 優秀な生命. Elsewhere it means "life", in context: NO4_BAR/0216 "lives", NO4_HWR_FRONT/0062–0063 "the sanctity of life", NO3_CHAPEL/0120 (untranslated), SCN038D/08. 生命力 (0027) is "vitality".
  - Binds `:36 0033`, `:44 0041`.
  - Glossary: §6 row added, scoped to the organism sense.
- **利点** → `advantage(s)` (10 / 9).
  - Census: 4 / 0 / 0 — 0017, 0019, 0031; p02 0064 "the advantages of both insects and mammals" agrees.
  - Glossary: §6 row added.
- **【ミラー】 · 【ジュディ】** → `【Miller】` · `【Judy】` (8 · 6), with brackets kept, as 【女】 (R §14.1).
  - Census: 30 / 2 / 0 · 16 / 0 / 0. Shipped SCN002OLD/04, 06 already use `【Miller】` as a prefix.
  - p01 and p02 use the labels as standalone `【Name】{br}` rows.
  - Glossary: §1 row added.
- **Conformance:**
  - `:6 0003` カバンごと → "bag and all" (鞄 row, R §8.1, §13.1).
  - 生き物 "creature" at `:9 0006` and `:12 0009` (R §15.1).
  - モンスター "monster" at `:42 0039` (R §8.1).

### 18.2 Speakers (PR Flag 6)
- 0001–0004: Miller to John, unlabelled. Her かしら/わ register fits, and she holds the sample (NO4_BAR/0392–0394). John's side is not shown.
- 0005–0042 follow the in-message labels. spk=0 throughout (F-009).
- Register fits R §1.10: articulate and assertive. かしら is carried by "I wonder" (0007), as p02 0046 does. Sentence-final わ/よ/ね have no markers.
- Glossary: none.

### 18.3 Movable codes, wraps and readings (PR Flags 2–5, 7)
- **Added `{p}`.** Exactly five rows differ from the source in their `{p}{w}{br}` sequence. All five are in Flag 2, and the reviewer proved each one forced by removing it in a scratch copy and re-running UNITCHECK:
  - `:9 0006` `{br} {w} {br}` → `{br} {p} {w} {br}`. Without it, the page from 0005 is 6 rows.
  - `:25 0022` `{w} {br}` → `{p} {w} {br}`. Without it, 5 rows from 0021.
  - `:37 0034` `{w} {br}` → `{p} {w} {br}`. Without it, 6 rows from 0033.
  - `:40 0037` `{p}` → `{p} {p}`. Without it, 6 rows from 0036.
  - `:45 0042` `{p}` → `{p} {p}`. Without it, 5 rows from 0041.
  - Each click is at a comma or colon. No `{br}` was moved, added or removed.
  - The page after each added click carries no repeated 【Name】 label. This is added to F-010's in-game check.
- **Restructures (step 6), all forced, nothing dropped.** The page model matters here: after a `{w}{br}` the next page opens with a blank row, then the label row, so a labelled reply has 2 text rows, and an unlabelled continuation 3.
  - `:19 0016` "Should this organism be what I imagine". The plain "If this organism is what I | imagine" ends a line in a lone "I".
  - `:20 0017` "with both insect and mammal advantages——that's my view." The source order ("the advantages of both insects and mammals") wraps to 4 rows where 3 are available.
  - `:22 0019` "The advantages…… of insects and mammals?". The source order leaves "advantages?" alone on the last row (R §1.12). Judy's hesitation is kept, one word earlier.
  - `:38 0035` "Another trait: keen sensory organs, like eyes and ears, to sense the outside world." This is 3 rows of 27. The clause-for-clause form takes 4. Every element is kept: すぐれた, 目や耳など, 外界を知る, のも特徴.
  - `:40 0037` uses a colon around the forced `{p}`; といえる → "you could call those".
- **Step 4, forced.** `:24 0021` 生物としての観点から言えば → "Biologically,". After 0019's `{w}{br}` the page is blank + 【Miller】 + text, so 0021 has 2 rows. "From a biological standpoint, Earth's most successful race is insects." takes 3. This is a shorter synonym, not an implication (wave-4 lesson: no unforced compression).
- **Readings accepted:**
  - 0002 料金は取らないわ → "I won't charge admission." This is Miller's dry joke about viewing the sample: the fee is named from context, and nothing is added to the plot.
  - 0012 わからないのかも → "Or maybe it's unknowable……", so that Judy's echo 0014 stays one word ("…Unknowable?").
  - 0021 種族 → "race". 0022 numbers spelled out (R §1.4); 種類 → "species".
  - 0042 "how superior an organism could be born" is stiff but literal (生まれる).
- **Suspected source typos** (F-023). Both readings are confirmed:
  - `:37 0034` 対向できる → 対抗できる "counter". 対向 is 1 / 0 / 0, only here, and 対抗 0.
  - `:45 0042` 生まれかが → 生まれるかが "could be born". 生まれか is 1 / 0 / 0, only here.
- Glossary: none.

### 18.4 Recurrences (PR Flags 8, 9)
- **Translated, identical:** 0025 `………{p}` matches NO4_BAR/0201, 0265, 0430, NO4_HWR_FRONT/0033 (after its 。), 0057, 0092, NO4_MACHINER90/0010, 0108, SCN038_5C1/10, SCN046B1/01, and 0123/0129 once 【Woman】 is stripped.
- **Untranslated twins, which CHECK pairs once translated:**
  - p02 0060 `………{w}{br}` (#20 head agrees); NO3_NO4/0007, 0061.
  - Labelled `_T` twins (F-013): NO4_BAR_T/0010, 0068, 0151 and NO4_HWR_FRONT_UP_T/0022, 0024, 0028 take `………` after the translated label.
- **Sibling agreement with #20 (head fae16dc).** It agrees on 生き物, 生物, 利点, 哺乳類, the labels, `………` and かしら → "I wonder". #20's integration only confirms the rows above.
- Glossary: none.

## Unit script NO4_TOOL_ROOM.p02 (PR #20, MERGED, 2026-10-26)

Judy and Miller finish p01's sample analysis: the organism, eggs, life stages and weak points. The unit ends with the locker narration at 0080. Reviewed twice:
- **Round 0** (fae16dc, merged with main 1477cf0 for review): CHANGES. Every mechanical gate passed, but there were three findings:
  - 1: `:8 0047` "making an | organism", a lone "an" at a wrap (R §1.12 rule 2, as applied in R §16.3).
  - 2: `:30 0069` "Given that it has an | exoskeleton", the same fault.
  - 3: PR Flag 6 claimed there were none.
- **Round 1** (3672de3, merged with main d0c362a for review): MERGE, squash c60bcc6. `git diff fae16dc 3672de3` changes exactly 0047 and 0069, and the PR body corrects Flag 6.

Figures:
- **Container.** NO4_TOOL_ROOM.SCR 3,636 / 65,535 bytes, 61,899 free; tokens 73 / 1,499 (MEASURE). The room is complete, 80 / 80 with p01.
- **Pages.** At most 4 rows per page (UNITCHECK, 38 rows, 0 violations). The whole store: 823 rows, 0 violations.
- **Ratio.** 1,302 ÷ 555 = 2.35 (PR figure).
- **Duplicates.** CHECK compared 83 duplicate pairs and 7 tag-variant pairs.
  - The reviewer's census made 237,479 comparisons: 38 rows × 2,083 other dump rows, at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？ dropped).
  - It found 178 hits, 98 of them against translated rows, with 0 divergences (§19.4).
- **F-011 wrap scan.** 68 wrapped lines, 0 problems in round 1. All 33 `{w}`- or authored-`{br}`-ended lines are ≤ 27 (`len()`); the longest is 0075, at 27.
- **F-012.** Every `+` row follows a `{br}` or `{w}{br}` ending; nothing glues.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-26. Line citations use PROJECT.md §7's numbering in `tl/script/NO4_TOOL_ROOM.p02.tsv` (line = row number − 39).

### 19.1 Terms promoted from §9, and one added
- **幼生体 · サナギ** → `larva · pupa` (5 · 4); 0072 "If this is the larva, … the pupa stage".
  - Census: 幼生体 1 / 0 / 0, 幼生 1 / 0 / 0 (the same row), サナギ 1 / 0 / 0, さなぎ and 蛹 0 / 0 / 0.
  - The seed's alternatives "larval form · chrysalis" were not taken. "chrysalis" names a butterfly's pupa, and Miller's register is general entomology.
  - Glossary: §6 row added; §9 row removed.
- **クローン羊** → `the cloned sheep` (16); 0053 "the birth of the cloned sheep".
  - Census: 1 / 0 / 0; クローン 1 / 0 / 0 (the same row).
  - The source gives no name, so "Dolly" would add one.
  - Glossary: §6 row added; §9 row removed.
- **ロッカー** → `locker` (6). The room name ロッカールーム (rooms/086) → "Locker Room" (11, under cap 14; blocked, F-006).
  - Census: 7 / 0 / 1 — NO4_TOOL_ROOM/0080, NO5_LOCKERROOM/0004–0007, NO2_MAINSTORAGE/0029–0030; rooms/086.
  - `:41 0080` ロッカーには何も入っていない → "The locker is empty.". This is a rewording under R §1.12 rule 1: "There's nothing in the locker." wraps "There's nothing in the | locker.", a one-word last row. Nothing is compressed.
  - NO5_LOCKERROOM/0005 ロッカーの中は空のようだ and 0006 このロッカーは空のようだ take "seems empty", keeping the hedge that 0080 does not have.
  - Glossary: §3 row added; §9 row removed.
- **成虫** → `adult(s)` (5 / 6). This is not a §9 seed; it is added.
  - Census: 2 / 0 / 0 — `:31 0070` "If that big one is the adult", `:36 0075` "All of these become adults?".
  - It is kept apart from 虫 "bug" (R §16.1) and 昆虫 "insect" (R §7.1).
  - Glossary: §6 row added.
- **Confirmed, not duplicated** (rows on main from #21, R §18.1):
  - 生物 "organism": `:8 0047`, `:9 0048`, `:16 0055`.
  - 生き物 "creature": `:5 0044`, `:19 0058`, `:25 0064`.
  - 哺乳類 "mammals" and 利点 "advantages": `:25 0064`.
  - 【Miller】 / 【Judy】 labels.
- Glossary: as above. No existing row is changed.

### 19.2 Speakers (PR Flag 8)
- Speakers follow the in-message labels; spk=0 throughout (F-009). Judy: 0044, 0050, 0055, 0060, 0066, 0075. Miller: the rest. 0080 is narration.
- Miller's かしら is carried by "I wonder" (`:7 0046`), as in p01 0007 (R §18.2). Sentence-final わ/よ/ね have no markers.
- Judy's register stays plain.
- Glossary: none.

### 19.3 Movable codes, wraps and readings (PR Flags 2–6, 9, 10)
- **Added `{p}`.** Exactly two rows differ from the source in their `{p}{w}{br}` sequence. Both are in the PR's Flags, and the reviewer proved each forced by removing it in a scratch copy and re-running UNITCHECK:
  - `:8 0047` `{w} {br}` → `{p} {w} {br}`, a leading `{p}` on a `+` row after 0046's `{br}`, at a sentence boundary (R §2.4).
    - Without it, the page from 0044 is 7 rows.
    - This is the chain F-010 names as 5 rows in the source.
    - Added to F-010's in-game check.
  - `:25 0064` `{p}` → `{p} {p}`, at the clause comma ("…of both insects and mammals,{p}then this creature is…"). Without it, the page from 0063 is 6 rows.
  - No `{br}` was moved, added or removed. All 19 `{w}` are kept in place.
- **Round-0 findings, fixed in round 1:**
  - `:8 0047` became "…making such an intricate organism should be quite impossible." It wraps 27 / 27 / 28 / 20, so the page stays at 4. "such an intricate" keeps これほど精巧な.
  - `:30 0069` became "Since it has an exoskeleton, it must either molt or undergo metamorphosis." It wraps 28 / 22 / 22. 以上 → "Since", and "either…or" carries か. 0069 has 3 rows on its page (cursor + 3). Any opening of "Given that it has an exoskeleton" puts "an" at column 20, and "metamorphosis." alone is the other trap.
  - Lesson for translators: a hand-read of the wrap missed both cases. Scan the wrapped lines with a script, as the PR's round 1 did.
- **Wording chosen for wraps, accepted as not §2.1 step 5** (the wave-4 lesson):
  - `:16 0055` "We're going to take on… that kind of organism?". The hesitation moves from before the verb to before the object, nothing is dropped, and そんな → "that kind of".
  - `:39 0078` 結論を急いじゃダメ → "But we mustn't be hasty in reaching a conclusion." This is longer than the source. "jump to conclusions" orphans "conclusions.", and "rush to a conclusion" ends a row in a lone "a".
  - `:41 0080`: see §19.1.
- **Readings accepted:**
  - `:19 0058` …とはなにか。 → "?". The wh-clause is interrogative in English, so "?" is the target punctuation (PROJECT.md §6 maps 。 for statements).
  - `:25 0064` 卵生もしくは卵胎生 → "oviparous or ovoviviparous". These are technical terms in Japanese too, in Miller's taxonomy register (NO4_BAR/0352). Judy's "Eggs…?" (0066) picks up 卵. "both" echoes p01 0017 両方の利点 and adds no fact.
  - `:13 0052` "That, in secret, research had been well under way." completes Judy's "That means——" (ってことね).
  - `:40 0079` 充分ある → "every chance".
- Glyph counts match on all 38 rows. `…。` and `──。` absorb the 。 (R §1.3).
- Glossary: none.

### 19.4 Recurrences
- **Translated, identical:**
  - `:21 0060` `………{w}{br}` matches the `………` family: NO4_BAR/0201, 0265, 0430; NO4_HWR_FRONT/0033, 0057, 0092, and 0123/0129 once 【Woman】 is stripped; NO4_MACHINER90/0010, 0108; NO4_TOOL_ROOM/0025; SCN038_5C1/10, SCN046B1/01.
  - The 【Judy】{br} / 【Miller】{br} label rows are identical to p01's.
- **Untranslated twins, which CHECK pairs once translated:**
  - 0060 ↔ NO3_NO4/0007, 0061, and NO4_BAR_T/0068 (labelled, F-013).
  - No other row of the unit recurs in any dump.
- Glossary: none.

## Unit script NO4.b01 (PR #19, MERGED, 2026-10-26)

A bundle of six whole small rooms: two bodies hacked to pieces (4001, 4102), the drop to the lower decks by wire lift (ENTRANCE), William's death and the hull rolling over (HWL_BACK 0001–0009), Judy alone in the corridor (0010–0018), and the regrouped party (HWL_BACK2). Reviewed twice:
- **Round 0** (44cd515, merged with main 74c4008 for review): CHANGES, one finding. `:15 NO4_ENTRANCE/0004` 降りられそうもない → "there's no getting down" dropped the そう hedge, and the geometry did not force it (§20.3).
- **Round 1** (0a44a5c, merged with main c035540 for review): MERGE, squash 77be2cb. `git diff 44cd515 0a44a5c` changes exactly `:15`, applying the finding's text verbatim.

Figures:
- **Containers** (MEASURE). All six rooms are complete:

  | File | Bytes | Free | Tokens | Rows |
  |---|---|---|---|---|
  | NO4_4001.SCR | 311 | 65,224 | 29 | 1/1 |
  | NO4_4101.SCR | 709 | 64,826 | 33 | 3/3 |
  | NO4_4102.SCR | 654 | 64,881 | 36 | 4/4 |
  | NO4_ENTRANCE.SCR | 1,067 | 64,468 | 38 | 5/5 |
  | NO4_HWL_BACK.SCR | 1,503 | 64,032 | 52 | 18/18 |
  | NO4_HWL_BACK2.SCR | 1,357 | 64,178 | 52 | 14/14 |

- **Pages.** At most 4 rows per page (UNITCHECK, 45 rows, 0 violations). The whole store: 868 rows, 0 violations.
- **Ratio.** 2,171 ÷ 931 = 2.33 (PR figure, round 0).
- **Duplicates.** CHECK compared 95 duplicate pairs and 7 tag-variant pairs; without the unit file it compares 83 and 7, so the unit adds 12 pairs.
  - The reviewer's census made 93,870 comparisons: 45 rows × every other dump row, at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？ dropped).
  - It found 27 hits with 0 divergences (§20.4).
- **Codes.** The authored `{p}{w}{br}` sequence is identical to the source's on all 45 rows, and the `…`/`‼`/`⁉` counts match. The unit has no `{w}` and no `──`.
- **F-011 wrap scan.** 120 wrapped lines: no lone "a"/"an"/"I", and no split title. Every authored-`{br}` line is ≤ 27 (`len()`). The one one-word row is `:23 HWL_BACK/0007` "something!" (§20.3).
- **F-012.** The only `+` rows are the sign rows, each after a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-26. Line citations use PROJECT.md §7's numbering in `tl/script/NO4.b01.tsv` (line = row order + 3).

### 20.1 Terms promoted from §9, added, and the counter frame
- **ワイヤーリフト** → `the wire lift` (13).
  - Census: 2 / 0 / 0 (NO4_ENTRANCE/0004, 0005).
  - Binds `:15 0004` "without the wire lift" and `:16 0005` "use the wire lift here".
  - Glossary: §3 row added; §9 row removed.
- **売店** (variant 売店のカウンター) → `the shop`; 売店のカウンター → `the shop counter` (8; 16).
  - Census: 2 / 0 / 0. HWL_BACK/0018 = HWL_BACK2/0014 byte for byte, and the targets are identical.
  - Binds `:34`, `:48` `The shop counter, it seems.{br}Can't see inside from here.{p}`.
  - Glossary: §2 row added; §9 row removed.
- **The 〜のカウンターのようだ frame is not made parallel** with #18's NO4_P_OFFICE/0012 両替所のカウンターのようだ。. The wave-5 seed asked for parallel wording; geometry rules it out. Each row takes the literal wording that avoids a one-word row (R §1.12 rule 1), measured with `codec.wrap(…, 28)`:
  - b01: "This seems to be the shop | counter." and "This must be the shop | counter." each orphan "counter.". "Looks like the shop counter." is 28 before an authored `{br}`. So b01 keeps `The shop counter, it seems.` (27).
  - b02: "The exchange counter, it | seems." orphans "seems.". So #18 keeps `This seems to be the exchange counter.{br}Hard to tell what's inside.{p}` ("This seems to be the | exchange counter.") unchanged.
  - Both keep the ようだ hedge and the seeded term. The sources are not duplicates, and their second sentences differ in the source (見えない vs 良くわからない).
  - Glossary: the §9 両替所 row's note is corrected to say so. #18 promotes it.
- **切り刻む · 無残に** → `hacked to pieces` · `brutally` (16 · 8), new.
  - Census: 切り刻 10 / 0 / 0, 無残 6 / 0 / 0, and the variant 無惨 1 / 0 / 0.
  - Binds:
    - `:4 4001/0001` "It's a body, brutally hacked to pieces."
    - `:8 4102/0001` "It's been hacked to pieces with what looks like a sharp blade." (鋭利な刃物, R §11.1)
    - `:11 4102/0004` "A body lies here, brutally hacked to pieces."
  - Shipped NO4_MACHINER90/0045 この無惨な殺され方 "such brutal killings" agrees.
  - Later rows take the same words: NO2_CABIN_2101/0001, 2103/0001, NO2_THIRDSTORAGE/0009, NO3_CABIN_3003/0003, NO3_CABIN_3105/0008, NO5_BANK/0008, NO6_BRIDGE/0020. 見るも無残 (NO3_MEDICALROOM/0006) is translated in context.
  - 死体が転がっている (6 / 0 / 0) → "A body lies here" is not fixed.
  - Glossary: §6 row added.
- **振動** → `tremor` (6), new.
  - Census: 5 / 0 / 0. "vibration" leaves "travels⁉" alone on a row at `:22 HWL_BACK/0006`, so the step-4 synonym is forced.
  - "tremor" fits the later rows too: NO6_HW_4/0001 先刻の振動, NO6_TOOLROOM/0003 今の振動, SPACESHIP_HW/0004 この振動. NO4_BAR_T/0177 (a developer note) is translated in context.
  - Glossary: §3 row added.
- **Conformance:** エントランスホール lowercase in dialogue at `:8`, and "Entrance Hall" on the sign. 死体 "body", 化け物 "monster", 乗客 "passengers", シャッター "shutter", 装備 "gear", 船体 "the hull", 回転 "roll over", and the deck sign as R §12.1.

### 20.2 Speakers (PR Flag 5)
- These are named from content (F-009), and every line is speaker-neutral in English.
  - 4101, 4102 and ENTRANCE (spk=0/1): Oakland or Wolg. 4101/0002 お前 to John fits Oakland. 4102/0001 is spk=- but spoken (だな).
  - HWL_BACK/0005 and 0007: Heming, as NO4_MACHINER90/0096. 0008 なんだと⁉ shares spk=5 but answers 0007.
  - HWL_BACK/0010–0018 (spk=2): Judy alone (ヤツよ, 逃げなきゃ), so 0011 and 0012 take "I".
  - HWL_BACK2/0006 そうだな answers 0005 on the same spk=5.
- Glossary: none. F-009 note added.

### 20.3 Movable codes, wraps and readings (PR Flags 2–6, 8)
- **Round-0 finding.** `:15 ENTRANCE/0004` 降りられそうもない keeps its hedge: `But from this height, it doesn't look like we can get down without the wire lift. John, would you go on ahead?{p}`, wrapping 24 / 28 / 27 / 28, 4 rows.
  - The room hedges 0002 降りられそうだ and 0003 なさそうだな. Shipped NO4_MACHINER90/0039 開きそうにない is "Doesn't look like it'll open.".
  - The round-0 "there's no getting down" stated an expectation as fact and was not forced by the page. It also left "John," at a row end apart from its question.
- **Binding `:23 HWL_BACK/0007`** (R §15.4): the first sentence reuses NO4_MACHINER90/0096's words. Each glyph follows its own source: 0007 `！` → `!`, 0096 `‼` → `‼`. "something!" is a one-word row, accepted on R §15.3's measurement of the same candidates.
- **Wording for geometry (PR Flag 3).** The reviewer confirmed none is an unforced step-5 compression:
  - 最後まで "to the last", 本当なのか "Is that true…?" and これは "It's" are equally faithful.
  - 振動 "tremor" is step 4, forced (§20.1).
  - "isn't wasted", the two sentences of 0013, "You're all right too, John?" (27), and 4102/0004's participle after the verb (ordinary order, not step 6) are all fine.
- **ヤツ = William** at `:21 HWL_BACK/0005` ヤツの意志 → "his will". The row's word is kept, and the §6 ヤツ note is extended to a named person in context. HWL_BACK/0010 and HWL_BACK2/0006 are the killer or monster → "him", as R §1.7.
- **ー not carried** at `:25 HWL_BACK/0009` 誰かなんとかしろー‼ → "Somebody do something‼".
  - Census: hiragana or kanji + ー is 2 / 1 / 0. The other two (ねー, NO4_BAR/0136, SCN046B2/06) are rough speech, not elongation, so this is the only shouted elongation.
  - The ～ row covers ～ only, and ‼ carries the shout.
- **Accepted:** 0005 ためにも → "If only so…"; 0012 外は海の中だ → "Outside is underwater." (= HWL_BACK2/0007).
- Glossary: §6 ヤツ note extended.

### 20.4 Recurrences (PR Flag 7)
- **Translated, identical:**
  - HWL_BACK/0008 `What⁉` = NO4_BAR/0245.
  - The sign HWL_BACK/0014–0017 = HWL_BACK2/0010–0013 = NO4_HWR_FRONT/0097–0100.
  - HWL_BACK/0013 = HWL_BACK2/0008 = 0009.
  - HWL_BACK/0018 = HWL_BACK2/0014.
- **Untranslated twin, which CHECK pairs once translated:** NO5_HW_R/0008 = HWL_BACK/0014 → `"Floor Information"{br}`.
- **Phrase families for later units, by hand:** 切り刻 and 無残 (§20.1); 鍵が掛かって → "This door is locked." (ENTRANCE/0001; #18 HWL_FRONT/0009 "Seems this door is locked." agrees).
- **Sibling #18 (head 0e3bb89):** NO4_SHOP/0005 "when the hull rolled over" agrees on 船体 and 回転. NO4_P_OFFICE/0012 keeps its wording (§20.1).
- Glossary: none.

## Unit script NO4.b02 (PR #18, MERGED, 2026-10-26)

A bundle of seven whole small rooms:
- HWL_FRONT: the monster's dissection, and the run when "he" shows up.
- HWL_KAIDAN: the chained stairs to Deck 3 and the barricade.
- HWR_BACK: the door they came in by.
- MACHINE: the smashed air tanks and the save point.
- P_OFFICE: the shot bodies and Wolg's reading of the killer.
- SHOP: the card key and the flashlight.
- STORAGE.

Reviewed twice:
- **Round 0** (0e3bb89, merged with main 963e300 for review): CHANGES, two findings. Both were hedges dropped where the geometry did not force it, the pattern of R §20.3 (§21.3).
- **Round 1** (f27559f, merged with main 1d0e120 for review): MERGE, squash aa4badb. `git diff 0e3bb89 f27559f` changes exactly `:43` and `:49`, applying the findings verbatim.

Figures:
- **Containers** (MEASURE). All seven rooms are complete:

  | File | Bytes | Free | Tokens | Rows |
  |---|---|---|---|---|
  | NO4_HWL_FRONT.SCR | 1,838 | 63,697 | 41 | 11/11 |
  | NO4_HWL_KAIDAN.SCR | 981 | 64,554 | 35 | 6/6 |
  | NO4_HWR_BACK.SCR | 643 | 64,892 | 33 | 2/2 |
  | NO4_MACHINE.SCR | 529 | 65,006 | 32 | 5/5 |
  | NO4_P_OFFICE.SCR | 1,507 | 64,028 | 50 | 12/12 |
  | NO4_SHOP.SCR | 787 | 64,748 | 38 | 6/6 |
  | NO4_STORAGE.SCR | 611 | 64,924 | 33 | 4/4 |

- **Pages.** At most 4 rows per page (UNITCHECK, 46 rows, 0 violations). The whole store: 914 rows, 0 violations.
- **Duplicates.** CHECK compared 99 duplicate pairs and 7 tag-variant pairs. Without the unit file it compares 95 and 7, so the unit adds 4: the save prompt, Save, Don't save, and the schedule notice.
  - The reviewer's census made 287,868 comparisons: 46 rows × every dump row, at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？ dropped).
  - It found 65 hits: 37 translated and identical, 28 untranslated, 0 divergent (§21.4).
- **Codes.** The authored `{p}{w}{br}` sequence matches the source's on 45 rows. The exception is `:35 P_OFFICE/0008`, with one `{p}` added (§21.3). The `…`/`‼`/`⁉` counts match. The unit has no `{w}` and no `──`.
- **F-011 wrap scan.** 121 wrapped lines: no lone "a"/"an"/"I". The only one-word row is the `Save` choice. Every authored-`{br}` line is ≤ 27 (`len()`).
- **F-012.** The one `+` row, `:20 KAIDAN/0006`, follows a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-26. Line citations use PROJECT.md §7's numbering in `tl/script/NO4.b02.tsv` (line = row order + 3).

### 21.1 Terms promoted from §9, and one added
- **両替所** (variant 両替所のカウンター) → `the currency exchange`; 両替所のカウンター → `the exchange counter` (21; 20).
  - Census: 1 / 0 / 0.
  - Binds `:39 P_OFFICE/0012` `This seems to be the exchange counter.{br}Hard to tell what's inside.{p}`. That is exactly the frame R §20.1 fixed: not parallel with 売店's `The shop counter, it seems.`, because each row takes the literal wording that orphans no word.
  - Glossary: §2 row added; §9 row removed.
- **カードキー** → `card key` (8). Census: 1 / 0 / 1 (NO4_SHOP/0001; items/010, blocked, F-006).
  - Binds `:40` "This body had a card key." The item name takes the same words.
  - Glossary: §3 row added; §9 row removed.
- **懐中電灯** → `flashlight` (10). Census: 1 / 0 / 1 (NO4_SHOP/0005; items/006, blocked).
  - "flashlight" over "torch" for the American setting (Philadelphia, R §1.9).
  - Binds `:44`.
  - Glossary: §3 row added; §9 row removed.
- **生存者** → `survivor(s)`, the same word as 生き残り. Census: 1 / 0 / 0.
  - Binds `:11 HWL_FRONT/0008` "there may be no survivors left…".
  - Glossary: §2 row added; §9 row removed.
- **乗組員** (variant 乗組員の制服) → `crew member(s)`, `the crew`; 乗組員の制服 → `crew uniforms`.
  - Census: 1 / 0 / 0.
  - It means the ship's own crew. The salvagers are サルベージャー.
  - Binds `:49 STORAGE/0004` "Inside are crew uniforms."
  - Glossary: §2 row added; §9 row removed.
- **チェーン** (alone) → `chain` (5), new.
  - Census: チェーン 3 / 0 / 1, of which 2 / 0 / 1 are チェーンカッター (R §11.1), so alone it is 1 / 0 / 0.
  - Binds `:16 KAIDAN/0002` "secured tight with a chain".
  - 鎖 (NO4_BAR/0422 "chains") is another word and is not fixed. A grep for 鎖 also hits 封鎖, "sealed off" at `:15`.
  - Glossary: §3 row added.
- **解剖** (R §18.1) → `the monster's dissection` at `:4 HWL_FRONT/0001`. This agrees with NO4_TOOL_ROOM/0011 "dissecting".
  - Glossary: §6 note updated (both rows shipped).
- **Conformance:**
  - 怪物 and 化け物 → "monster"; 虫 → "bugs" (R §16.1); ボンベ → "air tanks" (R §14.1); バリケード → "barricade", 撤去 → "clear" and 道具 → "a tool" (R §11.1).
  - 第３デッキ → "Deck 3"; フロア and フロアー → "floor"; 装備 → "gear"; 死体 → "body"; 乗客 → "passengers"; 人間 → "humans".
  - 船体 → "the hull" and 回転 → "rolled over", agreeing with NO4.b01; エントランスホール in lowercase; ヤツ → "he".
  - The save prompt, Save and Don't save as §4 and §6.

### 21.2 Speakers (PR Flag 4)
- These are named from content (F-009). None of the seven rooms has a `_T` draft, and every line is speaker-neutral in English.
  - HWL_FRONT/0001 is spk=- but spoken (ぞ).
  - HWL_FRONT/0002–0003 say 俺 and leave John to the dissection.
  - HWL_FRONT/0004–0006 read as Oakland, who leads the run.
  - P_OFFICE/0001–0008 read as Wolg: the ex-policeman's ballistics and his denial of the monster.
  - KAIDAN/0002 やがる → "The damn thing's", per R §13.3.
- Glossary: none. F-009 note added.

### 21.3 Movable codes, wraps and readings (PR Flags 2, 3, 5)
- **Round-0 findings, both hedges** (R §20.3's rule: a hedge stays unless the page forces it out).
  - `:49 STORAGE/0004` 使えそうな物は無いようだ.
    - Round 0 had "Nothing here looks usable.", the same English as `:24 MACHINE/0002` 使えそうな装備は何も無い, which has no ようだ.
    - The source keeps the two forms apart: plain 無い at NO2_TOFE_ROOM/0005 and NO3_MEDICALROOM/0001; 無いようだ at NO2_MAINSTORAGE/0030 and NO3_STORAGE/0002.
    - Now `There seems to be nothing that looks usable.` (wrapped 25 / 18).
    - Later rows of the family take "There seems to be nothing that looks usable" for 使えそうな物は無いようだ, and "No … looks usable" for plain 無い.
  - `:43 SHOP/0004` 特に役立ちそうな物は見当たらない.
    - Round 0 had "Nothing particularly useful is in sight.", which dropped the attributive そう.
    - Shipped NO4_BAR/0226 役に立ちそうな ("any medicine that might help") and this unit's `:10` 手がかりになりそうな ("might be a clue") both keep it.
    - Now `Nothing in sight looks particularly useful.` (22 / 20). "Nothing that looks particularly useful is in sight." orphans "sight.".
- **`{p}` added** at `:35 P_OFFICE/0008`, after "…easier for us to act, too.", a sentence boundary.
  - It is forced: without it the message wraps to 5 rows (26/26/26/27/27). It now runs 3 + 2.
  - Flagged (PR Flag 2).
- **Wording for geometry (PR Flag 3).** The reviewer confirmed that none of these is an unforced step-5 compression, and each keeps its hedge:
  - "I'm bad with bugs, you see." (でな)
  - "Seems this door is locked."
  - "There seems to be no going on without a tool to clear the barricade."
  - "A real clever one." (sarcastic 大したお利口さん)
  - "This seems to be the exchange counter." (§21.1)
- **Readings accepted (PR Flag 5):**
  - `:33 P_OFFICE/0006` 口径は９ミリ → "Nine-millimeter caliber.": a measurement spelled out per R §1.4. A caliber is not a name, as deck and cabin numbers are.
  - `:32 0005` 人間の仕業 → "the work of humans": generic, ahead of 0007's "Can't say how many".
  - `:22 HWR_BACK/0002` 浸入 → "the door we used to get into the ship": the sense of 侵入, a suspected source typo (F-024).
  - `:45 SHOP/0006` 『本日の船内イベント案内』 → `"Today's Shipboard Events," it reads.` The notice title carries 案内, and "Guide" would add nothing, so this is not a dropped fact. NO5_BANK/0005 takes the same words.
  - `:36 0009` "Both palms have holes put through them." keeps the passive.
- Glossary: none.

### 21.4 Recurrences (PR Flag 6)
- **Translated, identical:**
  - HWL_FRONT/0011 = NO4_HWR_FRONT/0101, byte for byte (R §14.1).
  - MACHINE/0001, s03 and s04 = the 12 NO4_BAR save prompts and choices.
- **Untranslated twins, which CHECK pairs once translated:**
  - HWL_FRONT/0011 = NO6_HW_1/0003 = NO6_HW_2/0006 = NO6_HW_2/0010.
  - SHOP/0006 = NO5_BANK/0005.
  - The NO3_CHAPEL save rows: 0039, 0049, 0070, 0079, 0111, 0114, 0129, 0130; s09–s35.
- **Phrase families for later units, by hand:**
  - 使えそうな物 … 無い / 無いようだ / 見当たらない(ようだ) (§21.3): NO1_CONTROLROOM/0002, NO1_STORAGE/0001, NO2_MAINSTORAGE/0030, NO2_TOFE_ROOM/0005, NO3_MACHINE/0001, NO3_MEDICALROOM/0001–0003, NO3_STORAGE/0002, NO5_BANK/0007, NO6_STORAGE/0002.
  - 銃で撃たれて死んでいる → "Shot dead with a gun." (`:37`, `:38`).
- Glossary: none.

## Unit script NO5.b01 (PR #25, MERGED, 2026-10-30)

A bundle of the seven NO5 rooms (58 rows, 1,144 source characters, tier D, ratio 29.06):
- BANK: the captured small monster, the blood web, the bodies.
- ENTRANCEL and ENTRANCEM: the flooding, the way up, the shutters.
- HW_L and HW_R: card doors, shutters, and the second deck sign.
- LOCKERROOM: the key, and the crew's "your job is Deck 6".
- SHOP: the fire extinguisher.

Reviewed once:
- **Round 0** (8d0fc61, merged with main 7be28e0 for review): MERGE, squash 4a6819e. Findings: none.

Figures:
- **Containers** (MEASURE). All seven rooms are complete:

  | File | Bytes | Free | Tokens | Rows |
  |---|---|---|---|---|
  | NO5_BANK.SCR | 1,111 | 64,424 | 40 | 9/9 |
  | NO5_ENTRANCEL.SCR | 1,585 | 63,950 | 45 | 11/11 |
  | NO5_ENTRANCEM.SCR | 1,430 | 64,105 | 42 | 12/12 |
  | NO5_HW_L.SCR | 761 | 64,774 | 33 | 5/5 |
  | NO5_HW_R.SCR | 1,172 | 64,363 | 45 | 12/12 |
  | NO5_LOCKERROOM.SCR | 843 | 64,692 | 38 | 7/7 |
  | NO5_SHOP.SCR | 495 | 65,040 | 30 | 2/2 |

- **Pages.** At most 4 rows per page (UNITCHECK, 58 rows, 0 violations). The whole store: 972 rows, 0 violations.
- **Duplicates.** CHECK compared 113 duplicate pairs and 7 tag-variant pairs. Without the unit file it compares 99 and 7, so the unit adds 14.
  - The reviewer's census made 120,988 comparisons: 58 rows × every dump row, at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？ dropped).
  - Real hits: the internal twins, BANK/0005 = NO4_SHOP/0006, and HW_R/0008 = the three shipped sign titles, all identical. The other hits are tag-only `{p}` rows matching tag-only rows, which is noise. Untranslated: ENTRANCEL/0006 = 0009 = NO6_ENTRANCE/0003.
- **Codes.** The authored `{p}{w}{br}` sequence matches the source's on 56 of 58 rows. The exceptions are `:16 ENTRANCEL/0004` and `:17 0005` (§22.3). The `…`/`‼`/`⁉` and ！/？ counts match. The unit has no `{w}` and no `──`.
- **F-011 wrap scan** (the reviewer's script, `build/script_merged.tsv`, 123 lines):
  - No lone "a", "an" or "I", and no split title.
  - Five lines end in "the", which R §1.12 rule 2 allows: BANK/0003, ENTRANCEL/0004, ENTRANCEM/0005, 0006, SHOP/0002.
  - The one one-word row is the sign entry `Bank/Cafe/Gym,`.
  - Authored-`{br}` lines are ≤ 27 (`len()`).
- **F-012.** One boundary, 0004 → 0005 (§22.3). The other eight `+` rows follow a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-30. Line citations use PROJECT.md §7's numbering in `tl/script/NO5.b01.tsv` (line = row order + 3).

### 22.1 Terms promoted from §9, three fixed sentences, and one note extended
- **Promoted as seeded** (PR Glossary additions):
  - 通信室 → `the communications room` (23), 1 / 0 / 0. `:16 ENTRANCEL/0004`. 無線室 stays "the radio room" (§9).
  - 銀行 → `a bank`; on the sign `Bank` (6; 4), 2 / 0 / 1. `:34 ENTRANCEM/0011`, `:50 HW_R/0010`.
  - 雑貨屋 → `a general store`; on the sign `General Store` (15; 13), 2 / 0 / 1. `:35 ENTRANCEM/0012`, `:49 HW_R/0009`. "General Store" (13) fits the rooms/082 cap of 14.
  - カフェ · スポーツジム → `Cafe` · `Gym` (4 · 3), 1 / 0 / 0 each. `:50 HW_R/0010`. No é (PROJECT.md §5.1). "Sports Gym" was not taken, because the row is 14 as it is.
  - ショップ → `the shop` (8), the same word as 売店, 1 / 0 / 0. `:61 SHOP/0002` "the shop's equipment".
  - 消火器 → `fire extinguisher` (17), 2 / 0 / 1. `:61 SHOP/0002`. NO6_HW_3/0003 in #22 takes the same words ("Used the fire extinguisher").
  - 浸水 → `flood / flooding / flooded`, as the line needs, 6 / 0 / 0. `:15 ENTRANCEL/0003` "The flooding's already started…⁉"; `:33 ENTRANCEM/0010` "…it's flooded." Shipped NO4_BAR/0068 has "a flood".
  - 担当 → `job` (3), 4 / 0 / 0. `:20 ENTRANCEL/0008` = `:23 0011` = `:31 ENTRANCEM/0008` "Our… job… is this floor."; `:54 LOCKERROOM/0002` "Isn't your job on Deck 6?".
  - 鍵 → `key`; the 鍵が掛か… / 鍵がかか… / 鍵がかけ… phrases → `locked`. Census: 26 / 0 / 5 (掛か 13, かか 5, かけ 1). `:56 LOCKERROOM/0004` "Found a key placed inside the locker."; `:44 HW_R/0004` "The door is locked". This agrees with shipped NO4_ENTRANCE/0001 and NO4_HWL_FRONT/0009.
  - Glossary: rows added to §2 (通信室, 銀行, 雑貨屋, カフェ · スポーツジム, ショップ), §3 (消火器, 鍵, 浸水) and §6 (担当). The §9 rows were removed.
- **Fixed sentences.**
  - **どうやらここから上に昇れそうだ。{p}** → `It looks like there's a way up from here.{p}` (41; wrapped 27 / 13). そう is kept as "looks like". Census 3 / 0 / 0: `:18 ENTRANCEL/0006` = `:21 0009` = NO6_ENTRANCE/0003, which is identical in #23 at 8ecdb7e. Promoted from §9 to §6.
  - **シャッターで封鎖されて、先に進めそうにない。{p}**, with the variant **シャッターで封鎖され、先に進めそうにない。{p}** → `A shutter has sealed it off. There seems to be no going any further.{p}` (68; wrapped 28 / 26 / 12).
    - The wave 6 seed, `It's sealed off by a shutter. …`, wrapped "It's sealed off by a | shutter.", a lone "a" (R §1.12 rule 2). The coordinator replaced it before review (HANDOFF → Decisions), and this is that replacement.
    - そう is kept as "There seems to be".
    - Census 6 / 0 / 0. され、: `:38 HW_L/0003`, `:40 0005`, `:47 HW_R/0007`. されて、: NO6_HW_1/0001–0002 (#23 at 8ecdb7e) and NO6_HW_5/0005 (#22 at a2a5ade), identical byte for byte.
    - CHECK cannot pair the two spellings, so the glossary row lists both.
    - Promoted from §9 to §6.
  - **シャッターで閉ざされて先には進めない。{p}** → `A shutter closes off the way. No going any further.{p}` (51; wrapped 24 / 26). New.
    - The source has no hedge, so the target has none, and it is kept apart from the hedged 封鎖 sentence.
    - "It's closed off by a shutter." strands "a" at the wrap.
    - Census 2 / 0 / 0: `:28 ENTRANCEM/0005` = `:29 0006`.
    - The plain シャッターが下りていて先には進めない (NO2_HW_5/0003) may reuse "No going any further."; NO3_NO4/0055 そうに無い is hedged.
    - Glossary: §6 row added.
- **§9 rows corrected, not yet rendered on main.** The coordinator's wave 6 replacements for the remaining seeded sentences are now the §9 text: 鍵が掛かっていて、扉は開かない。{p} → `It's locked, so the door won't open.{p}`; 水かさ…増えつづけてる…。{w}{br}急がないと…危険よ…。{p} → `The water… it keeps rising…{w}{br}Must hurry… it's dangerous…{p}`; 水が深すぎて…息が…でき…な…{p} → `The water's too deep… can't… brea… the…{p}`. These match #22 and #23 as they stand. They stay PROVISIONAL until one of those PRs merges. No shipped line is affected.
- **と書かれている** (§6, R §12.1): the note is extended for the row-alone case, with no target changed. The sign is NO5_HW_R/0008–0011:
  ```
  "Floor Information"{br}
  Entrance Hall/General Store{br}
  Bank/Cafe/Gym,{br}
  it reads.{p}
  ```
  - The rows measure 19, 27, 14 and 9, a 4-row page.
  - The title is NO4_HWR_FRONT/0097 byte for byte. The entries are joined by an unspaced "/". The indent is dropped (F-022).
  - The source gives と書かれている its own row, so R §12.1's `«last entry», it reads.` is carried across the source's own split. No text moves between messages.
  - No shipped line is affected.

### 22.2 Speakers (PR Flag 9)
- Judy (わ/よ, halting …) speaks BANK/0001–0003, ENTRANCEL/0007–0008 and 0010–0011, ENTRANCEM/0001–0002 and 0007–0010, HW_L/0001–0002, HW_R/0001–0003 and 0006, LOCKERROOM/0001, and SHOP/0001. ENTRANCEL/0007 borrows spk=1 (F-009).
- The party leader (ジョン, 急ごう, 始まらんがな) speaks ENTRANCEL/0001–0005 and ENTRANCEM/0003–0004, read as Oakland. The English is neutral.
- LOCKERROOM/0002–0003 (俺たち / お前たち to John) is one of Oakland's crew, or Oakland. The English is neutral.
- The rest is narration.

### 22.3 Movable codes, wraps and readings (PR Flags 2, 5–8, 10, 11)
- **`{p}` added** at `:16 ENTRANCEL/0004`, after "…at the very top.", at a sentence boundary. It is forced: without it the page runs 7 rows. The message now runs 4 + 2, and 0005's leading `{br}` row makes the second page 3.
- **Leading `{br}`** at `:17 ENTRANCEL/0005`, on the F-012 boundary after the untagged 0004 (R §2.3).
  - The source splits one sentence mid-clause (下へ下へと向かえば / たどり着けるはずだ). The `{br}` falls between the conditional and the main clause: "…if we keep heading down," / "we should reach it.".
  - 寄り道せずについて来いよ reuses NO4_HWR_FRONT/0142 付いて "Follow me, and no detours." byte for byte (PR Flag 4). 付いて and ついて are spelling variants, and CHECK does not pair them. HANDOFF's pointer, which read NO4_BAR/0142, was corrected by the coordinator.
- **Hedges** (wave 5's lesson, R §20.3). Every hedge is kept:
  - のだろうか: BANK/0006 "I wonder", SHOP/0002 "Could it have been".
  - 使えそうな: BANK/0007 "looks usable".
  - なりそう: ENTRANCEL/0003 "it looks like".
  - だろう: ENTRANCEL/0004 "probably". はず: 0005 "should".
  - ようだが + そうにない: ENTRANCEM/0011–0012 "seems … doesn't look like".
  - ようだ: HW_L/0004 = HW_R/0005 "It seems". そうにない: HW_R/0004 "looks impossible to open".
  - なさそう: LOCKERROOM/0001 = SHOP/0001 "doesn't seem". 空のようだ: LOCKERROOM/0005–0006 "seems empty". 役に立ちそうに無い: LOCKERROOM/0007 "don't look useful".
- **The 使えそうな物 family** (R §21.4): BANK/0007 見当たらない → "There's nothing else in sight that looks usable." It sits beside #22's NO6_STORAGE/0002 見当たらないようだ, "There seems to be nothing in sight that looks usable.", and shipped NO4_STORAGE/0004 無いようだ, "There seems to be nothing that looks usable.". The forms stay apart as the sources do.
- **Wording chosen for wraps** (PR Flag 7). None of these is a step-5 compression, and nothing is dropped. "we captured", "it's eerie……", "Found a key placed inside the locker.", "spare clothes" (着替え), "it looks impossible to open", "Now the ship's upside down" (今 / 反転).
- **Readings accepted:**
  - BANK/0008 "It has been brutally hacked to pieces." and 0009 "It's dead, with both its legs severed." take "It" for the examined body. The shipped fragments ("Shot dead between the eyes.", NO4_P_OFFICE/0009) are subjectless, but "Dead, with both legs severed." leaves "severed." alone on a row.
  - ENTRANCEL/0001 大事 (おおごと) → "a big deal". ENTRANCEM/0004 愚痴 → "griping", as shipped NO4_BAR/0137 愚痴る "quit griping". SCN002A/07 愚痴を言っても始まらん "There's no use complaining." is a different sentence and is not bound.
  - PR Flag 8 says まったく → "Honestly," is "as shipped", which is inexact: NO4_BAR/0017 is Collison's "Really,". まったく is not fixed, and the speaker differs. Accepted.
  - ENTRANCEL/0008 against LOCKERROOM/0002: the alternative scripts for different story states are each translated as written (PR Flag 11).
- **Suspected source typos** (PR Flag 10, F-025): `:14 ENTRANCEL/0002` 後回した for 後回しだ → "can wait"; `:12 BANK/0009` 啄ばまれた後 for 跡 → "peck marks". 1 / 0 / 0 each.
- Glossary: none beyond §22.1.

### 22.4 Recurrences (PR Flag 12)
- **Translated, identical:** BANK/0005 = NO4_SHOP/0006; HW_R/0008 = NO4_HWR_FRONT/0097 = NO4_HWL_BACK/0014 = NO4_HWL_BACK2/0010. Internal: ENTRANCEL/0006 = 0009; 0007 = 0010 = ENTRANCEM/0007; 0008 = 0011 = ENTRANCEM/0008; ENTRANCEM/0005 = 0006; HW_L/0001 = HW_R/0002; HW_L/0002 = HW_R/0003; HW_L/0003 = 0005 = HW_R/0007; HW_L/0004 = HW_R/0005; LOCKERROOM/0001 = SHOP/0001.
- **Untranslated twins:** ENTRANCEL/0006 = NO6_ENTRANCE/0003 (#23). The 封鎖 variant at NO6_HW_1/0001–0002 (#23) and NO6_HW_5/0005 (#22) is not paired by CHECK (§22.1).
- **Families for later units, by hand:**
  - 扉が歪んで: HW_R/0012 "The door is warped and can't be opened."; NO6_BRIDGE/0011 (#23 "The water pressure has warped the door, so it can't be opened."); NO3_CABIN_3106/0001 らしく … そうにない, hedged.
  - …危険よ: NO6_HW_4/0002, SPACESHIP_HW/0005.
  - シャッターが下りていて: NO2_HW_5/0003 (plain), NO3_NO4/0055 (そうに無い).
- Glossary: none.

## Unit script NO6.b01 (PR #23, MERGED, 2026-10-30)

A bundle of four NO6 rooms (37 rows, 839 source characters, tier D, ratio 39.03):
- BRIDGE: the locked radio room, the key, the shutter lock on Deck 5, the control panel, a body.
- ENTRANCE: Judy's flooding lines, the way up, Deck 6 ahead.
- HW_1 and HW_2: the sealing shutters, the shipboard-events schedule, locked and pressure-held doors.

Reviewed once:
- **Round 0** (8ecdb7e, merged with main c650d6d for review): MERGE, squash 388bb77. Findings: none.

Figures:
- **Containers** (MEASURE). All four rooms are complete:

  | File | Bytes | Free | Tokens | Rows |
  |---|---|---|---|---|
  | NO6_BRIDGE.SCR | 2,135 | 63,400 | 49 | 20/20 |
  | NO6_ENTRANCE.SCR | 622 | 64,913 | 33 | 4/4 |
  | NO6_HW_1.SCR | 513 | 65,022 | 28 | 3/3 |
  | NO6_HW_2.SCR | 1,293 | 64,242 | 37 | 10/10 |

- **Pages.** At most 4 rows per page (UNITCHECK, 37 rows, 0 violations). The whole store: 1,009 rows, 0 violations.
- **Duplicates.** CHECK compared 122 duplicate pairs and 7 tag-variant pairs. Without the unit file it compares 113 and 7, so the unit adds 9.
  - The reviewer's census made 77,182 comparisons: 37 rows × every dump row, at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final 。！？… dropped), against `tl/` on main plus #22 (a2a5ade) and #24 (12556a0). 50 hits, all translated and byte-identical.
- **Codes.** The authored `{p}{w}{br}` sequence matches the source's on 36 of 37 rows; the exception is `:5 BRIDGE/0002` (§23.2). The `…`/`‼`/`⁉`/`──` counts match on all 37.
- **F-011 wrap scan** (the reviewer's script, `build/script_merged.tsv`, 89 lines, plant-tested): no lone "a", "an" or "I", no one-word last row, no split title or "Deck | N". `:17 BRIDGE/0014` ends a row in "The", which R §1.12 rule 2 allows. Authored-`{br}`/`{w}` lines ≤ 27 (`len()`): 24, 14, 21, 26, 27, 27.
- **F-012.** One boundary, BRIDGE/0001 → 0002 (§23.2). The `+` rows 0015 and 0017 follow `{br}` endings.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-30. Line citations use PROJECT.md §7's numbering in `tl/script/NO6.b01.tsv` (line = row order + 3).

### 23.1 Terms promoted from §9, two new terms, four fixed sentences, one variant added
- **Promoted as seeded** (PR Glossary additions):
  - 無線室 → `the radio room`; room name `Radio Room` (14; 10), 2 / 0 / 4. `:4 BRIDGE/0001`, `:9 0006`. rooms/107 (cap 14), items/011, hints/001–002 are blocked (F-006). 通信室 stays "the communications room" (R §22.1). §2 row.
  - 水圧 → `the water pressure` (18), 7 / 0 / 0. `:14 BRIDGE/0011` "The water pressure has warped the door, so it can't be opened."; the fixed sentence below. NO4_BAR_T/0105 気圧と水圧 in context. §3 row.
  - 親父 → `your dad` (8), 2 / 0 / 0. `:11 BRIDGE/0008` "He'll make a fuss if we're late, your dad." keeps the source's postposed お前の親父は. NO3_NO4/0043 俺はお前の親父に雇われた takes the same words. Never "old man", which is じいさん (Collison). §6 row.
  - シャッターロック → `the shutter lock` (16), 1 / 0 / 0. `:17 BRIDGE/0014`. §3 row.
  - 航海のスケジュール → `the voyage schedule` (19), 1 / 0 / 0. `:13 BRIDGE/0010`. §6 row.
  - 水かさ → `the water (rising)` (9), 4 / 0 / 0, only inside the fixed sentence. §6 row.
- **New terms:**
  - 操作パネル → `control panel` (13); 防水シャッターの操作パネルがある → `There's a control panel for the watertight shutters.` (52). Census 5 / 0 / 0: `:15 BRIDGE/0012`; NO3_MACHINE/0004 opens with the identical sentence 防水シャッターの操作パネルがある。{br}, which CHECK does not pair (the second sentences differ), and must reuse the English byte for byte; NO3_MACHINE/0002 のようだ takes the same words hedged; NO3_FOODSTORAGE/0011, NO2_SUBSTORAGE/0005 in context. §3 row.
  - 舵 → `the ship's wheel` (16). Census 3 / 0 / 0, of which 2 are 操舵室 (NO4_BAR/0428, 0437, "the wheelhouse"); 舵 alone 1, `:16 BRIDGE/0013`. §3 row.
- **鍵 row, variant added** (a change to an existing row, written out here): NO6_BRIDGE/0001 鍵が締まっている is a fourth spelling of the "locked" phrase (締ま 1 / 0 / 0, already inside the row's 26 / 0 / 5). `:4` renders it "it seems to be locked". The row's Variants and note gain 鍵が締まって; its target is unchanged; no shipped line is affected. Also bound: `:9` "without a key", `:10` "So you found the key.", `:12 BRIDGE/0009` 扉には鍵がかかっている → "The door is locked." (shipped NO4_ENTRANCE/0001 この扉は… "This door is locked." agrees).
- **Fixed sentences promoted from §9 to §6** (the coordinator's wave 6 replacements, R §22.1; #22 at a2a5ade identical byte for byte):
  - 水かさ…増えつづけてる…。{w}{br}急がないと…危険よ…。{p} → `The water… it keeps rising…{w}{br}Must hurry… it's dangerous…{p}` (27 / 27). 4 / 0 / 0: `:24 ENTRANCE/0001` = `:31 HW_2/0001` = NO6_HW_4/0003 = NO6_HW_5/0001. Four … each side; the 。 after each … absorbed (R §1.3).
  - 水が深すぎて…息が…でき…な…{p} → `The water's too deep… can't… brea… the…{p}` (39; wrapped 28 / 10). 4 / 0 / 0: `:25 ENTRANCE/0002` = `:32 HW_2/0002` = NO6_HW_4/0004 = NO6_HW_5/0002. The source breaks できない across the gasps; the English breaks "breathe", and the subject of "can't" is implied (step 5, the coordinator's form, flagged). The seed's "I" stranded at a wrap.
  - 鍵が掛かっていて、扉は開かない。{p} → `It's locked, so the door won't open.{p}` (36; 24 / 11). 7 / 0 / 0: `:35 HW_2/0005` = `:37 0007` = NO6_HW_3/0005–0007, NO6_HW_4/0005, 0008. Unhedged as the source. 扉は鍵が掛かっていて開きそうに無い (NO3_HW_1/0005–6, NO3_HW_2/0002–3, 4 / 0 / 0) is a different, hedged sentence and keeps its そう.
  - 水圧で扉を開けられない。{p} → `The water pressure won't let the door open.{p}` (43; 28 / 14), unchanged from the seed. 5 / 0 / 0: `:38 HW_2/0008` = `:39 0009` = NO6_HW_4/0006–0007, NO6_HW_5/0004.
- Glossary: rows added to §2 (無線室), §3 (水圧, シャッターロック, 操作パネル, 舵) and §6 (親父, 航海のスケジュール, 水かさ, the four sentences); §3 鍵 variant added as above; the eight §9 rows removed. 教会 and 拠点 stay in §9 for NO3_CHAPEL.

### 23.2 Movable codes (PR Flag 2)
- **Leading `{p}`** at `:5 BRIDGE/0002`, a `+` row after the untagged 0001. 0001 ("…but it seems to be locked.", 68) and 0002 (52) cannot share a 4-row page in any wording that keeps この扉の向こう, らしい and ようだ; without the click the page runs 7 rows. With it, 3 + 3.
  - The click falls at the sentence boundary, and because `{p}` clears the box it also closes the F-012 glue boundary (R §2.3), so no leading `{br}` is needed.
  - This extends R §2.4 (a leading `{p}` on a `+` row after a `{br}` ending) to a `+` row after an untagged ending. Added to F-010's in-game check.
- No `{br}` moved, added or removed by hand; `{w}` untouched.

### 23.3 Departures, speakers, readings (PR Flags 3, 5, 6)
- **`:23 BRIDGE/0020`** 鋭利な刃物のようなもので切り刻まれている → `Something like a sharp blade has hacked it to pieces.{p}` (28 / 24). Active reorder, step 6, flagged; approved. Every passive wording strands "blade." on the last row ("It's been hacked to pieces with something like a sharp | blade."). Parity with shipped NO4_4102/0001 ("…with what looks like a sharp blade.") is not required: the sources differ (のようなもの vs らしき物) and are not a pair. The hedge and the glossary words (R §11.1, §20.1) are kept.
- **`:15 BRIDGE/0012`** 操作できない → "inoperable", step 4, forced: "…are broken and can't be operated." makes the page 5 rows.
- **Hedges** (wave 5's lesson, R §20.3), all kept: らしい "apparently" + ようだ "it seems" (`:4`); そうにない "Doesn't look like" (`:9`); のようなもの "Something like" (`:23`); どうやら…そう "It looks like" (`:26`); ようだ "seems" (`:27`); そうにない "There seems to be no going" (`:28`–`:29`). 一応 "Just in case", とやら "so-called", にも "too" (`:21`).
- **Speakers** (F-009). BRIDGE 0001–0008, 0014–0018 and HW_2/0003–0004 are one of Oakland's crew addressing John (俺, お前の親父, やりきれん, ならん) — plausibly Heming, but unnamed; the English is speaker-neutral. 0015 解除してみるか？ "Shall we try releasing it?" is his question, answered by his own 0016. BRIDGE 0009–0013, 0019–0020 and HW_2/0005–0010 are narration despite spk=0/1. The … lines are Judy (よ).
- **Readings accepted:** ん？ "Hm?"; やりきれん "hard to bear"; 記載されている "is written here"; 首が切断 "The head has been severed."; 恐怖の形相で朽ち果てている "has rotted away, frozen in a look of terror"; 動かしても "when you turn it" (the wheel).
- Wording chosen for wraps, all literal (PR Flag 3): 0008 postposed "your dad", 0017 "Deck 5, John" (no "Deck | 5"), ENTRANCE/0004 "Deck 6 seems to be up ahead." (28, a wrapped line), HW_2/0003 "a pretty complicated layout", HW_2/0004 "Follow me so you don't lose your way."
- Glossary: none beyond §23.1.

### 23.4 Recurrences (PR Flag 7)
- **Translated, identical:** HW_1/0003 = HW_2/0006 = 0010 = NO4_HWL_FRONT/0011 = NO4_HWR_FRONT/0101; ENTRANCE/0003 = NO5_ENTRANCEL/0006 = 0009; HW_1/0001–0002 = NO5_HW_L/0003, 0005, NO5_HW_R/0007 (the され、 variant).
- **#22 (NO6.b02, a2a5ade), identical:** the four sentences of §23.1 and the 封鎖 sentence at NO6_HW_5/0005.
- **Families for later units, by hand:** NO3_MACHINE/0004 first sentence = `:15`'s (§23.1); NO3_MACHINE/0002 hedged; 扉は鍵が掛かっていて開きそうに無い (NO3_HW_1, NO3_HW_2), hedged, kept apart from `:35`.
- Glossary: none.

## Unit script NO6.b02 (PR #22, MERGED, 2026-10-30)

A bundle of six NO6 rooms (27 rows, 495 source characters, tier D, ratio 66.38):
- HW_3: the fuel fire, the fire extinguisher, the locked doors.
- HW_4 and HW_5: Judy's flooding lines, and the doors held by water pressure, a lock or a shutter.
- STORAGE: instruments, toppled shelves.
- TOOLROOM: the chain cutter, a tremor, "let's go back".
- WIRELESSROOM: radio equipment that cannot reach the surface.

Reviewed once:
- **Round 0** (a2a5ade, merged with main 0b71bed for review): MERGE, squash 47b3edc. Findings: none.
- The head already carried the coordinator's wave 6 replacements for the seeded sentences (PR Flag 3, R §22.1, §23.1).

Figures:
- **Containers** (MEASURE). All six rooms are complete:

  | File | Bytes | Free | Tokens | Rows |
  |---|---|---|---|---|
  | NO6_HW_3.SCR | 963 | 64,572 | 36 | 7/7 |
  | NO6_HW_4.SCR | 813 | 64,722 | 36 | 8/8 |
  | NO6_HW_5.SCR | 648 | 64,887 | 31 | 5/5 |
  | NO6_STORAGE.SCR | 465 | 65,070 | 28 | 2/2 |
  | NO6_TOOLROOM.SCR | 517 | 65,018 | 38 | 4/4 |
  | NO6_WIRELESSROOM.SCR | 393 | 65,142 | 29 | 1/1 |

- **Pages.** At most 4 rows per page (UNITCHECK, 27 rows, 0 violations). The whole store: 1,036 rows, 0 violations.
- **Duplicates.** CHECK compared 135 duplicate pairs and 7 tag-variant pairs. Without the unit file it compares 122 and 7, so the unit adds 13.
  - The reviewer's census compared 27 rows × every dump row, `{p}{w}{br}` stripped: 56 translated pairs, all byte-identical, and no untranslated twin.
  - The 封鎖 sentence in both spellings (R §22.1): 6 / 0 / 0, identical.
- **Codes.** The authored `{p}{w}{br}` sequence and the `…`/`‼`/`⁉`/`──`/！/？ counts match the source on 27 of 27 rows (plant-tested script).
- **F-011 wrap scan** (the reviewer's script, `build/script_merged.tsv`, 60 lines, plant-tested): no lone "a", "an" or "I", no one-word last row, no split title. Authored-`{br}`/`{w}` lines ≤ 27 (`len()`).
- **F-012.** The one `+` row, TOOLROOM/0004, follows a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-30. Line citations use PROJECT.md §7's numbering in `tl/script/NO6.b02.tsv` (line = row order + 3).

### 24.1 Terms: nothing new; two notes extended
- **Rendered as fixed** (all already in the glossary; no §9 row is rendered here):
  - 消火器 `fire extinguisher`, 2 / 0 / 1: `:6 HW_3/0003`. Promoted at #25 (R §22.1).
  - 浸水 `flooding`, 6 / 0 / 0: `:11 HW_4/0001` "It's flooding…".
  - 振動 `tremor`, 5 / 0 / 0: `:11` 先刻の振動 "that tremor earlier", and `:28 TOOLROOM/0003` 今の振動 "That tremor just now". The sources differ, so the renderings differ around the fixed word.
  - チェーンカッター `chain cutter`, 2 / 0 / 1: `:26 TOOLROOM/0001`.
  - 回転 `roll over`: `:28`, with "the ship" supplied as the subject.
  - 無線装置 `radio equipment`, 海上 `the surface`: `:30 WIRELESSROOM/0001`.
  - The five §6 fixed sentences (R §22.1, §23.1): `:8–10`, `:15`, `:18` (鍵); `:13`, `:19` (水かさ); `:14`, `:20` (水が深すぎて); `:16–17`, `:22` (水圧); `:23` (封鎖).
- **Conformance with shipped lines, not fixed terms:**
  - 棚が倒れて `The shelves have toppled` (`:25`) matches NO4_SHOP/0004. 棚 is 4 / 0 / 0.
  - 廊下 `corridor` (`:4`) matches NO4_BAR/0058 and 0196. 廊下 is 5 / 0 / 16, and the system rows are room names (F-006).
  - 連絡 → "reach" (`:30`) follows NO4_HWR_FRONT/0006 "reaching the people up top". 連絡 is 6 / 0 / 0.
- **Not fixed**, because each occurs once in the source: 水流 "current", 計器類 "instruments", 燃料 "fuel" (2 / 0 / 0; NO3_CHAPEL/0126 in context), パイプ "pipe" (6 / 0 / 0; NO2_HW_3/0001–0005 in context).
- Glossary: notes extended, with no target changed and no shipped line affected:
  - §3 浸水: NO6_HW_4/0001 added.
  - §3 チェーンカッター: NO6_TOOLROOM/0001's wording added.

### 24.2 Readings and departures (PR Flags 4–8)
- **`:26 TOOLROOM/0001`** これは、チェーンカッターのようだ。 → `A chain cutter, it seems.{p}` (25), approved (PR Flag 5).
  - これは points at the examined item, and context carries it (step 5, flagged). This is R §20.1's frame for 売店のカウンターのようだ.
  - Measured with `codec.wrap(…, 28)`, every wording that keeps "This" or "It's" leaves "cutter." or "seems." alone on a row, or ends a row in "a" (R §1.12 rule 1). The reviewer re-measured each of these wordings: "This seems to be a chain cutter.", "This appears to be…", "This is a chain cutter, it seems.", "It's a chain cutter, it seems.", "This, it seems, is a chain cutter.", "It seems that this is a…".
  - "This seems a chain cutter." (26) was rejected. English seem + a bare noun phrase is evaluative ("seems a shame"), not identifying.
  - The ようだ hedge and the glossary term are kept.
- **`:6 HW_3/0003`, `:7 0004`**: the sources have no 。, so the targets have no period (R §4.3, PR Flag 4).
  - "Used the fire extinguisher" is subjectless as the source. "You used…" wraps "extinguisher" alone, so this is step 5, flagged.
  - みるみる → "before your eyes".
- **`:27 TOOLROOM/0002`** そう…戻りましょうか…。 → `I see… Shall we go back…`, with no "?". The source has no ？ (PROJECT.md §6), and the 。 after … is absorbed (R §1.3). The opposite case is R §13.3, where かしら？ keeps its ？. `:28` かしら…？ keeps "?".
- **Hedges** (wave 5's lesson, R §20.3), all kept:
  - ようだ: `:4` "seems to have caught fire"; `:26` "it seems"; `:30` "appears" + "it seems" (both ようだ).
  - そう: `:23` "There seems to be".
  - The 使えそうな物 family (R §21.3–§21.4): `:25` 見当たらないようだ → "There seems to be nothing in sight that looks usable." This sits beside NO5_BANK/0007 (plain 見当たらない) and NO4_STORAGE/0004 (無いようだ), each as its source.
  - `:24` 見た目には is a limiter, "To all appearances".
- **Wording measured, accepted:**
  - `:30`: "It appears to be working normally" makes the page 5 rows. "contact the surface" (28) fits, but "reach" stays, as shipped 連絡.
  - `:21` "The current is too strong to go any further." keeps the causal て as an ordinary too…to frame.
  - `:28` また… keeps its own halting slot, "Again…".
  - `:12` follows the source's … positions: "This place is… dangerous.{br}…Let's hurry."
- **Speakers** (F-009):
  - Judy: HW_4/0001–0004, HW_5/0001–0002 (spk=-, the fixed lines), and TOOLROOM/0002–0004 (ましょう, かしら; spk=- and 100).
  - Narration: HW_3/0001–0007 (spk=0) and HW_4/0005–0008 (spk=100).
  - The English is speaker-neutral.
- Glossary: none beyond §24.1.

### 24.3 Recurrences (PR Flag 9)
- **Translated, identical:**
  - The four §23.1 sentences across NO6_ENTRANCE, NO6_HW_2, HW_3, HW_4 and HW_5.
  - The 封鎖 sentence at HW_5/0005 = NO6_HW_1/0001–0002, and its され、 variant at NO5_HW_L/0003, 0005, NO5_HW_R/0007.
- **Families for later units, by hand:**
  - ここは危険よ！{br}急ぎましょう。 (SPACESHIP_HW/0005) may take `:12`'s "Let's hurry".
  - …戻りましょう (NO1_ENGINEROOM/0003) may take "let's go back" (`:29`; NO5_BANK/0003, NO5_HW_L/0002).
  - 扉は鍵が掛かっていて開きそうに無い (NO3_HW_1/0005–0006, NO3_HW_2/0002–0003) is hedged, and stays apart from `:8` (R §23.1).
  - 正常に動いているようだ (NO1_CONTROLROOM/0003) sits beside shipped NO4_MACHINE/0003 "seems to be running normally" and `:30`.
- Glossary: none.

## Unit script NO3_CHAPEL.p01 (PR #24, MERGED, 2026-10-30)

The first part of the chapel room (62 rows, 1,068 source characters, tier D, ratio 27.82):
- 0001–0011: Judy finds the chapel and asks John why William saved them.
- 0012–0038: the survivors (Wolg, Oakland, Heming, Judy) argue over making the chapel their base and who searches.
- 0039–0044: the save prompt and the talk-to lines that follow.
- The 16 save choices, and s28/s29, the engine vote.

Reviewed once:
- **Round 0** (12556a0, merged with main 5204c25 for review): MERGE, squash 6fe71ae. Findings: none.

Figures:
- **Container.** NO3_CHAPEL.SCR 9,559 / 65,535 bytes, 55,976 free, 364 tokens, 62/150 rows (MEASURE). Untranslated it had 57,297 free. p02/p03 share the file.
- **Pages.** At most 4 rows per page (UNITCHECK, 62 rows, 0 violations). The whole store: 1,098 rows, 0 violations.
- **Duplicates.** CHECK compared 152 duplicate pairs and 7 tag-variant pairs, against main's 135 and 7.
  - The +17 are 0039 joining the save-prompt group and the 16 Save / Don't save rows.
  - The reviewer's census: 129,332 comparisons (62 rows × every dump row), at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final punctuation dropped). It found 340 hits: 333 identical, 7 untranslated, 0 divergent.
  - Only 0039 and the s-rows recur.
- **Codes.** The authored `{p}{w}{br}` sequence differs from the source on 1 of 62 rows, `:37 0034` (PR Flag 2). The `…`/`‼`/`⁉`/`──` counts match on 62 of 62 (plant-tested script).
- **F-011 wrap scan** (the reviewer's script, `build/script_merged.tsv`, 99 lines, proved on 5 planted violations first): no lone "a", "an" or "I", no one-word continuation row, no split title. Authored-`{br}` lines ≤ 27 (`len()`; 0024 and 0038 at 27).
- **F-012.** Three `+` rows, 0005, 0042 and 0044, each after a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-30. Line citations use PROJECT.md §7's numbering in `tl/script/NO3_CHAPEL.p01.tsv` (line = row order + 3).

### 25.1 Terms promoted from §9, and one choice pair added
- **教会** → `the chapel`; `a chapel` at the discovery; room name `Chapel` (10; 8; 6). Cap 14 (rooms/040, blocked).
  - Census: 3 / 0 / 2. Rows: NO3_CHAPEL/0001; NO3_HW_1/0001 = NO3_NO4/0011 (…教会くらいね, untranslated); rooms/040, hints/013 (blocked, F-006).
  - `:4 0001` ここは…教会ね。{br}船の中にこんなに立派な教会があるなんて… → `This is… a chapel.{br}To think there's such a fine chapel inside a ship…`.
  - Judy is discovering the room, and the second clause marvels that a ship has one at all, so the indefinite article is right (PR Flag 5). NO3_NO4/0011 comes after she has seen it, so the default stays "the chapel".
  - "church" (the §9 alternative) is rejected: a room aboard a liner is a chapel.
  - Glossary: §2 row added; §9 row removed.
- **拠点** → `base` (4).
  - Census: 4 / 0 / 0. Rows: `:15 0012` ここを新たな拠点として → "We'll make this our new base"; NO3_NO4/0001 新しい拠点を探してくる and NO3_HW_1/0001 = NO3_NO4/0011 新しい拠点になりそうなのは (untranslated) take "a new base".
  - "base of operations" (the §9 alternative) is rejected: it is too long for these lines and adds nothing.
  - Glossary: §2 row added; §9 row removed.
- **握る · 握らない** (choice) → `Hold the round` · `Don't hold it` (14 · 13). Cap 27. New.
  - Census: 握 3 / 0 / 0: NO3_CHAPEL/0122, s28, s29.
  - These are the engine vote, not a handshake (the dispatch's guess). Three things show it:
    - 0122 (spk=2, Wolg per R §13.2) sets it up: 全員アモを一発取り出せ。{br}機関を止めることに賛成なら、右手に握れ。{br}イヤならなにも持つな。
    - The choice sits between the 0114 and 0129 save pairs.
    - 0123 ジョン以外は全員賛成か…… records the result.
  - "the round" is the one round of ammo 0122 asks for. 握らない is the empty hand (なにも持つな).
  - **Binds p02/p03:** 0122 must say "take out one round" … "hold it in your right hand" (or equivalent with "round" and "right hand"), in line with these choices and with the SCN046 subtitles `When you're ready, raise your right hand.` / `Open your hand.` (R §13.2, §13.4).
  - Glossary: §4 row added.
- **Applied, unchanged:**
  - Heming, Judy, John, William; 化け物 → monster (`:38`); 生き残り → survivors (`:15`, `:31`, `:43`, `:44`); 装備 → gear (`:29`); 上の連中 → the people up top (`:20`).
  - 人間たち → "people" (`:7`, the 人間 row's general use).
  - 虫かご → "a bug cage" (`:26`, in context per the §6 虫 note).
  - The save prompt (`:42`) and Save / Don't save (`:48–59`, `:62–65`).
- **Not fixed**, each once in the source: 秩序 "the order" (1 / 0 / 0), ダダ "tantrums" (1 / 0 / 0), 錯乱 "deranged" (3 / 0 / 0; NO4_BAR/0304 "lose your head" and NO3_CHAPEL/0052 in context), 食料 "food" (as shipped).
- **§9 is now empty.** These were the last wave 6 rows.

### 25.2 Speakers (PR Flag 3)
- **William is dead by this scene.** 0007 彼は他人のために、自分を犠牲にした is past tense, after NO4_HWL_BACK (R §20). The dispatch's suggestion that he speaks in 0012–0038 was wrong, and the translator corrected it.
- **Named from content** (F-009; spk=4 carries Wolg and Oakland, spk=2 Heming, Wolg and Judy, spk=5 Oakland or Wolg):
  - Wolg plans: 0012–0014, 0030 まず俺とジョンで行く, 0032 あんたのダダ.
  - Oakland is the frightened boss: 0015, 0023, 0025, 0031 (holding Wolg back), 0033.
  - Heming offers to go at 0035 and is addressed at 0036.
  - Judy: 0001–0011, 0034.
  - These stay uncertain: 0016–0017 (Wolg or Heming), 0018, 0020, 0022, 0026–0028, 0036 (Oakland assigning jobs, or Wolg), 0037 and 0038.
- Every line is speaker-neutral in English, so a corrected attribution changes no text.
- Glossary: none.

### 25.3 Movable codes and readings (PR Flags 2, 6, 7, 10)
- **`:37 0034`** `{br}` → `{br}{br}`: a `{br}` is added after "John and I will go." so いいでしょ…… takes its own row (`That's fine, isn't it……`) and does not wrap "That's | fine". The page is 3 rows. Approved.
- **Hedges** (wave 5's lesson, R §20.3), all kept:
  - `:20 0017` んだろう → "must".
  - `:22 0019` ありそうな気がする → "I have a feeling … may".
  - `:24 0021` かもしれん → "may"; `:25 0022` だろうな → "probably".
  - `:35 0032` 可能性は低い → "chances … slim".
  - `:45 0042` 恐れがある → "liable"; `:46 0043` ようだ → "Looks like"; `:47 0044` か → "I suppose".
- **Step 3/5/6 departures, flagged and accepted:**
  - `:39 0036` drops 二人, which the two names already say; keeping it makes the page 5 rows.
  - `:46 0043` 相当まいっているようだな has no subject. "Looks like it's taking quite a toll." keeps the referent open without inventing a pronoun.
  - `:5 0002` 少し…いいかしら → "Just a moment… may I?" (the ？ follows the question in English; R §13.3's かしら？ case is the source-marked one).
  - `:9 0006` 秩序 → "the order", not "the order of things", which left "things…" alone on the last row. The social-order sense reads from context. This is non-blocking.
- **Echoes:**
  - `:28 0025` ふ、ふざけるな！ → "D-don't give me that!" follows NO4_BAR/0255 and SCN046B2/05 "Don't give me that!" and the stutter-hyphen rule (R §4.3, §5.7).
  - `:21 0018` 理由だと？ → "A reason, you say?" follows SCN046B2/05 神だと！ "A god, you say!".
  - `:18 0015` 当分暮らすだと⁉ → "Live here for a while⁉" echoes 0014.
  - `:36 0033` なんだと‼ → `What‼`, as bound in R §6 (the ‼ form, unpaired by CHECK with なんだと⁉ "What⁉").
- Glossary: none.

### 25.4 Recurrences (PR Flag 8)
- **Translated, identical:** 0039 = the save prompt (NO4_BAR ×12, NO4_MACHINE/0001; R §3.4). The 16 s-rows = Save / Don't save.
- **Untranslated twins**, which CHECK pairs once translated: NO3_CHAPEL/0049, 0070, 0079, 0111, 0114, 0129, 0130 (p02/p03) must copy `:42`.
- **For p02/p03:** 0122 per §25.1; 0052 錯乱していたのか may take "deranged" (`:45`).
- Glossary: none.

---

## Unit script NO3_CHAPEL.p02 (PR #26, MERGED, 2026-10-30)

The second part of the chapel room (44 rows, 1,070 source characters, tier D, ratio 27.16):
- 0045–0049: the talk-to lines before the food search, and the save prompt.
- 0050–0070: the party reports the food, the survivor who targeted Judy, and the humanoid monster. Heming sends John and Judy to Deck 2. Then the save prompt.
- 0071–0079: the talk-to lines, and the save prompt.
- 0080–0088: the second attack. The laser-sighted gun points to one person, and Wolg's "shoot to kill" (answered by 0089 元警官の言うこととは思えん, p03).

Reviewed once:
- **Round 0** (7afbe0c, merged with main f542d01 for review): MERGE, squash 56e2531. Findings: none; four non-blocking notes (§26.2).

Figures:
- **Container.** NO3_CHAPEL.SCR 10,219 / 65,535 bytes, 55,316 free, 320 tokens, 106/150 rows (MEASURE). This unit cost 660 bytes, from 55,976 free.
- **Pages.** At most 4 rows per page (UNITCHECK, 44 rows, 0 violations). The whole store: 1,142 rows, 0 violations.
- **Duplicates.** CHECK compared 155 duplicate pairs and 7 tag-variant pairs, against main's 152 and 7. The +3 are 0049, 0070 and 0079 joining the save-prompt group.
  - The reviewer's census: 91,784 comparisons (44 rows × every dump row), at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final punctuation dropped).
  - It compared 48 translated pairs: 48 identical, 0 divergent. 12 untranslated hits (0111, 0114, 0129, 0130 ×3).
  - Only the save prompt recurs.
- **Codes.** The authored `{p}{w}{br}` sequence differs from the source on 2 of 44 rows, `:19 0060` and `:44 0085` (PR Flag 2, §26.2). The `…`/`‼`/`⁉`/`──` counts match on 44 of 44, and the `！`/`？` counts also match on 44 of 44.
- **F-011 wrap scan** (the reviewer's script, `build/script_merged.tsv`, 100 lines): no lone "a", "an" or "I", no one-word last row, no split title. Authored-`{br}` lines ≤ 27 (`len()`; 0055 and 0059 at 27).
- **F-012.** Five `+` rows, 0046, 0060, 0064, 0076 and 0085, each after a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-30. Line citations use PROJECT.md §7's numbering in `tl/script/NO3_CHAPEL.p02.tsv` (line = row order + 3).

### 26.1 Terms promoted from §9
- **残弾** (variant 銃の残弾) → `ammo` (4); 銃の残弾 → `the ammo left in your gun` (25).
  - Census: 2 / 0 / 0. Rows: `:36 0077` 残弾が少ないようだな → "You seem low on ammo."; `:37 0078` 銃の残弾には気をつけてな → "watch the ammo left in your gun".
  - Matches 弾切れ "out of ammo" (§3). The §9 alternative "rounds left" is rejected: "round" is bound to アモ for the engine vote (R §25.1), and two words for one noun would blur it.
  - Glossary: §3 row added; §9 row removed.
- **レーザーサイト** → `laser sight` (11).
  - Census: 1 / 0 / 0. `:43 0084` レーザーサイトを付けた銃 → "a gun fitted with a laser sight".
  - Glossary: §3 row added; §9 row removed.
- **人型の化け物** → `a humanoid monster` (18).
  - Census: 人型 1 / 0 / 0. `:15 0056`. 化け物 → monster per R §1.8.
  - "a monster shaped like a man" (the §9 alternative) wraps to an extra row on a 4-row page.
  - Glossary: §6 row added; §9 row removed.
- **厄介 · やっかい** (variants 厄介事 · やっかいなこと) → `trouble` (7).
  - Census: 9 / 0 / 0. Every row is listed here:
    - This unit: `:13 0054` どちらにしろ厄介だな → "Either way, it's trouble."; `:14 0055` なにが厄介だ！ → "What trouble!"; `:15 0056` 厄介事 → "isn't the only trouble"; `:46 0087` やっかいなこと → "one trouble after another".
    - Shipped and left in context: NO4_4101/0003 and NO4_HWR_FRONT/0087 やっかいだ "in trouble"; NO4_BAR/0422 やっかいなことに "Trouble is"; NO4_HWR_FRONT/0142 ちょっと厄介 "tricky"; NO4_BAR/0264 やっかい払い "Good riddance".
  - One word across 0054–0056 carries the source's echo: 0055 throws 0054's word back, and 0056 picks it up again.
  - Glossary: §6 row added; §9 row removed.
- **Applied, unchanged:** 化け物 → monster (0056, 0057, 0059, 0064, 0081); 生き残り → survivor(s) (0051, 0060, 0062, 0072); 死体 → bodies (0063); 見張り → watch (0061); 第２デッキ → Deck 2 (0067); 装備 → gear (0085); 人間 → human (0081, 0082); ジョンたち → "John and the others" (0050); 食料 → food; 錯乱 → "deranged" (0052, R §25.4); the save prompt (0049, 0070, 0079).
- **Not fixed, in context:** 調査 → "investigate/investigating" (0067, 0071, 0074); 予備 → "spare" (0077); 護身用 → "for self-defense" (0085).

### 26.2 Movable codes, readings and speakers (PR Flags 2–7)
- **Leading `{p}` on `+` rows** (R §2.4):
  - `:19 0060` `-` → `{p}`. Without it, the page from 0059 runs to 5 rows; with it, the pages hold 4 and 2.
  - `:44 0085` `{br}` → `{p}{br}`. Without it, the page from 0084 runs to 6 rows; with it, 4 and 3. The source `{br}` between 0085's two sentences is kept.
  - Both sit at sentence boundaries. Approved.
- **Hedges kept** (wave 5's lesson, R §20.3):
  - `:10 0051` らしい ×2 → "Apparently" … "it seems".
  - `:15 0056` そうだ → "It seems"; `:21 0062` そうだ → "apparently".
  - `:22 0063` らしい → "it seems"; `:23 0064` ようだ → "seems".
  - `:24 0065` だろうか → "I wonder"; `:25 0066` かもしれない → "may".
  - `:26 0067` いくまい → "can hardly"; `:36 0077` ようだ → "seem".
  - `:41 0082` らしい → "Apparently", 可能性が高い → "most likely"; `:47 0088` あるまい → "we'll just have to".
- **ヤツ as the head of a relative clause.** `:21 0062` ジュディを襲ったヤツ → "the guy who attacked Judy".
  - This is the killer, but the party does not know that yet. As the head of a relative clause, ヤツ cannot be "he" in English, so it is translated in context as a noun for a male person, as R §1.7 allows for common-noun uses.
  - As a bare pronoun for the monster or the killer it stays he/him/his. `:44 0085` そんなヤツ → "guys like that" is the 〜なヤツ type case.
  - Glossary: §6 ヤツ note extended.
- **Non-blocking review notes**, each accepted:
  - `:12 0053` 故意に殺そうとした → "he meant to kill her?" (PR Flag 6 calls it step 5). "meant to" carries the intent the question turns on, against 0052's 錯乱. The attempt is the established fact of 0051. Nothing is dropped, so the line is accepted as equivalent rather than as a compression. "he tried to kill her on purpose?" also fits, if a later edit wants it.
  - `:14 0055` なにが厄介だ！ → "What trouble!" is the dismissive echo of 0054. Out of context the English could read as an exclamation of how much trouble, but the next sentence ("It's only a person, just one.") fixes the reading. The ！ follows the source.
  - `:27 0068` 頼めるか → "can I ask you?" is elliptical but clear after "Deck 2 needs investigating." "can I count on you?" and "can I rely on you?" overrun the row and leave a one-word row.
  - `:5 0046` → "A misjudgment means death." must fit the 4th row of 0045's page (PR Flag 6).
  - `:23 0064` 深刻だった → "seems severe": "seems to have been severe" adds a fifth row.
  - `:34 0075` いくら…といっても → "Even with food" is equivalent.
- **Speakers** (PR Flag 3, F-009), all named from content:
  - Oakland: 0048, 0055 (addresses Wolg), 0057, 0073, 0074; probably 0081 and 0087.
  - Wolg: 0088 (0089 元警官 replies), and probably the reporting lines.
  - Heming: 0067 (named in 0068), and 0075–0076 (escape is his job, 0036).
  - Judy: 0066, 0069.
  - The others are uncertain. Every line is speaker-neutral in English, so a corrected attribution changes no text (checked line by line).
- **Echoes accepted:**
  - `:7 0048` follows NO4_BAR/0442 "What are you dawdling for?{br}Hurry up and go find one!", with ‼ per source.
  - `:37 0078` いざという時のために "For when it counts", as NO4_BAR/0288.
  - `:46 0087` まったく "Honestly", as NO4_MACHINER90/0043.
- Glossary: §6 ヤツ note extended; nothing else.

### 26.3 Recurrences and bindings for p03 (PR Flag 9)
- **The save prompt.** 0049, 0070 and 0079 copy `tl/script/NO3_CHAPEL.p01.tsv:42` (0039) byte for byte. NO3_CHAPEL/0111, 0114, 0129 and 0130 (p03) must copy it too, and CHECK pairs them.
- **0089** 元警官の言うこととは思えんな answers `:47 0088` "we'll just have to shoot to kill".
- Glossary: none.

### 26.4 A CHECK blind spot recorded in this integration: mid-row `{w}` (wave 7, PRs #27, #29)
- **Source.** `{w}` followed by text, not by `{br}`: `grep -cP '\{w\}[^{]' dumps/script.tsv` → 3 (NO3_NO4/0030, 0040, 0043); scene 0.
- **Engine.** `docs/ENGINE.md` §6: `{w}` waits for a click and keeps the box, and "the next byte follows it". The next sentence therefore continues on the same row with no separator, so an English target glues ("come.And").
- **Tools.** `tools/abyss/codec.py` `PAGE_ENDS = ('{p}', '{w}')` models `{w}` as a page start, so CHECK and UNITCHECK pass the glue.
- **Who found it.** The translators of NO3_NO4.p01 (#29 Flag 3) and NO3_NO4.p02 (#27 Flag 3) found it independently. Each fixes it with a `{br}` after the `{w}`.
- The reviewers of #29 and #27 check the fix on those three rows.
- PROJECT.md §7 gains the blind-spot line and FLAGS.md gains F-026, in this commit, ahead of those reviews, so that their reviewers find it listed.
- Glossary: none.

## Unit script NO3_NO4.p01 (PR #29, MERGED, 2026-10-30)

The first part of the NO3_NO4 room script (31 rows, 633 source characters, tier D, ratio 49.76):
- 0001–0012: the party sends Judy and John to look for a new base, and they settle on the chapel.
- 0013–0031: Wolg's night talk to John, the first half of his police story. It continues in NO3_NO4.p02 (#27).

Reviewed once:
- **Round 0** (61022fd, merged with main 0511790 for review): MERGE, squash e6a9aa1. Findings: none; four non-blocking notes (§27.2).

Figures:
- **Container.** NO3_NO4.SCR 4,506 / 65,535 bytes, 61,029 free, 239 tokens, 31/61 rows (MEASURE). This unit cost 700 bytes, from 61,729 free.
- **Pages.** At most 4 rows per page (UNITCHECK, 31 rows, 0 violations). The whole store: 1,173 rows, 0 violations.
- **Duplicates.** CHECK compared 160 duplicate pairs and 8 tag-variant pairs, against 155 and 7 on the same tree without the unit.
  - The reviewer's census: 64,666 comparisons (31 rows × every dump row), at three levels (exact; `{p}{w}{br}` stripped; `【Name】` stripped, ！？ → ⁉, final punctuation dropped).
  - 30 hits, plus the three `{br}` rows ↔ NO5_BANK/0004 as tag variants. 0 divergent.
  - Byte-identical to shipped rows: 0003 = NO4_HWR_FRONT/0048 `…All right.`; 0009 = NO4_BAR/0373 `…I don't mind.`; 0007 `………` = 7 exact rows and 3 tag variants.
  - 12 untranslated hits: NO3_HW_1/0001–0002, NO3_NO4/0061, 0034, 0036, 0039 (§27.3).
- **Codes.** The authored `{p}{w}{br}` sequence differs from the source on 2 of 31 rows, `:13 0010` and `:33 0030` (§27.2). The `…` counts match on 31 of 31; no ‼, ⁉ or ── in the unit.
- **F-011 wrap scan** (the reviewer's script, 68 wrapped lines): no lone "a", "an" or "I", no one-word last row, no split title. Authored-`{br}` and `{w}`-ended lines ≤ 27 (`len()`; 0014 and 0029 at 27).
- **F-012.** None: every `+` row (0019–0026, 0028–0031) follows a `{br}` ending.
- **F-026.** `:33 0030` takes `{w}{br}` after the mid-row `{w}` (25 / 23 columns). 0040 and 0043 are in p02.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-30. Line citations use PROJECT.md §7's numbering in `tl/script/NO3_NO4.p01.tsv` (line = row order + 3).

### 27.1 Terms promoted from §9
- **ワイフ** → `my wife` (7).
  - Census: 2 / 0 / 0. `:33 0030` いつも出迎えてくれるワイフが来ない → "My wife, who always met me at the door, didn't come."; NO3_NO4/0032 (p02, #27 head 7edf333) "I found my wife with no trouble at all."
  - The loanword affectation is not carried: "the wife" (the §9 alternative) reads as distance, which the story does not have.
  - Glossary: §6 row added; §9 row removed.
- **警察** (variant 警察を辞めた) → `the police`; 警察を辞めた → `quit the police force` (10; 21).
  - Census: 2 / 0 / 0, both 警察を辞めた. `:20 0017` 俺が警察を辞めた理由を…… → "The reason why I quit the police force……"; NO3_NO4/0041 (p02) "To go after him, I quit the police force."
  - "left the force" (the §9 alternative) is idiomatic but drops 警察. 元警官 stays "ex-policeman" (§2). 警官 alone is "cop" in context: `:24 0021` 無鉄砲な警官 → "a fearless, reckless cop", Wolg on himself, as Miller's "cop" (NO4_BAR/0231).
  - Glossary: §2 row added; §9 row removed.
- **Applied, unchanged:**
  - 新しい拠点 → "a new base" (0001, 0011); 教会 → "the chapel" (0011); 元警官 → "ex-policeman" (0014).
  - マガジンの予備 → "spare magazine" (0010); フッ、 → "Heh," (0017).
  - (頭の)いかれた殺人鬼 → "a crazed killer" (0018, 0024; R §1.7 binds both); ヤツ → him/he (0023, 0026, 0027).
  - ２２人 → "twenty-two people" (0019, R §1.4).
- **Not fixed, in context:** ガキ → "kid" (0018); 捜査 → "the case" (0029); 結果 → "As a result" (0026).

### 27.2 Movable codes, readings and speakers (PR Flags 2–6, 9)
- **`:13 0010` `{br}{br}` → `{br}{p}`** (PR Flag 2).
  - The three sentences need 5 rows whichever `{br}` is dropped: 26 | 21 + 23 | 26 + 20. Merging the first two still wraps to 3 rows.
  - The `{p}` sits at the sentence boundary after "just in case.". A `{br}` after it would open the new page on a blank row, so it is removed.
  - The step-6 reorder `Fire a shot to let us know if anything happens.` changes no sense. The literal order wraps `If anything happens, fire a | shot…`, a lone "a" (R §1.12 rule 2).
  - Approved.
- **`:33 0030` `{w}{w}{br}` → `{w}{br}{w}{br}`** (PR Flag 3). This is the F-026 fix (R §26.4): the second sentence starts its own row instead of gluing to "come." mid-row. Approved.
- **No `{p}` added in the `{w}` chains** 0018–0026 and 0027–0031 (PR Flag 9).
  - In the tool model, every `{w}` page fits 4 rows: 3/3/4/4/3/4/4 and 2/4/3/2/2.
  - If `{w}` keeps the box in game, both chains overflow in the Japanese too. This is recorded under F-010.
- **Hedges kept:** `:14 0011` なりそう → "could", くらい → "about the only"; `:20 0017` どうやら…ようだ → "seems"; `:22 0019` だけでも → "at least that I know of".
- **Non-blocking review notes**, each accepted:
  - `:17 0014` 守る → "guarding": "I'm used to protecting people." leaves "people." as a one-word last row (R §1.12 rule 1). The echo is carried by meaning: `:18 0015` "protect", `:19 0016` なにを → "Protect what, you ask?".
  - `:18 0015` uses a forward "it" for the inverted object (守れなかったんだ。{br}もっとも大切なものを……). "I couldn't protect{br}what mattered most…" leaves "protect" alone on a row before the `{br}`.
  - `:32 0029` drops the comma after "One day". With it, the line wraps to a one-word last row, "off.".
  - `:29 0026` あと一歩のとこまで追い詰めた → "came within one step of cornering him", equivalent to "had him all but cornered".
  - `:27 0024` wraps `…with my own hands, no | matter what.`. "no" is a function word, acceptable under R §1.12 rule 2.
- **Speakers** (PR Flag 4, F-009), named from content:
  - Wolg: 0001, 0003, 0013–0031.
  - Oakland: 0002, 0006, 0010.
  - Heming: 0004, 0008.
  - Judy: 0005, 0009, 0011, 0012.
  - spk=4 carries Oakland, Judy and Wolg; spk=0 carries Judy and Wolg. Every line is speaker-neutral in English.
- Glossary: none beyond §27.1.

### 27.3 Recurrences and bindings (PR Flags 7–8)
- **NO3_HW_1/0001–0002** (NO3.b01) = `:14 0011` and `:15 0012` byte for byte: `We've had a look all around, but about the only place that could make a new base is… the chapel.` · `Well then, shall we go call everyone here?`. Both stand alone there: Judy to John, before NO3_HW_1/0003's boarded door.
- **NO3_NO4.p02 (#27):**
  - 0061 `………`.
  - 0034, 0036 and 0039 `{br}`.
  - "my wife" (0032).
  - "quit the police force" (0041).
  - 一番大切なもの → "what mattered most to me" (0040), echoing `:18 0015` もっとも大切なもの.
  - All already match in #27 head 7edf333.
- Glossary: none.

## Unit script NO3_CHAPEL.p03 (PR #28, MERGED, 2026-10-30)

The third and last part of the chapel room (NO3_CHAPEL/0089–0132; 44 rows, 1,039 source characters, tier D, ratio 27.94):
- 0089–0097: the answer to Wolg's "shoot to kill", then the night talk about the engine noise.
- 0098–0110: the engine-power theory, and Wolg splitting the party.
- 0111–0114: Oakland's outburst, between save prompts.
- 0115–0130: the engine room is found, the vote with one round in the right hand, the fuel valve, and the save prompts.
- 0131–0132: the stained glass.

Reviewed twice:
- **Round 0** (d4a6b39, merged with main 1a9f070 for review): CHANGES. Every mechanical gate passed; there was one finding:
  - 1: `:43 0128` the line before the authored `{br}` wrapped to "stopping the engine will do." at 28 columns. It was unflagged, and the PR's Checks line said all such lines were ≤ 27 (R §1.12 rule 3, R §17 precedent).
- **Round 1** (92146e5, rebased on 0511790, merged with main 4feb2ee, which has #29, for review): MERGE, squash f45c28a. `git diff d4a6b39 92146e5` changes only `:43 0128` in the unit file. The PR body's Checks line and Flag 6 wording were corrected.

Figures (round 1, on the merge with 4feb2ee):
- **Container.** NO3_CHAPEL.SCR 10,288 / 65,535 bytes, 55,247 free, 143 tokens, 150/150 rows: the room is complete (MEASURE). Used bytes went from 10,219 to 10,288 (+69, from 55,316 free) while tokens went from 320 to 143: the dictionary is rebuilt per build, so the per-unit byte cost is not additive.
- **Pages.** At most 4 rows per page (UNITCHECK, 44 rows, 0 violations). The whole store: 1,217 rows, 0 violations. MERGE: keys that never matched 0.
- **Duplicates.** CHECK compared 165 duplicate pairs and 8 tag-variant pairs, against main's 160 and 8. The +5 are 0111, 0114, 0129 and 0130 joining the save-prompt group, and 0104 pairing with NO4_BAR/0164.
  - The reviewer's census: 44 rows × 1,899 script and scene dump rows (`{p}{w}{br}` stripped, `【Name】` stripped, ！？ → ⁉, final punctuation dropped).
  - It compared 81 pairs: 81 identical, 0 divergent, 0 untranslated. The 8 NO3_CHAPEL save rows have 1 distinct target.
- **Codes.** The authored `{p}{w}{br}` sequence differs from the source on 1 of 44 rows, `:37 0122` (§28.2). The `…`/`‼`/`⁉`/`──` counts match on 44 of 44.
- **Widths.** Lines ended by an authored `{br}`: 18, all ≤ 27 after codec.wrap (`len()`); the longest are 0121 and 0128 at 27.
- **F-011 wrap scan** (`build/script_merged.tsv`, 103 lines): no lone "a", "an" or "I", no one-word last row, no split title.
- **F-012.** Two `+` rows, 0118 and 0132, each after a `{br}` ending. **F-026:** the unit's sources have no `{w}`.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-30. Line citations use PROJECT.md §7's numbering in `tl/script/NO3_CHAPEL.p03.tsv` (line = row order + 3).

### 28.1 Terms promoted from §9
- **機関室** → `the engine room` (15). Cap 14 if it ever becomes a room name (hints/012–014, blocked).
  - Census: 9 / 0 / 3. Rows: `:8 0093`, `:14 0099`, `:15 0100` "The engine room? Why?", `:21 0106`, `:30 0115`, `:43 0128`; NO3_NO4/0054 ×2 in one row (#27 head 7edf333: "The engine room! Let's run for the engine room‼", agrees); NO2_NO3/0004, NO1_ENGINEROOM/0002 to come; hints/012–014.
  - Glossary: §2 row added; §9 row removed.
- **エンジン · 機関** (variant 機関を止める) → `the engine` (10), singular.
  - Census: エンジン 7 / 0 / 0; 機関 10 / 0 / 3, of which 9 / 0 / 3 are 機関室, so 機関 alone is 1 / 0 / 0 (`:37 0122` 機関を止める → "stopping the engine").
  - The §9 alternative "the engines" is rejected: nothing in the source counts them, and 0093 動いてるんだよ、エンジンが reads as one machine.
  - `:10 0095` 止めれば → "If we stop it": the engine of 0094, repeated, takes "it".
  - Glossary: §3 row added; §9 row removed.
- **動力 · 動力源** → `power` · `the power source` (5 · 16).
  - Census: 動力 2 / 0 / 0 in all, 動力 alone 1 (`:16 0101` 動力が生きている → "its power is still running", not "alive"), 動力源 1 (`:17 0102` 動力源を破壊すれば → "Destroy the power source"). "propulsion" (the §9 alternative) is rejected: the theory is about what keeps the ship at depth, not what moves it.
  - Glossary: §3 row added; §9 row removed.
- **浮上 · 浮き上がる** → `surface` · `float up` (7 · 8).
  - Census: 浮上 2 / 0 / 0 (`:17 0102`, `:31 0116` "the ship may surface"); 浮き上が 1 / 0 / 0 (`:18 0103` "it'll probably float up"). Two source verbs, two English verbs.
  - Glossary: §3 row added; §9 row removed.
- **燃料バルブ** (variant 燃料) → `the fuel valve`; 燃料 `fuel` (14; 4).
  - Census: 燃料 2 / 0 / 0 (`:41 0126`; NO6_HW_3/0001 "Fuel leaking from a pipe…", shipped); 燃料バルブ 1 / 0 / 0. SCN046_VALVE's "It" is this valve's engine (R §13.3).
  - Glossary: §3 row added; §9 row removed. R §24's "not fixed" note on 燃料 is superseded by this row.
- **アモ** → `round` (5).
  - Census: 1 / 0 / 0 (`:37 0122` 全員アモを一発取り出せ → "Everyone, take out one round."). Bound by R §25.1 to s28/s29 `Hold the round` / `Don't hold it`. "bullet" is rejected by that binding.
  - Glossary: §3 row added; §9 row removed.
- **例の生き残り** → `that survivor` (13).
  - Census: 2 / 0 / 0. `:30 0115` 例の生き残りの存在が気になるが → "That survivor still worries me, but…". "still" is carried by 例の, the concern of NO3_CHAPEL/0051, 0060, 0072, and it keeps "room." from a one-word last row. NO3_NO4/0046 (#27 head 7edf333) "that survivor seems likely to be on this deck", agrees.
  - "the survivor we know about" (the §9 alternative) is rejected as long and flat.
  - Glossary: §2 row added; §9 row removed.
- **ステンドグラス** → `the stained glass` (17).
  - Census: 1 / 0 / 0. `:46 0131` ステンドグラスは、ひび割れている → "Cracks run through the stained glass." (restructure, flagged): "The stained glass is cracked." is 29 columns and wraps "cracked." alone.
  - Glossary: §3 row added; §9 row removed.
- **Applied, unchanged:** 元警官 → ex-policeman (`:4 0089`); 社長 → "The boss" (`:22 0107`, third person, as NO4_BAR/0433); 見張りの順番 → "Our turn to keep watch" (`:12 0097`); 生命 → "lives" (`:35 0120`, the "life" sense); 下のデッキ → "the deck below" (`:13 0098`); ウォルグのヤツ → "That Wolg" (`:27 0112`, `:28 0113`, R §1.7); the save prompt (0111, 0114, 0129, 0130); 0104 わかった。 = NO4_BAR/0164 `All right.`.
- **Not fixed, in context:** 推測 "guess" (0101, 0117; 2 / 0 / 0), 出力 "output", 浮力 "buoyancy", 深度 "depth", 銃撃戦 "gunfight", 解雇 "fired", リーダー "the leader" (1 / 0 / 0 each).

### 28.2 Movable codes, readings and speakers (PR Flags 2–6, 8)
- **`:37 0122` `{br}{br}` → `{p}{br}`** (PR Flag 2).
  - Kept as `{br}`, the three sentences need 6 rows (2 + 3 + 1). The `{p}` replaces the first `{br}`, at the sentence boundary between the instruction ("take out one round") and the voting rule. A `{p}{br}` would open the new page on a blank row.
  - Pages 2 + 4. Approved, and added to F-010's in-game check.
- **0122 binding** (R §25.1, §13.2): "Right… Everyone, take out one round." / "If you're in favor of stopping the engine, hold it in your right hand." / "If not, hold nothing." This agrees with s28/s29 and the SCN046 subtitles "raise your right hand" / "Open your hand". なにも持つな is the empty hand of 握らない.
- **`:43 0128`** (round 1): ああ。だがエンジンを止めれば何が起こるかわからん。 → "Yeah. But stop the engine, and who knows what happens." The 〜すれば frame follows `:17 0102` ("Destroy the power source, and the ship may surface."). It wraps 26 / 27 before the authored `{br}`, so the page stays 4 rows.
- **`:4 0089` with p02's `:47 0088`** (R §26.3): "…we'll just have to shoot to kill." → "Not what I'd expect to hear from an ex-policeman." → `:5 0090` "We can't let any more of our people be killed." This reads as the exchange: the jab, then Wolg's answer.
- **Hedges kept** (R §20.3), each checked: `:8 0093` おそらく "probably"; `:9 0094`, `:10 0095` ×2, `:11 0096`, `:31 0116`, `:33 0118`, `:34 0119` かもしれ… "may"; `:17 0102` かもしれんな "Could be." and かもしれん "may"; `:18 0103` だろう, `:34 0119` だろうな "probably"; `:41 0126` はず "should"; `:47 0132` だろうか "Could".
- **Step-4–6 departures, flagged and accepted:**
  - `:28 0113` 帰ったら解雇してやる！ → "When we're back, he's fired!" (agency shift; "I'll fire him!" leaves "him!" alone).
  - `:38 0123` "All but John are in favor……"; `:40 0125` "But can we stop the engine…?"; `:18 0103` "Oddly, there's air aboard."; `:34 0119` 当分 → "for now"; `:46 0131` the stained-glass restructure; `:47 0132` "Could" for だろうか.
- **Readings accepted:** `:7 0092` and `:8 0093` keep the source's inverted order ("Bothering you? That sound."; "It's running, the engine."). `:15 0100` なぜだ。 → "Why?": a question in English, the ？ count's one difference.
- **Speakers** (PR Flag 6, F-009), named from content:
  - Wolg: 0090, 0104, 0106–0107 (俺とヘイミング…社長はここで待機), 0109–0110, 0120, 0122, 0126, 0128; probably 0115. He is on spk=5, 0 and 2. The vote is his (R §13.2).
  - Oakland: 0108, 0112–0113 (言いおって, 解雇); probably 0119 and 0127.
  - Heming, probably: 0099, 0101, 0103, 0105, 0116, 0121 (よかろう → "Let us all decide, then.").
  - 0089 is Heming or Oakland. 0091–0097, 0117–0118 and 0123–0125 stay uncertain. 0131–0132 are narration.
  - Every line is speaker-neutral in English, so a corrected attribution changes no text (checked line by line).
- Glossary: none beyond §28.1.

### 28.3 Recurrences
- **The save prompt.** 0111, 0114, 0129 and 0130 copy `tl/script/NO3_CHAPEL.p01.tsv:42` (0039) byte for byte. All 8 NO3_CHAPEL save rows are shipped and identical.
- **NO3_NO4.p02 (#27):** 0046 例の生き残り → "that survivor" and 0054 機関室 → "the engine room" agree with §28.1 in head 7edf333. The #27 reviewer confirms them against the glossary.
- Glossary: none.

## Unit script NO3_NO4.p02 (PR #27, MERGED, 2026-10-30)

The second and last part of the NO3_NO4 room script (NO3_NO4/0032–0061; 30 rows, 597 source characters, tier D, ratio 52.70):
- 0032–0044: the end of Wolg's police story to John (his wife's murder, quitting the force, being hired by Oakland), continuing NO3_NO4.p01 (#29).
- 0045–0047: Wolg sets out to search Deck 3 with Heming.
- 0048–0055: the water, the monster, the run for the engine room, the shutter.
- 0056–0061: Oakland's outburst, instructions to the searchers, another victim.

Reviewed once:
- **Round 0** (7edf333, cut from ae83b72, merged with main 1418e1f for review → f402f0f, no conflict): MERGE, squash 62509c4. Findings: none; two non-blocking notes (§29.2).

Figures (on the merge with 1418e1f, which has p01):
- **Container.** NO3_NO4.SCR 4,808 / 65,535 bytes, 60,727 free, 73 tokens, 61/61 rows: the room is complete (MEASURE). The file was at 61,029 free with p01 alone, so the unit cost 302 bytes. The dictionary is rebuilt per build, so this is less than the PR's 520 measured without p01. `containers negative: 0; under the reserve (2000 bytes): 0`.
- **Pages.** At most 4 rows per page (UNITCHECK, 30 rows, 0 violations). The whole store: 1,247 rows, 0 violations. MERGE: keys that never matched 0.
- **Duplicates.** CHECK compared 169 duplicate pairs and 8 tag-variant pairs, against main's 165 and 8.
  - The reviewer's census: 30 rows × every script and scene dump row, exact and with `{p}{w}{br}` stripped (！？ → ⁉), 56,940 comparisons.
  - It found 29 recurrences: 0 divergent, 0 untranslated.
  - 0061 `………` = NO3_NO4/0007, NO4_BAR/0201, 0265, 0430, NO4_HWR_FRONT/0057, 0092, SCN038_5C1/10, SCN046B1/01; tag variants NO4_MACHINER90/0108, NO4_TOOL_ROOM/0025, 0060.
  - The `{br}` rows 0034, 0036 and 0039 = p01's 0020, 0025 and 0028.
- **Codes.** The authored `{p}{w}{br}` sequence differs from the source on 3 of 30 rows, exactly PR Flag 2: `:12 0040` and `:15 0043` `{w} {p}` → `{w} {br} {p}` (F-026), and `:18 0046` `-` → `{p}` (§29.2). The `…`/`‼`/`⁉`/`──` counts match on 30 of 30.
- **Widths.** The reviewer's script ran codec.wrap(…, 28) per authored segment over 62 lines. It was proved on planted violations: a lone "I", an authored line at 28, a split "Mr.", a one-word last row, and `{w}` glue.
  - 18 lines end at an authored `{br}` or `{w}`, all ≤ 27 (`len()`); the longest are 0044 and 0059 at 27.
  - The 28-column lines (0045, 0053, 0059) are tool wraps.
  - No lone "a" or "I", no one-word last row, no split title.
- **F-012.** Every `+` row (0033–0037, 0039, 0040, 0042, 0043, 0046) follows a `{br}` ending.
- **F-026.** All three dump rows are now shipped with `{br}` after the mid-row `{w}`: 0030 (#29), `:12 0040` (line before the `{br}` 23 columns), `:15 0043` (10).

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-30. Line citations use PROJECT.md §7's numbering in `tl/script/NO3_NO4.p02.tsv` (line = row order + 3).

### 29.1 Terms: §9 promotions confirmed, one row added
- **§9 is empty.** The four seeds this unit renders were promoted by #28/#29, each citing this PR's head 7edf333, and the shipped lines agree:
  - ワイフ → "my wife" (`:4 0032`; R §27.1).
  - 警察を辞めた → "quit the police force" (`:13 0041`, word for word with p01 0017; R §27.1).
  - 例の生き残り → "that survivor" (`:18 0046`; R §28.1).
  - 機関室 → "the engine room" ×2 (`:26 0054`; R §28.1).
  - The rows' "(#27) agrees" notes are replaced by the shipped wording, and their Ruling column points here. No target changes.
- **閉じ込める** (variants 閉じ込めた, 閉じ込めていた) → `shut in` (7).
  - Census: 3 / 0 / 0. NO4_HWL_BACK2/0006 ヤツは閉じ込めたが → "We've shut him in" (shipped); `:25 0053` バカな、閉じ込めたはず‼ → "Impossible, he's supposed to be shut in‼"; NO2_MAINSTORAGE/0027 この先にいた怪物を閉じ込めていたのね (NO2, to come).
  - The elided subject of 0053 is the monster, so it takes "he" under the ヤツ rule (R §1.7). はず → "supposed to".
  - 閉じこめ (2 / 0 / 0: NO3_CHAPEL/0023 "locked in", shipped; NO4_BAR_T/0108) is people trapped, not the monster, so it stays in context.
  - Glossary: §6 row added.
- **Applied, unchanged:**
  - 親父 → "your dad" (`:15 0043`); 第３デッキ → "Deck 3" (`:17 0045`); 浸水 → "flooding" (`:23 0051`).
  - モンスター / 化け物 → "monster" (`:25 0053`, `:30 0058`, singular as NO3_CHAPEL/0035).
  - 社長 → "the boss" (`:28 0056`, Oakland on himself); 生き残り → "survivors", 人間 → "a human" (`:31 0059`).
  - ヤツ → he/him (0038, 0041, 0042); 一番大切なもの → "what mattered most to me" (`:12 0040`, = p01 0015).
- **Not fixed, in context:**
  - 眉間 "between her eyes" (2 / 0 / 0, echoing NO4_P_OFFICE/0009 "between the eyes").
  - 犠牲者 "victim" (2 / 0 / 0, as NO4_BAR/0402).
  - 復讐 "revenge", セーター "sweater" (1 / 0 / 0 each).

### 29.2 Movable codes, readings and speakers (PR Flags 2–5, 7–9)
- **`:12 0040`, `:15 0043` `{w} {p}` → `{w} {br} {p}`** (PR Flags 2–3). This is the F-026 fix (R §26.4), as 0030 in #29. Approved.
- **`:18 0046` leading `{p}`** on the `+` row after 0045's `{br}` (R §2.4).
  - Without it, the page from 0045 is 2 + 3 = 5 rows. 0046 is 74 characters and cannot take fewer than 3 rows.
  - With it, the pages are 3 (the last is the cursor row) + 3. The `{p}` sits at the sentence boundary.
  - Approved; added to F-010.
- **No `{p}` added in the `{w}` chains 0032–0037, 0038–0040, 0041–0043** (PR Flag 4).
  - Every `{w}` page fits 4 rows as the tools model it.
  - Between `{p}` clicks, the English runs 10 / 7 / 8 rows against the source's 7 / 5 / 4.
  - Recorded under F-010.
- **Departures** (PR Flag 8, §2.1 steps 5–6), each justified by a measured wrap, accepted:
  - `:7 0035` いつまでたっても編みあがらない → "forever unfinished": the knitting is implied by the sweater, and the page stays at 4.
  - `:14 0042` "there was no tracking him down…": "…I couldn't" leaves a lone "I".
  - `:16 0044` "I'll do everything I can to get you out of here." (the お前は topic is not fronted).
  - `:23 0051` supplies "the ship".
  - `:31 0059` "Be sure not to shoot a human by mistake.": "Don't shoot…" leaves "mistake." alone; "Be sure" carries よ.
- **Hedges kept:**
  - `:18 0046` 可能性が高いようだ → "seems likely"; `:27 0055` そう → "seems".
  - `:30 0058` 良さそうな → "good-looking"; `:31 0059` かもしれん → "may yet"; `:25 0053` はず → "supposed to".
- **`:27 0055`** シャッターが下りていて先には進めそうに無い。{p} → `The shutter is down, so there seems to be no going any further.{p}` (23 / 26 / 12).
  - "The shutter is down" follows shipped NO5_ENTRANCEM/0011–0012. "There seems to be no going any further" follows the §6 fixed 封鎖 sentence and keeps そう. It is not a byte duplicate.
  - NO2_HW_5/0003 シャッターが下りていて先には進めない。{p} (unhedged, NO2) should take `The shutter is down, so there's no going any further.{p}`. That keeps this frame and drops only the hedge, as the §6 閉ざされて row keeps the unhedged sentences apart.
- **`:29 0057` source typos** (PR Flag 10; F-027), read as the sense requires:
  - ぐずぐす for ぐずぐず → "What are you dawdling for!", the words of shipped NO4_BAR/0172. The source differs, so CHECK does not pair them.
  - 落ち着けれる for 落ち着ける → "somewhere we can settle in", as SCN002/02 腰を落ち着けた "settling in".
- **Readings accepted:**
  - `:9 0037` 眉間と掌 → "between her eyes and in her palms", the killer's signature (NO4_P_OFFICE/0009).
  - `:19 0047` よし → "Right," (NO4_HWL_FRONT/0006).
  - `:12 0040` and `:32 0060` 何もできなかった → "I couldn't do anything" both.
- **Non-blocking notes:**
  - `:15 0043` 復讐じゃ食うことはできん → "Revenge doesn't put food on the table." This renders the sense ("can't eat on revenge"), not a swapped idiom.
  - `:18 0046` からな (the reason for 0045) is carried by juxtaposition.
- **Speakers** (PR Flag 5, F-009), named from content:
  - Wolg: 0032–0046 (spk=4) and probably 0060.
  - Oakland: 0056 (わしは社長), and 0057 by its ぐずぐず echo of NO4_BAR/0172.
  - Wolg or Heming: 0058–0059.
  - Uncertain: 0047–0054.
  - Narration: 0055. Silence: 0061.
  - Every line is speaker-neutral in English, checked line by line.
- Glossary: none beyond §29.1.

### 29.3 Recurrences and bindings
- 0061 `………` and the `{br}` rows 0034/0036/0039 match p01 and the shipped rows (§29 Figures).
- NO2_MAINSTORAGE/0027 takes "shut in" (§29.1).
- NO2_HW_5/0003 takes the unhedged shutter sentence (§29.2).
- Glossary: none.

## Unit script NO3.b01 (PR #32, MERGED, 2026-10-31)

Seven small deck-3 rooms (NO3_CABIN_3002/3003/3104/3105/3106, NO3_FOODSTORAGE, NO3_HW_1; 51 rows, 1,105 source characters, tier D, ratio 29.98): John's examine text on bodies, doors, shutters and vents; Judy in the food storeroom (the lift and the battery) and choosing the chapel as the new base.

Reviewed once:
- **Round 0** (84adc22, merged with main bc2b1ac for review → 3366c46, no conflict): MERGE, squash 4ed66e9. Findings: none.

Figures (on the merge with bc2b1ac):
- **Containers.** MEASURE after MERGE: NO3_HW_1.SCR 1,751 / 65,535 (63,784 free), NO3_FOODSTORAGE 1,687 (63,848), NO3_CABIN_3105 1,152 (64,383), 3003 763 (64,772), 3002 369 (65,166), 3104 341 (65,194), 3106 287 (65,248); every room complete. `containers negative: 0; under the reserve (2000 bytes): 0`.
- **Pages.** At most 4 rows per page (UNITCHECK, 51 rows, 0 violations); whole store 1,298 rows, 0 violations. MERGE: keys that never matched 0.
- **Duplicates.** CHECK compared 183 duplicate pairs and 8 tag-variant pairs. The reviewer's census: 51 rows × every script and scene dump row, exact and with `{p}{w}{br}` stripped (！？ → ⁉), 96,798 comparisons, 64 recurrences, 0 divergent against `tl/` and the heads of the open sibling PRs #30, #31, #33.
- **Codes.** The authored `{p}{w}{br}` sequence equals the source's on 51 of 51 rows (PR Flag 2); no `{w}` in the unit. `…`/`‼`/`⁉`/`──` counts match on 51 of 51.
- **Widths.** 17 lines end at an authored `{br}`; the last wrapped line of each is ≤ 26 (`codec.wrap(…, 28)`, `len()`). The 28-column lines are tool wraps. No lone "a"/"an"/"I", no one-word last row (read in `build/script_merged.tsv`).
- **F-012.** Both `+` rows (NO3_CABIN_3104/0002, 3105/0007) follow a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-31. Line citations use PROJECT.md §7's numbering in `tl/script/NO3.b01.tsv` (line = row order + 3).

### 30.1 Terms promoted from §9, and rows added
- **Promoted, as seeded** (§9 → §3, §4, §6), each applied byte for byte:
  - 扉は鍵が掛かっていて開きそうに無い。{p} → `The door's locked. It looks like it won't open.{p}` (4 / 0 / 0): `:48`, `:49` NO3_HW_1/0005–0006; NO3_HW_2/0002–0003 in #30 already match. Hedged, kept apart from the unhedged §6 `It's locked, so the door won't open.`
  - シャッターは閉鎖され開きそうに無い。{p} → `The shutter's sealed. It looks like it won't open.{p}` (4 / 0 / 0): `:50`, `:51`, `:54` NO3_HW_1/0007, 0008, 0011; NO2_HW_4/0001 in #31 matches. The ロック · 閉ざされ siblings stay in §9 for #30/#31.
  - コントロール装置を破壊されたため… (2 / 0 / 0): `:34` NO3_FOODSTORAGE/0007; NO2_SUBSTORAGE/0008 in #33 matches.
  - エレベータは反応しない…。ここで狙撃された時に… (1 / 0 / 0) `:33` NO3_FOODSTORAGE/0006, and its 食料庫で sibling NO2_SUBSTORAGE/0007 (1 / 0 / 0, #33 matches); promoted as one row, CHECK does not pair them.
  - 通風孔に入る · 入らない (choice) → `Enter the vent` · `Don't enter` (4 / 0 / 0 each as choice rows): `:13`, `:14`, `:25`, `:26`; #31 NO2_CABIN_2001/s05–s06 and #33 NO2_SUBSTORAGE/s06–s07 match. 入らない in dialogue (NO5_HW_R/0006) stays in context.
  - 撃たれて死んでいる → `Shot dead.` (6 / 0 / 0): `:43` NO3_FOODSTORAGE/0016, as shipped NO4_P_OFFICE/0003, 0009–0011; NO2_THIRDSTORAGE/0010 (#33) to come.
  - 食料 · 食糧 → "food" (食料 39 / 0 / 3 incl. 食料庫 11 / 0 / 2; 食糧 3 / 0 / 0): `:40`, `:41`, `:43`. 保存用の食料 "preserved food" (#33). "provisions" rejected.
  - エレベータ · コントロール装置 · リフト · 食料運搬用のリフト → elevator · the controls · lift · a lift for carrying food (4 · 4 · 4 alone, 6 with ワイヤーリフト · 1, all script): `:33`–`:38`.
  - バッテリ · バッテリー → "battery" (2 / 0 / 1): `:36`; #30 NO3_STORAGE/0003 バッテリー agrees.
  - ハチェット → "hatchet" (2 / 0 / 2): `:47`, `:52`; never "axe".
- **Added** (PR Glossary additions):
  - ダンボール → "cardboard box"; 食糧のダンボールがある → `A cardboard box of food.` (2 / 0 / 0, `:40`, `:41`). The fragment is needed: "There's a cardboard box of food." wraps `…box of | food.` before the authored `{br}`.
  - 隣の部屋 → "the next room" (2 / 0 / 0, `:4`, `:7`). 木板 → "wooden boards" (2 / 0 / 0, `:46`, `:47`). 収容箱 → "storage box" (1 / 0 / 0, `:52`).
  - 腐臭 → "stench of decay" (1 / 0 / 0, `:40`), with 腐敗臭 (1 / 0 / 0) as shipped NO4_SHOP/0003.
  - 明かりになる物 → "something to use as a light" (3 / 0 / 0, `:18`–`:20`).
- **Applied, unchanged:** 死体 "body"; 化け物 "monster"; 通風孔 "An air vent" at first mention (`:8`, `:17`), "the air vent" after (`:19`, `:20`); 鍵 "locked" (`:15`, `:48`) and "A key" (`:31`); 乗客 "passengers" (`:10`); 操作パネル "control panel" (`:38`); 切り刻む · 無残に (`:9` = shipped NO4_4102/0004); ジョン "John" (`:37`).
- NO3_CABIN_3003/0002 = 3105/0005 天井には通風孔が見える。ここをたどって行けば… → `An air vent in the ceiling. It looks like following it could lead to another room.` (2 / 0 / 0, a CHECK pair); noted in §9's 天井に通風孔 row for #31/#33.
- Glossary: 18 rows added to §3, §4, §6; 12 §9 rows removed; §9 rows still needed by #30/#31/#33 kept, two notes pointed here.

### 30.2 Frame departures, readings and speakers (PR Flags 3–5, 7–11)
- **`:24 NO3_CABIN_3105/0008` `A body, hacked to pieces, lies here.{br}`** (PR Flag 3, step 6). The §9 frame `A body lies here, hacked to pieces.` wraps 27 + `pieces.` (7) before an authored `{br}`: a one-word last row (R §1.12). The reorder keeps every word and the glossary term. Accepted; the §6 row records it as the frame's variant before an authored `{br}`. `:22 3105/0006` keeps the frame (`A body lies here, shot with | a gun.`).
- **`:42 NO3_FOODSTORAGE/0015` `It seems a monster tore its head off.{p}`** (PR Flag 4). The §9 example `Its head was torn off by a monster, it seems.` wraps `…by a | monster,` (lone "a"). The active verb keeps ようだ as "It seems". The row is worded as the verb "tear … head off", active or passive, so it also covers #33 NO2_THIRDSTORAGE/0011 首を飛ばされている。化け物にやられたのだろう。 → `Its head has been torn off. A monster probably did it.{p}` (census 首を飛ばさ 2 / 0 / 0).
- **化け物 "a monster" in narration** (PR Flag 10): `:24` 3105/0008, `:39` FOODSTORAGE/0012, `:42` 0015. R §11.1: the article follows the line — generic "a" where no known monster is meant (NO4_BAR/0368), "the" for the known one (NO5_BANK/0006, NO3_CHAPEL/0035, 0064, NO3_NO4/0058). These bodies' killers are unspecified, and small monsters are aboard; #31 NO2_CABIN_2101/0001 and #33 NO2_THIRDSTORAGE/0011 take "a monster" too. Census 化け物 58 / 1 / 0, 怪物 21 / 0 / 0. Accepted.
- **……行きましょう。** `:32` FOODSTORAGE/0005 `……Let's go.` = the second sentence of #33 NO2_THIRDSTORAGE/0007 `I'm sorry.{br}……Let's go.` (sentence-level; CHECK does not pair a line inside a longer message).
- **Rewordings for wraps** (PR Flag 5), each measured and accepted: `:31` 0004 "here" supplied; `:37` 0010 `…impossible…… it seems.`; `:17` 3105/0001 移動手段 → "their way around"; `:19`/`:20` "using the air vent is dangerous…"; `:40` 漂っている → "drifts out"; `:43` 取り合いで → "fighting over the food"; `:10` 3003/0004 銃で撃たれた死体だ → `A body, shot with a gun.`
- **Hedges kept** (PR Flag 7): ようだ "seems"/"It seems"; そう "looks like"; `:27` 3106/0001 らしく…そうにない "seems … doesn't look like"; だろうか "Could …?"; かしら "I wonder"; みたい "it seems"; どうやら…ようだ "Seems".
- **Body pronoun "it"** (PR Flag 11), as shipped NO4_SHOP/0003; "they" only for the unseen occupants at `:16` 3104/0002.
- **Speakers** (PR Flag 8, F-009), from content: Judy at 3105/0001–0004, FOODSTORAGE/0001–0005, 0008–0010 (ね/わ/かしら/のね, "Go, John"), HW_1/0001–0002 (bound, R §27.3); narration (plain だ/ようだ) elsewhere. spk=100 carries both; the English is speaker-neutral where it matters.
- **`:52`–`:53` NO3_HW_1/0009 ends `{br}`, 0010 is not `+`** (PR Flag 13). Both kept as the source. With a `{br}` ending there is no glue whether or not the engine continues the box. No change.
- **Pre-choice prompts** (PR Flag 9): `:4`/`:7` 3 rows and `:17` 4 rows before choices; recorded under F-003 (whether the options share the box). Not blocking.
- Glossary: the §6 死体が転がっている and 首を飛ばされ rows point here.

### 30.3 Recurrences and bindings
- **NO3_HW_1/0001–0002 = NO3_NO4/0011–0012** byte for byte (`:44`, `:45`; R §27.3): source and target bytes equal, verified.
- For the open wave-8 PRs, already matching at their heads: #30 NO3_HW_2/0002–0003, NO3_STORAGE/0003 "battery"; #31 NO2_HW_4/0001, NO2_CABIN_2001/s05–s06; #33 NO2_SUBSTORAGE/0007–0008, s06–s07, NO2_THIRDSTORAGE/0007 (……Let's go.), 0011 ("torn off", "a monster").
- F-003 extended with the three prompts (`:4`, `:7`, `:17`).
- Glossary: none beyond §30.1.

## Unit script NO3.b02 (PR #30, MERGED, 2026-10-31)

Six small deck-3 rooms (NO3_HW_2, NO3_HW_3, NO3_MACHINE, NO3_MEDICALROOM, NO3_NO2, NO3_STORAGE; 25 rows, 502 source characters, tier D, ratio 65.55). All of it is John's examine text: locked doors and shutters, the watertight-shutter panel, three bodies, a drawer, a battery and a posted notice.

Reviewed twice:
- **Round 0** (5f3673c, merged with main 17f46ba → 4b724e6): CHANGES, three findings. (1) `:26 NO3_STORAGE/0002` dropped 使えそう's "looks" (§31.1). (2) The bodies at `:20`, `:22`, `:28` were "they"/"them" (§31.2). (3) `:11 NO3_MACHINE/0002` split the §3 操作パネル phrase with "here" (§31.1).
- **Round 1** (39dde92, merged with main 204f1e1 → 77134f3, no conflict): MERGE, squash 0a3bbec. Exactly the five prescribed rows changed. Findings: none.

Figures (round 1):
- **Containers.** MEASURE after MERGE: NO3_MEDICALROOM.SCR 898 / 65,535 (64,637 free), NO3_HW_2 775 (64,760), NO3_MACHINE 638 (64,897), NO3_STORAGE 543 (64,992), NO3_NO2 445 (65,090), NO3_HW_3 413 (65,122). Every room is complete. `containers negative: 0; under the reserve (2000 bytes): 0`.
- **Pages.** At most 4 rows per page (UNITCHECK: 25 rows, 0 violations); whole store 1,323 rows, 0 violations. MERGE: keys that never matched 0.
- **Duplicates.** CHECK compared 190 duplicate pairs and 8 tag-variant pairs. The reviewer's census split the 25 rows into sentences at `{br}`/`{p}`/`{w}` and searched them as substrings over every script and scene dump row. It found 67 hits, and every translated exact recurrence is byte-identical against `tl/` and the heads of #31 (4b8499c) and #33 (0c27480).
- **Codes.** The authored `{p}{w}{br}` sequence equals the source's on 25 of 25 rows; the unit has no `{w}`. The `…`/`‼`/`⁉`/`──`/`?` counts match on 25 of 25.
- **Widths.** Nine lines end at an authored `{br}`; the last wrapped line of each is ≤ 27 (8, 10, 14, 14, 16, 24, 24, 26, 27; `codec.wrap(…, 28)`, `len()`). No lone "a"/"an"/"I" and no one-word last row.
- **F-012.** Both `+` rows (`:12` NO3_MACHINE/0003, `:24` NO3_NO2/0002) follow a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-31. Line citations use PROJECT.md §7's numbering in `tl/script/NO3.b02.tsv` (line = row order + 3).

### 31.1 Terms promoted from §9, the 使えそう ruling, and rows added
- **Ruling a — 使えそう keeps "looks"** (PR Flag 4, round-0 finding 1). Census 使えそう 13 / 0 / 0.
  - Every shipped row keeps the attributive そう as "looks": NO4_MACHINE/0002, NO4_STORAGE/0004, NO5_BANK/0007, NO6_STORAGE/0002, NO3_MACHINE/0001, NO3_MEDICALROOM/0001–0003.
  - The wave-8 §9 seed for 〜には、(もう)使えそうなものは無いようだ dropped it in both siblings (`…nothing else usable in the drawer.` · `…nothing usable in the locker.`). R §20.3/§21.3 make a dropped hedge a CHANGES when the page does not force it.
  - `:26` NO3_STORAGE/0002 → `There seems to be nothing else in the drawer that looks usable.{p}` (25 / 23 / 13). もう is "else" (after 0001's ammo), and ようだ is "There seems".
  - NO2_MAINSTORAGE/0030 (#31) takes `The locker seems to hold nothing that looks usable.{p}` (24 / 26). Both straight placements strand a word: `…in the locker that looks | usable.` (28 / 21 / 7) and `…looks usable in the | locker.` (25 / 24 / 7). So the topic ロッカーには becomes the subject, a step-6 recast, flagged, and both hedges are kept. #31 round 1 already has it.
  - Plain 無い keeps no "seems": `:16` NO3_MEDICALROOM/0001 ほかには使えそうな物は無い → `There's nothing else that looks usable.{p}`, parallel to NO5_BANK/0007 `There's nothing else in sight that looks usable.` R §21.3's "No … looks usable" and "There's nothing … that looks usable" are both the plain form. #33 NO2_TOFE_ROOM/0005 matches byte for byte (2 / 0 / 0).
  - The §6 使えそう family row records it.
- **The 操作パネル phrase stays whole** (PR Flag 5, round-0 finding 3). `:11` NO3_MACHINE/0002 防水シャッターの操作パネルのようだ。{br} → `There seems to be a control panel for the watertight shutters here.{br}` (27 / 24 / 14). R §23.1 says it "takes the same words hedged".
  - "here" is supplied because `…for the watertight | shutters.` strands one word before the authored `{br}`. This follows the precedent of NO3_FOODSTORAGE/0004 (R §30.2).
  - "here" goes last so that "a control panel for the watertight shutters" stays one string. Round 0's `…a control panel here for the…` split it.
  - `:13` NO3_MACHINE/0004's first sentence equals NO6_BRIDGE/0012's byte for byte. Census 操作パネル 5 / 0 / 0. The §3 row's note is updated with the shipped form.
- **Promoted, as seeded** (§9 → §6):
  - シャッターはロックされていて開きそうに無い。{p} → `The shutter's locked. It looks like it won't open.{p}` (4 / 0 / 0), at `:4`, `:7`, `:8`, `:9`. The 閉ざされ sibling (2 / 0 / 0, #31) stays in §9.
  - 〜から、銃の弾をみつけた。{p} → `Found ammo in a desk drawer.{p}` (`:25`) · `Found ammo in the locker.{p}` (#31 matches). Census 銃の弾 2 / 0 / 0.
  - 『…』{br} + と書かれた用紙が(何枚か)張られている。{p} → `"Optional Cruise Tours,"{br}` + `read several posted sheets.{p}` (`:23`–`:24`). The と書かれている pattern (R §12.1) applies.
    - について is not carried in a title, as 案内 was not (R §21.3).
    - The + row's leading full-width space is dropped.
    - #33 NO2_NO3/0005–0006 `"Shipboard Precautions,"{br}` + `reads a posted sheet.{p}` matches. Census と書かれた用紙 2 / 0 / 0.
  - 扉は鍵が掛かっていて… (`:5`, `:6` = shipped NO3_HW_1/0005–0006) and バッテリー (`:27` `This seems to be a battery.{p}`) were already §3/§6 rows (R §30.1). Their "#30 matches" notes now point at shipped rows.
- **Added — 引き裂く "tear" · 切り裂く "slice"** (point raised by the coordinator; #33 Flag). Census 引き裂 6 / 0 / 0, 切り裂 1 / 0 / 1 (items/009, the wire cutter, blocked).
  - 引き裂く: shipped NO4_P_OFFICE/0003 滅茶苦茶に引き裂かれ and NO4_BAR/0250 ずたずたに引き裂かれ are "torn to shreds"; NO4_BAR/0310 人間を引き裂く is "rips people apart". `:28` 半分に引き裂かれ is "torn in half". #33 NO2_SUBSTORAGE/0010, 0012 バラバラに引き裂かれ is "torn to pieces".
  - 切り裂く: #33 NO2_SUBSTORAGE/0011 半分に切り裂かれ is "sliced in half". The two verbs are different words in the source and stay apart in English.
- Glossary: §6 rows added (ロック sentence, 使えそう family, ほかには…, 銃の弾をみつけた, 〜には使えそうなものは無いようだ with the corrected targets, 用紙 notice, 引き裂く · 切り裂く). The §3 操作パネル and バッテリ notes and the §6 扉は鍵 note are updated. Four §9 rows are removed, and the ロック/閉ざされ row is cut to its 閉ざされ half.

### 31.2 Readings, pronoun and recurrences
- **Ruling b — an examined body is "it"** (round-0 finding 2). This follows R §30.2, shipped NO4_SHOP/0003, NO5_BANK/0008, NO3_CABIN_3105/0007 and NO3_FOODSTORAGE/0012, 0016. The rows:
  - `:20` NO3_MEDICALROOM/0005 `…Examining the wound, it seems a gun killed it.{p}`
  - `:22` 0007 `Could it have been killed by a monster?{p}` (the frame of NO3_FOODSTORAGE/0012)
  - `:28` NO3_STORAGE/0004 `It seems it was attacked by a monster.{br}`. "Seems it was…" would leave `monster.` alone before the authored `{br}`.
  - "they" stays only for people not in view (NO3_CABIN_3104/0002). The §6 死体 row's note records this (a scope note added, pointing to R §30.2 and §31.2; the target "body" is unchanged). #31's NO2_CABIN_2101/0002 got the same finding.
- **Readings accepted** (PR Flags 6–7), with every hedge kept: ようだ/どうやら is "seems"; だろう "probably"; のだろうか "Could …?".
  - `:10` 船内の備品 → "shipboard equipment"; 特に使えそうな物は見当たらない → `Nothing in sight looks particularly usable.`, the NO4_SHOP/0004 frame.
  - `:12` スイッチを押しますか？ → `Press the switch?`.
  - `:18` 強奪された跡 → "signs of having been looted".
  - `:21` 見るも無残 → "a brutal sight to behold" (the §6 切り刻む · 無残に row's word); 端々 → "here and there".
  - `:22` 首が切り離され → "cut off", kept apart from 首を飛ばされ "torn off" and 首が切断され "severed" (§6).
- **Speakers.** All 25 rows are spk=- narration, read from content (plain だ/ようだ/ある).
- **For later units, by hand** (CHECK does not pair these):
  - 化け物に殺されたのだろうか (3 / 0 / 0): #33 NO2_SUBSTORAGE/0010, 0012 ここにいた化け物に… has `Could the monster that was here have killed it?`. `Could it have been killed by the monster that was here?{p}` (28 / 26) would parallel `:22`. That is #33's reviewer's call.
  - 化け物に襲われたようだ (2 / 0 / 0): NO1_CONTROLROOM/0004 どうやら… can reuse `It seems it was attacked by a monster.`
- **F-003.** NO3_MACHINE/0002 + 0003 is a 4-row prompt (source 2) before Yes/No; it is appended to F-003.
- Glossary: the 死体 note as above; nothing else beyond §31.1.

## Unit script NO2.b01 (PR #31, MERGED, 2026-10-31)

Nine deck-2 rooms (NO2_CABIN_2001/2101/2103, NO2_HW_1–5, NO2_MAINSTORAGE; 55 rows, 1,021 source characters, tier D, ratio 32.00). The corridors and cabins are John's examine text: shutters, locked doors, the steam valve, three bodies and the ceiling vent. NO2_MAINSTORAGE holds the killer's ambush, Wolg's arrival, Judy and Wolg after the SCN046A parting, and the wrenched door.

Reviewed twice:
- **Round 0** (cb42a85, merged with main ac1741c → ad42574, no conflict): CHANGES, two findings. (1) `:56` NO2_MAINSTORAGE/0030 dropped 使えそう's "looks" (R §31.1, ruling a). (2) `:8` NO2_CABIN_2101/0002 "Could the victim…" added a noun where the shipped convention is "it" (R §31.2, ruling b).
- **Round 1** (4b8499c, merged with main 24093f6 → d780938, no conflict): MERGE, squash 028dcdf. Exactly the two prescribed rows changed. Findings: none.

Figures (round 1):
- **Containers.** MEASURE after MERGE: NO2_MAINSTORAGE.SCR 2,713 / 65,535 (62,822 free); NO2_HW_3 942 (64,593); NO2_HW_1 645 (64,890); NO2_HW_5 557 (64,978); NO2_CABIN_2001 445 (65,090); NO2_CABIN_2101 383 (65,152); NO2_HW_2 377 (65,158); NO2_HW_4 371 (65,164); NO2_CABIN_2103 269 (65,266). Every room is complete. `containers negative: 0; under the reserve (2000 bytes): 0`.
- **Pages.** At most 4 rows per page (UNITCHECK: 55 rows, 0 violations); whole store 1,378 rows, 0 violations. MERGE: keys that never matched 0.
- **Duplicates.** CHECK compared 205 duplicate pairs and 9 tag-variant pairs; without the unit the figures are 190 and 8. The tag variant is 0023 ↔ NO4_HWR_FRONT/0128 `What about you?`. The reviewer's source-side census compared 55 rows with every dump row, exact and with `{p}{w}{br}` stripped: 38 pairs, 0 mismatches. Untranslated twins: #33 NO2_SUBSTORAGE/s06–s07 and NO2_TOFE_ROOM/s08–s09, already matching at its head.
- **Codes.** The authored `{p}{w}{br}` sequence equals the source's on 55 of 55 rows. There is no `{w}` and no `+` row. `…`/`‼`/`⁉`/`──` counts match on 55 of 55; `?` is added at 0004 ("Huh?") and 0008 ("eh?") as readings.
- **Widths.** 14 lines end at an authored `{br}`; the last wrapped line of each is ≤ 27 (`codec.wrap(…, 28)`, `len()`). No lone "a"/"an"/"I" and no one-word last row (read in `build/script_merged.tsv`).

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-31. Line citations use PROJECT.md §7's numbering in `tl/script/NO2.b01.tsv` (line = row order + 3).

### 32.1 Terms promoted from §9, and rows added
- **Promoted, as seeded** (§9 → §6), each applied byte for byte:
  - シャッターは閉ざされていて開きそうに無い。{p} → `The shutter's closed. It looks like it won't open.{p}` (2 / 0 / 0): `:14` NO2_HW_2/0001 = `:24` NO2_HW_5/0001. This completes the 閉鎖され / ロック / 閉ざされ family (R §30.1, §31.1).
  - シャッターが閉じていて先に進めない。{p} · シャッターが下りていて先には進めない。{p} → `The shutter is closed, so no going any further.{p}` · `The shutter is down, so no going any further.{p}` (2 / 0 / 0 · 1 / 0 / 0): `:10` = `:13` NO2_HW_1/0001, 0004; `:26` NO2_HW_5/0003.
    - R §29.2's `…so there's no going any further.` wraps `…any | further.`, a one-word last row, so it is replaced. This keeps the unhedged frame and "no going any further" of §6 閉ざされて.
    - NO3_NO4/0055 そうに無い stays hedged (R §29.2). Census シャッターが下りていて 4 / 0 / 0.
  - 天井に通風孔が見える。{br}ここから他の部屋に行けそうだ。 → `An air vent in the ceiling.{br}Looks like it could lead to other rooms.` (1 / 0 / 0): `:4`, そう kept as "Looks like".
    - The 壁に sibling (1 / 0 / 0, #33 NO2_SUBSTORAGE/0009) matches at #33's head, with its second sentence byte-identical.
    - 天井には…ここをたどって行けば (R §30.1) is its own sentence.
  - The §9 examples already promoted by #32/#30 are used exactly:
    - `:22` NO2_HW_4/0001 = shipped NO3_HW_1/0007, 0008, 0011, a CHECK pair.
    - `:5`–`:6` vent choices.
    - `:55` `Found ammo in the locker.{p}`.
    - `:56` `The locker seems to hold nothing that looks usable.{p}` (round 1, R §31.1).
    - The 死体が転がっている frame at `:7`, `:8`, `:9`. Their "#31" notes now point at shipped rows.
- **Added** (PR Glossary additions):
  - キサマ · きさま → "you bastard" (2 / 0 / 0 · 0 / 1 / 0). The killer: `:29` 0003 `Hey, you bastard!`, `:30` 0004 `Too much fun, you bastard!`. Shipped SCN046B2/05 (Wolg) has `You bastard, how many…`.
  - スパナ → "wrench" (1 / 0 / 0, `:51` 0025), US usage as 懐中電灯 "flashlight".
  - 鍵がかかっている…。{p} → `The door is locked…{p}` (4 / 0 / 0): `:11`, `:12`, `:23`, `:25`.
    - "The door" is supplied, because the examined object in a corridor is the door, as at NO6_BRIDGE/0009.
    - That row's source differs (扉には…。, no …), so CHECK does not pair the two. The glyph count follows each source.
    - Census 鍵がかかって 5 / 0 / 0.
- **Applied, unchanged:**
  - Names: Wolg, Heming, Oakland, John. 社長 "the boss" (`:43`).
  - 死体 "body"; 化け物 · 怪物 "monster" (`:7` "a monster", R §30.2; `:53` "the monster").
  - 閉じ込める "shut in" (`:53`, R §29.1).
  - The killer's laugh (R §9.1); 俺様 · 女神 "my very own goddess" (`:29`, R §9.1).
  - 切り刻む "hacked to pieces"; Retry?; Yes/No.
  - `:50` 0024 行けと言ってるだろう‼ follows SCN038B/20 `Go, I'm telling you‼` (a near-repeat, not paired).
- Glossary:
  - §6: five rows added (閉ざされ, 閉じていて · 下りていて, the ceiling/wall vent, 鍵がかかっている…, キサマ · きさま).
  - §3: one row added (スパナ).
  - Three §9 rows removed; §9 is now empty.
  - Notes updated to "shipped" on §4 通風孔に入る and on §6 閉鎖され, ロック, 閉じ込める, 死体が転がっている, 銃の弾, 〜には使えそうなものは無いようだ, 閉ざされて.

### 32.2 Speakers, readings and departures
- **NO2_MAINSTORAGE is three events** (PR Flag 5, F-009), read from content:
  - 0001–0018: the killer's ambush; Wolg arrives at 0010 `John, what happened⁉`.
  - 0019–0024: Judy and Wolg, after the SCN046A1–A3 parting, where Heming and Oakland are lost (行けっ！ウォルグ！).
  - 0025–0028: Judy at the door.
  - The events point opposite ways. 0017 いったん戻った方がいいな / 社長が無事とも言い切れん presumes Oakland alive and the party turning back. 0019 どうして追いついてこないの and 0022 先に行け have the party pressing on while Heming and Oakland fail to follow. So 0019/0021 do not exclude Heming from 0014–0018.
- **Speakers.**
  - Killer: 0001–0009, 0011–0012. His register is crude (やがった, ぜ, キサマ), with the mock courtesy of 0012 バラさせてもらう "allow me to carve up" (R §13.2).
  - Wolg: 0010, 0013, 0015, 0017, 0020, 0022, 0024.
  - Judy: 0019, 0021, 0023, 0026–0028 (ねぇ/の/のね/ましょう).
  - 0014/0016/0018 (のか, んでな, ああ) are male, not Judy; Heming or John. They stay open, rendered speaker-neutral.
  - 0025 （…） → `( )`, an inner thought, John or Judy, neutral.
  - Narration: 0029–0030.
- **0020 後で追いつく → `They'll catch up later.`** The subject is Heming and Oakland, not Wolg.
  - The line answers 0019's question.
  - 0021 そう──死んだのね reacts to the evasion.
  - 0023 あなたは？ only makes sense if Wolg has not said he will follow. "I'll catch up later" would make 0023 redundant.
- **The killer's name.** ジェイク・ノーマン "Jake Norman" (§1) appeared only in the PR's note. No row in this unit names him; Wolg first does at SCN046B1/03. No name is added to the text.
- **Step 5–6 departures** (PR Flag 4), each measured and accepted:
  - `:29` 0003 今だけは moved to the end, "just for now" (17 / 25 / 28 / 26). In the source position it left `you.` alone.
  - `:30` 0004 面白すぎるぜ → `Too much fun, you bastard!` with the subject implied; 面白すぎる may mean the situation as much as the person.
  - `:43` 0017 `Better head back for now.` ("We'd" implied), in Wolg's terse register.
  - `:56` 0030 the step-6 locker recast (R §31.1).
  - その俺様の女神 → "my very own goddess": English cannot stack その with "my".
- **Body pronoun "it"** (ruling b, R §31.2): `:8` NO2_CABIN_2101/0002 `…Could it have been attacked while asleep?{p}` (27 / 25 / 22). Its first sentence equals shipped NO3_CABIN_3105/0006's.
- **Hedges kept:**
  - らしい "apparently" (`:7`); のだろうか "Could …?" (`:8`).
  - そうに無い "It looks like" (`:14`, `:22`, `:24`); そうにない "It seems" (`:15`–`:17`); そうだ "Looks like" (`:4`).
  - ようだ + attributive そう "seems … looks usable" (`:56`).
- **Readings accepted** (PR Flag 6):
  - 0009 見込んだ "chose"; 0016 んでな "…, is all"; 0021 `──` → `——`.
  - 0027 `…、` → `…` with a lowercase continuation (R §11.3).
  - CABIN_2103 ばらばらになった "scattered".
  - HW_3 とても先に進めそうにない → `It seems there's no way to go any further…`, とても as "no way". Kept apart from the §6 封鎖 sentence, whose source has no とても.
- **F-003.** `:4` CABIN_2001/0001 (3 rows, source 2) before the vent choices and `:18` HW_3/0004 (3 rows, source 1) before Yes/No are appended to F-003.
- Glossary: none beyond §32.1.

## Unit script NO2.b02 (PR #33, MERGED, 2026-10-31)

Four small deck-2 rooms (NO2_NO3, NO2_SUBSTORAGE, NO2_THIRDSTORAGE, NO2_TOFE_ROOM; 43 rows, 829 source characters, tier D, ratio 39.66): Judy and John escape to deck 2 after the explosion, John alone in the sub-storeroom (the dead elevator, the vent, bodies, preserved food), Judy's outburst on self-sacrifice in the third storeroom, and the vent room.

Reviewed twice:
- **Round 0** (0c27480, merged with main ee9ed7b): CHANGES, two findings. (1) `:19`/`:21` NO2_SUBSTORAGE/0010 = 0012 and (2) `:36` NO2_THIRDSTORAGE/0009 turned the passive 〜されたのだろうか active (§33.2).
- **Round 1** (c0727e3, merged with main ec70d70 → 22c7b51, no conflict): MERGE, squash b7e0ea2. Exactly the three prescribed rows changed. Findings: none.

Figures (round 1):
- **Containers.** MEASURE after MERGE: NO2_SUBSTORAGE.SCR 1,835 / 65,535 (63,700 free), NO2_THIRDSTORAGE 1,053 (64,482), NO2_TOFE_ROOM 851 (64,684), NO2_NO3 787 (64,748); every room complete, deck NO2 complete. `containers negative: 0; under the reserve (2000 bytes): 0`.
- **Pages.** At most 4 rows per page (UNITCHECK: 43 rows, 0 violations); whole store 1,421 rows, 0 violations. MERGE: keys that never matched 0.
- **Duplicates.** CHECK compared 214 duplicate pairs and 9 tag-variant pairs. The reviewer's census (every unit row × every dump row, exact, `{p}{w}{br}`-stripped, 【】-stripped, ！？ → ⁉): 28 translated pairs, 0 mismatches — SUBSTORAGE/0008 = NO3_FOODSTORAGE/0007; TOFE_ROOM/0005 = NO3_MEDICALROOM/0001; s06–s07 = NO3_CABIN_3003, 3105, NO2_CABIN_2001 vent choices; s08–s09 = seven Yes/No pairs; THIRDSTORAGE/0006 = NO4_MACHINER90/0034, NO4_BAR/0391 (variant); 0010 = 0012; 0013 = 0015.
- **Codes.** The authored `{p}{w}{br}` sequence equals the source's on 43 of 43 rows; no `{w}`. `…`/`‼`/`⁉`/`──` counts match on 43 of 43; the one punctuation change is 0009's 。 → "?" on a "Could …" question, as shipped NO4_SHOP/0005, NO3_CABIN_3104/0002.
- **Widths.** 17 lines end at an authored `{br}`; the last wrapped line of each is ≤ 27 (`codec.wrap(…, 28)`, `len()`). No lone "a"/"an"/"I", no one-word last row.
- **F-012.** All six `+` rows (NO2_NO3/0002, 0006, SUBSTORAGE/0002, 0014, 0016, THIRDSTORAGE/0002) follow a `{br}` ending.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-31. Line citations use PROJECT.md §7's numbering in `tl/script/NO2.b02.tsv` (line = row order + 3).

### 33.1 Terms promoted and added; cross-unit sentences
- **Seeds and bound sentences, used byte for byte** (all already §3/§4/§6 rows from R §30.1, §31.1, §32.1; their "#33" notes now say shipped):
  - `:17` 0008 = NO3_FOODSTORAGE/0007 `The controls were destroyed, so this elevator can no longer be used.{p}` (CHECK pair).
  - `:16` 0007 食料庫で sibling of NO3_FOODSTORAGE/0006: `…It seems the sniper fire in the food storeroom destroyed the controls.{p}` (27 / 27 / 28 / 13); only "here" → "in the food storeroom" differs.
  - `:18` 0009 `An air vent in the wall.{br}Looks like it could lead to other rooms.`, the wall twin of shipped NO2_CABIN_2001/0001.
  - `:26`–`:27` `Enter the vent` · `Don't enter`; `:42` TOFE_ROOM/0004 通風孔に入りますか？ → `Enter the vent?` matches.
  - `:43` TOFE_ROOM/0005 = NO3_MEDICALROOM/0001 `There's nothing else that looks usable.{p}` (CHECK pair).
  - `:8`–`:9` NO2_NO3/0005–0006 `"Shipboard Precautions,"{br}` + `reads a posted sheet.{p}`, parallel to NO3_NO2/0001–0002.
  - `:34` THIRDSTORAGE/0007 `I'm sorry.{br}……Let's go.` — its second sentence = NO3_FOODSTORAGE/0005 `……Let's go.`
  - `:37` 0010 `Shot dead.` (§6 撃たれて死んでいる, variant 死んでる); `:38` 0011 `Its head has been torn off.` (§6 首を飛ばされ, passive).
  - `:22`/`:24` 保存用の食料 "preserved food"; `:15` 食料 "food" (§3).
- **引き裂く · 切り裂く** (PR Flag 8, coordinator point). Conform to the §6 row from R §31.1: `:19`/`:21` バラバラに引き裂かれ "torn to pieces"; `:20` 身体が半分に切り裂かれ `The body is sliced in half.`, kept apart from NO3_STORAGE/0004 身体を半分に引き裂かれ `The body is torn in half.` on purpose (different verbs). The PR's proposed バラバラに引き裂かれ row is already covered by that row; no new row. Census 引き裂 6 / 0 / 0, 切り裂 1 / 0 / 1, バラバラ 3 / 0 / 0 (NO3_MEDICALROOM/0006 バラバラで "in pieces" in context).
- **Added:** ハッチ → "hatch" (§3; 1 / 0 / 0, `:35` THIRDSTORAGE/0008 `A hatch…{br}`).
- Glossary: §3 ハッチ row added; "#33" notes set to shipped on §3 食料 · 食糧, エレベータ; §4 通風孔に入る; §6 撃たれて死んでいる, 首を飛ばされ, コントロール装置…, エレベータは反応しない…, ほかには使えそうな物は無い, 『…』 notice, 引き裂く · 切り裂く, the ceiling/wall vent; §6 死体 note extended (§33.2).

### 33.2 The passive だろうか frame (round-0 findings 1–2)
- Source: 〜(ら)れたのだろうか about a body — 8 / 0 / 0: NO2_CABIN_2101/0002, NO2_SUBSTORAGE/0010, 0012, NO2_THIRDSTORAGE/0009, NO3_CABIN_3104/0002, NO3_CABIN_3105/0007, NO3_FOODSTORAGE/0012, NO3_MEDICALROOM/0007.
- Target: the passive, with the body ("it") as subject: `Could it have been <participle> (by a monster)?`. Shipped before this unit, all passive: NO3_MEDICALROOM/0007 `Could it have been killed by a monster?`, NO3_FOODSTORAGE/0012 `Could it have been eaten by a monster?`, NO3_CABIN_3105/0007 `Could it have been cornered here and killed?`, NO3_CABIN_3104/0002 `…could they have been attacked inside?` (unseen occupants), NO2_CABIN_2101/0002 `…Could it have been attacked while asleep?`.
- Reasoning: literal first (the source is passive and keeps the body as topic), and the near-sibling must parallel — MEDICALROOM/0007's source differs from SUBSTORAGE/0010 only by ここにいた. Round 0's active `Could the monster that was here have killed it?` and `Could a monster have attacked it?` broke both. This decides the #30 reviewer's open note (R §31.2).
- Binds: `:19` = `:21` NO2_SUBSTORAGE/0010 = 0012 `It's been torn to pieces.{br}Could it have been killed by the monster that was here?{p}` (25 · 28 / 26); `:36` NO2_THIRDSTORAGE/0009 `Could it have been attacked by a monster? It's been brutally hacked to pieces.{p}` (27 / 23 / 26). The plain だろう (no か) stays "probably" (`:37`, `:38`).
- Glossary: §6 死体 note extended to name the frame.

### 33.3 Speakers, readings and wrap-forced wordings
- **Speakers** (PR Flag 4, F-009), from content: Judy at NO2_NO3/0001–0003, SUBSTORAGE/0001–0002, THIRDSTORAGE/0001–0008, TOFE_ROOM/0001–0003 (かしら/わ/の/のよ); narration (John's viewpoint, plain だ/ようだ) at SUBSTORAGE/0003–0016, THIRDSTORAGE/0009–0011, TOFE_ROOM/0005–0006; NO2_NO3/0005–0006 narration; TOFE_ROOM/0004 the prompt.
- **`:7` NO2_NO3/0004 黙って機関室へ急げっ！** is a rough male command, not Judy. Most likely Wolg, who is on this deck (SUBSTORAGE/0003 locks the door); not decidable from the dump (急げ 1 / 0 / 0). `Shut up and hurry to the engine room!` is speaker-neutral, so a later attribution changes no text. Recorded under F-009. 機関室 "the engine room" (§2).
- **`:23` SUBSTORAGE/0014 食繋ぐ** (PR Flag 9): read as 食い繋ぐ with the okurigana omitted, a written variant rather than a sure typo; 1 / 0 / 0, nothing to pair. `…we can hold out for a while.` Accepted.
- **Judy's outburst, THIRDSTORAGE/0001–0007**, against shipped NO3_CHAPEL/0003–0009 and SCN047C2/01–05: plain and emphatic, no markers; 助けてくれる "save" as NO3_CHAPEL/0003; ‼ ⁉ kept. Accepted.
- **Wrap-forced wordings** (PR Flag 5), each measured and accepted:
  - `:22`/`:24` 保存用の食料が置かれている → `Here's some preserved food.{br}` (27). 置かれている is existential in examine text; "here's" keeps the location. `Preserved food has been left here.` runs past 27 and strands `here.` before the authored `{br}`.
  - `:44` TOFE_ROOM/0006 低い音を立てて動いている → `It runs with a low hum.` (23). A hum is a low running sound; nothing is added. `It's running with a low hum.` is 28 before the authored `{br}`. 分からない "Hard to tell", as NO4_P_OFFICE/0012.
  - `:32` THIRDSTORAGE/0005 わからない ×2 → `I don't know` ×2, repetition kept; `…I don't understand!` strands one word before the authored `{br}`.
  - `:10` "up on that container…"; `:11`/`:41` じゃないかしら "maybe"; `:41` `……、` → `…… maybe` (R §11.3); `:15` "heading back"; `:20` `The body is sliced in half.` (a 6-row page otherwise); `:40` "something's here‼".
- **Hedges kept** (PR Flag 7): ようだ/ようで "seems"; そう "Looks like"/"looks like"; そうに無い "doesn't look like"; だろうか "Could …?"; だろう "probably"; かしら "I wonder"/"maybe".
- **F-003.** `:18` SUBSTORAGE/0009 is 3 rows (source 2) before the vent choices; appended to F-003. `:42` TOFE_ROOM/0004 is 1 row (source 1) before Yes/No.
- Glossary: none beyond §33.1–§33.2.

## Unit script SPACESHIP.b01 (PR #35, MERGED, 2026-10-31)

Figures (round 0):
- **Containers.** MEASURE after MERGE: SPACESHIP.SCR 661 / 65,535 (64,874 free), SPACESHIP_HW.SCR 694 (64,841); both rooms complete, deck SPACESHIP complete. `containers negative: 0; under the reserve (2000 bytes): 0`.
- **Pages.** At most 4 rows per page (UNITCHECK: 8 rows, 0 violations; the 4 at `:10` SPACESHIP_HW/0004); whole store 1,429 rows, 0 violations. MERGE: keys that never matched 0.
- **Duplicates.** CHECK compared 214 duplicate pairs and 9 tag-variant pairs. The reviewer's census (every unit row × every dump row, exact, `{p}{w}{br}`-stripped, 【】-stripped, ！？ → ⁉, final 。！？… dropped): 50,064 comparisons, 0 hits. Sub-sentence census matched the shipped renderings: なに⁉ 4 / 0 / 0 (NO3_CHAPEL/0057 "What⁉"), 急ぎましょう 2 / 0 / 0 (NO6_HW_4/0002 "Let's hurry."), 危険すぎ · 危険過ぎ 1 / 1 / 0 · 1 / 0 / 0 ("too dangerous", R §17.4), この振動 2 / 0 / 0 (NO4_HWL_BACK/0006 "this tremor").
- **Codes.** The authored `{p}{w}{br}` sequence equals the source's on 8 of 8 rows; one `{br}` moved within it (§34.2). No `{w}`, no `+` rows. `…`/`‼`/`⁉` counts match on 8 of 8.
- **Widths.** Five lines end at an authored `{br}`: 17, 21 (`:5`), 11 (`:8`), 17 (`:10`), 26 (`:11`), all ≤ 27 (`codec.wrap(…, 28)`, `len()`). No lone "a"/"an"/"I", no one-word last row.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-31. Line citations use PROJECT.md §7's numbering in `tl/script/SPACESHIP.b01.tsv` (line = row order + 3).

### 34.1 Terms promoted from §9
- Source: 制御装置 — 2 / 0 / 0 (SPACESHIP_HW/0004, NO1_CONTROLROOM/0003). Target: `the control system` (18). Binds `:10` `…Because we destroyed the control system earlier…`; NO1_CONTROLROOM/0003 (#34, in rework) `the engine's control system`, which the #34 reviewer accepted. Kept apart from コントロール装置 "the controls" (§3, R §30.1); 装置 alone stays unfixed (R §3.1). Glossary: §3 row added from §9.
- Source: 武器 — 7 / 0 / 1 (NO4_BAR/0097, 0269, 0332, NO4_BAR_T/0138, NO4_MACHINER90/0001, NO4_TOOL_ROOM/0037, SPACESHIP/0002; items/003). Target: `weapon(s)` (6 / 7); その武器 → `that weapon`. Shipped: NO4_BAR/0332, NO4_MACHINER90/0001 "weapons"; 0097 武器らしい武器 "real weapons", 0269 武器を携帯 "armed", NO4_TOOL_ROOM/0037 "greatest weapons" in context. Binds `:5`. Glossary: §3 row added from §9.
- Source: チャージ — 1 / 0 / 0. Target: `takes time to charge` (チャージに時間がかかる); "charge", never "recharge". Binds `:5`. Glossary: §3 row added from §9.
- Source: 落下 (船の落下が始まっている) — 1 / 0 / 0. Target: `the ship's starting to fall⁉` (28; wraps 23 / 17 with `This tremor…`). ⁉ one glyph. Binds `:10`. Glossary: §3 row added from §9.

### 34.2 The moved `{br}` at SPACESHIP/0002 (PR Flag 2)
- Source: `ジョン、その武器はチャージに時間が{br}かかるわ。{br}気をつけて‼`. Target: `John, that weapon{br}takes time to charge.{br}Be careful‼` (17 / 21 / 11).
- Reasoning: at the source position the first line is "John, that weapon takes time" = 28, over the 27 preferred for a line ended by an authored `{br}` (PROJECT.md §5.2). The source's own break already splits the clause (after 時間が); the moved break keeps a subject | predicate split and the count (2 → 2). Removing the `{br}` instead wraps to "…takes time" / "to charge.", a two-word row. Accepted.
- Binds `:5`. Glossary: none.

### 34.3 Who destroyed the control system (PR Flag 3)
- Source: SPACESHIP_HW/0004 さっき、制御装置を破壊したから…。 — no subject; 1 / 0 / 0.
- Target: `Because we destroyed the control system earlier…`.
- Evidence: SCN047C1/01–06 (alien voice to John) and C2/01–05 (Judy's declaration; the alien's ば、馬鹿な‼ at C2/03) name no act of destruction; no other row in the three dumps mentions it; 制御装置 elsewhere only at NO1_CONTROLROOM/0003, where it runs normally. Judy speaks to John, who is beside her (she has just handed him the alien gun, SPACESHIP_HW/0002).
- Reasoning: English needs a subject. "we" is the one that asserts no actor the source does not; "I" (Judy) or "you" (John) would each state a fact the text never gives, and a John-alone reading would more naturally name him (あなたが). The passive ("was destroyed") is rejected: the source is active 破壊した, and voice is kept (R §33.2). さっき → "earlier", as 先刻 at NO6_HW_4/0001.
- Binds `:10`. Glossary: none. A later in-game look that shows the act may narrow the pronoun; nothing else would change.

### 34.4 Speakers and readings
- **Speakers** (PR Flag 4, F-009): Judy on spk=100 (`:5` わ, `:11` よ / ましょう), spk=0 (`:4` なの) and spk=- (`:8` あなたが持っていて); `:7` (spk=-) Judy or John's thought; `:6`, `:9`, `:10` Judy or narration. Every line is speaker-neutral in English.
- `:6` 何の反応も示さない → `This door shows no response at all…` — kept apart from 反応しない "won't respond" (NO3_FOODSTORAGE/0006, NO2_SUBSTORAGE/0007): different verbs stay apart (R §31.1).
- `:8` 彼らの使っていた銃よ → `John, this is the gun they were using.`; 銃 stays "gun" (items/003 レーザーガン is blocked and not borrowed); あなたが持っていて → `You keep it.`
- `:11` ここは危険よ！ → `John, it's dangerous here!` (26) — a different source from NO6_HW_4/0002 ここは…危険よ "This place is… dangerous."; "this place is dangerous!" strands "dangerous!" before the authored `{br}`. 急ぎましょう "Let's hurry." as NO6_HW_4/0002 (R §24.3).
- `:4`, `:9` なに⁉ "What⁉", as NO3_CHAPEL/0057; the fragments kept.
- Glossary: none beyond §34.1.

## Unit script NO4_BAR_T.p01 (PR #36, MERGED, 2026-10-31)

Figures (round 0, squash 8a1e7ab):
- **Containers.** MEASURE after MERGE: NO4_BAR_T.SCR 9,315 / 65,535 (56,220 free; 58,098 before), tokens 524 / 1,499, 46/181 rows; NO4_BAR.SCR unchanged at 37,378. `containers negative: 0; under the reserve (2000 bytes): 0`. MERGE: keys that never matched 0.
- **Pages.** UNITCHECK: 46 rows, 0 violations, max 4 rows/page. Authored code diff: 14 rows, 9 `{p}` and 10 `{br}` added, none moved or removed (= PR Flag 2). No `{w}`. Six F-012 `+` boundaries (0012→0013, 0013→0014, 0015→0016, 0018→0019, 0023→0024, 0037→0038), each opened with `{br}` or `{p}` at a sentence end.
- **Duplicates.** CHECK: 214 duplicate pairs and 9 tag-variant pairs, the same with the file removed, so CHECK pairs **0** rows of this unit (every row is labelled, F-013). Reviewer's census (label stripped, `{p}{w}{br}` removed, final 。 dropped, ！？ → ⁉, `…。` → `…`; every unit row × every script and scene dump row, whole-row and sentence-level): **87,308 whole-row pairs, 200,252 sentence pairs, 77 matches**. Every translated twin reuses the shipped words except 0036's first sentence (§35.2).
- **Widths.** Lines ended by an authored `{br}`: 27 / 15 (0001), 26, 25, 23, 5, 13, 15, 23, all ≤ 27. Glyph counts 46 / 46 match.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-31. Line citations are in `tl/script/NO4_BAR_T.p01.tsv` (line = row order + 3).

### 35.1 Labels and terms
- **【男】** 6 / 0 / 0 → `【Man】` (5), promoted from §9. **【老人】** 10 / 0 / 0 → `【Old Man】` (9), new. All 16 rows are in this unit.
  - Reasoning: PROJECT.md §6 says to translate the name in the brackets. These labels are descriptions, not names. The draft withholds the names until the self-introductions (0012, 0038 for Collison; 0018 彼はウィリアム for William), as 【女】 withholds Judy's (R §14.1). So they are translated literally and title-cased, like `【Woman】`, and not resolved to names.
  - Content confirms the speakers. 【男】 0033 and 0035 are William's shipped NO4_BAR/0014 and 0016, and 0034 addresses him. 【老人】 0012 and 0038 are Collison introducing himself.
  - `【Old Man】` does not collide with じいさん → lowercase "old man" in dialogue (§6), which William uses at :36 0033.
- **Name labels**: 【オークランド】 42 / 3 / 0, 【ウォルグ】 29 / 2 / 0, 【ウィリアム】 6 / 0 / 0, 【コリスン】 20 / 0 / 0, 【ヘイミング】 14 / 1 / 0 → `【Oakland】` · `【Wolg】` · `【William】` · `【Collison】` · `【Heming】`.
  - Rule: any §1 name in a label takes its §1 short form in brackets. This matches shipped SCN002OLD/02, 03, 07 (`【Wolg】`, `【Heming】`) and the existing 【ミラー】 · 【ジュディ】 row (R §18.1).
  - Binding on NO4_BAR_T.p02 (#37) and every later `_T` unit. 【ヘイミング】 is not in this unit; its row follows the same rule.
- **母船** 2 / 0 / 0 → `mother ship` (11, two words), at :31 0028 `can no longer return to our mother ship` and :32 0029 `You've friends on your mother ship, surely?`.
  - Reasoning: the literal maritime term for a diving operation's surface vessel (PR Flag 8). "support ship" would be a gloss.
  - No alien craft is called 母船 in either dump, so the one-word sci-fi "mothership" is avoided and nothing clashes.
  - Shipped NO4_BAR/0009 has 海上 "up on the surface" for the same crew. That is another word and is not changed.
- **宝探し屋** 2 / 0 / 0 → `treasure hunter` (15): :42 0039 `but "treasure hunter" might be clearer` and :43 0040 `Treasure hunter⁉`.
  - The source has no 「」. The quotes mark the word as mentioned, for と言った方が, as shipped 狩り場 `"hunting ground"` (R §2.1).
- Glossary: §1 three rows added (【男】 promoted from §9, 【老人】, the name labels). §2 two rows added (母船, 宝探し屋).

### 35.2 Labelled copies of NO4_BAR.p01, and the one not reused (PR Flags 4–5)
- **Whole-row twins, byte-identical once the label is stripped:**
  - 0014 = NO4_BAR/0020; 0020 = 0042 = 0024; 0021 = 0043 = 0025; 0022 = 0044 = 0026.
  - 0031 = 0012; 0032 = 0013; 0033 = 0014; 0046 = 0028.
  - 0010 `………` = the 17 rows R §15.4 lists.
- **Sentence twins, shipped words reused:** 0001, 0009 (わからん `I don't know.`), 0013, 0015, 0016, 0018 / 0041 (まあ待て `Now, hold on.`), 0023, 0024, 0026, 0027, 0028 (申し訳ない and :15 もうしわけない `My apologies.`), 0029, 0030, 0036 (the 0018 part), 0037, 0039. 0001's last sentence = 0025 `W-who are you people⁉`.
- **:39 0036 まったく、なんという言いぐさじゃ → `Really, of all the things to say.`** Shipped NO4_BAR/0017 has `Really, what a thing to say.`.
  - 0036 joins 0017 and 0018, so it is not a row twin, and the byte-identity rule binds rows, not sentences inside a longer row.
  - With the label, 0017's words end a line in a lone "a" (`【Old Man】Really, what a`). R §1.12 rule 2 allows no exception for that.
  - The new wording is as literal. The precedent is R §4.5: labelled copies keep the shipped words "where they fit".
- **One-word last rows** (R §1.12 rule 1), each judged:
  - :24 0021 and :46 0043 `either.`: whole-row twins of NO4_BAR/0025, so they must stay byte-identical.
  - :26 0023 `mind.`: the shipped sentence, too long for one row after `【Collison】`. 0024 must open with `{br}` (F-012).
  - :28 0025 `people⁉`: "you people" carries お前たち's brusqueness and matches shipped NO4_BAR/0001 `who are you people…⁉`. "you all" would be less faithful and would also change :4 0001.
  - All four accepted and flagged.
- **Draft-only differences rendered literally, not forced to the shipped words:**
  - :37 0034 彼は → `he's` (shipped 彼ら "they").
  - :22 0019 今日は → `Today he seems to be in a foul mood.`, reordered so the wrap does not give `in a | foul mood`.
  - :48 0045 この子 without ここを案内した → `And this girl here is Judy Arsela.`
  - :30 0027 ⁉ per the draft (shipped 0003 ？).
- Glossary: none.

### 35.3 Readings, speakers, verbs
- Speakers come from the labels and from content (F-009); every row is `spk=-`. 0001–0011 have no shipped counterpart.
- **Two source verbs stay two English verbs (R §31.1):** 調べに来て (:7 0004) `investigate` and 調査で (:29 0026) `survey`.
- **Verbs already merged in shipped NO4_BAR, kept that way:**
  - 救助 and 助け both take "rescue", as shipped 0003 and 0009 already do.
  - 乗り込む takes "board" or "come aboard" in context, as shipped 0002, 0011 and 0022 are already mixed.
- 上で待機している (:10 0007) → `They're standing by up top.`, following the 上 → "up top" family (R §4.2).
- :11 0008 `How did that come about?` is a touch formal for William. "How'd that happen?" would leave `happen?` alone on the last row. Accepted.
- :41 0038: `{p}` after `golden years,`, at a clause boundary; otherwise the page is 5 rows. The leading `{p}` matches shipped 0019's grouping.
- Glossary: none.

### 35.4 Suspected source typo (PR Flag 9)
- :44 0041 そうも彼は虫の居所が悪いらしい, where the sense, and shipped NO4_BAR/0023, is どうも.
- Census: そうも 2 / 0 / 0. The other row is NO4_ENTRANCE/0004 降りられそうもない, which is legitimate. That leaves そうも彼は 1 / 0 / 0 and どうも彼は 1 / 0 / 0.
- Rendered with 0023's words byte for byte: `It seems he's in a foul mood.`
- FLAGS F-028. Glossary: none.

## Unit script NO1.b01 (PR #34, MERGED, 2026-11-01)

Three small deck-1 rooms (NO1_CONTROLROOM, NO1_ENGINEROOM, NO1_STORAGE; 8 rows, 151 source characters, tier D, ratio 215.03): John and Judy find the engine control room, a headless body, the engine room and a looted storeroom.

Reviewed twice:
- **Round 0** (3207a4e, merged with main b01c531): CHANGES, one finding. `:9` NO1_ENGINEROOM/0002 戻って知らせましょう had taken 報告's "report" (§36.1).
- **Round 1** (3e73bb9, merged with main 3c9a181, no conflict): MERGE, squash c5f8a29. Only `:9` changed. Findings: none.

Figures (round 1):
- **Containers.** MEASURE after MERGE: NO1_CONTROLROOM.SCR 655 / 65,535 (64,880 free), NO1_ENGINEROOM 971 (64,564), NO1_STORAGE 355 (65,180). All three rooms are complete, so deck NO1 is complete. `containers negative: 0; under the reserve (2000 bytes): 0`.
- **Pages.** At most 4 rows per page (UNITCHECK: 8 rows, 0 violations; the 4 rows are at `:6` 0003). Whole store: 1,483 rows, 0 violations. MERGE: keys that never matched 0.
- **Duplicates.** CHECK compared 214 duplicate pairs and 9 tag-variant pairs, the same as without the unit. The reviewer's census compared every unit row with every dump row (exact, `{p}{w}{br}`-stripped, 【】-stripped, ！？ → ⁉, final 。 dropped): 16,688 pairs, 0 matches. The sanity twins NO5_LOCKERROOM/0001 = NO5_SHOP/0001 and NO2_TOFE_ROOM/0005 = NO3_MEDICALROOM/0001 are found.
- **Codes.** The authored `{p}{w}{br}` sequence equals the source's on 8 of 8 rows. There is no `{w}` and no `+` row. `…` counts match on 3 of 3 rows.
- **Widths.** Two lines end at an authored `{br}`: `:6` "control system." (15) and `:7` "The head can't be found." (24). No line ends in a lone "a" or "I", and no last row is a single word.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-10-31. Line citations use PROJECT.md §7's numbering in `tl/script/NO1.b01.tsv` (line = row order + 3).

### 36.1 Terms promoted from §9, the 知らせる split, and rows added
- **戻って知らせる is "tell", kept apart from 報告に戻る "report"** (PR Flag 7, round-0 finding 1).
  - Source: 戻って知らせましょう, 1 / 0 / 0 (NO1_ENGINEROOM/0002). 知らせ is 5 / 0 / 0 in all. 報告に戻 is 3 / 0 / 0 (NO1_ENGINEROOM/0003, NO4_HWL_KAIDAN/0004, NO4_BAR/0234).
  - Evidence: every shipped 知らせる is "tell / let … know / alert" (NO3_NO4/0010 "let us know", NO4_BAR/0157 "let them know", NO4_BAR/0375 "alert everyone", NO5_ENTRANCEM/0002 "We have to tell everyone…"). Every shipped 報告 is "report" (NO4_HWL_KAIDAN/0004, NO4_HWR_FRONT/0049, NO4_BAR/0234).
  - Reasoning: the literal rendering is good English, so it stands (translation_prompt.md §2). Two source verbs stay two English verbs (R §31.1, §35.3). The wave-9 §9 seed grouped them under "head back and report". It is split here.
  - Target: `:9` `The engine room… Let's head back and tell them.` (27 / 19). "head back" is 戻る, as `:10` and shipped NO4_HWR_FRONT/0049. "them" is the elided object, the rest of the party. `:10` 0003 keeps `…let's head back and report…`.
  - Glossary: two §6 rows (報告に戻る; 戻って知らせる), replacing the §9 row.
- **Promoted as seeded** (§9 → §6), byte for byte:
  - `:4` ほかには何も入っていない{p} → `There's nothing else inside.{p}` (28, one row). The source has no 。, and the "." is added as a reading. 1 / 0 / 0.
  - `:11` 使えそうな物はすでに奪われた後のようだ。{p} → `It seems anything that looked usable has already been taken.{p}` (22 / 25 / 11). そう is "looked" (R §31.1), ようだ is "seems", and the passive is kept. 奪われ is "taken"; 強奪 stays "looted" (NO3_MEDICALROOM/0003). 1 / 0 / 0.
  - 制御装置 was already promoted to §3 by #35 (R §34.1). `:6` `It seems to be the engine's control system.{br}` agrees; its "(#34)" note now says shipped.
- **Added — 首が見当たらない → `The head can't be found.`** (24), at `:7` before the authored `{br}`. 1 / 0 / 0; 首 is 7 / 0 / 0.
  - "The head" follows shipped NO3_MEDICALROOM/0007 and NO6_BRIDGE/0019.
  - The 見当たらない "in sight" phrasing of the 使えそう family, "The head is nowhere in sight." (29), wraps `sight.` alone before the `{br}`.
  - 首を飛ばされ "torn off", 首が切り離され "cut off" and 首が切断され "severed" stay separate words (R §30.2, §31.2).
- **Added — 棚には使えそうなものはなさそうだ。{p} → `The shelves seem to hold nothing that looks usable.{p}`** (24 / 26), at `:5` (PR Flag 2). This is a step-6 recast on the frame of shipped NO2_MAINSTORAGE/0030 (R §31.1).
  - Both straight placements strand a word: `There seems to be nothing on | the shelves that looks | usable.` (28 / 22 / 7) and `…nothing | that looks usable on the | shelves.` (25 / 24 / 8).
  - なさそう is "seem" and 使えそう is "looks", so both hedges are kept. なさそう 6 / 0 / 0; 1 / 0 / 0 for this sentence.
- Glossary: §6 rows added (報告に戻る, 戻って知らせる, ほかには何も入っていない, 奪われた後, 棚には…なさそう, 首が見当たらない). The §2 機関室 and §3 制御装置 notes now say shipped. The last three wave-9 §9 rows are removed, so §9 is empty.

### 36.2 Readings and speakers
- **Carried rulings applied:** `:7` どうやら化け物に襲われたようだ → `It seems it was attacked by a monster.` is byte-identical to shipped NO3_STORAGE/0004 (R §31.2): the body is "it", and どうやら…ようだ is one "seems". 化け物に襲われたよう is 2 / 0 / 0.
- `:6` なぜか正常に稼動しているようだ → `For some reason, it seems to be running normally.` "running normally" is as shipped NO4_MACHINE/0003; 正常に is 3 / 0 / 0. Both ようだ are kept ("It seems to be … / it seems to be …").
- `:8` ここは…。 → `This place…`.
- `:10` 今はここを調査するより → `rather than investigating here now`, literal.
- **Speakers** (PR Flag 6, F-009):
  - CONTROLROOM 0001–0004 and STORAGE/0001 are spk=- narration (plain だ/ようだ).
  - ENGINEROOM/0001 is unmarked: John or Judy.
  - ENGINEROOM/0002 (spk=0) and 0003 (spk=100; ましょう, addresses John) are Judy.
  - Every line is speaker-neutral in English.
- Glossary: none beyond §36.1.

## Unit script NO4_BAR_T.p02 (PR #37, MERGED, 2026-11-01)

Figures (round 1, head 4b3b4d1, squash baa917b):
- **Round 0** (6e77413): CHANGES, two one-word last rows (§37.1). **Round 1**: MERGE, only `:16 0059` and `:38 0081` changed, byte-identical to the reviewer's scratch fix.
- **Containers.** MEASURE after MERGE: NO4_BAR_T.SCR 10,274 / 65,535 (55,261 free; 56,220 after p01), tokens 493 / 1,499, 94/181 rows; NO4_BAR.SCR unchanged at 37,378. `containers negative: 0; under the reserve (2000 bytes): 0`. MERGE: keys that never matched 0.
- **Pages.** UNITCHECK: 48 rows, 0 violations, max 4 rows/page; store 1,531 rows, 0 violations. Authored code diff: 22 rows, every one in PR Flag 5. No `{w}` changed; none followed directly by text. Six F-012 `+` boundaries (0053→0054, 0061→0062, 0063→0064, 0066→0067, 0068→0069, 0073→0074), each opened with `{br}` or `{p}` at a sentence end.
- **Duplicates.** CHECK: 223 duplicate and 13 tag-variant pairs across the tree; this unit's 9 identical rows (0078, 0079, 0082, 0084, 0085, 0090, 0091, 0093, 0094) and 4 tag variants (0086, 0087, 0089, 0092) are among them. Reviewer's census (label stripped, `{p}{w}{br}` removed, final 。 dropped, ！？ → ⁉, `…。` → `…`, 眼 = 目; every unit row × every script and scene dump row): **91,104 whole-row pairs, 182,060 sentence pairs, 73 matches, 0 differ**. 0081 censused by hand (奇妙な物音 2 / 0 / 0).
- **Widths.** Lines ended by an authored `{br}` or `{w}` ≤ 27, except 0078 (28, inherited, R §1.12). Glyph counts 48 / 48 match.

Census counts are rows per store (script / scene / system), from the reviewer's grep of `dumps/` on 2026-11-01. Line citations are in `tl/script/NO4_BAR_T.p02.tsv` (line = row order + 3).

### 37.1 Sentence twins keep the shipped words; the two orphans (round-0 findings 1–2)
- **:38 0081** だが、わしは奇妙な物音で目を覚ました。{w}{br} = shipped NO4_BAR/0055 with だが、 in front.
  - Round 0 had `But a strange noise woke me.` (28 before `{w}`), the noise as subject, offered as a §2.1 step-6 restructure to avoid `noise.` alone.
  - Ruling: R §35.2 binds sentence twins inside longer rows to the shipped words; a rewording is allowed only where a lone "a" or "I" would end a line. Every rendering with "I" as subject strands `noise.`, so R §1.12 rule 1 keeps the literal words with the orphan flagged, as #36's 0023 `mind.`. The §2.1 ladder applies only to units over budget.
  - Target: `But I awoke to a strange noise.{w}{br}` (24 / 6); the page from 0080's `{p}` holds 28, 24, 24, 6 = 4 rows.
  - The round-0 review's `Yet a strange noise woke me.` measures 28, not 27 (translator's correction); immaterial.
- **:16 0059** (whole-row twin of NO4_BAR/0040) wrapped to a last row of `spider-shaped?` alone, unflagged. A label `{br}`, as at 0055, 0058, 0061, avoids it without changing a word: `【Miller】{br}Mr. Collison, what kind of creature is this monster? Might it be spider-shaped?{p}` (8 / 26 / 25 / 26, 4 rows).
- **Label `{br}`** (label alone on the first row) is accepted wherever the shipped words would otherwise leave a one-word last row: 0055, 0058, 0059, 0061. Precedent: the source's own NO4_TOOL_ROOM `【ミラー】{br}`.
- **0057** adds そいつらはまだ船内にいるんだろ？ to shipped 0038; the shared part keeps 0038's words (`This information affects our safety. Tell me the truth.`).
- Glossary: none. The PR's label row (【Collison】 · 【Oakland】 · 【Wolg】 · 【Heming】) is already on main from #36 (R §35.1).

### 37.2 The two clicks at :49 0092 (PR Flag 5)
- 0090, 0091, 0093 are exact twins of NO4_BAR/0062, 0063, 0065, and 0092's text is fixed by its tag-variant pairing with 0064. The page from 0089's `{w}{br}` is full (4 rows) at 0091, and 0092 + 0093 + the cursor row make 5. So clicks can only go in 0092.
- The two options: one click mid-clause (`For the ship had already{p}sunk deep…`), or a leading `{p}` plus `{p}` before the ending `{br}`, giving pages 4 / 2 / 4, the third opening on a blank row.
- Ruling: the two clicks at sentence ends. R §2.4 prefers a leading `{p}` and avoids a blank first row where an alternative exists; none does here. The round-0 PR cited R §26.2, whose 0085 is a leading `{p}` before text; round 1 corrected the citation to R §2.4.
- First `{p}{br}` in the project (0 / 0 / 0 in the dumps). Joins F-010's in-game checks.
- Other movable codes: `{p}` at sentence ends 0047, 0056 (5 rows otherwise; 0047 also a lone "a"); `{br}` at sentence ends 0050, 0051, 0070, 0071 (a split "Old | man", lone "a"/"A", a one-word last row); leading `{p}` 0062 (a `+` row, 5 rows otherwise), 0080, 0083 (R §2.4); 0086, 0087 carry shipped 0059/0060's `{p}`; 0094 copies shipped 0066's leading `{p}`. All approved.

### 37.3 Readings, speakers, recurrences
- Speakers from the labels and content (F-009); every row is `spk=-`. 0078–0094 are Collison's unlabelled narration (わし, じゃ), continuing from 0077.
- Final 。 missing from 15 draft rows (PR Flag 2): the shipped `.`/`?` is kept so twins match.
- No shipped counterpart, rendered literally: 0057's added clause, 0072 `【Wolg】Ngh…!` (§6 くっ), 0080 はずじゃろう → "must have slept soundly", 0083 `After a while, I realized the sound was coming from outside the ship.`, 0088 強いなんてものじゃない → `Strong is hardly the word.` None recurs.
- **Untranslated recurrence:** 気持ちはわかる 3 / 0 / 0 (NO4_BAR/0037, this unit's 0056, NO4_HWR_FRONT_DOWN_T/0003 【ヘイミング】). NO4_T reuses `I understand how you feel.` (F-008).
- Glossary: none.
