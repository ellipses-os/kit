# Team rituals: the weekly board, the monthly all-hands, and pilots

Once each person's day runs on its own, the same machinery can prepare the meetings the whole team shares. Two patterns worked, and one rule for changing either of them.

## The weekly lane board

A person-by-person status round in a weekly team meeting tends to run long, and most of it is people telling each other things that are already written down. A lane board replaces it.

- Pick four to eight lanes: the projects or areas that matter this quarter. Each lane has one owner.
- Each lane has one standing "Lane status" task on the board. Before the meeting, the owner posts one comment on it in a fixed shape: STATUS (on track, at risk, blocked), MOVED, NEXT 7 DAYS, BLOCKED BY, ASK OF THE ROOM. A comment is used because most task boards keep only one current status update per project, and a comment keeps the history.
- The evening before the meeting, the owner of the ritual's Claude builds the board: one card per lane, blocked lanes first, then at risk, then on track. A lane with no owner update is filled from its open tasks and labeled "auto, no update from {owner}". Every card links its sources.
- After the lanes: "Outside the lanes" (blockers that fit no lane), a short round for anyone whose note didn't land on a card, and "Asks and decisions", each with an owner and a date.
- The morning of the meeting, a refresh run rebuilds it, marks what's new, and publishes to the same link, so the link never changes.
- The meeting walks the board, blocked lanes first. Every ask leaves the room with an owner and a date said aloud.
- Close with a one-question rating (1 to 10, and "did you get to speak?"), stored without names.

Never on the board: anyone's time off or leave, pay, performance, anything from a one-to-one, customer names, pricing the room shouldn't see. Items that carry one are left out and counted as "{n} items withheld".

Setting it up, once:

1. Agree the lanes and owners in the meeting before you start.
2. Each lane owner creates their own "Lane status" task in the lane's project (one writer: nobody's Claude creates tasks for someone else), or the ritual owner creates them by hand with each owner's OK.
3. Send owners the comment shape and the deadline (for example noon the day before).
4. Fill the lanes, task names and the board's fixed link into `tasks/lane-board.md`.

Templates: `tasks/lane-board.md` and `tasks/pilot-review.md`.

## The monthly all-hands

A monthly all-hands that walks through every number becomes long and flat, and the slides drift out of date. A readout built from live data fixes most of it:

- Build the page a few business days into the month from the sources on the data map, with each figure's source and data-through date.
- Keep numbers only as exceptions: a figure gets airtime when it moved past a line you set in advance (for example 10% against the same period last year, or against target). The rest sit in a collapsed appendix.
- Give each manager or department a box to fill in their own words before the meeting: what moved, what's stuck, what they need. The page saves their notes; the run never writes for them.
- Keep the human parts: mission and values at the top if you read them, every manager's voice, and the owner's closing remarks.
- Refresh the page on meeting morning. If the calendar shows no meeting that month, skip and log it.
- End with the same one-question rating, and review the format after two meetings.

Template: `tasks/monthly-all-hands.md`.

## Changing a ritual: a pilot with a decision rule

Changing how the team meets is a people decision, so treat it like an experiment with the answer written down first.

1. Fix the length: a set number of meetings (for example three to six).
2. Write the measures before the first meeting, each with a pass line. For example: finished on time; opener under {N} minutes; no topic retold by {N} or more people; every ask left with an owner and a date; median rating at least {N}; most people got to speak.
3. Write the decision rule before the first meeting: keep, keep with changes, or go back, and exactly which results lead to each.
4. Keep the old way running as the fallback (for example, the usual agenda still gets built and links the new board).
5. A measures run after each meeting scores it from the verbatim transcript and writes one row to a sheet. It never edits an earlier row. Build the sheet before the first meeting: one row per meeting, one column per measure with a pass/miss formula next to it, a column for which record was used, and a summary tab with the pass lines and the decision rule's inputs as editable cells. Add a baseline row or two from meetings in the old format.
6. A final run applies the decision rule as written, says which branch the data landed in, and drafts the recommendation for the people who decide. People decide.

Template: `tasks/pilot-review.md`.
