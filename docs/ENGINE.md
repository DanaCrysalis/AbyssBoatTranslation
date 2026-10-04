# Abyss Boat — engine and text format notes

Abyss Boat (アビスボート), Leaf, Windows (DirectX 8), 2001. Reverse-engineered from the
retail CD (`AB_01`, volume `ABYSS_BOAT`) for this translation. Addresses are virtual
addresses in the retail `AbyssBoat.exe` (image base 0x400000). Everything marked
**verified** was confirmed by reading the executable and by a lossless round trip of every
file; **assumed** items need an in-game check (listed in `FLAGS.md`).

## 1. Where the text is

| Store | Game file | Rows | What |
|---|---|---|---|
| `script` | `SCRIPT.PAK` → 81 `*.SCR` room scripts (73 contain text; `$~NO4_TOOL_ROOM.SCR` is an identical copy of `NO4_TOOL_ROOM.SCR`) | 1,709 | dialogue and examine text (1,702 messages), choice options, a few speech-bubble lines |
| `scene` | `SCRIPT.PAK` → 38 `*.SCE` cutscenes | 190 | subtitles |
| `system` | `AbyssBoat.exe` | 188 | menu help, room names, item names and descriptions, hints, deck names, error dialogs |

Not covered by the dumps: text drawn into images (`GPARTS.PAK`/`PICTDAT.PAK` `*.LGF`
— menu graphics, title, dialog buttons); enemy names in `ENEMYINF.PAK` are internal
labels and are never shown. `MAPDAT.PAK` has no text.

## 2. Archives (`*.PAK`, "LAC")

`"LAC\0"`, u32 count, count × 36-byte entries: name[27] (every byte bitwise inverted,
NUL-padded), u8 compressed, u32 size, u32 offset. Compressed entries are u32 unpacked
size + LZSS (4 KiB ring, start 0xFEE, flag byte LSB first, 1 = literal, match = 12-bit
position + 4-bit length+3). The game reads uncompressed entries too, so BUILD stores
replaced files uncompressed. **verified** (`tools/abyss/lac.py`).

## 3. Room scripts (`*.SCR`, "LAFSCR")

Header (all offsets u16 — a script can never exceed **65,535 bytes**):

| Offset | Field |
|---|---|
| 0x00 | `LAFSCR\0\x01` |
| 0x08 | u32 file size |
| 0x10 | u8 0x44, u8 **NCH** = characters in the character table |
| 0x12 | TA — label table (u16 code offsets) |
| 0x14 | TB — word-offset table (u16 offsets into the text section) |
| 0x16 | TX — text section: NCH × 2-byte characters, then NUL-terminated words |
| 0x18 | END — end of text; the bytes after it are kept verbatim |
| 0x20 | bytecode, up to TA |

**Text is dictionary-compressed.** Statement `0x91` is followed by tokens and a `00`. A
token is a byte 1–250, or a page prefix `FB`–`FF` plus a byte: token n indexes the list
[characters…, words…] with n = byte (1–250), `FB y` = 250+y, `FC y` = 500+y, `FD y` =
750+y, `FE y` = 1000+y, `FF y` = 1250+y — at most **1,499 tokens** per file. Characters
whose first byte is 1–4 are control codes and copy one byte (0x41EB50); words are copied
by 0x41EAE0, which copies control codes 2, 5, 6, 7 together with the byte after them.
Decoder: 0x41E960. **verified.**

Choice options (statement `0x86`) and a few other lines are inline strings in
expressions (`EB <bytes> 00`). Jumps go through the label table; `E9 hi lo` expressions
reference strings by code offset. The rebuilder (`tools/abyss/scr.py`) re-tokenises every
message with a fresh dictionary, splices the bytecode, and fixes the label table and every
`E9` reference. Its parser mirrors the interpreter (statement loop 0x42A543, handler table
0x42BE28 indexed through 0x42BF34; expression evaluator 0x401000 → 0x4010C0 → 0x401140 →
0x4012A0 → 0x401310 → 0x4013D0 → token reader 0x401620). **verified**: all 81 scripts
parse to the exact end of their code; all 81 rebuild from their own text with every
message, label target, inline string and `E9` target identical, and the predicted size
equals the built size.

Speaker: statement `0xA9` (5 arguments) precedes most lines; its first argument is the
speaker's slot in that scene. The dumps carry it as `spk=N`. Slots are per file, not
global (in `NO4_BAR`: 6 = Oakland, 2 = Rob Collison, 7 = William).

## 4. Cutscenes (`*.SCE`)

