# Ellipses OS kit

A free kit for running a small company on Claude, so that every open loop keeps moving and people still press Send themselves.

Version 0.5.

## What it is

Every person's Claude reads the same company rulebook before it does anything, then that person's own rules, then the task in front of it. Scheduled runs prepare each person's day: a morning brief, the agendas for today's meetings, an evening debrief, and drafts of the messages they owe. Nothing reaches another person until a human sends it. Every claim a draft makes carries a receipt (where it came from and when it was read), and a second Claude that has not seen the draft checks those receipts before anything is marked ready.

The kit has these parts:

| Folder | What's in it |
|---|---|
| `learn/` | Short chapters on how the system works and why each rule exists, plus optional team rituals (a weekly lane board, a monthly all-hands page, pilots), a self-refreshing reference page, and a starter question bank for a course |
| `configure/` | Templates with `{PLACEHOLDERS}` for your company rules, the open-loops procedure, personal rules, brand rules, project and org instructions, and a data source map |
| `build/` | The owner's one-paste setup (`BUILD_THIS_FOR_YOUR_ORG.md`), a per-person setup paste, a self-check paste, a first-week checklist, a paste that sets up your house style (`MAKE_IT_LOOK_GOOD.md`), and a paste that builds a short course for your team (`BUILD_YOUR_COURSE.md`) |
| `tasks/` and `skills/` | The prompt templates for each scheduled run, and the skills they lean on |
| `tools/` | A privacy scan to run on your filled-in files before you share them outside the company |

The `ellipses/` folder describes a live call co-pilot that pairs well with the kit.

## Who it's for

Owners and operators of teams of roughly 3 to 50 people who already use Claude and want the same habits across everyone's setup: one rulebook, one daily rhythm, one task board, and a human step before anything goes out. It assumes someone on the team is comfortable pasting long prompts and reading what Claude reports back. No coding is needed.

## What you need

- A Claude Team plan (Enterprise also works). The org-wide pieces (organization instructions and skills provisioned for everyone) are Team and Enterprise features. Scheduled tasks themselves run on any paid plan.
- Google Workspace or Microsoft 365, connected to Claude, for mail, calendar and files.
- A task board with a Claude connector, such as Asana.
- A meeting transcript source, if you want agendas and action items from meetings: your video platform's own transcript or a notetaker app.
- One owner who can spend an afternoon on the build and about a week watching the first runs.

## How long setup takes

These are estimates from one build, not promises.

| Step | Time |
|---|---|
| Owner build | Two to four hours in one sitting, mostly the interview and reading what Claude drafts |
| Each person | 30 to 45 minutes with the per-person paste |
| Settling in | One to two weeks of small rule changes before the runs feel routine |

## Where to start

1. Read `learn/00-start-here.md` (ten minutes).
2. Open a new Claude chat in a project, attach this kit, and paste `build/BUILD_THIS_FOR_YOUR_ORG.md`.
3. Set up your house style with `build/MAKE_IT_LOOK_GOOD.md`, so every brief and page looks like your company from the first run.
4. Give each teammate the setup paste the build produces for them.
5. Work through `build/FIRST_WEEK.md`. At the end of the week, have everyone run `build/SELF_CHECK.md`.
6. The week after, build a short course for your team with `build/BUILD_YOUR_COURSE.md`.

## Claude features used

Each line was checked against Anthropic's help center on Nov 15, 2026. Menus move; if a step doesn't match your screen, search the help center for the feature name.

| Feature | What the kit uses it for | Source |
|---|---|---|
| Scheduled tasks | Every run on the company clock. Available on paid plans including Team; each task has an approval mode and runs in the cloud | [Schedule recurring tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) |
| Organization instructions | A short pointer to your company rules, read in every conversation. Owners set it; maximum 3,000 characters | [Set organization instructions](https://support.claude.com/en/articles/14546867-set-organization-instructions) |
| Skills provisioned for the organization | The receipts gate, the writing cleanup and your brand skill, given to everyone at once | [Provision and manage skills](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization) |
| Team plan admin controls | Single sign-on, connector controls, org-wide skills, org instructions | [Plans and pricing](https://claude.com/pricing) |

## As is

This kit is provided as is, with no warranty of any kind and no promise of support. You build it in your own Claude account; nobody behind this kit ever sees your data, your keys or your runs. You are responsible for what your scheduled tasks do, including anything they send. Read every template before you use it, and change what doesn't fit your company.

## Not affiliated with Anthropic

This kit is an independent project. It is not made, endorsed or supported by Anthropic. "Claude" is Anthropic's product; questions about Claude itself go to Anthropic's help center.

## License

The kit is free to read, learn from, use and adapt. Selling it, or making money from it for other people, needs a commercial license.

- Everything except the scripts and the writing-cleanup skill (the learning chapters, templates, prompts and this README) is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). The full text is in `LICENSE`.
- One added permission from the author: you may use the kit to run your own organization's internal work, including at a for-profit company. Setting it up for your own team is not "commercial" in this sense.
- What needs a commercial license: selling the kit or anything built from it, bundling it into a paid product, or charging other people or companies to set it up or run it for them. For a commercial license, email info@ellipsesapp.ai .
- The scripts in `tools/` are licensed under the [MIT License](https://opensource.org/license/mit) (full text in `tools/LICENSE`).
- `skills/writing-cleanup/SKILL.md` adapts Wikipedia text and stays under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), as its header says.

If you share a changed version, keep the credit and share it under the same license. A credit line like this is enough:

> Based on the Ellipses OS kit by Lawrence Johnson (https://github.com/ellipses-os/kit), CC BY-NC-SA 4.0.

Details are in `NOTICE`.
