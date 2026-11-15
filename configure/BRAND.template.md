# {BRAND_FILE}: the {COMPANY_NAME} house style

Version {YYYY-MM-DD}a. Owner: {OWNER_NAME}. Lives in {RULES_FOLDER}; read it by exact title.

## When it applies

Everything Claude builds for internal use: pages, agendas and private notes, briefs and debriefs, reports, dashboards, docs, decks, PDFs and charts. It applies unless the person asks for a different style in that request.

Customer-facing material follows {CUSTOMER_BRAND_GUIDE} instead, never this file. Email drafts keep the drafts rules in {COMPANY_RULES_FILE} section 7.

## Colors

Check every text color against its background for contrast (4.5:1 for body text, 3:1 for large text and focus rings).

| Token | Hex | Use |
|---|---|---|
| primary | {#RRGGBB} | Large headings, icons, the main chart series. Small text only if contrast passes |
| primary-deep | {#RRGGBB} | Header bands, buttons, links, any small colored text |
| accent-1 | {#RRGGBB} | Callout borders, focus rings, the second chart series |
| accent-2 | {#RRGGBB} | Sparing highlights, the third chart series |
| ink | {#RRGGBB} | Body text and headings |
| muted | {#RRGGBB} | Secondary text, labels, axis text |
| bg | {#RRGGBB} | Page background |
| surface | {#RRGGBB} | Cards, panels, form fields |
| line | {#RRGGBB} | Borders and rules |
| ok | {#RRGGBB} | Done and success states |
| alert | {#RRGGBB} | Alerts and the red send-time block only |

## Type

- Headings and body: {FONT}, with a fallback stack ending in system-ui and Arial.
- Numbers in tables: a monospace font.
- Where the font can't load (email, some document editors): Arial.
- Body 16 to 17px, line-height about 1.5.

## The logo

{HOW THE LOGO APPEARS IN A PAGE.} Recommended: draw it as inline SVG plus text, copied exactly from this file, so no page ever reads an image file from disk. Reading image files inside a scheduled run can stop the run at an approval prompt. No logo in email drafts.

```html
{PASTE THE LOGO MARKUP HERE}
```

## Roles

- Shared agenda: {HEADER TREATMENT}. Decision boxes in {COLOR}.
- Private notes: a visibly different header (for example a dark band and the label "PRIVATE NOTES"), so they can't be confused with an agenda on a shared screen.
- Briefs and debriefs: white header, the logo, a rule above any private section.
- Reports and dashboards: {TREATMENT}.
- Charts: current series in primary, comparison in accent-1, third in accent-2; baselines muted and dashed; source and data-through date under every chart.

## Copy-paste starter

```css
:root{--primary:{#};--primary-deep:{#};--accent-1:{#};--accent-2:{#};--ink:{#};--muted:{#};--bg:{#};--surface:{#};--line:{#};--ok:{#};--alert:{#};--font:"{FONT}",system-ui,Arial,sans-serif}
body{background:var(--bg);color:var(--ink);font-family:var(--font);font-size:17px;line-height:1.55}
a{color:var(--primary-deep)}
```
