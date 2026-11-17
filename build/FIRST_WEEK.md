# The first week

A checklist for the owner after the team is set up. Most problems in the first week are setup steps, not bugs, and most are cheap to fix if you catch them in the first two days.

## Day 1: did everyone's first brief arrive?

- For each person, check their runs log for a "started" and a "finished" line from the morning brief. No log line means the task didn't run; a start with no finish means it stopped partway.
- A missing brief is almost always one of: the task's approval mode left at "ask", a connector missing from the task, the rules file not found by exact title, or the time zone set as an offset instead of a name.
- Have anyone whose brief didn't arrive run `build/SELF_CHECK.md` with you on a call.

## Day 2: the first drafts

- Ask each person to send one draft from their debrief, through any of the three exits: sent as written, changed and sent (with "Gate #code" if they changed a fact), or deleted.
- Look at one sent message per person for a leaked red block or "RECEIPTS" line. The debrief's leak check should flag it too; if it didn't, check that it's in their debrief prompt.

## Day 3: the board

- Look at the task board for duplicates and for tasks with no "Created by Claude from:" line. Duplicates usually mean two people's Claudes are creating tasks for the same person; check the one-writer rule is in everyone's setup.
- Check that nobody's Claude is completing or re-dating someone else's tasks.

## Day 4: the rules

- Collect every "the rules should say..." from the week into one list. Send it to your one rules editor as proposed lines, each with its reason and a receipt.
- Ship one rules version with those lines, and check the next morning's runs logs show the new version.

## Day 5: ask, in person

Ask each person three questions, out loud rather than in a form:

1. What slowed you down this week?
2. What did your Claude do that surprised you?
3. Is there anything you stopped trusting?

Write the answers down. They're the best input for the course (`build/BUILD_YOUR_COURSE.md`), for the next rules version, and for deciding what to build next.

## End of week one

- Everyone runs `build/SELF_CHECK.md` on their own and pastes the one-line result into their runs log.
- Count what you can see without opening anyone's private work: runs logs with start and finish lines, additions written to the shared folder, drafts sent by each of the three exits.
- Start the course the following week, not before.

## Things that helped adoption in the original build

- **One person first.** The owner ran the whole system alone for a week before anyone else joined.
- **Small waves.** One pilot teammate, then groups of three or four.
- **Live setup sessions.** A short group call where everyone pastes their setup together and the owner fixes problems on the spot. Faster than written instructions alone, and people see that everyone else hits the same snags.
- **A quick way to get help.** People were told exactly who to ask and how ("paste your runs log line and the error"), and got an answer the same day.
- **Short explainer videos,** made from code so they can be re-rendered when a rule changes.
- **A self-repair path.** The self-check paste, so people could inspect and fix their own setup without waiting for the owner.
