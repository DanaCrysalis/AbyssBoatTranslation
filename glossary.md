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
| クライド | — | Clyde | 5 | — | Heming's given name, Oakland's address to him (SCN046A2/02); 0 / 1 / 0 | R §13.1 |
| ジェイク・ノーマン | — | Jake Norman | 11 | — | the killer's name (Wolg, SCN046B1/03); ジェイク, ノーマン occur only in the full name; 0 / 1 / 0 | R §13.1 |
| 【女】 (label in a message) | — | 【Woman】 | 7 | — | brackets kept, in shipped rooms too (NO4_HWR_FRONT/0123, 0129) and in the `_T` files; Judy before she is named; 16 / 0 / 0 | R §14.1 |
| 【ミラー】 · 【ジュディ】 (labels in a message) | — | 【Miller】 · 【Judy】 | 8 · 6 | — | brackets kept, as 【女】 and shipped SCN002OLD/04, 06; NO4_TOOL_ROOM p01–p02 and the `_T` files; 30 / 2 / 0 · 16 / 0 / 0 | R §18.1 |

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
| ホール | — | the hall | 8 | — | lowercase in dialogue; エントランスホール is its own row (§2) | R §2.1 |
| 甲板 | — | deck ("on deck") | 4 | — | the ship's open deck; never デッキ (第Nデッキ → "Deck N") | R §2.1 |
| 社長 | — | the boss | 8 | — | Oakland, as his crew calls him; in direct address "boss" | R §3.1 |
| 雇い主 | — | employer | 8 | — | Oakland as employer of his crew and of Miller (NO4_BAR/0127, NO4_MACHINER90/0036; NO4_BAR_T/0162 copies 0127); 3 / 0 / 0 | R §16.1 |
| 上の連中 | — | the people up top | 17 | — | the salvagers' surface crew; 上 alone for the same crew takes the same words (SCN002/05); 下の連中 is not fixed | R §3.2, §4.2 |
| 海上 | — | the surface | 11 | — | "up on the surface" in p01 0009 | R §3.1 |
| 第Nデッキ | 第２デッキ … 第６デッキ (full-width digit) | Deck N ("Deck 4") | 6 | 10 (deck names, F-006) | capitalised with an Arabic numeral; デッキ alone (このデッキ, 下のデッキ) is lowercase "deck" in context | R §5.1 |
| 元警官 | — | ex-policeman | 12 | — | Wolg's past; 警官 alone in context (Miller's sarcastic "cop", NO4_BAR/0231) | R §5.1 |
| 警察 | 警察を辞めた | the police; 警察を辞めた: quit the police force | 10; 21 | — | Wolg's past: NO3_NO4/0017 "The reason why I quit the police force……", 0041 the same words; 警官 alone in context (NO3_NO4/0021 "cop"); 2 / 0 / 0 | R §27.1, §29.1 |
| 生き残り | 生き残りグループ | survivor(s); 生き残りグループ: survivor group | 8 (9); 14 | — | the people still alive aboard | R §5.1 |
| 生存者 | — | survivor(s) | 8 (9) | — | same word as 生き残り; NO4_HWL_FRONT/0008 "there may be no survivors left"; 1 / 0 / 0 | R §21.1 |
| 乗客 | — | passenger(s) | 10 (9) | — | as shipped NO4_BAR/0028, 0094, 0191, 0198, 0393; NO4_HWR_FRONT/0122 "a passenger on board this ship"; 15 / 0 / 0 | R §14.1 |
| 乗組員 | 乗組員の制服 | crew member(s); the crew; 乗組員の制服: crew uniforms | 11 (12); 8; 13 | — | the ship's own crew, never the salvagers; NO4_STORAGE/0004 "Inside are crew uniforms."; 1 / 0 / 0 | R §21.1 |
| 客船 | — | passenger ship | 14 | — | this ship; 例の客船 → "that passenger ship" (0279) | R §6.1 |
| 船体 | — | the hull | 8 | — | lowercase; 船 alone stays "the ship"; a repeat in one sentence may take "it" (NO4_MACHINER90/0098); SCN047C1/05 "the vessel" in context, referent left open (alien ship or the passenger ship); 5 / 1 / 0 | R §15.1, §17.1 |
| 便所 | — | the toilet | 10 | — | lowercase; Collison's word (0292, NO4_HWR_FRONT/0011) | R §6.1 |
| 通風孔 | — | air vent; "the vent" / "vent(s)" after first mention | 8; 8 | — | lowercase; "the air vent" at a scene's first mention (NO4_BAR/0294), then "vent" | R §7.1 |
| 中央ダクト | — | the central duct | 16 | — | lowercase; NO4_BAR/0302 only | R §7.1 |
| 操舵室 | 操舵室のデッキ | the wheelhouse; 操舵室のデッキ: the wheelhouse deck | 14; 19 | — | lowercase in dialogue; never "the bridge" (ブリッジ, rooms/108); 2 / 0 / 0 | R §11.1 |
| ブリッジ | — | the bridge; room name: Bridge | 10; 6 | 14 (rooms/108, F-006) | lowercase in dialogue (NO4_MACHINER90/0019, 0020, 0028, 0029; NO6_BRIDGE/0017); 操舵室 stays "the wheelhouse"; 5 / 0 / 1 | R §16.1 |
| 倉庫 | 第Nデッキ倉庫 | storeroom ("the storeroom"; "the Deck 3 storeroom") | 9 | 14 (room names, F-006) | lowercase in dialogue; 食料庫 stays "the food storeroom"; "Deck 3 Storeroom" (16) is over the room cap (F-020) | R §11.1 |
| 右舷 · 左舷 | — | starboard · port | 9 · 4 | — | lowercase in dialogue (NO4_HWR_FRONT/0096); 1 / 0 / 9 · 1 / 0 / 5; room names (第Nデッキ右舷廊下 …) over cap 14 in any full form (F-021) | R §12.1 |
| エントランスホール | — | entrance hall; on a sign or as a room name: Entrance Hall | 13 | 14 (rooms/066, 084) | lowercase in dialogue and narration (NO4_4102/0001, NO4_STORAGE/0002); 6 / 0 / 2 | R §12.1 |
| フロアーインフォメーション | 『フロアーインフォメーション』 | "Floor Information" (the deck-sign title) | 19 | — | 4 / 0 / 0; sign entries joined by unspaced "/", ≤ 27 per `{br}` row, indent dropped (F-022) | R §12.1 |
| パーサーオフィス | — | Purser's Office | 15 | 14 (rooms/065, F-021) | capitalised, a sign entry; 3 / 0 / 1 | R §12.1 |
| メインダイニング | — | Main Dining | 11 | — | capitalised, a sign entry; 3 / 0 / 0 | R §12.1 |
| ラウンジ | — | Lounge | 6 | — | capitalised, a sign entry; 3 / 0 / 0 | R §12.1 |
| ビアー＆ラガーズ | 『ビアー＆ラガーズ』 | Beer & Lagers | 13 | — | the bar's name, capitalised; 4 / 0 / 0 (NO4_HWR_FRONT/0102 `"Beer & Lagers," it reads.`) | R §12.1 |
| キャビン | キャビンＮＮＮＮ (rooms/*) | cabin; on the sign: Cabins; room names: Cabin NNNN | 5; 6; 10 | 14 (room names) | 部屋 stays "room" (R §1.6); 3 / 0 / 15 | R §1.6, §12.1 |
| 売店 | 売店のカウンター | the shop; 売店のカウンター: the shop counter | 8; 16 | — | lowercase; NO4_HWL_BACK/0018 = NO4_HWL_BACK2/0014 `The shop counter, it seems.`; the 両替所 frame is not made parallel (R §20.1); 2 / 0 / 0 | R §20.1 |
| 両替所 | 両替所のカウンター | the currency exchange; 両替所のカウンター: the exchange counter | 21; 20 | — | lowercase; NO4_P_OFFICE/0012 `This seems to be the exchange counter.{br}Hard to tell what's inside.{p}`, not parallel with 売店 (R §20.1); 1 / 0 / 0 | R §20.1, §21.1 |
| 通信室 | — | the communications room | 23 | — | lowercase; NO5_ENTRANCEL/0004 only; never 無線室 "the radio room" (§2); 1 / 0 / 0 | R §22.1 |
| 無線室 | 無線室の鍵 (items/011) | the radio room; room name: Radio Room | 14; 10 | 14 (rooms/107, F-006) | lowercase in dialogue (NO6_BRIDGE/0001, 0006); 通信室 stays "the communications room"; hints/001–002, items/011 blocked; 2 / 0 / 4 | R §23.1 |
| 銀行 | — | a bank; on the sign: Bank | 6; 4 | 14 (rooms/088, F-006) | lowercase in narration (NO5_ENTRANCEM/0011 "A bank seems to lie ahead"), capitalised on the sign (NO5_HW_R/0010); 2 / 0 / 1 | R §22.1 |
| 雑貨屋 | — | a general store; on the sign: General Store | 15; 13 | 14 (rooms/082, F-006) | lowercase in narration (NO5_ENTRANCEM/0012), capitalised on the sign (NO5_HW_R/0009 `Entrance Hall/General Store`); never "sundries shop"; 2 / 0 / 1 | R §22.1 |
| カフェ · スポーツジム | — | Cafe · Gym (sign entries) | 4 · 3 | — | capitalised, sign entries, NO5_HW_R/0010 `Bank/Cafe/Gym,` only; no é (charset); not "Sports Gym"; 1 / 0 / 0 each | R §22.1 |
| ショップ | — | the shop (same word as 売店) | 8 | — | lowercase; NO5_SHOP/0002 ショップの備品 → "the shop's equipment"; 1 / 0 / 0 | R §22.1 |
| 教会 | — | the chapel; "a chapel" at the discovery (NO3_CHAPEL/0001); room name: Chapel | 10; 8; 6 | 14 (rooms/040, F-006) | lowercase in dialogue; never "church"; NO3_HW_1/0001 = NO3_NO4/0011 …教会くらいね take "the chapel"; hints/013 blocked; 3 / 0 / 2 | R §25.1 |
| 拠点 | — | base ("our new base"; 新しい拠点 → "a new base") | 4 | — | NO3_CHAPEL/0012 "We'll make this our new base"; NO3_NO4/0001, NO3_HW_1/0001 = NO3_NO4/0011 to come; not "base of operations"; 4 / 0 / 0 | R §25.1 |
| 機関室 | — | the engine room | 15 | 14 (if a room name; hints/012–014 blocked, F-006) | lowercase in dialogue; NO3_CHAPEL/0093, 0099, 0100 ("The engine room?"), 0106, 0115, 0128; NO3_NO4/0054 ×2 "The engine room! Let's run for the engine room‼"; NO2_NO3/0004, NO1_ENGINEROOM/0002 to come; 9 / 0 / 3 | R §28.1, §29.1 |
| 例の生き残り | — | that survivor | 13 | — | the one who targeted Judy (NO3_CHAPEL/0051, 0060, 0072); NO3_CHAPEL/0115 "That survivor still worries me"; NO3_NO4/0046 "that survivor seems likely to be on this deck"; 生き残り alone stays "survivor(s)"; 2 / 0 / 0 | R §28.1, §29.1 |

## 3. Items, currency, mechanics
| Source | Variants | Target | Cols | Cap | Note | Ruling |
|---|---|---|---|---|---|---|
| 潜水装備 | — | diving gear | 11 | — | | R §1.9 |
| 装備 | — | gear ("our gear") | 4 | — | the party's equipment (NO4_BAR/0129, 0212, 0254, 0305; NO4_MACHINER90/0016, 0084); 装備する in equip/*, camp/001 (blocked) in context; 潜水装備 is its own row; 16 / 0 / 6 incl. 潜水装備 ×3 | R §15.1 |
| 電波 | — | radio waves | 11 | — | ＶＬＦ帯の電波 → "VLF-band radio waves" | R §3.1 |
| 超音波 | — | ultrasound | 10 | — | | R §3.1 |
| 長波 | — | longwave | 8 | — | | R §3.1 |
| 無線装置 | — | radio equipment | 15 | — | 無線機 is its own row; 無線室 is a §9 row; 装置 and 設備 alone are not fixed | R §3.1, §14.1 |
| 無線機 | — | the radio | 9 | — | NO4_HWR_FRONT/0103 only (1 / 0 / 0); 無線装置 stays "radio equipment" | R §14.1 |
| ボンベ | — | air tank(s) | 9 (8) | — | the diving tanks someone smashed: NO4_HWR_FRONT/0124, NO4_MACHINE/0002, NO4_MACHINE_T/0001; 3 / 0 / 0 | R §14.1 |
| 潜水艇 | — | submersible | 11 | — | never "submarine" (潜水艦, 0 rows) | R §3.1 |
| 地上用の設備 | — | land-based equipment | 20 | — | NO4_BAR/0175 and SCN011/04 | R §3.2 |
| 回転 (the ship) | — | roll over (noun: roll) | 9 (4) | — | the capsized ship turning on its long axis | R §3.1 |
| 弾切れ | — | out of ammo | 11 | — | SCN029/02, SCN046A1/07; items/000 (blocked) in context | R §4.1 |
| 薬品 | — | medicine | 8 | — | NO4_BAR/0226, NO3_MEDICALROOM/0002 | R §5.1 |
| ソナー | — | the sonar | 9 | — | ソナーの反応 → "the contact" … on/from the sonar (0272); ソナーに反応が無い in context | R §6.1 |
| ハンドガン | — | handgun | 7 | — | never "pistol"; ハンドガン程度 → "a mere handgun" (0343); equip/000, items/000 (blocked) take the same word | R §7.1 |
| 鞄 | カバン · バッグ · 旅行鞄 | bag; 旅行鞄: suitcase | 3; 8 | — | 鞄, カバン, バッグ one word (NO4_TOOL_ROOM/0003 カバンごと in context); plural as the line needs; バッグ 1 / 1 / 0 | R §8.1, §13.1 |
| マガジン | — | magazine; 予備のマガジン · マガジンの予備 → "spare magazine(s)" | 8 | — | the gun's magazine, never "clip"; NO3_NO4/0010 takes "spare magazine" | R §10.1 |
| バリケード | — | barricade (verb "barricade(d)" where the line wants it) | 9 | — | 5 / 0 / 0; 撤去 → "clear" (0444; NO4_HWL_KAIDAN/0006 takes the same verb) | R §11.1 |
| チェーンカッター | — | chain cutter | 12 | 39 (hints/006, blocked) | never "bolt cutters"; NO6_TOOLROOM/0001 `A chain cutter, it seems.` (R §20.1 frame); hints/006 takes the same words; 2 / 0 / 1 | R §11.1, §24.1 |
| 工具 | — | tools | 5 | — | 2 / 0 / 0; 道具 is not fixed ("a tool", 0441; NO4_HWL_KAIDAN/0006 in context) | R §11.1 |
| 刃物 | 鋭利な刃物 | blade; 鋭利な刃物: a sharp blade | 5; 13 | — | 3 / 0 / 0 (NO4_BAR/0439 "every blade"; NO4_4102/0001, NO6_BRIDGE/0020) | R §11.1 |
| シャッター | 防水シャッター | shutter; 防水シャッター: watertight shutter | 7; 18 | 39 (hints/011, blocked) | lowercase; 31 / 1 / 1 (防水シャッター 3 / 0 / 0, the control panels NO3_MACHINE/0002, 0004, NO6_BRIDGE/0012) | R §13.1 |
| ロッカー | ロッカールーム (rooms/086) | locker; room name: Locker Room | 6; 11 | 14 (rooms/086, F-006) | lowercase; NO4_TOOL_ROOM/0080 何も入っていない → "The locker is empty."; 空のようだ (NO5_LOCKERROOM/0005–0006) → "seems empty"; 7 / 0 / 1 | R §19.1 |
| ワイヤーリフト | — | the wire lift | 13 | — | lowercase; NO4_ENTRANCE/0004, 0005; never "winch line"; 2 / 0 / 0 | R §20.1 |
| 振動 | — | tremor | 6 | — | the ship shaking (NO4_HWL_BACK/0006 "this tremor"); NO6_HW_4/0001, NO6_TOOLROOM/0003, SPACESHIP_HW/0004 take the same word; NO4_BAR_T/0177 (developer note) in context; 5 / 0 / 0 | R §20.1 |
| カードキー | — | card key | 8 | 43 (items/010, blocked) | two words, never "keycard"; NO4_SHOP/0001 "This body had a card key."; 1 / 0 / 1 | R §21.1 |
| 懐中電灯 | — | flashlight | 10 | 43 (items/006, blocked) | never "torch"; NO4_SHOP/0005 "A flashlight is lying here."; 1 / 0 / 1 | R §21.1 |
| チェーン (alone) | — | chain | 5 | — | NO4_HWL_KAIDAN/0002 "secured tight with a chain"; チェーンカッター is its own row; 鎖 (NO4_BAR/0422 "chains") not fixed; 1 / 0 / 0 alone | R §21.1 |
| 消火器 | — | fire extinguisher | 17 | 43 (items/007, blocked) | NO5_SHOP/0002 "There's a fire extinguisher lying here."; NO6_HW_3/0003 takes the same words; 2 / 0 / 1 | R §22.1 |
| 鍵 | 鍵が掛かって(い)る · 鍵がかかって · 鍵がかけられて · 鍵が締まって | key; locked (鍵が掛か…/鍵がかか…/鍵がかけ…/鍵が締ま… → "locked") | 3; 6 | — | NO5_LOCKERROOM/0004 "Found a key placed inside the locker."; NO5_HW_R/0004 "The door is locked"; NO6_BRIDGE/0001 締まっている "locked" (variant added, R §23.1); カードキー is its own row; 26 / 0 / 5 (掛か 13, かか 5, かけ 1, 締ま 1) | R §22.1, §23.1 |
| 水圧 | — | the water pressure | 18 | — | NO6_BRIDGE/0011 "The water pressure has warped the door"; the fixed 水圧で扉を… sentence (§6); NO4_BAR_T/0105 気圧と水圧 in context; 7 / 0 / 0 | R §23.1 |
| シャッターロック | — | the shutter lock | 16 | — | NO6_BRIDGE/0014 "The shutter lock on Deck 5 is still engaged."; 1 / 0 / 0 | R §23.1 |
| 操作パネル | 防水シャッターの操作パネル | control panel; 防水シャッターの操作パネル: a control panel for the watertight shutters | 13; 43 | — | NO6_BRIDGE/0012 `There's a control panel for the watertight shutters.{br}`; NO3_MACHINE/0004 opens with the same sentence and reuses it; NO3_MACHINE/0002 (+ ようだ), NO3_FOODSTORAGE/0011, NO2_SUBSTORAGE/0005; 5 / 0 / 0 | R §23.1 |
| 舵 (船の舵) | — | the ship's wheel | 16 | — | NO6_BRIDGE/0013 only; 操舵室 stays "the wheelhouse"; 1 / 0 / 0 alone (3 with 操舵室) | R §23.1 |
| 浸水 | — | flood / flooding / flooded, as the line needs | 5 / 8 / 7 | — | shipped NO4_BAR/0068 "a flood"; NO5_ENTRANCEL/0003 "The flooding's already started…⁉", NO5_ENTRANCEM/0010 "…it's flooded.", NO6_HW_4/0001 "It's flooding…"; 6 / 0 / 0 | R §22.1, §24.1 |
| 残弾 | 銃の残弾 | ammo ("You seem low on ammo."); 銃の残弾: the ammo left in your gun | 4; 25 | — | NO3_CHAPEL/0077, 0078; 弾切れ stays "out of ammo"; never "rounds left"; 2 / 0 / 0 | R §26.1 |
| レーザーサイト | — | laser sight ("a gun fitted with a laser sight") | 11 | — | NO3_CHAPEL/0084 only; 1 / 0 / 0 | R §26.1 |
| エンジン · 機関 | 機関を止める | the engine (singular) | 10 | — | NO3_CHAPEL/0093, 0094, 0116, 0118, 0125, 0128; 機関 alone only 0122 機関を止める → "stopping the engine"; a repeat may take "it" (0095); 機関室 is §2; 7 / 0 / 0 · 1 / 0 / 0 | R §28.1 |
| 動力 · 動力源 | — | power · the power source | 5 · 16 | — | NO3_CHAPEL/0101 動力が生きている → "its power is still running"; 0102 動力源を破壊すれば → "Destroy the power source"; never "propulsion"; 1 / 0 / 0 each | R §28.1 |
| 浮上 · 浮き上がる | — | surface · float up | 7 · 8 | — | the ship rising: NO3_CHAPEL/0102, 0116 "the ship may surface"; 0103 "it'll probably float up"; 2 / 0 / 0 · 1 / 0 / 0 | R §28.1 |
| 燃料バルブ | 燃料 | the fuel valve; 燃料: fuel | 14; 4 | — | NO3_CHAPEL/0126 "If we close the fuel valve"; 燃料 as shipped NO6_HW_3/0001; 1 / 0 / 0 · 2 / 0 / 0 | R §28.1 |
| アモ | — | round ("take out one round") | 5 | — | NO3_CHAPEL/0122 only, bound to s28/s29 `Hold the round` / `Don't hold it` (§4); never "bullet"; 1 / 0 / 0 | R §25.1, §28.1 |
| ステンドグラス | — | the stained glass | 17 | — | NO3_CHAPEL/0131 "Cracks run through the stained glass."; 1 / 0 / 0 | R §28.1 |

## 4. Classes, units, system terms
| Source | Variants | Target | Cols | Cap | Note | Ruling |
|---|---|---|---|---|---|---|
| セーブする · セーブしない | — | Save · Don't save | 4 · 10 | 27 | the save choice pair (choice rows, §8) | R §1.9 |
| Ｒｅｔｒｙ？ | — | Retry? | 6 | — | the game-over prompt, the source's own English: type ASCII `Retry?` (encodes to the source bytes) | R §10.1 |
| はい · いいえ (choice) | — | Yes · No | 3 · 2 | 27 | `choice` rows only (8 / 0 / 0 each); はい in dialogue is in context | R §10.1 |
| 握る · 握らない (choice) | — | Hold the round · Don't hold it | 14 · 13 | 27 | the engine vote after NO3_CHAPEL/0122 (s28 / s29), never a handshake; 0122 右手に握れ takes "hold it in your right hand"; 1 / 0 / 0 each | R §25.1 |

## 5. Verbal tics — decided, never mix
<!-- What is fixed is the word; punctuation follows the source line. -->
| Speaker | Source tic | Treatment | Note | Ruling |
|---|---|---|---|---|

## 6. Stock phrases and interjections
| Source | Variants | Target | Cols | Note | Ruling |
|---|---|---|---|---|---|
| ヤツ | — | he / him / his | 2 / 3 / 3 | the monster or the killer, never "it"; a named person in context (NO4_HWL_BACK/0005 William → "his"); a type of person (〜なヤツ) in context; head of a relative clause in context (NO3_CHAPEL/0062 "the guy who attacked Judy") | R §1.7, §20.3, §26.2 |
| 化け物 | 怪物 | monster | 7 | synonyms, one target; NO4_BAR/0083 has both: repeat "monster" | R §1.8 |
| 人型の化け物 | — | a humanoid monster | 18 | NO3_CHAPEL/0056 only; 化け物 → monster; 1 / 0 / 0 | R §26.1 |
| 厄介 · やっかい | 厄介事 · やっかいなこと | trouble ("Either way, it's trouble."; echo なにが厄介だ！ → "What trouble!"; "one trouble after another") | 7 | NO3_CHAPEL/0054–0056, 0087; shipped "in trouble" (NO4_4101/0003, NO4_HWR_FRONT/0087), "Trouble is" (NO4_BAR/0422), "tricky" (0142), やっかい払い "Good riddance" (0264) in context; 9 / 0 / 0 | R §26.1 |
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
| 虫 | — | bug | 3 | 虫 alone: NO4_HWL_FRONT/0002, NO4_MACHINER90/0050, 0052; 昆虫 (insect), 成虫, 虫の居所 are other words; 虫かご (NO3_CHAPEL/0023) in context; 3 / 0 / 0 | R §16.1 |
| 生き物 | — | creature | 8 | as shipped NO4_BAR/0040; NO4_MACHINER90/0064, 0072; NO4_TOOL_ROOM ×5; 9 / 0 / 0 | R §15.1 |
| 潜入 (する) | — | come aboard ("the moment we come aboard", "did we even need to come aboard?") | 11 | the salvagers entering the wreck: NO4_MACHINER90/0011, 0089; 2 / 0 / 0 | R §15.1 |
| 節足動物門鋏角亜門 | — | phylum Arthropoda, subphylum Chelicerata | 40 | Miller's taxonomy, NO4_BAR/0352 only; lowercase ranks, capitalised taxa | R §8.1 |
| フッ | — | Heh | 3 | Wolg's wry scoff; punctuation per source (フッ… → "Heh…", フッ、 → "Heh,"); not グフッ (SCN038B/17, a grunt) | R §7.1 |
| クッ · ククッ · クカカカカカカッ | クッ、ククッ、クカカカカカカッ。 · クッ、ククッ。 · ククッ、クカカカカカカッ | Heh · Heh-heh · Kahahahahaha; run together: "Heh, heh-heh, kahahahahaha." | 3 · 7 · 12; 27 | the killer's laugh, 6 / 7 / 0 rows; one syllable per カ; punctuation per source; not くっ (Ngh) | R §9.1 |
| うおおおっ (battle cry) | — | "R" for う, one "a" per お, "h" for っ | — | SCN038B/10 う+お×11+っ‼ → "Raaaaaaaaaaah‼" (14); the きゃあ…っ pattern; ‼ ⁉ as the source | R §9.1 |
| ～ (long-vowel mark) | — | repeat the vowel once per ～; a final っ after a word is dropped | — | SCN038B/11 行け～～～っ。 → "Goooo." (Go + 3 o); after ン the syllable's vowel: SCN046A3/01 → "Hemiiiiiiiing‼" (Hemi + 7 i); 0 / 2 / 0 | R §9.1, §13.1 |
| グフッ | — | Guh | 3 | grunt as he is struck, SCN038B/17 only ("——Guh‼"); not フッ | R §9.1 |
| 俺様 | — | no fixed word: the killer's swagger is carried by register | — | 俺様の…… → "My very own……" (SCN038_5C1/06); 俺様の女神 → "my very own goddess" (NO2_MAINSTORAGE/0003); 3 / 4 / 0 | R §9.1 |
| 妹 | 妹さん | sister: "my sister" / "his sister"; the echo 妹？ → "Sister?" | 6 | William's dead sister; 妹さん drops さん (R §1.2) → "his sister" (NO4_HWR_FRONT/0075, 0080); SCN038D/17 "To my sister…" | R §10.1 |
| 親玉 | — | the big one | 11 | the parent monster, NO4_BAR/0438 only; never "boss" (社長) | R §11.1 |
| 巣 | 化け物の巣 | nest; 化け物の巣: the monster's nest ("a monster's nest" at 0368) | 4; 18 | 4 / 0 / 0; 蜘蛛の巣 (NO5_BANK/0006) is a web, in context | R §11.1 |
| と書かれている | — | it reads: `"«text»," it reads.`; ending a multi-row sign: `«last entry», it reads.` | 8 | 7 / 0 / 0; alone on its row after a sign (NO5_HW_R/0011): previous row ends `«last entry»,{br}`, then `it reads.{p}` | R §12.1, §22.1 |
| ウスノロ | — | dimwit (pl. dimwits) | 6 | the killer's word for his victims: 親愛なるウスノロ → "my dear dimwit", てめえらウスノロ → "you dimwits", そのウスノロ → "those dimwits"; 0 / 3 / 0 | R §13.1 |
| メス | — | bitch (あのメス → "that bitch") | 5 | the killer on Judy, SCN046B1/10–11; article in context; 0 / 2 / 0 | R §13.1 |
| 売女 | — | whore (お前の売女 → "your whore") | 5 | the killer on Wolg's murdered wife, SCN046B2/07; 0 / 1 / 0 | R §13.1 |
| ワイフ | — | my wife | 7 | Wolg's murdered wife, his police story: NO3_NO4/0030 "My wife, who always met me at the door…", 0032; the loanword affectation is not carried; 2 / 0 / 0 | R §27.1, §29.1 |
| 神 | — | god, lowercase ("a god", "that god of yours") | 3 | SCN046B2/02–05; 女神 is the 俺様 row's "goddess"; NO4_BAR_T/0144 神は──主は in context; 1 / 4 / 0 (女神 3 / 0 / 0) | R §13.1 |
| 生肝 | — | raw liver | 9 | SCN046B2/04 only (アレの生肝 → "that thing's raw liver"); 0 / 1 / 0 | R §13.1 |
| ゲームオーバー | — | game over ("it's game over") | 9 | in dialogue, SCN046A2/01 only (Heming to Oakland); 0 / 1 / 0 | R §13.1 |
| 船内イベント | 『本日の船内イベント案内』 | shipboard events | 16 | the schedule notice, 5 identical rows (NO4_HWR_FRONT/0101, NO4_HWL_FRONT/0011, NO6_HW_1/0003, NO6_HW_2/0006, 0010) + NO4_SHOP/0006, NO5_BANK/0005; 7 / 0 / 0 | R §14.1 |
| 無茶を言う | 無茶を言うな · 無茶を言わないで · 無茶を言ってる | in context: "ask the impossible" answering a request; "be absurd" answering a stance | 18; 9 | request: NO4_BAR/0155, 0352, 0389; stance: NO4_MACHINER90/0024, 0031, echo 0032 "being absurd"; 無茶 alone, 無茶苦茶 not fixed; 6 / 0 / 0 | R §16.1 |
| 処分 | — | dispose of; それなりの処分 (NO4_MACHINER90/0036) in context: "the consequences" | 10 | SCN047A/03 "Dispose of the specimen.", C1/05 "must be disposed of" (#16, shipped); 1 / 2 / 0 | R §16.1, §17.1 |
| 人間 | — | human(s); "people" where the line is general | 5 (6) | as shipped NO4_BAR/0035, 0132, 0246, 0333, NO4_HWR_FRONT/0003, 0005, SCN046B1/11, B2/01, SCN047B3/02, C2/04–05; "people" NO4_BAR/0310, NO4_HWR_FRONT/0004; 外の人間 (NO4_BAR/0003) in context; 21 / 5 / 0 | R §17.1 |
| 実験 · 検体 · フェーズ２ | — | experiment · specimen · Phase 2 | 10 · 8 · 7 | the aliens' terms: SCN047A/01, C1/03, EPILOG/03 · SCN047A/03 · EPILOG/03 (Arabic digit); 0 / 3 / 0 · 0 / 1 / 0 · 0 / 1 / 0 | R §17.1 |
| 自己犠牲 | — | self-sacrifice | 14 | SCN047C1/03 only (自己犠牲という習性 → "habit of self-sacrifice"); 0 / 1 / 0 | R §17.1 |
| ハイ (katakana) | — | Yes | 3 | SCN047A/02, 04 `Yes.` (a duplicate pair); はい in dialogue stays in context (EPILOG/03 "Yes……"), はい choice is §4; 0 / 2 / 0 | R §17.1 |
| うう | — | Uuh (one "u" per う, "h" closing) | 3 | SCN047A/05 うう…。 → "Uuh…"; ううむ (NO3_CHAPEL/0119) is another word; 0 / 1 / 0 | R §17.1 |
| 哺乳類 | — | mammal(s) | 7 (6) | Miller's science talk: NO4_TOOL_ROOM/0017, 0019, 0022, 0029, 0031, 0033, 0034, 0037, 0064; 9 / 0 / 0 | R §18.1 |
| 感覚器官 | — | sensory organs | 14 | NO4_TOOL_ROOM/0035, 0037; 2 / 0 / 0 | R §18.1 |
| 解剖 (する) | — | dissect / dissection | 7 / 10 | NO4_TOOL_ROOM/0011 "dissecting", NO4_HWL_FRONT/0001 "the monster's dissection" (both shipped); never "autopsy"; 2 / 0 / 0 | R §18.1, §21.1 |
| 生物 | 全生物 | organism(s); 全生物: all organisms | 8 (9); 13 | Miller's word, kept apart from 生き物 "creature"; NO4_TOOL_ROOM ×8; 新種の生物 (NO4_BAR/0457 "a new species") and 生物としての観点 (0021 "Biologically") in context; 海洋生物学者 is §2; 9 / 0 / 0 | R §18.1 |
| 生命 · 生命体 (an organism) | — | life form | 9 | no hyphen; 優秀な生命 (NO4_TOOL_ROOM/0033), 恐るべき生命体 (0041); 生命 as "life" (NO4_BAR/0216, NO4_HWR_FRONT/0062–0063, SCN038D/08) and 生命力 in context; 2 / 0 / 0 | R §18.1 |
| 利点 | — | advantage(s) | 10 (9) | NO4_TOOL_ROOM/0017, 0019, 0031, 0064; 4 / 0 / 0 | R §18.1 |
| 成虫 | — | adult(s) | 5 (6) | the grown form of the creature: NO4_TOOL_ROOM/0070 "the adult", 0075 "become adults"; 虫 alone is "bug"; 2 / 0 / 0 | R §19.1 |
| 幼生体 · サナギ | — | larva · pupa ("the pupa stage") | 5 · 4 | Miller's life-stage terms, NO4_TOOL_ROOM/0072 only; never "chrysalis"; 1 / 0 / 0 each | R §19.1 |
| クローン羊 | — | the cloned sheep | 16 | NO4_TOOL_ROOM/0053 only; no name added ("Dolly"); 1 / 0 / 0 | R §19.1 |
| 切り刻む · 無残に | 切り刻まれた · 切り刻まれている · 切り刻まれ · 無惨 | hacked to pieces · brutally (無残に切り刻まれた死体 → "a body, brutally hacked to pieces") | 16 · 8 | the bodies: NO4_4001/0001, NO4_4102/0001, 0004; 無惨な殺され方 "such brutal killings" (NO4_MACHINER90/0045); 見るも無残 (NO3_MEDICALROOM/0006) in context; 切り刻 10 / 0 / 0, 無残 6 / 0 / 0, 無惨 1 / 0 / 0 | R §20.1 |
| 担当 | — | job ("Our… job… is this floor."; "Isn't your job on Deck 6?") | 3 | the party's assigned search area: NO5_ENTRANCEL/0008 = 0011 = NO5_ENTRANCEM/0008, NO5_LOCKERROOM/0002; not "assigned"; 4 / 0 / 0 | R §22.1 |
| どうやらここから上に昇れそうだ。{p} | — | `It looks like there's a way up from here.{p}` | 41 | fixed sentence: NO5_ENTRANCEL/0006, 0009 = NO6_ENTRANCE/0003; keep the そう hedge; 3 / 0 / 0 | R §22.1 |
| シャッターで封鎖されて、先に進めそうにない。{p} | シャッターで封鎖され、先に進めそうにない。{p} | `A shutter has sealed it off. There seems to be no going any further.{p}` | 68 (28 / 26 / 12) | fixed sentence, both spellings one target: NO5_HW_L/0003, 0005, NO5_HW_R/0007 (され、) = NO6_HW_1/0001–0002, NO6_HW_5/0005 (されて、); replaces the wave 6 seed, which stranded "a"; 6 / 0 / 0 | R §22.1 |
| シャッターで閉ざされて先には進めない。{p} | — | `A shutter closes off the way. No going any further.{p}` | 51 (24 / 26) | unhedged, kept apart from the 封鎖 sentence: NO5_ENTRANCEM/0005 = 0006; plain シャッターが下りていて先には進めない (NO2_HW_5/0003) may reuse "No going any further."; 2 / 0 / 0 | R §22.1 |
| 親父 | — | your dad (お前の親父 → "your dad") | 8 | Oakland, to John, by his crew: NO6_BRIDGE/0008 "…if we're late, your dad." (postposed as the source), NO3_NO4/0043; never "old man" (じいさん, Collison); 2 / 0 / 0 | R §23.1 |
| 航海のスケジュール | — | the voyage schedule | 19 | NO6_BRIDGE/0010 "The voyage schedule is written here." only; 船内イベントのスケジュール表 stays as shipped (R §21.4); 1 / 0 / 0 | R §23.1 |
| 水かさ | — | the water (rising): 水かさ…増えつづけてる → "The water… it keeps rising…" | 9 | only in the fixed sentence below; 4 / 0 / 0 | R §23.1 |
| 水かさ…増えつづけてる…。{w}{br}急がないと…危険よ…。{p} | — | `The water… it keeps rising…{w}{br}Must hurry… it's dangerous…{p}` | 27 / 27 | fixed sentence, Judy: NO6_ENTRANCE/0001 = NO6_HW_2/0001 = NO6_HW_4/0003 = NO6_HW_5/0001; 4 … each side; replaces the wave 6 seed; 4 / 0 / 0 | R §23.1 |
| 水が深すぎて…息が…でき…な…{p} | — | `The water's too deep… can't… brea… the…{p}` | 39 (28 / 10) | fixed sentence, Judy drowning: NO6_ENTRANCE/0002 = NO6_HW_2/0002 = NO6_HW_4/0004 = NO6_HW_5/0002; 4 …; the subject of "can't" implied (step 5); 4 / 0 / 0 | R §23.1 |
| 鍵が掛かっていて、扉は開かない。{p} | — | `It's locked, so the door won't open.{p}` | 36 (24 / 11) | fixed sentence, unhedged: NO6_HW_2/0005, 0007 = NO6_HW_3/0005–0007, NO6_HW_4/0005, 0008; 扉は鍵が掛かっていて開きそうに無い (NO3_HW_1/0005–6, NO3_HW_2/0002–3) is hedged, kept apart; 7 / 0 / 0 | R §23.1 |
| 水圧で扉を開けられない。{p} | — | `The water pressure won't let the door open.{p}` | 43 (28 / 14) | fixed sentence: NO6_HW_2/0008–0009 = NO6_HW_4/0006–0007, NO6_HW_5/0004; 5 / 0 / 0 | R §23.1 |
| 閉じ込める | 閉じ込めた · 閉じ込めていた | shut in ("We've shut him in"; "he's supposed to be shut in") | 7 | the monster's confinement: NO4_HWL_BACK2/0006, NO3_NO4/0053 (はず → "supposed to"); NO2_MAINSTORAGE/0027 to come; 閉じこめ in context (NO3_CHAPEL/0023 "locked in"); 3 / 0 / 0 | R §29.1 |

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

## 10. Open questions
<!-- one line each, with the FLAGS id. A closed question is deleted here; its answer stays in rulings.md. -->
