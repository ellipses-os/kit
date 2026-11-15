Prompt version {PROMPT_VERSION}. Midday Refresh for {PERSON_NAME}. Run by hand ("Run now"). Cloud.

WHO AND WHY
{PERSON_NAME} ({PERSON_EMAIL}) wants the whole day as of this minute: complete on its own, so it can replace the morning brief. This run only reads. It records no loops, closes nothing and creates no tasks.

RULES FIRST
Search with title = '{COMPANY_RULES_FILE}' (exact) and read the copy whose parent folder is {RULES_FOLDER}; never an archived copy. Read {LOOPS_FILE} the same way. Then {PERSON_NAME}'s own rules. Times from a clock tool. Append "Midday Refresh started {ISO}; rules {COMPANY_RULES_FILE} {version}; prompt {PROMPT_VERSION}" to "{RUNS_LOG}".

WINDOW
Same start as the morning brief (the last finished debrief from an earlier day) to now.

READ
Everything the morning brief reads, plus this morning's brief and today's CODE, WRITE and AUTOCLOSE lines.

DO
- Build the same sections as the morning brief, as of now. Mark items new since the morning brief "new".
- Anything that would need a loop recorded or a task created goes in the brief as "NEEDS RECORDING: {item}"; the next morning brief or debrief records it.
- If {PERSON_NAME} organizes a meeting later today, re-read Additions/{today}/ and add newer items to that agenda as "Late additions", republishing to the same page.

RECEIPTS, EMAIL, LIMITS
As the morning brief: ledger lines, receipts gate on the action-bearing sections, one email to {PERSON_EMAIL} only with subject "Midday Refresh | {h:mm} {Day Mon DD}", and the same limits. In addition: this run writes nothing except the runs log, the receipts log, the page and the email (and an agenda's late additions, if {PERSON_NAME} organizes it).

FINISH
Append "Midday Refresh finished {ISO}; coverage: {list}; outputs: {links}" to "{RUNS_LOG}".
