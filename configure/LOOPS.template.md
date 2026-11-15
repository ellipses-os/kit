# {LOOPS_FILE} · Open loops · {COMPANY_NAME}

Version: {YYYY-MM-DD}a
Owner: {OWNER_NAME}. Editor: {RULES_EDITOR}, the same as {COMPANY_RULES_FILE}. This file is the procedure behind {COMPANY_RULES_FILE} section 4. Where the two differ, the company rules win. Every run reads this file by exact title with its parent folder confirmed as {RULES_FOLDER}, never an archived copy.

Why this exists: when every request became a task, Claude created tasks faster than people closed them, and about half of them were messages or waits that a draft or a watch line already covered. {Replace with your own reason and date when you adopt it.}

## 1. What a loop is

A loop is something a person owes or is owed, said by a human in mail, chat or a meeting transcript, or told to Claude directly. Each loop has one owner (the person who owes it) and one outcome.

Not loops:
- Claude's own suggestions, open questions and top picks. They stay in the brief.
- "Someone should handle this" with no named owner. List it in the brief as "owner not named"; never pick the most likely person.
- A message nobody was asked to answer.

Record a request as a request. Don't write that someone committed to it unless they said so.
Don't widen a loop. "Ask the supplier for a quote" ends when the question is sent. If the person also needs the quote, that is a second loop, a wait.

## 2. The record

A document named "{OPEN_LOOPS_DOC}" in the person's own storage, beside their runs log. The first run that needs it creates it. Read it with a tool that returns plain text. Append only: never edit or delete a line. If your file connector can't append to a word-processor document, keep this record as a plain text or markdown file instead. It is Claude's memory, not a checklist; the person acts in mail, the task board and the brief.

Line formats:
- `LOOP #L-MMDD-xNN | owe or waiting | {owner} owes {who} | Done when: {outcome, with its scope} | source: {link}, read {time} {date} | deadline: {date a human said, or none} | review: {date} | act: {draft #code, chat {link}, watch, or task {link}}`
- `UPDATE #L-MMDD-xNN | {what changed: new source, new deadline, part answered, nudge sent 1 of 2, draft deleted} | {source, read time}`
- `CLOSED #L-MMDD-xNN | done or dropped | {evidence link, or "per {name}, {where they said it}"} | {time}`
- `REOPENED #L-MMDD-xNN | {why} | {source, read time}`
- `OPEN {date} | {count} | {every open ID, comma separated}`

IDs: the date first recorded, a letter for the writer (B morning brief, D debrief, A agendas, C a chat), then two digits. A chat re-reads the doc after it appends and renumbers its own line if the ID was taken.

A deadline is a date a human said. A review date is Claude's own date to look again: the deadline when there is one, otherwise 7 days out. A review date is never a due date, never "overdue", and never written into the task board.

Every debrief ends by appending one OPEN line. The next run starts from the last OPEN line and the lines after it. If the count and the IDs disagree, the run says so in COVERAGE and rebuilds the open set from the LOOP, CLOSED and REOPENED lines.

## 3. Each run, in this order

The midday refresh only reads: it lists what is new or due and writes no line. The next writing run records what it found.

1. Read the open loops (the last OPEN line and everything after it) and the person's open tasks (a fresh query, same run).
2. Read the run's normal sources. Match what is new against open loops, open tasks and loops closed in the last 30 days, by owner, outcome and scope (which report, which version, which month). A second mention of the same thing, in any channel, is an UPDATE, never a new loop.
3. Record each new loop once, the first time it is seen.
4. Check open loops for evidence (section 5) with what the run already read. Make extra reads only for loops at their review date or touched by something new.
5. Append UPDATE and CLOSED lines, then act on new loops (section 4). The debrief appends OPEN last.

## 4. Where the person acts

- An email the person owes: a draft (company rules section 7). Its CODE line ends "| loop {ID}". No task.
- A chat reply the person owes: the brief, with a link to the message and paste-ready text.
- Something owed to the person: a watch line in the brief when its review date comes or its deadline passes. No task on the person waiting.
- Work a message can't finish (build, fix, publish, pay, order, ship, hold a meeting, an analysis), and decisions others are blocked on: a task on the run's own person, with "Created by Claude from:" and "Done when:". A due date only when a human said one.
- A small choice that rides on a reply ("Tuesday or Wednesday?") stays with its draft, under a red RECOMMENDED line.

