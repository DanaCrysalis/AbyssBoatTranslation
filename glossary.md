# Glossary — Abyss Boat

<!-- Read in full before every unit, so keep it SHORT: one row per term, the Note column at most one
line. Reasoning, evidence and history go in rulings.md, referenced in the Ruling column as "R §k.n".
Coverage is what STATUS prints, not a line here — a hand-kept coverage note goes stale. -->

**Every entry here is fixed.** Use the target form exactly as written, everywhere. To change one,
follow `translation_prompt.md` §4.3: state the correction explicitly, list every shipped line that
must change, and write the reasoning in `rulings.md`. The reviewer is the only writer of this file;
translators propose rows in their PR's Glossary additions.

**Columns.** Source · Variants (every other spelling the dumps use, including source typos — the
duplicate census pairs them) · Target · Cols (measured column count of the target) · Cap (fixed-width
limit if the term lives in a table) · Note (≤ 1 line; scope such as "capitalised as a place name,
lowercase as a common noun" goes here so a gate does not misread the row) · Ruling.

## 1. People
| Source | Variants | Target | Cols | Cap | Note | Ruling |
|---|---|---|---|---|---|---|
| ジュディ | ジュディ・アルセラ | Judy; full name Judy Arsela | 4; 11 | — | アルセラ occurs only in the full name | R §1.1 |
| ロブ・コリスン | コリスン | Rob Collison; コリスン alone: Collison | 12; 8 | — | ロブ occurs only in the full name | R §1.1 |
| ビル・オークランド | オークランド · ビル | Bill Oakland; オークランド alone: Oakland; ビル alone: Bill | 12; 7; 4 | — | ビル alone once, SCN046A2/01 | R §1.1 |
| ウィリアム | — | William | 7 | — | | R §1.1 |
| ジャック・ウォルグ | ウォルグ | Jack Wolg; ウォルグ alone: Wolg | 9; 4 | — | ジャック occurs only in the full name | R §1.1 |
| レベッカ・ミラー | ミラー | Rebecca Miller; ミラー alone: Miller | 14; 6 | — | レベッカ occurs only in the full name | R §1.1 |
| コリスンさん | コリスンさんたち | Mr. Collison; たち: Mr. Collison and the others (in address: your group, Mr. Collison) | 12; 27 (24) | — | surname + さん → title + surname; never split from the name at a wrap | R §1.2 |
| オークランドさん | — | Mr. Oakland | 11 | — | as コリスンさん | R §1.2 |
| ミラーさん | — | Miss Miller | 11 | — | Collison's form (the only speaker of it) | R §1.2 |
| ジョン | — | John | 4 | — | the player, Oakland's son; `{name}` is unused, the source spells the name out | R §3.1 |
| ヘイミング | ヘイミングたち | Heming; たち: Heming and the others (NO4_BAR/0232 "Heming's team" stands in context) | 6; 21 (13) | — | older salvager; たち 1 / 1 / 0, per the «Name»たち row | R §3.1, §5.1, §9.1 |
| ウォルグさん | — | Mr. Wolg | 8 | — | as コリスンさん; never split from the name at a wrap; Collison's form | R §5.1 |
| «Name»たち | ウォルグたち · ヘイミングたち · ジョンたち | «Name» and the others ("Wolg and the others") | 19 (Wolg, John); 21 (Heming) | — | default for a name + たち; in context where a line wants it (0232); コリスンさんたち is its own row | R §9.1 |

## 2. Factions, places, ranks
| Source | Variants | Target | Cols | Cap | Note | Ruling |
|---|---|---|---|---|---|---|
| サルベージャー | サルベージ | salvagers (sg. salvager) | 9 (8) | — | サルベージ, the work: "salvage" | R §1.9 |
| 沈没船引き揚げ業者 | 沈没船のサルベージ業者 · 沈没船を引き上げる業者 | shipwreck salvage firm | 22 | — | other phrasings in context, with "shipwreck salvage" | R §1.9 |
| 責任者 | — | the one in charge | 17 | — | keeps William's echo, 0022 | R §1.9 |
| 学者 | 学者さん | scientist | 9 | — | さん dropped, carried by tone (R §1.2) | R §1.9 |
| 海洋生物学者 | — | marine biologist | 16 | — | | R §1.9 |
| フィラデルフィア | — | Philadelphia | 12 | — | | R §1.9 |
| 食料庫 | — | the food storeroom | 18 | — | lowercase in dialogue; the room name (rooms/044) is decided with the system store | R §2.1 |
| 下層 | — | the lower decks | 15 | — | the ship's own lower decks, above the party now the ship is capsized | R §2.1 |
| フロア | フロアー | floor | 5 | — | 下層のフロア → "a floor on the lower decks" | R §2.1 |
| ホール | — | the hall | 8 | — | lowercase in dialogue; エントランスホール is its own row (§9) | R §2.1 |
| 甲板 | — | deck ("on deck") | 4 | — | the ship's open deck; never デッキ (第Nデッキ → "Deck N") | R §2.1 |
| 社長 | — | the boss | 8 | — | Oakland, as his crew calls him; in direct address "boss" | R §3.1 |
| 上の連中 | — | the people up top | 17 | — | the salvagers' surface crew; 上 alone for the same crew takes the same words (SCN002/05); 下の連中 is not fixed | R §3.2, §4.2 |
| 海上 | — | the surface | 11 | — | "up on the surface" in p01 0009 | R §3.1 |
| 第Nデッキ | 第２デッキ … 第６デッキ (full-width digit) | Deck N ("Deck 4") | 6 | 10 (deck names, F-006) | capitalised with an Arabic numeral; デッキ alone (このデッキ, 下のデッキ) is lowercase "deck" in context | R §5.1 |
| 元警官 | — | ex-policeman | 12 | — | Wolg's past; 警官 alone in context (Miller's sarcastic "cop", NO4_BAR/0231) | R §5.1 |
| 生き残り | 生き残りグループ | survivor(s); 生き残りグループ: survivor group | 8 (9); 14 | — | the people still alive aboard | R §5.1 |
| 客船 | — | passenger ship | 14 | — | this ship; 例の客船 → "that passenger ship" (0279) | R §6.1 |
| 便所 | — | the toilet | 10 | — | lowercase; Collison's word (0292, NO4_HWR_FRONT/0011) | R §6.1 |
| 通風孔 | — | air vent; "the vent" / "vent(s)" after first mention | 8; 8 | — | lowercase; "the air vent" at a scene's first mention (NO4_BAR/0294), then "vent" | R §7.1 |
| 中央ダクト | — | the central duct | 16 | — | lowercase; NO4_BAR/0302 only | R §7.1 |

