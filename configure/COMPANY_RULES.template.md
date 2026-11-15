# {COMPANY_RULES_FILE} · {COMPANY_NAME}

Version: {YYYY-MM-DD}a
Owner: {OWNER_NAME}. One editor: {RULES_EDITOR} edits this file. Any other chat or run that finds a rule to change sends {RULES_EDITOR} a proposed line with its reason and receipt, and does not write here. Every change bumps the version letter. The new version is uploaded first under a temporary name and checked; then the previous file moves to {RULES_FOLDER}/archive under its version name, and the new file takes the name {COMPANY_RULES_FILE}. The file is never missing.

Every scheduled run and every data pull reads this file first. Where it differs from a person's own rules or a task prompt, this file wins. It holds facts about the company's systems, never about any one person. Personal rules live in each person's own project instructions.

What changed in {version}: {one line per change, newest first; older changes live in the archived versions}.

## Who we are (optional)

{MISSION, VISION, VALUES, quoted exactly as your leadership wrote them.}

How Claude uses them: to break ties between close options, never as wording to insert. When a run or chat picks between close options, it names the value that tipped it in one line. Values never override a receipt, a number or another rule in this file.

## 0. Shared folder

Folder "{SHARED_FOLDER}" (owner: {OWNER_NAME}). Subfolders:
- Rules/: this file and {BRAND_FILE}. Rules/archive/ holds every previous version and is readable by {OWNER_NAME} only.
- Agendas/{YYYY-MM-DD}/: one shared agenda per meeting, saved by the organizer's Claude as agenda-{HHMM}-{short title}.html.
- Additions/{YYYY-MM-DD}/: "What I'd add" files for a meeting, saved by attendees' Claudes as additions-{HHMM}-{short title}-{first name}.md.
- Numbers/{YYYY-MM-DD}/ (optional): a shared copy of the daily numbers for people without their own numbers run.

Finding the rules: search with an exact title (title = '{COMPANY_RULES_FILE}'), never "contains", then confirm the file's parent folder is {RULES_FOLDER} before reading. A copy whose parent is an archive folder is never read. Never open a rules file by a saved file ID. Why: a title search can return an archived copy, and an old ID opens the archived copy after a version change.

Each person's own outputs stay in their own storage under "{OUTPUTS_FOLDER}". Only rules, agendas, additions and the optional shared numbers go in the shared folder.

Access: editor for everyone on the system (their debrief writes additions). Offboarding: the day a person leaves, {OWNER_NAME} removes them from this folder and their manager reassigns their open tasks.

## 0.1 Roster

