---
name: receipts-gate
description: Blind check of the load-bearing claims in a draft (by its #MMDD-NN code), a brief, an agenda, a task or a pasted claims ledger, before it is marked ready or sent. Re-derives each claim from its source, upgrades secondhand claims, recomputes numbers, sweeps recent mail, chat and transcripts, and returns PASS, FIX or HOLD. Use when asked to "gate", "send check", "check the receipts", "is this still true" or "where did that number come from", or when a scheduled task's finish step says to run the receipts gate.
---

# Receipts gate

This skill checks the claims a person will act on without reading the draft they sit in, so the check can't be anchored by the draft's conclusion. It is the send-time half of the Receipts section in your company rules (section 11 in the kit's template). The write-time half is the ledger every generating step ends with. Read that section from the company rules file before the first gate of a session: it is the source of truth for the classes, the primary-source map and the verdicts. `references/ledger-format.md` holds the line formats.

## What you need

One of: a draft code, the name of a brief or agenda, a task, or a ledger pasted as text. If a draft has no RECEIPTS block, build one from its instructions and numbers, mark every line S, and say so in the result. That is the only time the operator reads the draft.

## Two roles: operator and checker

The operator is whoever invokes the skill (a chat, or a scheduled run at its finish step). The checker is a fresh agent that sees only the ledger.

1. Operator: find the output and copy its ledger.
   - Draft: find it by the code in its red first line (never by recipient), copy the red block from the code line through the GATE line.
   - Brief: the RECEIPTS lines under COVERAGE.
   - Agenda: the collapsed Receipts block at the end.
   - Task: the lines after "Created by Claude from:".
2. Operator: start the checker with the Agent tool. Give it the ledger, the output's id, the ledger's stamp, the current date and time, and this instruction: "Run the receipts gate procedure in receipts-gate/SKILL.md on this ledger. You have not seen and must not fetch the output itself." Nothing else. If no Agent tool is available, the operator runs the procedure from the copied ledger only, without re-opening the output, and labels the result `self-gated`.
3. Checker: run the procedure below and return the result block.
4. Operator: act on the verdict, log FIX and HOLD lines, and write the GATE line back into the ledger.

## The procedure (checker)

Budget: about five to ten tool calls for a draft, scaled to the ledger. One call per line is the norm; the sweep is up to four calls. Never widen into a general search. Re-check lines that carry an instruction first. If the budget runs out, list every line left unchecked; an instruction resting on one of them is a HOLD.

Step 1, read the rules. Find the company rules file by exact title (never "contains") and confirm its parent folder is the Rules folder, never an archive. Never open it by a saved file ID. Note its version. An R line citing an older version is stale until re-read.

Step 2, re-derive P and T lines. Query the same source the line names, the same record, and compare. A difference is a FIX with the source's value. A source that errors or isn't connected is a HOLD if the line carries an instruction, otherwise "not re-read".

Step 3, upgrade S lines. Find the owning system in the primary-source map and query it. Agrees: the line becomes P. Disagrees: FIX with the primary's value. No primary exists: the line stays S and must carry `labeled: per {name}`, and the output must show "Source: {name} ({channel}, {date}); not yet confirmed in {system}". An unlabeled S line is a FIX whose correction is the labeled version.

Step 4, recompute I lines. Redo the calculation from its inputs (each checked under steps 2 and 3), then test its "wrong if". A different result is a FIX with the new value and the inputs that moved.

Step 5, re-read R lines against the rules file text from step 1. Different wording, or a rule the file no longer holds, is a FIX with the file's wording. A cap or price set in sent mail is a T line; re-read the mail.

Step 6, the freshness sweep, up to four calls, only for the people and topics the ledger names, since its stamp: mail from those people; chat conversations with them; team chat search for the topic; meeting transcripts with them. Anything that touches a ledger line is a FIX (a newer fact replaces the claim) or a HOLD (it changes the ask: the person already did it, a decision moved, someone is now out, a thread has a newer message).

Step 7, verdict.
- PASS: every line re-derives, every S was upgraded or is labeled, every I recomputes, and the sweep found nothing touching the ledger.
- FIX: at least one line is wrong, stale or unlabeled, and a source gives the right value. Return corrected lines only, in the ledger's words, with new class, source and read time. Never a rewrite of the output, never a change of voice, never a new ask.
- HOLD: two primaries disagree; a primary an instruction rests on can't be reached; the sweep found something that changes the ask; the budget ran out on an instruction line; or the same line would be a FIX twice in one run. Return both receipts and what the operator has to decide.
One HOLD makes the verdict HOLD. Otherwise one FIX makes it FIX.

## Result block

```
RECEIPTS GATE | {output id} | {PASS, FIX or HOLD} | {time} {date} | {n} calls
{per ledger line: OK, FIX, HOLD or unchecked | class | claim | source re-read | read {time}}
Unchecked (budget): {lines, or "none"}
FIX lines: {corrected lines, or "none"}
HOLD: {the contradiction, both receipts, the decision needed, or "none"}
Swept since {stamp}: mail {n}, chat {n}, team chat {n}, transcripts {n}; touching the ledger: {list or "none"}
Unverified in the output (S lines that stayed S): {list with labels, or "none"}
```

No confidence percentages and no "likely" or "probably": a line is re-derived, corrected, held or not re-read.

## After the verdict (operator)

- PASS: write `GATE | PASS {time} {date} | {n} calls` into the ledger. The output may be marked ready. Remove any earlier HOLD and WHAT TO DO lines.
- FIX: apply the corrected lines where each claim appears, and only there. A new-thread draft is updated in place, then re-read (recipients, subject, links, attachments). A reply draft is never edited in place: make a fresh reply draft with the same code and retire the old one. Update the ledger, then gate once more with a fresh checker.
- HOLD: never mark ready, never send. On a draft, add two lines directly under the code line: a red line `HOLD: {contradiction, both receipts}`, and under it a highlighted line `WHAT TO DO: Don't edit or send this draft in your mail. In Claude, say "Fix #{code}", then "Gate #{code}". Send only the draft that passes, after deleting the red block.` One WHAT TO DO line per draft. In a brief, list it under HOLD at the top.
- Never write to a draft a person saved by hand (its message ID differs from its last CODE or WRITE line) or one with an attachment; report the change instead.
- Append every FIX and HOLD to the person's receipts log:
  `{ISO time} | {run or chat} | {output id} | {claim as written} | {original class} | {what the source said} | {correcting source} | {FIX or HOLD} | {resolved by}`

## What the gate never does

It never reads the output it is checking (the operator reads it once, to copy the ledger). It never rewrites voice or adds an ask. It never sends or posts anything, and writes only to the receipts log, the run's own outputs and the ledger it was handed. It never sweeps a source the ledger doesn't name. It never turns a HOLD into a PASS by reasoning; a HOLD ends with a person.

## Worked example (invented)

Ledger handed to the checker, stamp 7:12 am Mar 4:

```
S | The Q2 offer applies to annual plans only | Sam, chat message Mar 2 | read 7:05 am Mar 4
T | Priya is out Thursday and Friday | Priya, chat Feb 27 | read 7:06 am Mar 4
R | trial credits count at half value against the discount cap | memory of the rules | read 7:07 am Mar 4
```

The third line is mislabeled: a rule from memory is S, so the checker treats it as S.

Checker: the billing system's offer record covers monthly and annual plans (FIX, now P). Priya's chat since the stamp has a newer message: "back Friday after all" (HOLD: the ask depended on her being out Friday). The rules file has no "half value" line; the owner's sent mail from Feb 20 says trial credits count at full value (FIX, now T). Verdict HOLD, seven calls. The operator adds the HOLD and WHAT TO DO lines, lists it at the top of the brief, and the person settles it in a chat.
