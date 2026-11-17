# Make it look good

How the original build got every brief, agenda, report, page and PDF to come out polished and on-brand, every time, from every person's Claude. And a paste that does the setup for your company.

## The short version

Claude makes good-looking pages when it's told exactly what your brand is, in one place, every time. Left alone, each chat invents its own look, and two people's briefs come out looking like they're from two companies. The fix is boring and it works:

1. **One brand file** that every Claude reads.
2. **A copy of it as a skill** the whole organization gets, for when the file can't be read.
3. **One line in the organization instructions** that says anything visual uses it.
4. **Roles,** so a shared agenda, private notes and a brief each look different on purpose.
5. **Task prompts that ask for the good stuff:** charts, a plain-language summary, a linked page, not just an email.

## What was in the original brand file

These are the pieces that made the biggest difference. `configure/BRAND.template.md` has a slot for each.

- **Tokens, not adjectives.** Eleven to fifteen named colors with hex values and a use for each ("primary-deep: header bands, buttons, links, any small colored text"). "Make it on-brand" gets you a guess; a token table gets you the brand.
- **Contrast rules on the tokens themselves.** Which colors may be text on white and which may not. A bright brand color often fails as small text; the file says so, so Claude uses the deeper shade for links and small labels.
- **One signature element.** Something that makes every page recognizable at a glance: a thin colored rule across the top, a distinct header band, a particular card style. Pick one or two and use them everywhere.
- **The logo as inline markup.** The logo drawn as inline SVG plus typed text, copied exactly from the brand file. Never an image file. A scheduled run that reads an image file from disk can stop at an approval prompt with nobody there to click it, and the brief never arrives.
- **Type.** One web font with a fallback stack, sizes and line height, and what to use where the font can't load (email and some document editors: Arial or similar).
- **Roles.** Each kind of output gets its own treatment:
  - shared agenda: a colored header band, decision boxes in a soft accent
  - private notes: a visibly different, darker header and a label like "PRIVATE NOTES", so they can't be confused with an agenda on a shared screen
  - briefs and debriefs: a light header with the logo, a rule above any private section
  - reports and dashboards: the title band and the chart rules
  - decks: the logo on the cover and the closing slide
  - email drafts: no logo, plain font, the person's signature typed into the body
- **Chart rules.** Which color is the current series, which is the comparison, which is the third; baselines muted and dashed; the source and the data-through date under every chart.
- **A copy-paste starter.** A few lines of CSS with every token, so a page starts right instead of being fixed afterwards.

## What the task prompts asked for

The brand file makes things look consistent. The prompts make them useful:

- **A linked page, not just an email.** Briefs, debriefs and the midday refresh go out as a short email plus a link to a private page with charts. Email is for the headline; the page is for the detail.
- **Charts where a number moves.** Yesterday against the same day last week, with the source under it.
- **An "explain it like I'm five" block** on anything with a number or a decision in it. People read it first, and it catches muddled thinking.
- **A PDF copy** of briefs and agendas saved to the person's own storage, for the record.
- **The brand checklist at the end of every build step:** signature element at the top, logo in the header, colors only from the tokens, the right role.

## Built-in help worth turning on

Claude may offer skills or artifact types for design, charts, documents, decks and spreadsheets, depending on your plan and settings. Where your Claude lists them, they raise the floor a lot: charts come out cleaner, decks and documents export to the usual file formats, and pages work on a phone. Check what your organization has under its skills and artifact settings, and point your brand file at them ("decks use the {COMPANY_NAME} design system when one is listed").

## Keep it working in scheduled runs

- Build pages with Claude's file tools (write and edit), never with a script that reads files from disk.
- Keep the logo inline in the brand file and the skill; never in an assets folder a run has to read.
- Email drafts keep their own plain rules. A heavily styled email breaks in half the mail apps your recipients use.

---

## The paste: set up your brand

Paste everything below the line into a new Claude chat in your project. Attach your brand guide if you have one, or give your website's address.

---

Set up our house style for everything our Claudes make for internal use. I am {OWNER_NAME} at {COMPANY_NAME}. Our website is {WEBSITE_URL}. {"Our brand guide is attached." or "We don't have a brand guide."}

GROUND RULES
- Never send or post anything. Show me each piece and wait for my yes.
- Customer-facing material (our store, ads, packaging) keeps our customer brand guide, never this file.

STEP 1: READ OUR LOOK
From the brand guide, or by reading our website, list: our colors (with hex values), our fonts, our logo, and anything distinctive about the layout. Tell me where each one came from. If you can't read the site, say so and ask me for screenshots or the brand guide.

STEP 2: THE TOKENS
Fill the token table in `configure/BRAND.template.md` from what you found. For every color, check its contrast as text on white and on our page background (4.5:1 for body text, 3:1 for large text). Where our brand color fails as small text, propose a deeper shade for links, buttons and small labels, and show both. Propose soft tints for tinted sections and callouts.

STEP 3: THE SIGNATURE AND THE LOGO
Propose one or two signature elements that make our pages recognizable at a glance, based on our real look. Then draw our logo as inline SVG plus typed text, so pages never load an image file. Show it to me at 40px tall on a white background and on our darkest band. If our logo is too detailed to draw well, propose a simpler mark plus the company name in our font, and say so.

STEP 4: ROLES
Propose a treatment for each role: shared agenda, private notes (visibly different), briefs and debriefs, reports and dashboards, decks, charts. Build one small sample page for each role with made-up content, and show me all of them side by side.

STEP 5: THE FILES (after my yes)
Give me:
1. Our filled brand file, "{BRAND_FILE}", ready to save in {RULES_FOLDER}.
2. The kit's `skills/brand-template/` filled in and renamed `{company-slug}-brand`, as a zip I can upload under organization settings.
3. One line for our organization instructions: "Anything visual (pages, artifacts, agendas, briefs, reports, dashboards, decks, docs, PDFs, charts) uses the {COMPANY_NAME} house style: the {company-slug}-brand skill, or {BRAND_FILE} in {RULES_FOLDER}, unless the person asks for another."
4. The lines to add to our task prompts so briefs, debriefs and agendas come with a linked page, charts with sources, and an "explain it like I'm five" block.

STEP 6: TEST
Have me run one morning brief by hand after the files are in place. Then look at the page it made and list anything that doesn't match the brand file.
