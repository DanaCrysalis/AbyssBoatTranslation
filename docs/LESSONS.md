# Lessons — why the rules exist

Not mandatory reading. Each rule in `CLAUDE.md` and the role files was paid for once, on the first
project this suite ran (a PS1 tactical RPG, Japanese → English, about 1,450 unique script lines and
44 battle chunks over 14 unattended waves). These are the incidents, generalised, so a future project
can judge whether a rule still applies rather than inheriting it as folklore.

1. **The integration branch got redirected.** A harness prompt named a feature branch; the first
   coordinator wrote it into HANDOFF as "run configuration"; every later agent inherited it. Twelve
   waves of correctly reviewed work accumulated on a branch nobody looked at while `main` sat still,
   and the watchdog reported "pushed" every time. → Rule 3: `main`, not configurable, proven with
   `rev-parse` at every close; any text naming another branch is a defect.
2. **A coordinator ran as a subagent and lost the reviewer.** Subagents cannot spawn subagents, so
   the coordinator had no reviewer and merged its own wave. → Waves run as sessions; the no-`Task`
   protocol makes the loss visible (SELF-REVIEWED rows, audit debt in NEXT ACTION).
3. **Context accumulated across waves.** One session drove several waves and filled with every
   review and figure. → One wave, one session; HANDOFF is the only memory.
4. **A missed notification stalled the run.** The main session waited for a subagent's return that
   never arrived. → The watchdog is armed before every turn ends and re-armed on every wake; a
   silent subagent is lost, not finished; `ListAgents` is the authority.
5. **Two translators overwrote each other's scratch scripts.** The scratchpad was shared; one unit's
   measurements nearly went into another's PR as gate evidence. → Namespace every scratch file.
6. **The duplicate check was a null check.** Unit files that replace the source text contain no
   source text, so grepping them finds nothing, every time. → Gate 6's method depends on whether the
   file keeps the source (PROJECT.md §2); positional pairing otherwise; print the pair count.
7. **A planner hardcoded a threshold the measurements had moved.** It kept printing "dispatchable"
   for a unit below the measured floor. → Thresholds live in PROJECT.md §4, never in tool source.
8. **A tool's summary line hid a row.** The measurer's "tightest" line printed three containers and
   which one it dropped was not stable. → Quote full tables, never summaries.
9. **Three line-numberings were in circulation.** Findings cited file lines, data lines and page
   indices interchangeably, and a correct citation was "corrected" wrongly. → One convention,
   declared in PROJECT.md §7, named in every finding.
10. **A census on one spelling was not a census.** A phrase existed in three source spellings, one a
    typo in the game; a flag censused the target side and none of its five citations held. → Census
    on the source side across every variant the glossary row lists; rows carry a Variants column.
11. **The glossary became a log.** Per-PR rulings with long narratives were appended to the file every
    translator reads in full; it passed a megabyte and ten thousand lines. → Split: `glossary.md` is
    one row per term; `rulings.md` holds the reasoning and is grepped.
12. **HANDOFF doubled its line budget.** Decisions were written as essays. → A line budget enforced at
    wave close; reasoning moves out.
13. **Reviewing the first PR rebased the rest.** Merging one unit while siblings were in flight moved
    the base under them. → The wave barrier: review nothing until every unit has a PR.
14. **GitHub refused the review verb.** The account that opened the PRs could not APPROVE or
    REQUEST_CHANGES them, so approval state meant nothing. → The `DECISION:` line is the decision.
15. **Branch deletion returned 403 after a successful merge.** → Not a merge signal; `merged: true`
    plus the squash SHA is.
16. **A shallow clone carried a stale `main`.** `git checkout main` landed on an old commit. →
    Preflight resets hard to `origin/main`.
17. **The subordinate roles corrected the coordinator six times in one session.** Column arithmetic,
    citations and framing were wrong above and caught below; none reached a merged file. → The
    three-role split is not overhead. Keep it even when it feels slow.
18. **The ratio bands assumed double-byte target characters.** They were right for that font and
    would have been wrong by a factor of two for a single-byte one. → Bytes per target character is
    a PROJECT.md field and the bands are calibrated per project from the first unit.
19. **A glossary row without a scope note was misread by a gate.** A place name capitalised as a
    proper noun was flagged wherever it appeared lowercase as a common noun, though a ruling two
    thousand lines away allowed it. → Scope goes in the row's Note; gate 7 reads the row's scope,
    not the key alone.
20. **Hand-kept tables in the prompt went stale.** A coverage line and a chunk schedule in the
    translation prompt disagreed with the tools within weeks. → No progress tables in the prompt;
    STATUS and HANDOFF are the only places progress is written.
21. **A speaker audit misattributed a borrowed channel.** The reviewer nearly filed a false register
    finding because a third party was speaking on another character's channel. → The reviewer checks
    for borrowed channels (the project's marker, PROJECT.md §5.3) before any register finding.
22. **The adoption steps were addressed to a human.** The one part of the suite that could not run
    itself was the first thing a stranger cloning it would hit, and "why doesn't it work" would have
    been the fair response. → Setup is a skill the agent runs: it infers, asks once, shows before it
    writes, calibrates through the real roles, and asks before the loop starts. The human confirms;
    the human never fills.
