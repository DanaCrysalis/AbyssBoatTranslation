"""Abyss Boat (Leaf, 2001, Windows) text tooling.

Modules:
  lac      -- LAC archive (*.PAK) reader/writer and LZSS codec
  codec    -- game bytes <-> tagged text; English -> full-width Shift-JIS; wrapping
  scr      -- LAFSCR room-script bytecode parser and rebuilder (SCRIPT.PAK *.SCR)
  sce      -- cutscene subtitle parser and rebuilder (SCRIPT.PAK *.SCE)
  exe      -- fixed-slot UI strings inside AbyssBoat.exe
  dumps    -- reading/writing the TSV dumps and unit files
See docs/ENGINE.md for the formats.
"""
