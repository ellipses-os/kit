# Ledger formats

## A ledger line

```
{class} | {claim, one line} | {source, specific enough to re-query: tool and record, or document and date} | read {h:mm am/pm} {Mon DD}
```

- I lines add `| wrong if: {one line}`.
- R lines add `| version {rules version}`.
- S lines that stay S add `| labeled: per {name}`.
- Read times are the times of the actual calls, from a clock, never the time the output was put together.

## Classes

| Class | Meaning |
|---|---|
| P | The system that owns the fact, queried this run |
| T | The thread, transcript or sent message itself, read in full this run |
| R | The rules file, read this run by exact title with its parent folder confirmed |
| S | A message about a system, a summary, a task, an earlier output, memory, a run's own report |
| I | A calculation or conclusion from named inputs, with "wrong if" |

## The gate line

```
GATE | {PASS, FIX or HOLD} | {h:mm am/pm} {Mon DD} | {n} calls
```

Add `self-gated` when no separate checker was available.

## Receipts log line

```
{ISO time} | {run or chat} | {output id} | {claim as written} | {original class} | {what the source said} | {correcting source} | {FIX or HOLD} | {resolved by}
```

## Where the ledger sits

| Output | Place |
|---|---|
| Email draft | Red lines headed RECEIPTS, directly under the red code line, above the greeting. Deleted with the red block before sending |
| Brief or debrief | Under COVERAGE, headed RECEIPTS |
| Agenda or notes page | A collapsed block at the end: `<details><summary>Receipts</summary>...</details>` |
| Task | Right after the "Created by Claude from:" line |
| Chat answer a person will act on | The same lines in plain text at the end |
