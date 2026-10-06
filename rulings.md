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