## 3. Items, currency, mechanics
| Source | Variants | Target | Cols | Cap | Note | Ruling |
|---|---|---|---|---|---|---|
| 潜水装備 | — | diving gear | 11 | — | | R §1.9 |
| 電波 | — | radio waves | 11 | — | ＶＬＦ帯の電波 → "VLF-band radio waves" | R §3.1 |
| 超音波 | — | ultrasound | 10 | — | | R §3.1 |
| 長波 | — | longwave | 8 | — | | R §3.1 |
| 無線装置 | — | radio equipment | 15 | — | 無線機 and 無線室 are §9 rows; 装置 and 設備 alone are not fixed | R §3.1 |
| 潜水艇 | — | submersible | 11 | — | never "submarine" (潜水艦, 0 rows) | R §3.1 |
| 地上用の設備 | — | land-based equipment | 20 | — | NO4_BAR/0175 and SCN011/04 | R §3.2 |
| 回転 (the ship) | — | roll over (noun: roll) | 9 (4) | — | the capsized ship turning on its long axis | R §3.1 |
| 弾切れ | — | out of ammo | 11 | — | SCN029/02, SCN046A1/07; items/000 (blocked) in context | R §4.1 |
| 薬品 | — | medicine | 8 | — | NO4_BAR/0226, NO3_MEDICALROOM/0002 | R §5.1 |
| ソナー | — | the sonar | 9 | — | ソナーの反応 → "the contact" … on/from the sonar (0272); ソナーに反応が無い in context | R §6.1 |
| ハンドガン | — | handgun | 7 | — | never "pistol"; ハンドガン程度 → "a mere handgun" (0343); equip/000, items/000 (blocked) take the same word | R §7.1 |
| 鞄 | カバン · 旅行鞄 | bag; 旅行鞄: suitcase | 3; 8 | — | 鞄 and カバン one word (NO4_TOOL_ROOM/0003 カバンごと in context); plural as the line needs | R §8.1 |

## 4. Classes, units, system terms
| Source | Variants | Target | Cols | Cap | Note | Ruling |
|---|---|---|---|---|---|---|
| セーブする · セーブしない | — | Save · Don't save | 4 · 10 | 27 | the save choice pair (choice rows, §8) | R §1.9 |