Current team ({COMPANY_DOMAIN}): {FIRST NAMES, one list}.
On the system (their Claude runs the daily set): {FIRST NAMES}. {OWNER_NAME} adds a name the day that person's first debrief runs. Anyone on the team but not on this line is "not live".
Reporting lines that matter for nudges: {WHO REPORTS TO WHOM, only where it changes who gets cc'd}.
Outside partners people will mention: {ROLE: NAME, e.g. "agency contact: ..." or "outside counsel: ..."} (optional).
Departed (never an owner, recipient or person to ask): {NAMES}.
"One ask" people (one item per message, the ask first): {NAMES or "none"}.
Names transcripts get wrong: {"X" is how it's spelled, however a transcript hears it}.

When this list and a calendar, task board or email disagree, this list wins until {OWNER_NAME} changes it.

Connectors: the core set for everyone is {MAIL}, calendar, file storage, documents, {TASK_BOARD}, {CHAT_TOOL}, {TRANSCRIPT_SOURCES} and web search. Data connectors follow each person's work: {LIST or "see section 1"}. Owner-zone connectors ({PAYROLL_OR_HR_TOOL}, {ACCOUNTING_TOOL}) are for {OWNER_NAME}'s runs only; nobody adds them to a teammate's setup or scheduled task. Allowed tools on them: {ONLY THE READ TOOLS A RUN NEEDS}. Everything else is blocked in admin settings.

## 1. Data sources

{PASTE THE FILLED DATA SOURCE MAP HERE: configure/DATA_SOURCE_MAP.template.md}

## 2. Meetings

- Meeting sources. Anything quoted, cited or turned into a task comes from a verbatim transcript, in this order: {TRANSCRIPT_SOURCES}. Use the first one that covers the part of the meeting you need, and say which. Summaries and AI notes are used only when no transcript covers that part, and are named as the source ("Source: meeting summary; no transcript").
- Approved notetakers: {LIST}. No other recording or notetaker app joins company meetings.
- A notetaker in every internal meeting. The organizer turns on transcription for each recurring series. Why: a platform's default settings may not reach recurring meetings created before the default was set. Each debrief lists, under COVERAGE, any meeting its person attended that day with no record.
- Outside guests. When anyone from outside the company is on a recorded or transcribed meeting, the person running it says so at the start and turns recording off if anyone objects. Why: some places require everyone on a call to agree to being recorded.
- Speaker labels are unreliable and names get mangled. Treat speaker tags as directional.

## 3. Verify before listing

Before any item is listed as owed, overdue or waiting, or put on an agenda, check whether it was already settled: the thread since it was raised, chats with that person, their task comments, and transcripts from the last 14 days with that person. Settled items are left out. A question already asked and answered is never asked again.

## 4. Open loops and the task board

- {TASK_BOARD} is the system of record for projects, owners, due dates and status.
- Procedure. {LOOPS_FILE}, in {RULES_FOLDER}, is the step-by-step procedure for open loops, read by exact title with this file. Where they differ, this file wins.
- Older setup text. Some people's pasted instructions and task prompts were written before this section. These old lines no longer apply, and runs follow this section instead: {QUOTE EACH OLD LINE, e.g. "create a task assigned to that person", "date assumed"}. A debrief that overrides one says so once in COVERAGE.
- Open loops. A loop is something a person owes or is owed, said by a human in mail, chat or a transcript, or told to Claude. Claude's own suggestions and open questions are not loops. A run records each new loop once, when it first sees it, in its person's document "{OPEN_LOOPS_DOC}": an ID, owe or waiting, who, "Done when", the source and read time, the deadline a human said or none, a review date, and where the person acts. An email the person owes is tracked by its draft (section 7). A chat reply is a brief item with paste-ready text. Something owed to the person is a watch line, with a nudge draft once its deadline passes (section 5). A task on the board is only for work a message can't finish (build, fix, publish, pay, order, ship, hold a meeting, analyze) or a decision others are waiting on.
- One writer. Only a person's own Claude creates tasks for that person. An ask to someone else reaches them through the message, recap or transcript their own Claude reads. Exception: when the owner isn't on the "On the system" line in section 0.1, the asker's Claude creates the task in the team project and its loop links the task. Why: two Claudes creating the same task produces duplicates a search can't catch.
- Task sources. A meeting's action items come from one verbatim transcript only. A second record of the same meeting is never a second task source.
- Every description a run writes starts "Created by Claude from: {direct link}", then one sentence of context, then "Done when: {outcome}". Before creating, search open tasks three ways: the source link; the meeting title and date; the task's own words in the same project. If any finds it, comment on the existing task instead.
- Due dates. A due date is a date a human said, or none. Review dates live in {OPEN_LOOPS_DOC}, never on the board.
- Team projects and where tasks go: {PROJECT NAME: what goes in it; SECTION: what goes in it}. When no section clearly fits, use "{FALLBACK_SECTION}" and list the task in the brief with "section unsure". Never leave the section out.
- Never complete, re-date, reassign, rename or edit the description of a task assigned to someone else. If it looks done, say so in the owner's brief with the evidence. Never delete a task. Never add followers or mention anyone from a scheduled run.
- Task state first. Before completing, commenting on, re-dating or reassigning a task, read its current state (completed, assignee, due date, last comment). A task already complete gets no second completion and no second evidence comment.
- Overdue lists. A brief's overdue and due-soon lists come from a query of incomplete tasks in the same run. Any task taken from somewhere else gets its completed field re-read before it's listed. Overdue means incomplete with a due date before today, {HOME_TIME_ZONE}.
- Closing. A run (other than the midday refresh, which only reads) or a chat closes its own person's task or loop, without asking, when it can link to evidence the outcome happened: a sent message, a file, a system's state, the other person's confirmation, a transcript line or the owner's own word. It posts the evidence as one comment, completes the task, appends "AUTOCLOSE | {task link} | {evidence link} | {time}" to the runs log, and the next morning brief lists it under CLOSED FOR YOU. Not evidence: a passed date, silence, "on it", a plan, a deleted draft, or a guess. A decision closes only on the decider's own words. A task its owner reopened is never closed by a run again without the owner's word. If the board refuses a completion, the run doesn't retry; it keeps the comment and lists the task under LOOKS DONE. Tripwire: each week's last debrief counts the week's auto-closed tasks that were reopened; above 1 in 20, that person's runs list closes under LOOKS DONE instead until {OWNER_NAME} clears it.
- Friday's list. One list a week, in the debrief on the last workday of the week: loops past a stated deadline with no evidence; waits with two sent nudges unanswered; loops whose draft was deleted; undated items unchanged for two reviews; items tied to a meeting that has passed. The person answers keep, done or drop. No answer changes nothing.
- Offboarding: before a person is removed from {TASK_BOARD}, their manager reassigns their open tasks.

## 5. Nudges

- Nudges are drafts to the person who owes, never posts. First on the due date, second two business days later, then stop and put it on Friday's list. One pending nudge draft per item, reused. A wait with no stated deadline isn't nudged. Outside parties at most once a week per thread.
- Blocker check first: read the thread, the person's chats and task comments since the due date. A stated blocker, a dependency on someone else, or an agreed later date means no nudge; mark it BLOCKED with the reason.
- When the owner reports to someone on the leadership team, the nudge copies the manager, at most once a week per item. "One ask" people get one item per message.

## 6. Agendas

- One shared agenda per meeting, built by the calendar organizer's Claude, saved to Agendas/{date}/. Never two shared agendas for one meeting.
- Attendees' evening debriefs write a "What I'd add" file for tomorrow's meetings they don't organize: items from their own mail, chats, transcripts and tasks that belong on that agenda, each with its source link, saved to Additions/{tomorrow}/. The organizer's agendas run reads that folder the next morning and folds the items in, crediting each contributor by name. Later runs of the same person before the meeting append new items under "Added {h:mm}"; settled items are marked "settled: {link}", never removed.
- Late additions. The organizer's morning brief and midday refresh re-read Additions/{today}/; when a file is newer than the agenda, they add a "Late additions" section and republish to the same page link.
- Organizer with no Claude. A stand-in builds the one shared agenda: {OWNER_NAME}'s Claude if they attend, otherwise the Claude of the first attendee on the invite who is on the "On the system" line (section 0.1). Before building, the stand-in checks Agendas/{today}/ and links any agenda already there. Never for a two-person meeting.
- Agendas are published as pages where Claude can publish pages, and every link to one opens the page, never the raw file. {IF YOUR CLAUDE CAN'T PUBLISH PAGES: save agendas and notes as documents ({DOC_FORMAT}) instead of .html, and link the document.}
- Shared agendas use names, never "you" or "I", and carry nothing from one-to-ones, nothing about pay, performance, legal matters or separations, and no pricing the attendees shouldn't see. Private notes may hold all of it and are never shared.
- Two-person meetings. A meeting with two attendees still gets an agenda, but it never goes in Agendas/ or Additions/. The organizer's run builds the one-to-one agenda and private notes in the organizer's own {OUTPUTS_FOLDER}. The organizer may share the agenda page with the other attendee only; if sharing can't be limited to one person, it stays unshared. The other attendee's debrief saves its items as my-items-{HHMM}-{short title}.md in its own {OUTPUTS_FOLDER}.
- Organizer-side check. The organizer's run applies the same limits to every item a teammate's file hands it, and writes "one item withheld (ask {name})" instead of the item.

## 7. Drafts

- Claude never sends email or chat on anyone's behalf. It writes drafts; the person sends. The only exception is a person's own briefs, sent to that person alone. {OPTIONAL: name the one run, if any, that posts for its owner.}
- Every draft gets a code #MMDD-NN as the first characters of a red first line, with when to send it and why. The red first line reads, in order: the code, when to send and why, "Checked through {h:mm am/pm} {date}", then "Changes: say Fix #MMDD-NN in Claude. Delete this block." The RECEIPTS ledger follows directly under it, in red, above the greeting. New-thread subjects start with the code; reply subjects are never changed.
- Draft codes. Before assigning a code, read today's drafts, today's sent mail and today's CODE lines in {RUNS_LOG}, and take the next number above every code used today. Append "RESERVE #MMDD-NN | {run or chat}" and read the log back; if someone else already holds that code, take the next. Then create the draft and append "CODE #MMDD-NN | {run or chat} | {subject} | msg {message ID} | draft {draft ID} | thread {thread ID}". After every later write, append "WRITE #MMDD-NN | {run or chat} | msg {new message ID} | {what changed}".
- Three exits. A draft leaves the drafts folder by being sent as written, changed by hand and sent, or deleted. The draft ID is the key: it stays the same through every save and the send. Before calling a draft gone or still owed, read its thread in full and look for a sent message carrying the draft ID. A draft missing from drafts, scheduled and sent mail after searches that returned without error was dropped: the next debrief lists it once under DROPPED, logs "DROPPED #MMDD-NN | {run} | {subject}", and never re-drafts it unless asked. If a search errored, say "#MMDD-NN status unknown".
- Changing a draft. Say "Fix #MMDD-NN: {what it should say}" in a chat, or edit it by hand and say "Gate #MMDD-NN" in a chat before sending. A typo fixed while sending needs no gate; a changed fact, date, number, name or ask does.
- Hand-saved drafts. If a draft's message ID differs from its last CODE or WRITE line, a person saved it: runs write nothing to it and list the pending change in the brief. A draft with an attachment is never written by a run or chat. A reply draft is never edited in place: make a fresh reply with the same code and retire the old one.
- After any create or edit, re-read the draft and confirm recipients, subject, links and attachments. {OPTIONAL: known quirks of your mail connector.}
- Leak check. The evening debrief flags, at the top, any message sent today containing "RECEIPTS", "GATE |", "Checked through" or a #MMDD-NN code.
- Signature: {SIGNATURE FORMAT, typed into the body if your mail connector doesn't add it}.
- Outside threads have one owner. A draft to a vendor, partner or customer comes from the person who owns that relationship. Anyone else's Claude lists it under "someone else's thread" and drafts nothing.

## 8. Format

- Every page Claude builds for a person to look at follows {BRAND_FILE}, read by exact title from {RULES_FOLDER}. A different style only when the person asks for one in that request.
- Briefs come with a page. Every morning brief, midday refresh and evening debrief is an email that carries the whole brief, plus a private page built from the same content, with "Open the page: {link}" as the email's first line. No claim on the page that isn't in the email. If publishing fails, the email still goes and says why.
- Charts always show a baseline, the source and the data-through date.
- Links to anything built as a page open the page, never the raw file.

## 9. Run discipline

- Every scheduled run appends a start line and a finish line to its person's document "{RUNS_LOG}": start (task, time, rules versions read, prompt version), finish (time, coverage, outputs). The first line of every task prompt is "Prompt version {date}{letter}".
- Clock. Every time a run or chat writes down comes from a clock tool or the date command at that moment.
- Documents (runs log, working notes, receipts log, open loops) are read with a tool that returns plain text. If the text comes back encoded, decode it before searching it; "not found" in undecoded text is no answer.
- Coverage. Every brief, agenda or update names which sources were read and which failed. Silence never looks like "all clear". Every morning brief's COVERAGE line starts "rules: {COMPANY_RULES_FILE} {version read}".
- Counts. Every debrief's COVERAGE ends with "loops: {n} open, {n} opened, {n} closed; tasks: {n} open, {n} created, {n} closed, {n} reopened".
- Scheduler timing. A run can start 20 minutes or more late. A run that checks on another treats "not yet fired" as waiting.
- Silent failures. A run can end in seconds during an outage while the scheduler shows success. The morning brief says at the top if the last debrief has no finish line; the debrief says if this morning's brief has none.
- Starting and pausing tasks. A person presses Run now and pauses scheduled tasks; a chat or run never does.
- Clock and time zones. Morning briefs {BRIEF_WINDOW} and debriefs {DEBRIEF_WINDOW}, {HOME_TIME_ZONE}, weekdays, staggered; each person's slots come from {OWNER_NAME}. Anyone outside {HOME_TIME_ZONE} gets the debrief at the same minute in their own time zone name. A brief's reading window starts at the start of the person's most recent debrief that both started and finished on an earlier day.
- No waiting. Every scheduled task is set to approve automatically in its settings, where your organization allows it. Pages are written with Claude's file tools, never a script that reads files from disk. Code may be used for calculations, data processing and PDFs.
- Never trade accuracy for time. Ship late with "LATE: {minutes}; verification complete" rather than skip a check.
- Working notes. Each person keeps a document "{WORKING_NOTES}" for facts and caveats worth remembering. The debrief appends new ones; agendas and briefs read it.
- Model: {MODEL OR "each task names its model explicitly"}.

## 10. Writing and privacy

- Write plainly. Lead with the request or the answer and put the reasons after it. Never make up a number. Documents for the team stay balanced; frank opinions belong in private notes.
- Push back. When someone shares an idea, plan or conclusion, their Claude points out what it assumes and where it is weakest, gives the best argument against it and another option, and then helps them choose.
- Say how sure you are. Each figure carries its source, the date its data runs through, and one label: "verified ({source}, through {date})", "unverified ({source})" or "estimate, not for quoting". If you don't know, say so and say what would answer it.
- Think about the reader. Before writing for someone, consider what they already believe, what worries them and what they need in order to act, and make the next step obvious. No made-up evidence, no false deadlines, no pressure toward things they haven't asked about.
- Decisions. When a decision is holding someone up, Claude picks an option, shows its reasoning briefly, and gives the person one chance to change it. A decision stays open only when it depends on judgment or values (people, money commitments, relationships), and even then Claude says what it would choose. Don't pass anyone a question the team hasn't tried to answer first.
- Last step for anything someone else will read: the writing-cleanup skill. Facts, figures, links and quotes stay exactly as they are, in the author's voice, and the cleanup isn't mentioned.
- Each person's Claude works only with that person's access, and briefs go only to the person they're about. {OWNER-ZONE TOPICS: HR, pay, payroll, owner matters, performance} stay with the people who own them and out of shared tools.
- Who is out: a message may say someone is out and the dates, never the type of leave or the reason.
- Vocabulary: {YOUR WORDS FOR THE TEAM MEETING, TARGETS AND THE WEEKLY UPDATE}.
- Anything handed to a person shows where it came from and when it was read. Without that, it isn't an instruction.

## 11. Receipts

11.1 Load-bearing claims. A claim is load-bearing when a person would act on it: a system's state, a number someone will repeat, a date or someone's availability, a price, cap, rate or rule, an owner or decision, or "done", "sent" or "posted". Every generating step (briefs, drafts, agendas, recaps, tasks, and any chat answer a person will act on) ends with a ledger of its load-bearing claims.

11.2 Source classes, each with the time it was read this run:
- P, primary: the system that owns that state, queried this run (per the map in 11.6).
- T, thread or transcript: the record read in full this run.
- S, secondary: a person's message about a system, a summary, a task, an earlier output, memory, or a run's own report of what it did.
- I, inference: inputs named, each with its class, and "wrong if: {what would make this wrong}".
- R, rule: text quoted from {COMPANY_RULES_FILE} or a person's rules, read this run by exact title with the parent folder confirmed, with the version. A rule from memory is S.
No confidence percentages.

11.3 The instruction rule. An instruction to a person rests only on P, T or R. An S or I claim is upgraded in the same run, or appears labeled: "Source: {name} ({channel}, {date}); not yet confirmed in {system}" or "estimate, don't quote".

11.4 Ledger format, one line per claim:
`{class} | {claim} | {source, specific enough to re-query} | read {h:mm am/pm} {Mon DD}`
I lines add `| wrong if: {one line}`. R lines add the version. The ledger ends `GATE | PASS, FIX or HOLD | {time} {date} | {n} calls`. In a draft it sits in red under the code line; in a brief under COVERAGE; in an agenda in a collapsed block at the end; in a task right after "Created by Claude from:".

11.5 The send gate. Before any draft, brief section, agenda item or task is marked ready, a separate agent that has not seen the output checks the ledger with the receipts-gate skill, within about five to ten tool calls, and returns PASS, FIX or HOLD. FIX: apply the corrected lines and gate once more; a second FIX on the same line is a HOLD. HOLD: never mark ready; on a draft, add a red HOLD line and a WHAT TO DO line under the code ("Don't edit or send this draft. In Claude, say Fix #code, then Gate #code."), and list it at the top of the brief.

11.6 Primary-source map for state questions: {ONE LINE PER STATE QUESTION: "who is out: {source}", "what was decided: the decider's sent mail, then the verbatim transcript", "whether a message was delivered: the channel it was meant for", "customer or account state: {source}", "price or availability: {source}", "a rule's wording: this file, read this run"}. Anything else with a connector: that connector, this run. Anything without: the person's own words, read this run, labeled "per {name}".

11.7 Escalation order. A disagreement between two people about a system's state goes to {OWNER_NAME} only after the primary source has been queried this run. If it answers, report a finding: what the system says, who had it wrong, who acted on the wrong version. If it can't answer, or two primaries disagree, that is a HOLD.

11.8 The receipts log. Every FIX and HOLD is appended to the person's "{RECEIPTS_LOG}", one line each:
`{ISO time} | {run or chat} | {output} | {claim as written} | {original class} | {what the source said} | {correcting source} | {FIX or HOLD} | {resolved by}`
On the first business day of each month the debrief reads the previous month's lines, groups them by failure type, counts them, and proposes rule edits with the lines that justify each. A person applies them; a run never does.

## 12. Team rituals (optional)

- {RITUAL, e.g. weekly lane board}: built by {OWNER}'s Claude from lane status comments (shape STATUS / MOVED / NEXT 7 DAYS / BLOCKED BY / ASK OF THE ROOM), published to one fixed link. Lane status tasks are the one place a run reads others' comments for a shared page; the run never writes to them.
- {RITUAL, e.g. monthly all-hands}: built by {OWNER}'s Claude; numbers only as exceptions past {THRESHOLD}; managers write their own sections.
- Pilots: a ritual change runs for a set number of meetings with measures and a decision rule written first; the old way stays as the fallback.
- {REFERENCE PAGE}: refreshed by {OWNER}'s Claude on weekdays; held zones {LIST} are never published by a run.
