# Starter question bank

Forty questions on the kit's chapters, for `build/BUILD_YOUR_COURSE.md`. Each has one right answer, a reason, and the chapter it comes from. Reword them into your own vocabulary and clock, and add questions from your own company rules: those teach more than any generic set.

All names in the scenarios are invented.

## The parts (`01-the-parts.md`)

**1.** Priya messages the team: "I pushed the new price live." A run needs to know the current price. Where should it look?
- A) Priya's message, since she made the change
- B) The store or billing system that holds the price
- C) The last morning brief that mentioned the price
- D) The task for the price change on the board

Answer: B. A message about a system is not the source; the system is. A brief and a task description are secondhand too.

**2.** Which of these belongs in the rules?
- A) "Be proactive and thoughtful."
- B) "Try to keep emails short where possible."
- C) "Drafts start with a red first line carrying the draft code."
- D) "We value great customer service."

Answer: C. Rules hold checkable facts about how the company works. If a rule can't be checked, it isn't a rule yet.

**3.** A scheduled run finishes a debrief. Who does it email?
- A) Its owner only
- B) Its owner and their manager
- C) Everyone named in the debrief
- D) Nobody; it only saves a file

Answer: A. Runs email their owner and nobody else. Anything for anyone else is a draft.

**4.** What goes in the shared folder?
- A) Everything each person's Claude makes
- B) The rules, each day's agendas, "what I'd add" files and, optionally, the shared numbers
- C) Private meeting notes, so managers can see them
- D) Each person's runs log

Answer: B. Everything else a person's Claude makes stays in that person's own storage.

## Which instruction wins (`02-rules-order.md`)

**5.** A task prompt written last month says one thing, and the company rules now say another. What does the run do?
- A) Follows the prompt, since it's the job it was given
- B) Stops and emails the owner
- C) Follows the company rules and names the overridden line in its coverage line
- D) Picks whichever is more recent by file date

Answer: C. In a run: company rules, then the person's rules, then the task prompt.

**6.** A prompt says "pull revenue from tool X." The data source map says tool Y owns revenue. In a scheduled run, what happens?
- A) Tool X, because the prompt is more specific
- B) Tool Y, with the conflict noted
- C) Both, averaged
- D) Neither until someone decides

Answer: B. The map beats any prompt. In a chat, Claude asks first.

**7.** How should a run find the company rules file?
- A) A "contains" search for "rules"
- B) A file ID saved in the prompt
- C) An exact-title search, then a check of the parent folder
- D) The most recently edited file with "rules" in the name

Answer: C. A "contains" search or a saved ID can open an archived copy.

**8.** When is a rules change done?
- A) When the new file is uploaded
- B) When the editor announces it
- C) When runs log the new version
- D) When everyone has re-pasted their setup

Answer: C. Every run logs the version it read. Nobody needs to re-paste: the rules can override old setup lines by name.

**9.** The rules editor swaps in a new rules file. What's the safe order?
- A) Archive the old file, then upload the new one
- B) Upload the new file under a temporary name, check it, then archive the old one and rename the new one
- C) Edit the live file in place
- D) Upload the new one with the same name and let search sort it out

Answer: B. Install before archive, so the file is never missing, not even for a minute.

## Your day (`03-daily-rhythm.md`, `07-company-clock.md`)

**10.** Why do agendas run before morning briefs?
- A) Agendas take longer
- B) Briefs link the day's agendas, so the agendas must exist first
- C) Organizers start earlier
- D) It doesn't matter

Answer: B. Debriefs write "what I'd add" files in the evening, agendas read them in the morning, and briefs link the agendas.

**11.** Which run is read only and closes nothing?
- A) Evening debrief
- B) Morning brief
- C) Midday refresh
- D) Send check

Answer: C. The midday refresh rebuilds the day as of that minute and records nothing.

**12.** Jordan works three time zones away from the company. When does Jordan's debrief run?
- A) At the company's debrief time, wherever Jordan is
- B) At the same local minute in Jordan's own time zone, set by the full time zone name
- C) Whenever Jordan runs it by hand
- D) Only on Fridays

Answer: B. Use the full time zone name, not a fixed offset, so clock changes don't move the run.