## 5. Verbal tics — decided, never mix
<!-- What is fixed is the word; punctuation follows the source line. -->
| Speaker | Source tic | Treatment | Note | Ruling |
|---|---|---|---|---|

## 6. Stock phrases and interjections
| Source | Variants | Target | Cols | Note | Ruling |
|---|---|---|---|---|---|
| ヤツ | — | he / him / his | 2 / 3 / 3 | the monster or the killer only, never "it"; a type of person (〜なヤツ) in context | R §1.7 |
| 化け物 | 怪物 | monster | 7 | synonyms, one target; NO4_BAR/0083 has both: repeat "monster" | R §1.8 |
| 殺人鬼 | — | the killer | 10 | "a … killer" with a modifier (いかれた殺人鬼); the 鬼 pun at NO4_HWR_FRONT_UP_T/0004 in context | R §4.1 |
| じいさん | 爺さん · 爺 · じじい | old man | 7 | "Old man," at a sentence start; 爺 and じじい (pejorative) added 2026-10-06 | R §1.9, §3.3 |
| ふん | — | Hmph | 4 | the interjection only (not 踏んで); punctuation per source: ふん、 → "Hmph," | R §3.2 |
| くっ | — | Ngh | 3 | grunt of strain or frustration; punctuation per source (くっ、 → "Ngh,"; くっ…！ → "Ngh…!") | R §4.1 |
| くそ | くそっ · くそおおおっ | Damn | 4 | the curse only (not ともかくそんな); elongation stretches the vowel (くそおおおっ‼ in context) | R §4.1 |
| きゃあ…っ (scream) | — | "A" for きゃ, one "a" per あ, "h" for っ | — | SCN034/02 きゃ+あ×10+っ‼ → "Aaaaaaaaaaah‼" (13); ‼ ⁉ as the source | R §4.1 |
| ここまでの状況をセーブできます。セーブしますか？ | — | You can save your progress so far. Do you want to save? | 55 | the save prompt, 21 rows; wraps 26 + 28 | R §3.4 |
| お嬢さん | — | young lady | 10 | Collison to Miller | R §1.9 |
| 虫の居所が悪い | 虫の居所 | in a foul mood; the echo: "Foul mood?" | 14; 10 | | R §1.9 |
| 一匹 | １匹 | a single beast | 14 | only where the line turns on the animal counter (0033–0034); else a plain "one" | R §1.5 |
| 分身 | — | part of him | 11 | the young as pieces of the monster itself | R §1.9 |
| 部屋 | — | room | 4 | every kind of room, passenger cabins too; "cabin" is キャビン | R §1.6 |
| 大部屋 | — | large room | 10 | as 部屋; the shared rooms groups held out in (0089) | R §2.1 |
| 死体 | — | body | 4 | a dead body, person or unknown; 死骸 (carcass) and 遺体 (remains) are separate rows | R §6.1 |
| 見張り | 見張りを立てる · 見張りにつく · 見張りの交代 · 見張りの順番 | watch: "stand watch", "keep watch", "change of watch" | 5 | the duty, not the person ("lookout" only if a line names one) | R §6.1 |
| 遺体 | — | remains | 7 | a person's dead body, respectful (0294 "We found no remains"); 死体 is "body", 死骸 "carcass" | R §7.1, §8.1 |
| 死骸 | — | carcass | 7 | a creature's dead body (0387; 0455 化け物の死骸 → "the monster's carcass"); never "corpse" | R §8.1 |
| モンスター | 小型モンスター · 小さいタイプのモンスター · 小さなモンスター · 小さいモンスター · 小モンスター | monster; the small kind: small monster(s) | 7; 13 (14) | — | synonym of 化け物 · 怪物, one target; 小モンスター is hints/005 (blocked) | R §8.1 |
| 蜘蛛 | クモ | spider | 6 | both spellings, one word; クモのような形 → "spider-shaped" (0040); 蜘蛛の巣 (NO5_BANK/0006) in context | R §7.1 |
| 昆虫 | — | insect | 6 | 昆虫採集 is its own row ("bug collecting") | R §7.1, §8.1 |
| 昆虫採集 | — | bug collecting | 14 | NO4_BAR/0389 only ("No time for bug collecting.") | R §8.1 |
| 節足動物門鋏角亜門 | — | phylum Arthropoda, subphylum Chelicerata | 40 | Miller's taxonomy, NO4_BAR/0352 only; lowercase ranks, capitalised taxa | R §8.1 |
| フッ | — | Heh | 3 | Wolg's wry scoff; punctuation per source (フッ… → "Heh…", フッ、 → "Heh,"); not グフッ (SCN038B/17, a grunt) | R §7.1 |
| クッ · ククッ · クカカカカカカッ | クッ、ククッ、クカカカカカカッ。 · クッ、ククッ。 · ククッ、クカカカカカカッ | Heh · Heh-heh · Kahahahahaha; run together: "Heh, heh-heh, kahahahahaha." | 3 · 7 · 12; 27 | the killer's laugh, 6 / 7 / 0 rows; one syllable per カ; punctuation per source; not くっ (Ngh) | R §9.1 |
| うおおおっ (battle cry) | — | "R" for う, one "a" per お, "h" for っ | — | SCN038B/10 う+お×11+っ‼ → "Raaaaaaaaaaah‼" (14); the きゃあ…っ pattern; ‼ ⁉ as the source | R §9.1 |
| ～ (long-vowel mark) | — | repeat the vowel once per ～; a final っ after a word is dropped | — | SCN038B/11 行け～～～っ。 → "Goooo." (Go + 3 o); SCN046A3/01 in context; 0 / 2 / 0 | R §9.1 |
| グフッ | — | Guh | 3 | grunt as he is struck, SCN038B/17 only ("——Guh‼"); not フッ | R §9.1 |
| 俺様 | — | no fixed word: the killer's swagger is carried by register | — | 俺様の…… → "My very own……" (SCN038_5C1/06); 俺様の女神 → "my very own goddess" (NO2_MAINSTORAGE/0003); 3 / 4 / 0 | R §9.1 |

