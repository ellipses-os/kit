# Receipts

A draft is only as good as the claims a person will act on. Receipts make every such claim traceable, and a blind check makes sure the trace holds before anything is marked ready.

## Which claims need a receipt

A claim is load-bearing when someone would act on it:

- a system's state: live, posted, in stock, scheduled, paused
- a number someone will repeat
- a date, or someone's availability
- a price, cap, rate or rule
- an owner or a decision
- "done", "sent" or "posted"

Background, tone and context are not claims.

## The five classes

Each load-bearing claim gets one line in a ledger, with a class and the time it was read:

| Class | Meaning |
|---|---|
| P, primary | The system that owns the fact, queried in this run |
| T, thread or transcript | The record itself, read in full in this run (the email thread, the verbatim transcript, the sent message) |
| R, rule | Text quoted from the rules file, read in this run by exact title, with its version |
| S, secondhand | Someone's message about a system, a summary, a task description, an earlier brief, memory, or a run's own report of what it did |
| I, inference | A calculation or conclusion, with its inputs and one line: "wrong if: ..." |

No confidence percentages. Where a claim came from and how old it is are the confidence.

## The instruction rule

An instruction to a person (an ask, a date, a number they'll repeat, "you can send", "this is live") rests only on P, T or R. An S or I claim is either upgraded in the same run by asking its source, or it appears in the draft labeled: "Source: {name} ({channel}, {date}); not yet confirmed in {system}" or "estimate, don't quote".

## The ledger line

```
{class} | {claim, one line} | {source, specific enough to re-query} | read {time} {date}
```

I lines add `| wrong if: {one line}`. R lines add the rules version. The ledger ends with a gate line: `GATE | PASS, FIX or HOLD | {time} {date} | {n} calls`.

Where the ledger lives: at the top of a draft in red, under the draft code, deleted before sending; under the coverage line in a brief; in a collapsed block at the end of an agenda.

## The blind gate

Before a draft, brief section, agenda item or task is marked ready, a separate Claude that has never seen the draft gets the ledger and nothing else. It re-reads every P, T and R line at the source, tries to upgrade every S line to P, recomputes every I line, and sweeps mail, chat and transcripts since the ledger's stamp for anything that touches the people or topics it names. It keeps to a small budget (about five to ten tool calls a draft).

It returns one of three verdicts:

| Verdict | When |
|---|---|
| PASS | Everything re-derives and nothing newer touches it |
| FIX | A line is wrong or stale and a source gives the right value. The gate returns corrected lines only, never a rewrite of the draft |
| HOLD | Two sources disagree, a source an instruction rests on can't be reached, or something newer changes the ask. A person settles it in a chat, never by editing the draft by hand and never by sending |

Why blind: a checker that reads the draft gets anchored by its conclusion. A checker that sees only the claims has to find each one again.

## The log and the monthly loop

Every FIX and HOLD goes to the person's receipts log, one line each: when, which output, the claim as written, its class, what the source said, the source, the verdict, who resolved it. Once a month the debrief groups the lines by failure type (secondhand taken as primary, rule from memory, stale fact, escalation before checking the source, budget), counts them, and proposes rule changes with the lines that justify each. A person decides; a run never changes a rule.

## Escalation order

When two people disagree about a system's state, ask the system first. If it answers, report the finding: what the system says, who had it wrong, who acted on the wrong version and needs to know. Only when the system can't answer, or two systems disagree, does it go to a person to decide.
