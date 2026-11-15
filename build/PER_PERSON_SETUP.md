# Per-person setup

The owner's build fills this in for each teammate and hands them the file. The teammate opens a new Claude chat, pastes everything below the line, and follows along. About 30 to 45 minutes (estimate).

Before pasting, the teammate should be signed in to Claude with their work account and have their mail, calendar and file storage connected. If they aren't sure, the paste checks.

---

You are setting up my Claude for {COMPANY_NAME}'s operating system. I am {PERSON_NAME}, {ROLE}, {PERSON_EMAIL}, time zone {PERSON_TIME_ZONE}. My manager is {MANAGER_NAME}.

GROUND RULES FOR THIS CHAT
- Never send an email or post a message to anyone, including me.
- Ask before you create or change anything in my mail, files, task board or scheduled tasks. Show me what you'll create, then wait for my yes.
- Never delete anything.
- Never touch anyone else's files, tasks or settings.
- Plain, short sentences. One step at a time.

STEP 1: CHECK MY CONNECTORS
I need: {CORE_CONNECTORS, e.g. mail, calendar, file storage, documents, {TASK_BOARD}, {CHAT_TOOL}, {TRANSCRIPT_SOURCE}, web search}. For my work I also use: {DATA_CONNECTORS or "none"}. I must not have: {OWNER_ZONE_CONNECTORS or "none"}; if any of those are connected on my account, tell me and don't use them. List what's connected and what's missing. For each missing one, tell me where to connect it and wait.

STEP 2: READ THE COMPANY RULES
Search my file storage for a file titled exactly "{COMPANY_RULES_FILE}" (exact title, not "contains"). Confirm its parent folder is {RULES_FOLDER}. Read it and tell me its version line. If you find more than one, or one in an archive folder, tell me and use only the one in {RULES_FOLDER}. If you can't find it, stop and tell me to ask {OWNER_NAME} for access to {SHARED_FOLDER}.

STEP 3: MY PROJECT
Tell me how to create a Claude project called "{PERSON_NAME} · Work" if I don't have one. Then give me this text to paste into its instructions, exactly, and wait until I say it's done:

```
{FILLED PROJECT INSTRUCTIONS AND PERSONAL RULES FOR THIS PERSON}
```

STEP 4: MY DOCUMENTS
With my approval, create in my own file storage (not the shared folder):
- a document "{RUNS_LOG}"
- a document "{RECEIPTS_LOG}"
- a document "{OPEN_LOOPS_DOC}"
- a document "{WORKING_NOTES}"
- a folder "{OUTPUTS_FOLDER}"
Write a first line in the runs log: "Setup {date}; rules {version from step 2}".

STEP 5: MY SCHEDULED TASKS
Create these with your scheduling tool, one at a time, after showing me each one's name, schedule and time zone:
{TABLE OF THIS PERSON'S RUNS: name | schedule | time zone | template}
The prompts:

{FILLED TASK PROMPTS, ONE PER RUN}

After each one, tell me to open its settings and (1) set the approval mode to approve automatically, if our organization allows it, (2) check the model is {MODEL}, (3) check its connectors include what it needs. If you can't create scheduled tasks here, give me each prompt as a file and the settings to enter on the Scheduled page.

STEP 6: TEST
Have me run my evening debrief once by hand. When it's done, read my runs log and tell me: did it log a start and a finish, which rules version it read, and did an email reach me. If anything failed, help me fix it.

STEP 7: SELF-CHECK
Run the self-check below on my setup and show me the result.

{PASTE build/SELF_CHECK.md BELOW ITS LINE HERE}

STEP 8: DONE
Tell me, in three lines: when my first morning brief will arrive, how to fix a draft (say "Fix #code" in a chat), and who to ask if something looks wrong ({OWNER_NAME}).
