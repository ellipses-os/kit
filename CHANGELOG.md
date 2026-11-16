# Changelog

## 0.4.1 (2026-11-16)

- Commercial license requests now go to info@ellipsesapp.ai.

## 0.4 (2026-11-15)

- License: the kit is now CC BY-NC-SA 4.0, with an added permission to use it for your own organization's internal work, including at a for-profit company. Selling it, bundling it into a paid product, or charging others to set it up needs a commercial license. The scripts stay MIT, and the writing-cleanup skill stays CC BY-SA 4.0. See `README.md` and `NOTICE`.

## 0.3 (2026-11-15)

- License chosen: CC BY-SA 4.0 for everything except the scripts, MIT for `tools/`. `LICENSE` now holds the full CC BY-SA 4.0 text, `tools/LICENSE` the MIT text, and `README.md` and `NOTICE` say how to credit the kit.
- Name: the kit is now the Ellipses OS kit.

## 0.2 (2026-11-15)

- One loop, one tracker, in full: a new procedure file, `configure/LOOPS.template.md` (append-only open-loops document, line formats, what closes a loop, what a person can say, a one-time backlog cleanup and an end-of-week audit). The company rules, the brief, debrief, agendas and refresh templates and the self-check now read it.
- Old setup text: the company rules can quote and override outdated lines in people's pasted setup, so nobody has to re-paste.
- Team rituals (optional): `learn/11-team-rituals.md`, with `tasks/lane-board.md` (a weekly board of project lanes, blocked first, built from lane status comments), `tasks/monthly-all-hands.md` (a monthly page from live data, numbers only as exceptions, managers write their own sections) and `tasks/pilot-review.md` (measures after each pilot meeting and a final run that applies a decision rule written in advance).
- Publish or hold: `learn/12-publish-or-hold.md` and `tasks/reference-refresh.md`, a weekday run that publishes facts it can prove at the source and holds everything else on a branch for the page's owner.
- Meetings: an approved-notetakers line, and a reminder that platform transcript defaults may not reach older recurring meetings.
- Clock: runs check that the previous run finished, since an outage can end a run with nothing produced while the scheduler shows success; people, not chats, start and pause scheduled tasks.
- `learn/10-what-broke.md`: new rows for the failures above and a "Sites and pages" table.
- `ellipses/`: checked against ellipsesapp.ai again.

## 0.1 (2026-11-15)

First version, for early readers before public release.

- `README.md`: what the kit is, who it's for, what you need, setup time, the Claude features it relies on with links checked Nov 15, 2026, and the "as is" and "not affiliated" lines.
- `learn/`: eleven short chapters, from the parts of the system to the failures behind each rule.
- `configure/`: templates for company rules, personal rules, brand rules, project instructions, organization instructions and the data source map.
- `build/`: the owner's one-paste build, a per-person setup paste, and a self-check paste.
- `tasks/`: prompt templates for numbers, agendas, morning brief, midday refresh, evening debrief, send check and weekly update, each with the same safety limits.
- `skills/`: receipts-gate, a brand skill template, and writing-cleanup (CC BY-SA 4.0, adapted from Wikipedia's "Signs of AI writing").
- `ellipses/`: a short description of the live meeting co-pilot, checked against its public site on Nov 15, 2026, and a link to it.
- `tools/privacy_scan.py`: a scan for emails, phone numbers, long IDs, money amounts and your own list of names, to run before you share your filled-in files.
- `LICENSE`: placeholder until a license is chosen.
