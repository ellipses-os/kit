# Build your course

A paste that turns this kit's chapters and your own company rules into a short course for your team: lessons people can finish in ten to fifteen minutes each, a quiz at the end of every lesson, and a final check. Run it after your team is set up and their runs are working, not during setup.

## Why a course, and why after setup

In the original build, people learned the system in two very different modes:

- **Setup** is do-this-now: paste, connect, test, done. People are busy and anxious to see their first brief arrive. They don't retain much.
- **Understanding** comes over the following weeks: why a draft has a red block, what a HOLD means, why their Claude closed a task without asking. That's what a course is for.

Mixing the two made both worse. A long test at the start of setup felt like a gate and taught little. A course that starts after the first week, in small pieces, stuck.

What worked in the course itself:

- **Start at lesson one.** No placement test up front. The same questions work better as the final check, once people have done the lessons.
- **Open each lesson with a short invented scenario.** A made-up teammate, a made-up vendor, one thing that goes wrong. Never a real person or a real customer.
- **One "explain it like I'm five" fold per lesson,** for the people who want the plain version first.
- **A "one thing to remember" card** before each quiz.
- **Scenario questions, not definitions.** "Sam's draft says the promo is live but the store shows it paused. What happens at the gate?" beats "What does HOLD mean?"
- **A reason for every wrong answer,** shown after the person picks it, plus the source chapter or rule.
- **At least one question per lesson that calls back to an earlier lesson,** so the ideas connect.
- **70% to pass a lesson, 80% for the final check,** unlimited retakes, best score counts.
- **Recognition, not permission.** Everyone gets the full system on day one. Finishing the course earns a badge or a shout-out, not access.
- **One supervised run for the people who'll write rules or tasks others depend on:** take one real draft through a fix, a gate and a send, with a manager reading the receipts before Send.

## What you need first

- Your filled company rules file (from `configure/COMPANY_RULES.template.md`), so lessons can use your real vocabulary, clock and rules.
- Your filled brand file (from `configure/BRAND.template.md`; see `build/MAKE_IT_LOOK_GOOD.md`), so the course looks like your company.
- `learn/questions.md` from this kit, the starter question bank.
- About an hour of the owner's time for the review pass, then a few minutes per lesson.

---

Paste everything below the line into a new Claude chat in a project that has this kit attached and can read your company rules and brand file.

---

You are building a short internal course that teaches my team how our Claude operating system works. I am {OWNER_NAME}, {ROLE} at {COMPANY_NAME}.

READ FIRST
1. The kit's `learn/` chapters, in the order `learn/00-start-here.md` gives.
2. Our company rules file, "{COMPANY_RULES_FILE}", by exact title in {RULES_FOLDER}. Where it differs from the kit, our file wins.
3. Our brand file, "{BRAND_FILE}", by exact title in {RULES_FOLDER}. Every page you build follows it.
4. The kit's `learn/questions.md`, the starter question bank.

GROUND RULES
- Never send or post anything to anyone. You build pages; I share them.
- No real customers, vendors, prices or numbers anywhere in the course. Scenarios use invented names, and every invented name is clearly made up.
- No teammate's real name in a scenario, and nothing about anyone's pay, performance, leave or one-to-ones.
- Plain, short sentences. No jargon a new hire wouldn't know without a definition right next to it.

STEP 1: THE PLAN (show me, then wait)
Propose the lessons. Start from these, merge or cut to fit how we work, and keep it to six to ten lessons:
1. The parts and their names (`01`)
2. Which instruction wins (`02`)
3. Your day: what runs when, and what lands in your inbox (`03`, `07`)
4. Receipts and the three verdicts (`04`)
5. The human step: draft codes and the three ways a draft ends (`05`)
6. One loop, one tracker: what goes on the board and what doesn't (`06`)
7. Privacy zones (`08`)
8. What broke, and the rule each failure produced (`10`)
9. Optional: team rituals, if we run them (`11`)
10. Optional: pushing back on Claude. How to ask for the assumptions, the weak step and the strongest counter, and why a Claude that only agrees is a risk.

For each lesson give: a one-line goal, the invented scenario it opens with, the "one thing to remember", and which of our company rules it teaches. Flag any lesson where our rules and the kit differ.

STEP 2: THE QUESTIONS (show me, then wait)
For each lesson, six or seven multiple-choice questions:
- Start from `learn/questions.md`. Reword them into our vocabulary and our clock.
- Add at least two questions per lesson from our own company rules, quoting the rule's section.
- At least one question per lesson calls back to an earlier lesson.
- Every question has four options, one right answer, a one-line reason for each wrong option, and a source (kit chapter or our rule section).
Then a final check of 25 to 35 questions drawn from all lessons.
Show me the full question set as a table I can edit. I'll mark any I want changed.

STEP 3: BUILD (after my yes)
Build one page per lesson plus a course home page and a final check page, in our house style:
- The home page lists the lessons in order with a short line each, and a "Start lesson 1" button.
- Each lesson page: the scenario, the lesson in short sections, an "explain it like I'm five" fold, a "one thing to remember" card, then the quiz.
- The quiz shows one question at a time, says right or wrong with the reason after each answer, and shows the score at the end. 70% passes. Retakes allowed.
- The final check opens with a note to take it after the lessons; 80% passes.
- Pages work on a phone. Keyboard focus is visible. Colors pass contrast.
Publish each page as a private artifact (or build them as one small static site if I ask), and give me the links in order.

STEP 4: TRACKING (ask me which)
Offer three options and recommend one for a team our size:
a. None. People tell their manager their score. Fine under ten people.
b. A shared sheet. Each quiz page shows a short "copy my result" line (name, lesson, score, date) that the person pastes into a sheet their manager can see.
c. Automatic. The quiz pages save results to a store that knows who is signed in, if our setup offers one. Only with my explicit go, and never visible to other teammates.

STEP 5: HAND-OFF
Give me:
- the links, in order
- a three-line message I can send the team (I send it, not you): what the course is, that it starts after setup, and that lesson one takes about ten minutes
- a short note for managers on the supervised run, if we use it
- a list of every place the course quotes our rules, so a rules change tells me which lesson to update

KEEPING IT CURRENT
When our company rules change, the person who edits them checks that list and asks this chat to update the affected lesson and its questions. A course that teaches an old rule is worse than no course.
