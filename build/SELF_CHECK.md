# Self-check

Anyone can paste this into a new Claude chat to inspect their own setup and fix it with Claude. It reads everything and changes nothing until you say yes. Run it after setup, after the first week, and whenever something feels off.

---

Check my setup for {COMPANY_NAME}'s operating system. Read only until I approve a repair. Never send anything to anyone, never delete anything, never touch anyone else's files, tasks or settings.

Check each item, then show me one table: item, result (OK, FIX or ASK), what you found, the fix. Times from a clock tool.

1. Company rules. Search by exact title "{COMPANY_RULES_FILE}" (never "contains"). Exactly one copy whose parent is {RULES_FOLDER}? Its version line? Any copy outside that folder that I can read (an archive copy is FIX: tell me to ask {OWNER_NAME} to restrict it)?
1a. Open-loops procedure. Is "{LOOPS_FILE}" in {RULES_FOLDER} (exact title)? Does my open loops document end with an OPEN line from my last debrief, and do its count and IDs agree?
2. My project. Does my work project's instructions start with the company block (read the rules first, Claude drafts and I send, receipts, writing cleanup)? Are my personal rules under it, with my email as the only recipient of my runs?
3. Connectors. Is each of my core connectors connected and answering a simple read? Is any owner-zone connector connected on my account ({OWNER_ZONE_CONNECTORS})? If so, FIX: tell me to disconnect it.
4. Skills. Do I have receipts-gate, writing-cleanup and our brand skill?
5. My documents. Do my runs log, receipts log, open loops, working notes and outputs folder exist in my own storage, and can you read each as plain text?
6. Scheduled tasks. List mine: name, schedule, time zone, model, enabled, last run, approval mode if you can see it. Compare with the company clock in the rules: right slot, right time zone (my debrief in my own time zone), model as the rules say. Each prompt's first line carries a prompt version; tell me which ones are older than the current kit templates. Any task without a LIMITS block is FIX.
7. Runs log. For each scheduled task, the last three business days: is there a "started" line and a "finished" line? Which rules version did each read? A start with no finish, or a missing day, is FIX with the likely cause (approval prompt, missing connector, late scheduler).
8. Drafts. List my open drafts that carry a #MMDD-NN code. Does each have a CODE line in my runs log? Any draft with a HOLD line I haven't settled? Any draft older than five business days?
9. Receipts log. Does it exist? How many FIX and HOLD lines in the last 30 days, grouped by type?
10. Shared folder. If I attend meetings I don't organize: did my debrief write additions files in the last week? Is there any file of mine in Agendas/ or Additions/ for a two-person meeting? If so, FIX: tell me to move it to my own outputs folder.
11. Task board. Any tasks created by my Claude in the last two weeks with a due date nobody said, no "Done when" line, or no section? Any task my Claude created for someone else?

Then:
- Give me the FIX list in order of risk, privacy first.
- For each fix you can make yourself (a document to create, a prompt line to add), show me the change and wait for my yes.
- For each fix only I can make (a setting, a connector, a sharing change), give me the exact steps.
- For anything that needs {OWNER_NAME} (the rules file, the shared folder, organization settings), write me a short note I can send them myself.
- Finish with one line I can paste into my runs log: "Self-check {date}: {n} OK, {n} fixed, {n} open".
