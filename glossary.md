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

## 2. Factions, places, ranks
| Source | Variants | Target | Cols | Cap | Note | Ruling |
|---|---|---|---|---|---|---|

## 3. Items, currency, mechanics
| Source | Variants | Target | Cols | Cap | Note | Ruling |
|---|---|---|---|---|---|---|

## 4. Classes, units, system terms
| Source | Variants | Target | Cols | Cap | Note | Ruling |
|---|---|---|---|---|---|---|

## 5. Verbal tics — decided, never mix
<!-- What is fixed is the word; punctuation follows the source line. -->
| Speaker | Source tic | Treatment | Note | Ruling |
|---|---|---|---|---|

## 6. Stock phrases and interjections
| Source | Variants | Target | Cols | Note | Ruling |
|---|---|---|---|---|---|

## 7. Register per character
| Character | Register | Contractions? | Markers | Ruling |
|---|---|---|---|---|

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
| ジョン | — | John | — | 95 lines; the player | setup |
| ジュディ | ジュディ・アルセラ | Judy; full name Judy Arsela | Alsera, Arcella | NO4_BAR/0027 (full name); 47 | setup |
| ロブ・コリスン | コリスン | Rob Collison | — | NO4_BAR/0019; 43 | setup |
| ビル・オークランド | オークランド · ビル | Bill Oakland | — | NO4_BAR/0021; 56 | setup |
| ウィリアム | — | William | — | NO4_BAR/0015; 34 | setup |
| ジャック・ウォルグ | ウォルグ | Jack Wolg | Walg, Volg | NO4_BAR/0032; 66 | setup |
| レベッカ・ミラー | ミラー | Rebecca Miller | — | NO4_BAR/0042; 51 | setup |
| ヘイミング | — | Heming | Hayming, Haming | NO3_CHAPEL/0036; 35 (not in NO4_BAR.p01) | setup |
| サルベージャー | サルベージ | salvager(s) | salvage crew | NO4_BAR/0002; 3 | setup |
| 社長 | — | the boss (Oakland, as his crew calls him) | the president | 13 (not in NO4_BAR.p01) | setup |
| 責任者 | — | the one in charge | the leader | NO4_BAR/0021–0022; 3 | setup |
| ヤツ | — | him (the killer) | that guy, it | 50 | setup |
| 殺人鬼 | — | the killer | murderer | 7 | setup |
| 化け物 | 怪物 | monster | creature, thing | 59 + 21 | setup |
| じいさん | 爺さん | old man | gramps | NO4_BAR/0014; 10 | setup |
| セーブする · セーブしない | — | Save · Don't save | — | choice pairs; 84 "セーブ" | setup |
| 第Nデッキ | — | Deck N | the Nth deck | every deck | setup |
| 右舷 · 左舷 | — | starboard · port | — | room names, dialogue | setup |
| フィラデルフィア | — | Philadelphia | — | NO4_BAR/0054 | setup |

## 10. Open questions
<!-- one line each, with the FLAGS id. A closed question is deleted here; its answer stays in rulings.md. -->
