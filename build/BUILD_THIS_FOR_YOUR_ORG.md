# Build this for your org

The owner's one-paste setup. It takes two to four hours in one sitting (estimate).

## Before you paste

1. You are an owner of a Claude Team or Enterprise organization, or you can ask one to do the admin steps.
2. Your mail, calendar, file storage and documents (Google Workspace or Microsoft 365) and your task board are connected to your own Claude account.
3. Create a Claude project called "Build" and add this kit's files to it (or attach the kit's zip to the first message).
4. Open a new chat in that project and paste everything below the line.

You stay in the chat for the whole build. Claude asks before it creates anything and never sends anything to anyone.

---

You are helping me build an operating system for my company on Claude, using the kit attached to this project (or this message). Read these kit files first, in full: `learn/00-start-here.md` to `learn/10-what-broke.md`, every file in `configure/`, `tasks/` and `skills/`, and `build/PER_PERSON_SETUP.md` and `build/SELF_CHECK.md`. If you can't find them, stop and tell me.

GROUND RULES FOR THIS CHAT
- Never send an email or post a message to anyone, including me. Everything for another person is a file or a draft I send myself.
- Ask before you create, change or move anything in my mail, files, task board, calendar or scheduled tasks. Show me what you'll create, then wait for my yes. Batch related items into one approval.
- Never delete anything. If something should go, tell me and I'll do it.
- Read only on every data source (store, accounting, payroll, marketing tools). You may read to learn their shape; you never write to them.
- When you don't know something about my company, ask. Never invent a name, number, date or tool.
- Keep a build log as you go: a document called "Build log" in my own storage, one dated line per step, so I can stop and resume.
- Plain, short sentences. Ask at most five questions at a time, with choices where you can.

PHASE 1: WHAT'S HERE
Check and report, one line each, then wait:
- Which plan and role I'm on, if you can tell; if not, ask me.
- Which connectors I have connected: mail, calendar, file storage, documents, task board, team chat, meeting transcripts, web search, and any data sources.
- Whether you can create scheduled tasks from this chat, and whether you have an Agent tool for blind checks.
- What's missing, and what each gap means for the build (for example, no scheduling tool means I'll paste task prompts into the Scheduled page myself).

PHASE 2: THE INTERVIEW
Ask in five rounds. After each round, play back what you heard in a short table and let me correct it before moving on.
A. The company: name, email domain, home time zone, what we do in one line, the owner (me) and who will be the one editor of the company rules, mission and values if we have them written down (quoted exactly; optional).
B. The people: everyone who will use the system (first name, role, work email, time zone, manager), who organizes which recurring meetings, anyone who prefers one ask per message, anyone who has left and might still show up on invites, outside partners people mention often (role and first name only).
C. The tools: mail, file storage, documents, task board (and its projects and sections, which you may read), team chat, meeting transcript sources in order of trust, and for each number we repeat (sales, orders, subscribers, cash, stock, whatever applies) which tool owns it and which tools only cross-check it. Which tools are owner-zone (payroll, HR, accounting) and which of their read tools a run truly needs.
D. The rhythm: our workday days and hours, the weekly team meeting (day, time, who runs it), and which runs each person gets. Default: everyone gets morning brief, evening debrief and midday refresh; meeting organizers also get agendas; I get numbers and send check. Propose a company clock from `learn/07-company-clock.md` with each person in their own minute, and let me change it.
E. The limits: what must never be automated (for example anything that commits money, messages to certain partners, anything legal or HR), topics that never go in a shared document, who owns each outside relationship, our email signature format, and any words we use for our meetings, targets or reports.

PHASE 3: FILL THE TEMPLATES
From my answers, fill:
1. The company rules from `configure/COMPANY_RULES.template.md`, with the data source map from `configure/DATA_SOURCE_MAP.template.md` as section 1. Delete any section or line that doesn't fit us, and say which you deleted and why. Every rule keeps a one-line "Why". Leave nothing in curly braces.
2. The brand file from `configure/BRAND.template.md`. If I have no brand guide, ask for two colors and a font, and keep it minimal.
3. The organization instructions from `configure/ORG_INSTRUCTIONS.template.md`. Count the characters with code and keep it under 3,000, with room to spare.
4. My project instructions and personal rules from `configure/PROJECT_INSTRUCTIONS.template.md` and `configure/PERSONAL_RULES.template.md`.
5. My task prompts from `tasks/`, one per run I get, with my slots and names filled in. Keep every LIMITS block exactly.
6. The brand skill from `skills/brand-template/`, renamed for us.
Ask me whether my Claude can publish private pages; if not, set agendas, notes and brief pages to documents instead, using the fallback lines in the templates. Show me each file in full (as files I can open, not pasted into the chat) and wait for my approval or edits. Then run the writing-cleanup skill over the company rules and the brand file without changing any fact.

PHASE 4: THE SHARED FOLDER AND MY DOCUMENTS
With my approval, in my file storage:
- Create the shared folder with Rules/, Rules/archive/, Agendas/ and Additions/ (and Numbers/ if I want shared numbers).
- Save the company rules and the brand file into Rules/ under their exact titles.
- Create my own documents: runs log, receipts log, open loops, working notes, and an outputs folder.
- Then test the lookup: search for the company rules by exact title, confirm the parent folder, read the version line back to me.
If your connector can't create folders or files (some file connectors need an admin to turn on write tools first), give me each file to upload and the folders to make by hand, and wait. Then give me the sharing steps you can't do yourself, as a short checklist: who gets edit access to the shared folder, that Rules/archive/ is mine only, and that the folder is not shared outside the company.

PHASE 5: THE ADMIN STEPS (I DO THESE)
Give me a checklist with the exact text to paste and what to click, and wait while I do them:
- Paste the organization instructions.
- Upload the three skills (give me each as a zip file: receipts-gate, writing-cleanup, and our brand skill).
- Check that skills, code execution and scheduled tasks are on for the organization.
- For owner-zone connectors: block every tool except the read tools we named in round C.
- Set tool permissions so scheduled runs can email their owner and save files, and leave send-to-others and delete at "ask". On Microsoft 365, write tools (drafts, files) may need an administrator's consent before Claude can use them; tell me if that applies to us.
Tell me to check the help center if a menu doesn't match, since menus move.

PHASE 6: MY PROJECT
Give me my project instructions as one block to paste into my work project's instructions, and wait until I say it's done.

PHASE 7: MY SCHEDULED TASKS
For each of my runs, show me the name, schedule, time zone, model and prompt in one table, and wait for my yes. Then create them with your scheduling tool, one at a time. After each, tell me to set its approval mode to approve automatically (if our organization allows it) and to check its model and connectors. If you can't create scheduled tasks here, give me each prompt as a file with the settings to enter by hand.
Then have me run the evening debrief once by hand ("Run now"). When it finishes, read my runs log and tell me whether it logged a start and a finish, which rules version it read, and whether its email reached me.

PHASE 8: TEAMMATE PASTES
For each teammate from round B, add them to the "On the system" line in the company rules on the day their first debrief runs (remind me), and fill `build/PER_PERSON_SETUP.md` with their name, email, role, time zone, slots, runs and anything from round E that applies to them. Give me each as a separate file. Do not send them. Recommend I run the system alone for at least a week before handing out the first one, then a pilot teammate, then small groups.

PHASE 9: CHECK AND HAND OVER
Run `build/SELF_CHECK.md` on my setup and fix what you can with my approval. Then give me a one-page build report as a file: what's done, what I still need to click, my first-week checklist (read every brief, fix rules through the one editor, watch the runs log), and the dates for the pilot teammate and the first wave. Append the last line to the build log.
