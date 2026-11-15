# The human step

Claude drafts. People send. This is the line the whole system is built around.

## What runs may and may not do

- A run emails its owner and nobody else. No To, Cc or Bcc to anyone but the owner, ever.
- Anything meant for another person is a draft in the owner's mail.
- Runs read chat; they never post to it. In a live chat, Claude gives the text to paste.
- One named exception at most: a weekly update that posts its owner's status update, which the owner edits before the meeting.

## Draft codes

Every draft gets a code as the first characters of a red first line: `#MMDD-NN` (month, day, a two-digit number). New-thread subjects start with the code; reply subjects are never changed, because changing them breaks threading.

The red first line says, in order: the code, when to send it and why, "Checked through {time} {date}", and "Changes: say Fix #code in Claude. Delete this block." The receipts ledger sits under it, also in red. The person deletes the red block before sending.

### Handing out codes without collisions

Two chats can read the log at the same moment and pick the same number. So:

1. Read today's drafts, today's sent mail and today's code lines in the runs log; pick the next number above all of them.
2. Append `RESERVE #MMDD-NN | {run or chat}` to the runs log and read it back. If someone else's line already has that code, take the next one.
3. Create the draft, then append `CODE #MMDD-NN | {run or chat} | {subject} | msg {message id} | draft {draft id} | thread {thread id}`.
4. After any later change to the draft, append `WRITE #MMDD-NN | {who} | msg {new message id} | {what changed}`.

The draft ID stays the same through every save and through the send; message IDs change on every save. Match drafts by draft ID.

## The three ways a draft ends

1. Sent as written.
2. Changed by hand and sent. If the person changed a fact, date, number, name or ask, they say "Gate #code" in a chat first, and the gate rebuilds the receipts from the current text. A typo fix needs no gate.
3. Dropped. The person deletes it. The next debrief lists it once under DROPPED, logs a DROPPED line, and never re-drafts it unless asked. Dropping closes nothing; the loop it served stays open.

Before a run calls a draft gone or still owed, it reads the draft's thread in full and looks for a sent message carrying the draft ID. Never by subject alone.

## Rules that protect hand edits

- A draft whose message ID no longer matches its last CODE or WRITE line was saved by a person. Runs don't write to it; they list the pending change in the brief instead.
- A draft with an attachment is never written by a run (editing drops attachments).
- A reply draft is never edited in place. To change one, make a fresh reply draft with the same code and retire the old one with a one-line note to its owner.
- People: open a draft right before you change or send it, and close drafts you're not working in. An open window can save an old copy over a run's fix.

## Decisions

When a decision is blocking someone, the person's Claude makes the call: it pulls the data, picks an option, shows the logic in a few lines, and gives the person one chance to approve or redirect. A decision stays open only when it turns on judgment or values (people, money commitments, relationships), and even then Claude leads with a recommendation. Nothing goes to another person as a question nobody has tried to answer.

## Leak check

Every evening, the debrief looks at mail sent today for a leftover code, "RECEIPTS", "GATE |" or "Checked through". If it finds one, it flags it at the top, so a leaked ledger is followed up the same day.