Packed: u16 last frame, f32 fps, camera name[28]; u16 n + n × model name[28]; u16 n +
n × (clip name[28], u16 start, u16 end, f32 fps); u16 n + n × (Shift-JIS text, NUL, u16
start frame, u16 end frame, u8 flag, + 4 bytes when flag ≠ 0); then sound/event tables.
Nothing points into the subtitle block, so subtitles may change length. **verified.**

## 5. The renderer — why English is full-width

Text is drawn from bitmap fonts `GPARTS.PAK/MINCHO18.FNT`, `MINCHO18T.FNT`,
`MINCHO24.FNT`: 7,938 glyphs (42 Shift-JIS lead bytes 0x81–0x9F, 0xE0–0xEA × 189 trail
bytes 0x40–0xFC), 4 bits per pixel, **no single-byte glyphs**. The message layout routine
(0x41F100) copies two bytes per character into fixed line buffers, and the menu helper
(0x4079F0) advances two bytes per character. So every displayed character must be a
double-byte Shift-JIS code: English is written in **full-width Latin** (Ａｂｃ),
**2 bytes per character, 1 column per character.** Translators type plain ASCII; the
tools convert it (`tools/abyss/codec.py`), mapping `'` and `"` to ’ ‘ “ ” because the
font has no full-width straight quotes. **verified.**

The font draws 0x8189 (♂ in Shift-JIS) as a "!!" ligature and 0x818A (♀) as "!?".
The dumps show them as ‼ and ⁉.

A narrower look is possible later with a font hack (two Latin letters per glyph in the
code points the translation frees up, or a renderer patch for half-width advance); see
`FLAGS.md`. Nothing in the tools assumes it.

## 6. Control codes (message renderer 0x41F100, jump table 0x41F518)

| Byte | Tag | Meaning |
|---|---|---|
| 01 | `{p}` | wait for a click, then clear the box |
| 02 | `{w}` | wait for a click, keep the box (never last; the next byte follows it) |
| 03 | `{br}` | line break |
| 04 | `{name}` | the player's name (exe string at 0x45FCAC; BUILD writes "John") — unused by the original text, which spells ジョン out |
| 06 n | `{pause:n}` | timed pause — unused by the original text |
| 07 n | `{num:n}` | insert numeric variable n — unused by the original text |

In the system store, `{br}` is the byte `\` the menu helper treats as a new line; it costs
one byte, may not be last and may not be doubled (the helper draws the byte after it
unconditionally).

## 7. Geometry

| Box | Columns × rows | Status |
|---|---|---|
| Message box | **28 × 4** — the renderer wraps at 0x38 bytes (one closing punctuation mark may hang into column 29); the 4th line break fills the box (0x41F6A0) | verified in code; source never exceeds 4 rows per message |
| Subtitles | 28 × 4 assumed | **assumed** — the source has a few lines of 30–51 columns |
| Choice options, inline lines | 28 assumed | **assumed** |
| System strings | per-slot bytes, see the `slot=` context | verified (fixed-stride arrays) |

The engine does **not** word-wrap — it breaks mid-word at column 28. The tools word-wrap
translations at spaces (`codec.wrap`), so translators do not author line breaks for
width; `{br}` in a translation is a deliberate break. A message marked `+` continues the
previous message's box and column.

## 8. Executable strings

Tables (fixed stride, index × stride in code): option help 0x45D258 ×90 ×6, equip messages
0x45D478 ×80 ×4, room names 0x45D5B8 ×30 ×120 (6 decks × 20 slots; "Ｆｌｏｏｒｎ" entries
are placeholders), camp-menu help 0x45E3C8 ×55 ×6, items 0x45E518 ×88 ×15, hints 0x45EA78
×80 ×17, deck names 0x45EFC8 ×22 ×6. Standalone strings (error dialogs, window title)
use Windows ANSI calls and are written in plain ASCII. Player name: 20-byte buffer
0x45FCAC; its default (0x45FE04, 8 bytes) is copied by `push` at 0x42A486 — BUILD writes
the new default into `.rdata` slack and repoints that push.

## 9. Windows 10 notes (not translation, but they decide what a tester sees)

- The installer (`install.exe`, `abyssUninst.exe`) was translated separately (see the
  project history); the Start Menu shortcut names were changed in both together.
- The game creates a GDI font named "ＭＳ ゴシック" (0x460704) and uses ANSI APIs with
  Shift-JIS strings; on an English Windows without Japanese locale/fonts any remaining
  Japanese shows as mojibake. The script text itself is drawn from the bitmap font and is
  unaffected.
