# What broke and what we changed

Every rule in this kit came from a failure. These are the general lessons, without the company details. If you skip a rule, read its row first.

## Rules and versions

| What broke | What changed |
|---|---|
| Several chats each produced a "latest" rules file | One editor, a version on every change, the file in the shared folder is the file |
| A chat found an archived rules copy by a name search and quoted it as current | Archive readable by the owner only; runs find the rules by exact title and check the parent folder |
| The rules file was missing for a few minutes during a swap, and a run started in that gap | Install the new file before archiving the old one |
| Many rules versions in one evening; nobody could tell which runs had picked up which | Every run logs the version it read; a change isn't done until the log shows it |
| The rules file grew until every run spent a long time reading it | Prune regularly; move procedures to their own files |

## Runs and the clock

| What broke | What changed |
|---|---|
| Runs stopped at an approval prompt nobody was there to click | Each scheduled task set to approve automatically; the first run of each one checked by hand |
| A run building a page stopped on a script that read a file from disk, even with automatic approval | Pages built with Claude's file tools; code only for calculations |
| A tool left at "ask" was simply missing from an unattended run | Allow the few tools runs need (email the owner, save a file); leave the rest at "ask" |
| The scheduler fired late, and a backup check built a second brief | "Not yet fired" means wait; backup watchdogs removed |
| A clock change moved one person's debrief out of their workday | Debriefs use each person's own time zone name |
| Run logs carried times ahead of the real clock | Every stamp comes from a clock tool |
| A task created through a different screen ran without a model set | Check every new task's settings after creating it |
| A search of a downloaded document found nothing because the text came back encoded | Read documents with a tool that returns plain text; "not found" in undecoded text is no answer |

## Drafts and sending

| What broke | What changed |
|---|---|
| Two chats handed out the same draft code within a minute | Reserve the code in the log, read it back, then create the draft |
| Sent and deleted drafts were reported as still owed and rebuilt | Match drafts by draft ID; read the whole thread; three exits |
| A sent email still carried its receipts block | Receipts always at the very top in red; an evening leak check |
| A draft said "it's on your calendar" before the invite existed | The gate treats "on your calendar" and "posted" as system-state claims that need the system |
| A handoff went to a teammate as an open question | Make the call, show the logic, one chance to redirect |
| The mail connector rewrote links into redirect links on save | Accepted as is; a redirect isn't a fix |
| Editing a draft dropped its attachment | Runs never write to a draft with an attachment |

## The task board

| What broke | What changed |
|---|---|
| A run overwrote task descriptions with its evidence | Evidence goes in comments, never the description |
| Half the tasks a Claude created were messages or waits that a draft already covered | A task only for real work or a decision; messages are tracked by their drafts |
| Two Claudes created the same task for one person a minute apart | Only the owner's own Claude creates the owner's tasks |
| Claude-made due dates turned guesses into overdue counts | A due date is a date a human said, or none |
| New tasks piled into one section of a project | Read the sections and pick the right one |
| A brief listed a task as overdue that was finished days earlier | Overdue lists come from a fresh query of incomplete tasks in the same run |
| A chat tried to complete a task a run had already closed, and doubled the evidence | Read a task's state before touching it |
| Comments saying "draft ready" reached people with no context | No "draft ready" comments; codes stay in the owner's runs log |
| A hold on assigning teammates parked their work on the sender | Turn assignment rules on deliberately, with a one-time handover |
| Proven work stayed open because the proof was worded differently | A run closes its own person's task on any linkable evidence, and lists it |

## Meetings and privacy

| What broke | What changed |
|---|---|
| One-to-one files sat in a folder the whole team could read | Two-person meetings never go in the shared folder |
| Two write-ups of one meeting made the same task twice | Action items come from one verbatim transcript only |
| A notetaker joined late and missed the start | Use the next transcript source for the part it missed, and say so |
| Summaries were quoted as if they were what people said | Quotes and tasks come from verbatim transcripts; summaries are named as summaries |
| "Most senior attendee builds the agenda" left two Claudes building | A named stand-in rule, and a check for an existing agenda before building |
| A connector meant for the owner alone went on the whole team's list | Lock owner-zone connectors at the tool level and say so in the rules |

## Receipts

| What broke | What changed |
|---|---|
| Wrong claims reached a person, and none was arithmetic: a deal's terms taken from a message, "pushed live" repeated without checking, a run reporting it posted when it had only drafted, a rule quoted from memory | Receipts with five classes, the instruction rule and a blind gate |
| A disagreement went to the owner before anyone asked the system | Escalation order: ask the system first |
| A checker read an archived rules file and passed a stale rule | The checker follows the same exact-title, parent-folder lookup |

## Not yet solved in our build

Name these in your own rules if they bite you.

- Long-running chats can still drift from the rules; restart long work in a fresh chat with a handoff note.
- Some chat systems don't expose direct messages to Claude; a brief that claims chat coverage should say what it could and couldn't read.
- Members' task prompts lag the current templates; the rules file overrides them, but a quarterly refresh is cleaner.
