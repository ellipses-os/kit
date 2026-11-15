---
name: {company-slug}-brand
description: The {COMPANY_NAME} house style for internal work. Use it whenever you make something people will look at, including pages, artifacts, agendas, private notes, briefs, debriefs, reports, dashboards, one-pagers, docs, decks, PDFs and charts, unless the person asks for a different style. Not for customer-facing material or email drafts.
---

# {COMPANY_NAME} house style

This skill is a copy of {BRAND_FILE} for when the file can't be read. The file in {RULES_FOLDER} wins when they differ; read it by exact title when you can.

## How to use it

1. Read {BRAND_FILE} from {RULES_FOLDER} (exact title, parent folder confirmed). If you can't, use the tokens below.
2. Pick the role: shared agenda, private notes, brief, report, deck or chart. Each has its own header treatment.
3. Start from the starter CSS below. Write pages with your file tools; don't use a script that reads image files from disk.
4. Check contrast on every text color you use.
5. Put the source and data-through date under every chart.

## Tokens

| Token | Hex | Use |
|---|---|---|
| primary | {#RRGGBB} | {USE} |
| primary-deep | {#RRGGBB} | {USE} |
| accent-1 | {#RRGGBB} | {USE} |
| accent-2 | {#RRGGBB} | {USE} |
| ink | {#RRGGBB} | Body text |
| muted | {#RRGGBB} | Secondary text |
| bg | {#RRGGBB} | Page background |
| surface | {#RRGGBB} | Cards |
| line | {#RRGGBB} | Borders |
| ok | {#RRGGBB} | Done states |
| alert | {#RRGGBB} | Alerts only |

Font: {FONT}, falling back to system-ui and Arial.

## Logo

```html
{PASTE THE LOGO MARKUP FROM {BRAND_FILE}}
```

Never an image file, a data URI, or a logo read from disk inside a page a run builds. No logo in email drafts.

## Roles

- Shared agenda: {TREATMENT}
- Private notes: {TREATMENT, visibly different from an agenda}
- Briefs: {TREATMENT}
- Reports and dashboards: {TREATMENT}
- Decks: {TREATMENT}
- Charts: primary for the current series, accent-1 for comparison, accent-2 for a third; baselines muted and dashed.

## Starter

```css
:root{--primary:{#};--primary-deep:{#};--accent-1:{#};--accent-2:{#};--ink:{#};--muted:{#};--bg:{#};--surface:{#};--line:{#};--ok:{#};--alert:{#};--font:"{FONT}",system-ui,Arial,sans-serif}
body{background:var(--bg);color:var(--ink);font-family:var(--font);font-size:17px;line-height:1.55}
a{color:var(--primary-deep)}
```

## Packaging

Rename the folder to `{company-slug}-brand`, fill every placeholder, zip the folder (the zip must contain SKILL.md), and have an owner add it under organization settings so everyone gets it.
