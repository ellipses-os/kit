# Configure

Templates for every file the system reads. The owner's build (`build/BUILD_THIS_FOR_YOUR_ORG.md`) fills them in with you; you can also fill them by hand.

| Template | Becomes | Lives in | Read by |
|---|---|---|---|
| `COMPANY_RULES.template.md` | `{COMPANY_RULES_FILE}` (for example `COMPANY-RULES.md`) | The shared Rules folder | Every run and every data pull, first |
| `PERSONAL_RULES.template.md` | Each person's own rules | Their project instructions (or a file in their own storage the instructions point to) | Their runs, second |
| `BRAND.template.md` | `{BRAND_FILE}` (for example `BRAND.md`) | The shared Rules folder | Anything that builds a page, deck or chart |
| `PROJECT_INSTRUCTIONS.template.md` | The instructions of each person's Claude project | Claude, in the project's settings | Every chat in that project |
| `ORG_INSTRUCTIONS.template.md` | Organization instructions (under 3,000 characters) | Claude admin settings | Every conversation in the organization |
| `DATA_SOURCE_MAP.template.md` | Section 1 of the company rules | Inside the company rules | Every run that writes a number |

## Placeholders

Every placeholder is in `{CURLY_CAPS}`. The ones used across files:

| Placeholder | Meaning | Example |
|---|---|---|
| `{COMPANY_NAME}` | Your company's name | Northwind Supply |
| `{COMPANY_DOMAIN}` | Your email domain | northwind.example |
| `{OWNER_NAME}` | The person who owns the rules | Dana |
| `{RULES_EDITOR}` | The one chat or person that edits the company rules | "the Rules chat in Dana's project" |
| `{HOME_TIME_ZONE}` | The company's time zone name | America/Denver |
| `{SHARED_FOLDER}` | The shared folder's name | Claude Shared |
| `{RULES_FOLDER}` | The Rules subfolder | Claude Shared/Rules |
| `{COMPANY_RULES_FILE}` | The company rules file's exact title | COMPANY-RULES.md |
| `{BRAND_FILE}` | The brand rules file's exact title | BRAND.md |
| `{TASK_BOARD}` | Your task board | Asana |
| `{MAIL}` | Your mail system | Gmail, Outlook |
| `{CHAT_TOOL}` | Your team chat | Google Chat, Slack, Teams |
| `{TRANSCRIPT_SOURCES}` | Transcript sources, in order | "the notetaker app, then the video platform's transcript" |
| `{RUNS_LOG}` | Each person's runs log document | Claude runs log |
| `{RECEIPTS_LOG}` | Each person's receipts log document | Receipts log |
| `{OPEN_LOOPS_DOC}` | Each person's open loops document | Open loops |
| `{WORKING_NOTES}` | Each person's working notes document | Working notes |
| `{OUTPUTS_FOLDER}` | Each person's own outputs folder | Claude Outputs |

## Before you publish your company rules

- Read every line. Delete what doesn't fit. A rule nobody follows weakens the ones they do.
- Every rule keeps its one-line "Why" with a date. Write your own when you add one.
- Check the file has a version line and the one-editor line at the top.
- Check nothing private is in it (see `learn/08-privacy-zones.md`). The whole team reads this file.