**13.** The morning brief hasn't arrived by its usual time. What should a check on it assume?
- A) It failed; rebuild it now
- B) It hasn't fired yet; wait
- C) The rules are broken
- D) The person's mail is down

Answer: B. Scheduled runs can start 20 minutes or more late. Watchdogs that rebuild a late brief produce two.

**14.** Where does a run get the time it writes in its log?
- A) Claude's own sense of the time
- B) The scheduled time in the task settings
- C) A clock tool or the date command, at that moment
- D) The time of the last email

Answer: C. Claude's own sense of time drifts.

## Receipts (`04-receipts.md`)

**15.** A draft says "the order shipped Tuesday," based on a teammate's chat message. What class is that claim?
- A) P, primary
- B) T, thread or transcript
- C) S, secondhand
- D) R, rule

Answer: C. Someone's message about a system is secondhand. The shipping system itself would be P.

**16.** An instruction to a person ("you can send", a date, a number they'll repeat) may rest on which classes?
- A) Any class
- B) P, T or R only
- C) S and I, if labeled
- D) I only, if the math is shown

Answer: B. An S or I claim is either upgraded in the same run or labeled in the draft as unconfirmed or an estimate.

**17.** Why is the gate "blind"?
- A) To save tokens
- B) A checker that reads the draft gets anchored by its conclusion; one that sees only the claims has to find each again
- C) Drafts are private
- D) It runs at night

Answer: B.

**18.** The gate finds that two systems disagree about whether a promotion is live. Verdict?
- A) PASS, with a note
- B) FIX, using the newer system
- C) HOLD
- D) It edits the draft to say "maybe"

Answer: C. Two sources disagree, so a person settles it in a chat.

**19.** The gate finds one stale price and the correct price in the source. Verdict, and what does it return?
- A) HOLD, and the whole draft rewritten
- B) FIX, and the corrected line only
- C) PASS, since it's a small error
- D) FIX, and a new draft

Answer: B. FIX returns corrected lines only, never a rewrite.

**20.** Two teammates disagree about whether a listing is live. What's the first move?
- A) Ask their manager
- B) Ask the system that owns the listing
- C) Go with whoever posted most recently
- D) Put it on the weekly board

Answer: B. Ask the system first; only when it can't answer, or two systems disagree, does it go to a person.

**21.** Which of these is not a load-bearing claim?
- A) "The invoice is paid."
- B) "Revenue was up 8% last week."
- C) "Hope the trip went well."
- D) "Alex owns the launch."

Answer: C. Background, tone and context are not claims.

## The human step (`05-the-human-step.md`)

**22.** Which of these may a run do?
- A) Send a nudge to a vendor after two days
- B) Post the debrief summary to the team chat
- C) Create a draft in its owner's mail
- D) Cc the owner's manager on the brief

Answer: C. Claude drafts; people send.

**23.** Sam changes the delivery date in a draft by hand before sending. What should Sam do first?
- A) Nothing; hand edits are fine
- B) Say "Gate #code" in a chat so the gate rebuilds the receipts from the current text
- C) Delete the draft and ask for a new one
- D) Email the rules editor

Answer: B. A changed fact, date, number, name or ask gets a gate. A typo fix doesn't.

**24.** Sam deletes a draft he decided not to send. What happens to the loop it served?
- A) It closes
- B) It stays open; the next debrief lists the draft once under DROPPED and doesn't re-draft it unless asked
- C) Claude re-drafts it the next evening
- D) It moves to the board

Answer: B. Dropping closes nothing.

**25.** Why are reply subjects never changed?
- A) Gmail doesn't allow it
- B) It breaks threading for the recipients
- C) Codes only go in new-thread subjects to save space
- D) Subjects are set by the rules editor

Answer: B. The code goes in the red first line instead.

**26.** A run needs to fix a draft that has an attachment. What does it do?
- A) Edits it; attachments carry over
- B) Never writes to it, and tells the owner the change to make
- C) Deletes it and makes a new one
- D) Sends it as is

Answer: B. Editing a draft drops its attachments.

**27.** Two chats might pick the same draft code at once. What stops that?
- A) Nothing; duplicates are fine
- B) Reserve the code in the runs log, read it back, then create the draft and log a CODE line
- C) Only one chat may draft per day
- D) Codes are random