One writer. A run never creates a task for another person, unless that person isn't on the system yet (company rules section 0.1). When the owner wasn't in the meeting or on the thread, the asker's debrief drafts the message that tells them, and the waiting loop reads "not yet sent" until it goes out.

## 5. What closes a loop

Done: something the run can link to shows the outcome happened, in any channel and any wording.
- "Send the revised quote": the sent message with the quote in it. Not "I'm working on it".
- "Get a delivery date": an answer that gives the date. Not "checking".
- "Decide whether to renew": the decider's own words choosing. Not "leaning toward it".
- "Send the three figures": all three. One of three is an UPDATE.
- The owner's own clear word counts. Record it as "per {name}".

Dropped: the owner or the asker says it's no longer needed, or a condition a human stated has been met.

Never closes a loop: a passed date or meeting; silence; "on it", "thanks", "will send Friday"; a plan; a deleted draft; a sent draft that said something else ("I need another day" is an UPDATE); a guess that other work replaced it.

Don't add conditions nobody asked for. A closed loop stays closed unless something new says otherwise.

## 6. Drafts and nudges

- A sent draft closes only what it actually did.
- A deleted draft: the DROPPED line; the loop stays open, gets no new draft unless asked, and goes on the end-of-week list.
- A draft made obsolete by another answer: say once in the brief "#code is obsolete, delete it". Never write to it.
- Nudges follow company rules section 5. Only sent nudges count. After two sent with no answer, the loop goes on the end-of-week list.

## 7. What the briefs show

- Morning brief: YOU OWE (with draft code or chat text, nearest deadline first), OWED TO YOU (waits at review or past deadline), CLOSED FOR YOU (with evidence links).
- Debrief: loops opened and closed today; COVERAGE ends with the loop and task counts.
- Last debrief of the week: the end-of-week list and the count of reopened auto-closes.
- A loop that isn't due for review isn't listed. The doc holds it.

## 8. What a person can say

In any Claude chat, or by replying to their own debrief email:
- "Log: I told Sam I'd send the quote by Friday." Records a loop Claude couldn't see, such as a promise made in person.
- "Done #L-0304-D03", or "Done: the quote, I told him at lunch." Closes it on their word.
- "Drop #L-0304-D03." "Keep #L-0304-D03" leaves it open and moves the review a week.
- "Reopen ..." for anything closed wrongly. Unticking the task does the same.

## 9. Backlog cleanup (one time, when you adopt this file)

Paste into a Claude chat:

```
Backlog cleanup. Read {COMPANY_RULES_FILE} and {LOOPS_FILE} first. List every open task assigned to me. For each, look for evidence under the Closing rule: my sent mail, my chats, transcripts, files, and the task's own comments. Sort them into:
A. Done, with the evidence link.
B. Duplicate of another open task (name the one to keep).
C. A message already covered by a draft, or already sent.
D. Tied to a meeting or date that has passed, or no longer needed (say why).
E. Still real.
Show each group as a numbered list with a count, then wait. When I approve a group or line numbers, complete those tasks and write one line in my runs log with the counts. For group E, remove due dates nobody said, keep real deadlines, and record anything I'm waiting on as a loop. Don't touch anyone else's tasks.
```

## 10. Loop audit (end of week, when asked)

```
Loop audit. Don't read my open loops doc yet. Pick 10 requests or promises from my mail, chats and transcripts of the last 7 days, from mixed channels, including some with no date. Then check each against my open loops doc and the task board: recorded, right owner, right outcome? Then pick 10 items closed this week and check the evidence really shows the outcome. Report misses and wrong closes with links. Change nothing.
```

## 11. Limits

- A promise made in person is invisible until someone logs it (section 8).
- If the task board refuses completions, those tasks stay open until their owner ticks them; the loop still records the evidence.
- The doc grows. Decide when to start a new one (for example each quarter, carrying the last OPEN line across).
