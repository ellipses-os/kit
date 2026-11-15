# One loop, one tracker

An open loop is something a person owes or is owed, said by a human in mail, chat or a transcript, or told to Claude. The system tracks each loop in exactly one place. Most failures in this area came from tracking the same thing twice.

## Where a loop lives

| The loop | Where it's tracked |
|---|---|
| An email the person owes | The draft that answers it, by its code |
| A chat reply the person owes | The brief, with paste-ready text |
| Something owed to the person | A watch line in the brief; a nudge draft once its deadline passes |
| Real work a message can't finish (build, fix, publish, pay, order, ship, hold a meeting, analyze) | A task on the board |
| A decision others are waiting on | A task on the board |

Every loop is also one line in the person's "Open loops" document: an ID, owe or waiting, who, the outcome that ends it ("Done when"), the source and when it was read, a deadline only if a human said one, a review date, and where the person acts.

Claude's own suggestions and open questions are not loops. They stay in the brief.

## Task board rules

- One writer. Only a person's own Claude creates tasks for that person. An ask to someone else is the asker's waiting loop; it reaches the owner through the message, recap or transcript the owner's own Claude reads. If the owner isn't on the system yet (the company rules list who is), the asker's Claude may create the task in the team project and say so.
- Search before creating. By the source link, by the meeting title and date, and by the task's own words. If any search finds it, comment on the existing task instead.
- Every task a run writes starts the same way: "Created by Claude from: {direct link}", one sentence of context, and "Done when: {outcome}".
- Due dates are dates a human said. Claude never invents one. Review dates live in the Open loops doc, not on the board.
- Pick the right section. Read the project's sections first and file the task where it belongs. Leaving the section out drops it in the first section.
- Read the task before touching it. Completed, assignee, due date, last comment. Never complete something twice.
- Never touch someone else's task. No completing, re-dating, reassigning, renaming or editing it. If it looks done, say so in the owner's brief with the evidence.
- No comments to say a draft is ready. Comments notify every follower; a draft code means nothing outside its owner's mail.

## Closing

A run closes its own person's task or loop, without asking, when it can link to evidence that the outcome happened: a sent message, a file, a system's state, the other person's confirmation, a transcript line, the owner's own word. It posts the evidence as one comment, completes the task, logs an AUTOCLOSE line, and the next brief lists it under CLOSED FOR YOU.

Not evidence: a passed date, silence, "on it", a plan, a deleted draft, or a guess that other work replaced it. A decision closes only on the decider's own words. A task its owner reopened is never closed by a run again without the owner's word.

If the board refuses the completion, the run doesn't retry. It keeps the evidence comment and lists the task under LOOKS DONE for the owner to tick.

Tripwire: at the end of each week, count the week's auto-closed tasks that were reopened. Above about 1 in 20, the person's runs stop closing and list closes under LOOKS DONE until the owner clears it.

## Friday's list

One list a week replaces daily approval lists: loops past a stated deadline with no evidence, waits with two unanswered nudges, loops whose draft was deleted, undated items unchanged for two reviews, and items tied to a meeting that has passed. The person answers keep, done or drop. No answer changes nothing.

## Nudges

Nudges are drafts to the person who owes, never posts. First on the due date, second two business days later, then stop and put it on Friday's list. Before any nudge, check the thread for a stated blocker or an agreed later date. Outside parties get at most one nudge a week per thread.