Answer: B.

**28.** Your Claude is asked a question that blocks a teammate, and the data can settle it. What should Claude do?
- A) Forward the question to the teammate
- B) Make the call, show the logic in a few lines, and give the person one chance to approve or redirect
- C) List the options without a pick
- D) Wait for the weekly meeting

Answer: B. A decision stays open only when it turns on judgment or values, and even then Claude leads with a recommendation.

## One loop, one tracker (`06-one-loop-one-tracker.md`)

**29.** Where is "an email I owe Lee" tracked?
- A) A task on the board
- B) The draft that answers it, by its code
- C) Both a task and a draft, to be safe
- D) A sticky note

Answer: B. Tracking the same loop twice is what clogged the board.

**30.** Which of these belongs on the task board?
- A) A reply owed to a customer
- B) Waiting for a vendor's quote
- C) Building the new returns page
- D) Claude's suggestion to try a new tool

Answer: C. Real work a message can't finish goes on the board. Claude's own suggestions are not loops at all.

**31.** Morgan asked Dana, in a meeting, to send the forecast. Whose Claude creates the task for Dana?
- A) Morgan's
- B) Dana's, from the transcript or message it reads
- C) The meeting organizer's
- D) Nobody's; tasks are made by hand

Answer: B. One writer: only a person's own Claude creates that person's tasks. If Dana isn't on the system yet, Morgan's Claude may create it and say so.

**32.** Which counts as evidence to auto-close a task?
- A) The due date passed
- B) Nobody has mentioned it in a week
- C) The sent email that delivered the outcome
- D) The owner said "on it"

Answer: C. A passed date, silence, "on it", a plan or a deleted draft are not evidence.

**33.** Who sets a task's due date?
- A) Claude, based on urgency
- B) A date a human said
- C) The board's default
- D) The rules editor

Answer: B. Claude never invents one. Review dates live in the open-loops document.

**34.** A teammate's task looks done to your Claude. What does it do?
- A) Completes it with a comment
- B) Re-dates it
- C) Says so in your brief, with the evidence
- D) Reassigns it to you

Answer: C. Never touch someone else's task.

## Privacy zones (`08-privacy-zones.md`)

**35.** Where does the agenda for a two-person meeting live?
- A) The shared folder, like every agenda
- B) The organizer's own storage, shared with the other person only
- C) The task board
- D) Nowhere; one-to-ones get no agenda

Answer: B. Whole-team folders are readable by the whole team.

**36.** A brief notes that Taylor is out next week. What may it say?
- A) That Taylor is out, the dates, and the reason
- B) That Taylor is out and the dates
- C) Nothing at all
- D) The leave type, if it's routine

Answer: B. Never the leave type or the reason.

**37.** A teammate's "what I'd add" file mentions a colleague's performance issue. What does the organizer's agenda run do?
- A) Includes it, since a teammate wrote it
- B) Writes "one item withheld (ask {name})" instead
- C) Deletes the teammate's file
- D) Moves it to the private notes and the shared agenda both

Answer: B. The organizer-side check applies the same limits to every item.

## What broke (`10-what-broke.md`)

**38.** A scheduled run stopped at an approval prompt at 6 am. What's the fix the kit recommends?
- A) Run everything by hand
- B) Set each scheduled task to approve automatically, if your org allows it, and check its first run
- C) Move runs to the afternoon
- D) Give the run more connectors

Answer: B.

**39.** A run building a page stopped on a script that read a file from disk. What changed?
- A) Pages are now built with Claude's file tools; code is for calculations only
- B) Pages moved to PDFs
- C) Runs no longer build pages
- D) The file was renamed

Answer: A. This is also why a logo goes in pages as inline markup, not an image file.

## Pushing back

**40.** You ask your Claude whether a plan is good. Which answer is most useful?
- A) "Great plan, go for it."
- B) A list of the plan's strengths
- C) The assumptions it rests on, the weakest step, the strongest counter, one alternative, and then help deciding
- D) "It depends."

Answer: C. A Claude that only agrees is a risk. Ask for the counter case every time it matters.