## 7. Register per character
| Character | Register | Contractions? | Markers | Ruling |
|---|---|---|---|---|
| Rob Collison | elderly retiree; courteous, old-fashioned diction; じゃ/わし/おる carried by word choice, no dialect spelling | yes, moderate | "of late", "Just so.", "a most reliable fellow", "You've friends…", "Now listen", "By all means."; Miller is "young lady" / "Miss Miller" | R §1.10 |
| Bill Oakland | salvage boss; formal and measured with strangers (我々/私, plain だ); his わし to his crew stays plain, never folksy | yes | "We're salvagers.", "No doubt about it.", "I don't quite follow.", "Quite right." | R §1.10 |
| William | hostile survivor; rough, blunt, drops subjects (ぜ/ねえ/よ) | yes, heavy; standard contractions only, no eye dialect ('em, ain't, gonna) | "You'd better not…", "Means nothing if…", "Are you an idiot or what⁉", "Isn't that nice." | R §1.10 |
| Jack Wolg | salvager, ex-policeman (NO3_NO4); direct, terse, serious (俺) | yes | calls Collison "old man"; "Old man, I'm being serious.", "Tell me the truth." | R §1.10 |
| Rebecca Miller | marine biologist; articulate, assertive; わ/かしら/のよ carried by modal softening and firmness, never by markers | yes | "Might it be…?", "Just so you know", "Suit yourself!" | R §1.10 |
| Heming | older salvager; calm, mildly old-fashioned politeness (ませんかな) | yes | "might we hear…", "Believe what you will", "Don't get so heated." | R §1.10 |

## 8. Fixed-width caps
<!-- tables in the game whose entries have a hard width: unit names, class names, item names, the player name -->
| Table | Cap | Note |
|---|---|---|
| room names (`system/rooms`) | 14 characters | exe slot 29 bytes; system store blocked (F-006) |
| deck names (`system/menus`, `decks/*`) | 10 characters | exe slot 21 bytes; blocked (F-006) |
| camp-menu help (`camp/*`) | 27 characters, each `{br}` costs half a character | exe slot 54 bytes; blocked (F-006) |
| option help (`options/*`) · equip messages (`equip/*`) · hints (`hints/*`) | 44 · 39 · 39 characters | exe slots 89 · 79 · 79 bytes; blocked (F-006) |
| item name + description (`items/*`) | 43 characters including `【name】` and `{br}`s | exe slot 87 bytes; blocked (F-006) |
| choice options (script `choice` rows) | 28 columns, 27 preferred | one line, not wrapped; assumed (F-003) |
| player name (`{name}`) | "John", 4 columns | written by BUILD; the source spells ジョン out instead |

