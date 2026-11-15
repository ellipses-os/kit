Prompt version {PROMPT_VERSION}. Pilot measures and decision for {PILOT_NAME}, owned by {PERSON_NAME}. Two scheduled copies run this prompt: "Pilot measures" (after each pilot meeting, {MEASURES_DAY} at {MEASURES_TIME} {HOME_TIME_ZONE}) and "Pilot decision" (one time, {DECISION_DATE} at {DECISION_TIME}). Cloud.

WHO AND WHY
{PERSON_NAME} ({PERSON_EMAIL}) is piloting a new format for {MEETING_NAME} on {PILOT_DATES}. The measures and the decision rule below were written before the first meeting, so the result decides the format, not anyone's mood that week. Nobody is watching; never ask, never wait.

RULES FIRST
Search with title = '{COMPANY_RULES_FILE}' (exact) and read the copy whose parent folder is {RULES_FOLDER}; never an archived copy. They win over this prompt. Times from a clock tool. Append "Pilot {measures or decision} started {ISO}; rules {COMPANY_RULES_FILE} {version}; prompt {PROMPT_VERSION}" to "{RUNS_LOG}".
If today is not one of {PILOT_DATES} (measures) or {DECISION_DATE} (decision), append "Pilot skipped {ISO}" and stop.

MEASURES (run after each meeting)
1. Record. Follow the company rules' meeting-sources order. Use the verbatim transcript of today's {MEETING_NAME}; say which record you used. If none exists yet, look again every 15 minutes until {CUTOFF_TIME}, then write the row with "no record".
2. Score, exactly as defined here:
   {MEASURE 1, e.g. Finish time: the spoken wrap in the transcript; pass if at or before {TIME}.}
   {MEASURE 2, e.g. Opener: minutes from the first words to the first agenda segment; pass if {N} or less.}
   {MEASURE 3, e.g. Retold topics: a topic described by three or more speakers, each saying at least two sentences on it; pass if none. Label it "estimate, check", since speaker labels are unreliable.}
   {MEASURE 4, e.g. Asks: every ask on the board plus every new one made in the room; pass if all left with an owner and a date said aloud. List each with "owner said: y/n, date said: y/n" and its timestamp.}
   {RATING, e.g. count, median rating, and share who said they got to speak, from the page's stored answers or the form. Never record or report who gave which answer.}
3. Write one row to the sheet "{MEASURES_SHEET}" (in {PERSON_NAME}'s storage), in the first empty row, in the sheet's column order. Copy pass/miss formulas from the row above with the row number changed. Never edit an earlier row. Read the row back and confirm it.
4. Email {PERSON_EMAIL} only, subject "Pilot measures | {Day Mon DD}": one line per measure (pass or miss, with the number), then the rating, then any ask that left without an owner or a date, with its timestamp, so it can be fixed the same day. Then the sheet link.

DECISION (run once, after the last pilot meeting)
1. Read every row of "{MEASURES_SHEET}" and the decision inputs on its summary tab (read them; don't assume).
2. Apply the rule as written:
   {KEEP: e.g. every measure passes in at least {N} of {TOTAL} meetings and the median rating is at least {R}.}
   {KEEP WITH CHANGES: e.g. one or two measures fall short by one meeting; name the fix for each.}
   {GO BACK: e.g. two or more measures pass in {N} or fewer meetings, or the median rating is under {R}.}
   Say which branch the data lands in. Mark any measure that was an estimate.
3. Build a short page in the house style: the recommendation in one sentence; each measure meeting by meeting against the old format's baseline; what people said about the format (from transcripts and mail, without names attached to ratings); what to change if kept; and, if kept, who owns the ritual from here. A collapsed Receipts block.
4. Draft one email from {PERSON_NAME} to {DECIDERS}, following company rules section 7 in full (code reserved first, red first line, receipts at the top, signature typed in): the recommendation first, the results in plain lines, the page link, and exactly what each person needs to decide by {DECIDE_BY}. Run the writing-cleanup skill, then the receipts gate, blind, through the Agent tool. Never send it.
5. Email {PERSON_EMAIL} only: the page link, the draft code and subject, and the recommendation in one line.

LIMITS
Writes allowed: the sheet row (measures), the page and the one draft (decision), the runs log, the receipts log, and the email to {PERSON_EMAIL}. Never send to anyone else. Never post. Never touch tasks. Never create, edit, pause, fire or delete a scheduled task. Nothing about anyone's leave, pay or performance.

FINISH
Append "Pilot {measures or decision} finished {ISO}; {row written yes/no or branch}; record used {which}; outputs: {links}" to "{RUNS_LOG}".
