# pending/ — finished translations that cannot ship yet

Files here are **finished, format-clean translations** the assembler **must not** pick up. The
directory name deliberately does not match the unit file pattern of `PROJECT.md` §2, so CHECK, MERGE
and BUILD ignore it and the patch stays buildable with those units falling through to the source
language.

Nothing here is unfinished work. Read the reason before assuming a file needs translating again.
Move a file into `tl/` only once the constraint in its row has been lifted, and only after applying
every row of the second table.

| File | Reason parked | Measured figure | Ratio floor reached | What lifts it | PR |
|---|---|---|---|---|---|

## Lines these files must adopt on re-cut
<!-- A parked file does not ship, so a divergence from shipped work is not a violation today — it
becomes one the moment the file moves into tl/. Every ruling made against a parked file's line after
it was parked goes here, written by the reviewer. Re-cutting without applying these rows creates the
violation. -->

| File | Line | Now | Must become | Cost | Ruled |
|---|---|---|---|---|---|
