# The rules order

When two instructions disagree, the system needs one answer every time. Here it is.

## In a scheduled run

1. Company rules win.
2. Then the person's own rules.
3. Then the task prompt.

The prompt is the job. The rules are the law. A prompt written last month can carry a line the company rules have since replaced; the run follows the rules and says in its coverage line which old line it overrode.

## In a chat

Organization instructions and the person's own instructions shape behavior. The company rules are read when the chat does company work (drafting for someone else, pulling a number, touching the task board) or when someone asks.

## For data

The data source map beats any prompt. If a prompt says "pull everything from tool X" and the map says tool Y owns that number, a run follows the map and notes the conflict. A chat asks first.

## For decisions and meetings

- A decision is settled by what the decider wrote (sent mail, a chat message) or said on a verbatim transcript. A summary, a task description or memory is secondhand.
- The roster in the company rules settles who is on the team. Someone who left is never an owner, recipient or person to ask.

## How the rules file stays trustworthy

These habits came from real failures (see `10-what-broke.md`):

- One editor. One chat or one person edits the company rules. Everyone else proposes lines, with the reason and a receipt.
- A version on every change. The first line of the file carries its version (for example `2026-03-04a`). The old file moves to an archive folder only the owner can read.
- Install before archive. Upload the new file under a temporary name, check it, then archive the old one and rename the new one. The rules file is never missing, not even for a minute.
- Read by exact title, check the folder. A run finds the rules with an exact-title search and confirms the parent folder before reading. Never a "contains" search and never a saved file ID: both can open an archived copy.
- A change isn't done until a run shows it. Every run logs the version it read. When the new version appears in the runs log, the change took effect.
- Every rule says why. A one-line reason under each rule, with the date. People follow rules they understand, and a later editor can tell which rules are safe to drop.

## Keep it short

Every run reads the rules file first, every time. A long file costs time and money on every run and buries the rule that matters. When the file passes about 30 to 40 pages, prune: merge rules that say the same thing, drop the "why" stories older than a few months into an archive note, and move procedures into their own files that the rules point to.
