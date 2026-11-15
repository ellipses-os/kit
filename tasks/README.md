# Task prompt templates

One template per recurring run. Each is a complete, standalone prompt: a scheduled task starts fresh every time and remembers nothing, so every prompt carries its own rules-first step, its own limits and its own finish line.

| Template | Who runs it | Example slot |
|---|---|---|
| `numbers.md` | Organizers and owners | Weekdays early morning |
| `agendas.md` | Meeting organizers | Weekdays before the first meeting |
| `morning-brief.md` | Everyone | Weekdays at the start of the day |
| `midday-refresh.md` | Everyone, by hand | Anytime |
| `evening-debrief.md` | Everyone | Weekdays at the end of the day |
| `send-check.md` | Anyone who drafts a lot | Twice a day |
| `weekly-update.md` | The owner of the weekly team meeting | Once a week |

## Filling them in

Replace every `{PLACEHOLDER}`. The build (`build/BUILD_THIS_FOR_YOUR_ORG.md`) does this for you. Placeholders used in every template:

- `{PERSON_NAME}`, `{PERSON_EMAIL}`, `{PERSON_TIME_ZONE}`: whose run it is.
- `{COMPANY_RULES_FILE}`, `{RULES_FOLDER}`: the company rules and where they live.
- `{RUNS_LOG}`, `{RECEIPTS_LOG}`, `{OPEN_LOOPS_DOC}`, `{WORKING_NOTES}`, `{OUTPUTS_FOLDER}`: the person's own documents and folder.
- `{SHARED_FOLDER}`: the shared folder.
- `{PROMPT_VERSION}`: today's date plus a letter, for example `2026-03-04a`. Bump it on every change and keep the old version.

## The safety limits every template carries

Do not remove these. They are what makes it safe to let a run work unattended.

1. **Email the owner only.** The only recipient of anything a run sends is `{PERSON_EMAIL}`. No To, Cc or Bcc to anyone else.
2. **Draft for everyone else.** Anything meant for another person is a draft in the owner's mail. Never sent, never posted.
3. **Read only on data sources.** Never call a write tool on a store, marketplace, ad account, email platform, accounting or payroll system.
4. **Never post to team chat.** Read it; give paste-ready text in the brief instead.
5. **Never touch someone else's task.** No completing, re-dating, reassigning or editing it.
6. **Never change scheduled tasks.** No creating, editing, pausing, firing or deleting any scheduled task from inside a run.
7. **Never delete.** No deleting files, drafts or tasks.
8. **Nothing private in shared places.** Leave out anyone's leave type or reason, pay, performance, HR and one-to-one content from anything shared.

If a step can't be done inside these limits, the run says so in its coverage line and stops that step.

## After creating each task

- Set its approval mode to approve automatically, if your organization allows it.
- Check its model and connectors.
- Run it once by hand, read the runs log, and only then trust the schedule.
