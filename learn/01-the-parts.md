# The parts

The system has four parts and a shared shelf. The names are short on purpose so people use them out loud.

## Sources

The systems that own the facts: your store or billing system, your accounting tool, your calendar, your mail, your meeting transcripts. A source is where a run goes to find out what is true right now. A message about a system ("I pushed it live") is not the source; the system is.

The data source map (`configure/DATA_SOURCE_MAP.template.md`) says which source answers which question. A run that is asked for a number goes to the map first.

## Rules

Plain-text files every Claude reads before it works:

- the company rules, one file for everyone, in a shared folder
- each person's own rules, in their own project instructions
- the task prompt, for a scheduled run

Rules hold facts about how the company works: who is on the team, which source owns which number, how drafts are marked, what never goes in a shared document. They are not a style guide and not a wish list. If a rule can't be checked, it isn't a rule yet.

## Runs

Scheduled tasks on a fixed clock. Each run reads the rules, reads its sources, does one job (a brief, an agenda, a debrief, a send check), writes a start line and a finish line to its owner's runs log, and emails only its owner. Runs never send to anyone else.

## You

The person who reads, decides and presses Send. Claude drafts; people send. A run can make a recommendation and show its reasoning, but a decision about people, money or relationships stays with a human.

## The shared shelf: the Board and the Files

- The Board is your task board (Asana or similar). It holds real work and real decisions, one task per piece of work, with an owner.
- The Files are one shared folder with four parts: the rules, each day's agendas, each person's additions for tomorrow's meetings, and optionally the shared daily numbers. Everything else a person's Claude makes stays in that person's own storage.

## How the parts map to layers

If you think in systems, the same thing has four layers:

| Layer | What it holds |
|---|---|
| Interaction | Chats, scheduled runs, the person who sends |
| Rule | Company rules, personal rules, task prompts, org instructions, skills |
| State | Runs logs, open-loops docs, receipts logs, working notes, the task board, the shared folder |
| Data | Connectors to your sources |

Each layer can sit in one of three zones: shared (everyone), private (one person) or owner (the few people who see pay, payroll and the books). See `08-privacy-zones.md`.
