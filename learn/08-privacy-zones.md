# Privacy zones

Decide what lives where before you connect anything. Moving things after the fact is harder than it sounds.

## The three zones

| Zone | Who sees it | What goes there |
|---|---|---|
| Shared | Everyone on the team | Company rules, brand rules, shared agendas, "what I'd add" files, optional shared numbers |
| Private | One person | Their chats, scheduled tasks, drafts, runs log, open loops, receipts log, working notes, private meeting notes, their own outputs folder |
| Owner | The few people who see pay, payroll and the books | Payroll and HR systems, accounting, owner matters |

## Rules that hold the zones

- Each person's Claude sees that person's access and nobody else's. Briefs go only to the person they're about.
- Never in a shared document: pay, performance, legal matters, separations, anything from a one-to-one, vendor pricing the readers shouldn't see, anyone's leave type or reason. Shared agendas use names, never "you" or "I". Private notes may hold any of it and are never shared.
- Two-person meetings never go in the shared folder. A one-to-one still gets an agenda, but it lives in the organizer's own storage and may be shared with the other person only. Whole-team folders are readable by the whole team, and one-to-one files dropped there are readable by everyone.
- An organizer-side check. The organizer's agenda run applies the same limits to every item a teammate's file hands it, and writes "one item withheld (ask {name})" instead of the item.
- Who is out. A message may say someone is out and the dates. Never the leave type or the reason.
- Customer data in aggregate. Any statistic about customers that leaves the company uses groups large enough that no one can be singled out.

## Owner-zone data

On a team plan, connectors the owner adds may become available to the whole organization; you may not be able to keep a connector to one person. Check how your plan behaves before you connect payroll or accounting. Being available isn't the same as being connected (each person signs in with their own account), but plan for the worst case:

- Where your admin settings allow it, block every tool on an owner-zone connector except the few read tools a run needs.
- Write that limit into the company rules, so a chat that can see the connector knows it may not use it.
- Never add owner-zone connectors to a teammate's setup or scheduled task.
- Plan connectors before creating a scheduled task. In our build, a task kept the connector list it was created with, so adding or removing one meant recreating the task. Check whether that's still true for you.

## Offboarding

The day someone leaves: remove them from the shared folder, and have their manager reassign their open tasks before they're removed from the task board (some boards hand orphaned tasks to whoever clicks remove). Add them to the departed list in the company rules so no run treats them as an owner or recipient again.
