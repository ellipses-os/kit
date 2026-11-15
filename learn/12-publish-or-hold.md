# Publish what's proven, hold the rest

Some pages the team reads every day (a service catalog, a policy summary, a how-we-work guide) go stale the week after someone writes them. A scheduled run can keep them current without anyone remembering to ask, as long as it knows what it may change on its own and what must wait for a person.

## The pattern

1. Keep the page's source in a private repository (or any store with versions and branches), not only in a hosting tool. Every change is then a commit someone can read and undo.
2. A weekday run reads the window since its last finished run: the systems that own each fact on the page, plus mail, chat, transcripts and task-board changes on the page's topics.
3. For each fact on the page, it checks the owning system (the data source map decides which).
4. It sorts every change into a tier:

| Tier | What | Where it goes |
|---|---|---|
| Auto | A fact swap (a price, a date, a status, a count) where the new value is P or T from this run, no sources disagree, and the blind gate passes | Straight to the live page, with a cap per run |
| Rewrite | A section rewritten or rebuilt from a meeting or a thread, under the same conditions, outside the held zones | Straight to the live page, with a smaller cap |
| Held | Anything in a held zone; anything where sources disagree; anything the gate returned FIX twice or HOLD on; anything over the caps | A branch, for the page's owner to read and merge |

5. Held zones are written down in advance and never published by a run: regulated claims (legal, compliance, safety, medical or financial), pricing policy, anything customer-facing, and anything still being decided.
6. One email to the page's owner: PUBLISHED (what changed, with sources), NEEDS YOU (held changes with a recommended call each), and anything broken in a live system the run noticed but didn't touch.
7. If the run can't reach the repository, it changes nothing anywhere, emails the owner what failed, and stops.

No repository? The same pattern works with a document that keeps version history: the run edits AUTO and REWRITE changes in place and puts every held change in a "Proposed changes" section at the top, with its source and a recommended call, for the owner to accept or delete. Keep the page's published copy separate from the document the run edits.

## Live figure cards (optional)

A small card at the top of a section can show a few live figures, each with its source and data-through date. A card that fails its checks keeps its previous figures and says when they're from. Never put owner-zone figures on a team page.

## Why it works

The run never decides anything that needs judgment. It publishes only what it can prove at the source, and the proof (the receipt) is in the commit. Everything else becomes a short list of decisions for one person, with a recommendation. The page stays current, and the owner spends a few minutes a day instead of an afternoon a month.

## Things to plan for

- A chat may not be able to start or pause a scheduled task; a person presses Run now or pauses it in the scheduler.
- Large sites (videos, big images) may be too large to upload from a chat. Deploy from the repository instead.
- Turn off preview deploys that would publish branches to public addresses, or keep them behind a sign-in.

Template: `tasks/reference-refresh.md`.
