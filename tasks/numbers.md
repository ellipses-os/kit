Prompt version {PROMPT_VERSION}. Numbers for {PERSON_NAME}. Weekdays at {HH:MM} {HOME_TIME_ZONE}. Cloud.

WHO AND WHY
{PERSON_NAME} ({PERSON_EMAIL}) wants yesterday's numbers from every source on the data map, checked before they're written, so the morning brief and the team can quote them without re-pulling. A number that fails a check is left blank with the reason. Nobody is watching; never ask, never wait.

RULES FIRST
Search with title = '{COMPANY_RULES_FILE}' (exact) and read the copy whose parent folder is {RULES_FOLDER}; never an archived copy. Section 1 (the data source map and its checks) governs every number. Read {BRAND_FILE} the same way. Times from a clock tool. Append "Numbers started {ISO}; rules {COMPANY_RULES_FILE} {version}; prompt {PROMPT_VERSION}" to "{RUNS_LOG}".

PULL
For each line of the data source map that {PERSON_NAME}'s connectors can answer: yesterday, week to date, and the same period a year earlier where the source has it. Primary sources only; cross-checks are labeled as cross-checks. On {WEEK_START_DAY} add last week; on the first business day of the month add last month.

CHECK
Run the map's checks on every figure before writing it (freshness, totals, same period, same currency, no double count, plausible range, right source, labeled). A figure that fails is blank with "check failed: {which}, {why}".

WRITE
- numbers.md and numbers.html in "{OUTPUTS_FOLDER}/{YYYY-MM-DD}/numbers/": every figure with its source and data-through date, a chart against a baseline wherever there is one, in the house style, written with Claude's file tools (code is fine for the calculations).
- {OPTIONAL: a copy of numbers.html to Numbers/{YYYY-MM-DD}/ in {SHARED_FOLDER}, leaving out anything in the owner zone.}
- Publish the page privately.

RECEIPTS
Every figure is a P line (or I for anything calculated, with "wrong if"). Run the receipts-gate skill on the headline figures, blind, through the Agent tool. Append FIX and HOLD lines to "{RECEIPTS_LOG}".

OUTPUT
No email unless a source failed or a figure is held; then one email to {PERSON_EMAIL} only, subject "Numbers | {Mon DD}: {n} held", listing what and why.

LIMITS
Read only on every data source: never call a write tool. Email {PERSON_EMAIL} only. Owner-zone figures never go in the shared copy. Never change scheduled tasks. Never delete anything.

FINISH
Append "Numbers finished {ISO}; figures {n}; held {n}; coverage: {list}; outputs: {links}" to "{RUNS_LOG}".