## 9. PROVISIONAL — seen in the dumps, not yet rendered
<!-- Seeded per wave by the coordinator (`glossary: provisional seeds for wave N`). Rows here are
NOT decisions. The first translator to render one promotes it in the PR's Glossary additions, saying
so; the reviewer moves the row up into its section in the integration commit. -->
| Source | Variants | Proposed | Alternatives | Where seen | Wave |
|---|---|---|---|---|---|
| 右舷 · 左舷 | — | starboard · port | — | room names, dialogue | setup |
| 無線機 | — | the radio | the radio set | NO4_HWR_FRONT/0103 (near-duplicate of NO4_BAR/0171, R §3.6); 1 / 0 / 0 | 1 |
| 無線室 | — | the radio room | — | NO6_BRIDGE/0001, 0006; rooms/107, items/011, hints/001–002 (cap 14 as a room name); 2 / 0 / 4 | 1 |
| エントランスホール | — | entrance hall | lobby | NO4_4102/0001, NO4_HWL_BACK/0017, NO4_HWR_FRONT/0100 …; 6 / 0 / 2 rows (rooms/066, 084); ホール alone is fixed in §2 (R §2.1) | 1 |
| 操舵室 | — | the wheelhouse (操舵室のデッキ → "the wheelhouse deck") | the helm | NO4_BAR/0428, 0437; ブリッジ is "the bridge" (rooms/108); 2 / 0 / 0 | 3 |
| バリケード | — | barricade | — | NO4_BAR/0421–0444, NO4_HWL_KAIDAN/0005–0006; 5 / 0 / 0 | 3 |
| チェーンカッター | — | chain cutter | bolt cutters | NO4_BAR/0444, NO6_TOOLROOM/0001, hints/006; 2 / 0 / 1 | 3 |
| 倉庫 | 第Nデッキ倉庫 | storeroom ("the Deck 3 storeroom") | storage room | NO4_BAR/0424; rooms/053, 069, 105, items/013; 1 / 0 / 4 | 3 |
| 工具 | — | tools | — | NO4_BAR/0423–0424; 道具 (NO4_HWL_KAIDAN/0006) in context; 2 / 0 / 0 | 3 |
| マガジン | — | magazine ("spare magazine") | clip | NO4_HWR_FRONT/0020, NO3_NO4/0010; 2 / 0 / 0 | 3 |
| Ｒｅｔｒｙ？ | — | Retry? (the source's own English, kept) | — | NO4_HWR_FRONT/0036, NO2_MAINSTORAGE/0007; 2 / 0 / 0 | 3 |
| はい · いいえ (choice) | — | Yes · No | — | choice rows, NO4_HWR_FRONT/s11 s12 s17 s18 …; 8 / 0 / 0 each as choices | 3 |
| 妹 | 妹さん | sister (William's; "my sister", "his sister") | little sister | NO4_HWR_FRONT/0031–0032, 0075–0082; R §8 "To my sister"; 5 / 1 / 0 | 3 |
| 『フロアーインフォメーション』 · パーサーオフィス · メインダイニング · ラウンジ · ビアー＆ラガーズ · キャビン | — | "Floor Information" · Purser's Office · Main Dining · Lounge · Beer & Lagers · Cabins | Purser · Dining | the deck sign NO4_HWR_FRONT/0097–0100 = NO4_HWL_BACK/0014–0017 = NO4_HWL_BACK2/0010–0013, byte-identical; `{br}`-ended lines, 27 cols with the leading space; 3 / 0 / 1 | 3 |
| クライド | — | Clyde | — | SCN046A2/02, Oakland to the one who betrays him (likely Heming's given name); 0 / 1 / 0 | 3 |
| ジェイク・ノーマン | — | Jake Norman | — | SCN046B1/03, Wolg naming the killer; 0 / 1 / 0 | 3 |
| ウスノロ | — | dimwit ("my dear dimwit") | slowpoke | SCN046B1/02, B2/06, B2/07, the killer's word for his victims; 0 / 3 / 0 | 3 |
| メス · 売女 | — | the bitch · whore | that female | SCN046B1/10–11 (the killer on Judy), B2/07; 0 / 2 / 0 · 0 / 1 / 0 | 3 |
| 神 · 生肝 | — | god · raw liver | — | SCN046B2/02–04; 女神 is in the 俺様 row (§6); 4 / 4 / 0 · 0 / 1 / 0 | 3 |

## 10. Open questions
<!-- one line each, with the FLAGS id. A closed question is deleted here; its answer stays in rulings.md. -->
