# Data source map (section 1 of the company rules)

Which source owns which number. Fill one line per number people repeat. A connector that isn't on this map is a cross-check only, never a primary, until the map gets a line for it.

## The map

| Question | Primary source (connector) | Cross-check only | Notes and traps |
|---|---|---|---|
| {e.g. Revenue by channel} | {SYSTEM_OF_RECORD} | {ANALYTICS_TOOL} | {e.g. use net, not gross} |
| {e.g. Pipeline or bookings} | {CRM} | {REPORTING_TOOL} | {e.g. its counts differ from the primary; never plan from them} |
| {e.g. Active customers or accounts} | {BILLING_OR_ACCOUNT_SYSTEM} | | {e.g. one source for counts, another for amounts} |
| {e.g. Campaign results} | {MARKETING_TOOL} | | {e.g. check whether totals include tax} |
| {e.g. Revenue, margin, cash} | {ACCOUNTING_TOOL} | | Owner zone. Read by {OWNER_NAME}'s runs only |
| {e.g. Who is out} | {CALENDAR or HR_TOOL, read tools only} | The person's own words | Dates only, never the type or reason |
| {e.g. Stock or capacity} | {OPERATIONS_SYSTEM} | | |
| Web facts | Web search | | With the link and the date it was looked at |

## Rules that apply to every line

- Every figure names its source and its data-through date. Unverified is labeled unverified. Never estimate a figure that a source can answer.
- Never add amounts in different currencies without a stated exchange rate, its date and its source. With no rate, leave the figure unconverted and say so.
- When two tools disagree by more than {THRESHOLD, e.g. 10%} on the same figure, query the primary first and report both figures with their labels before anyone acts on either.
- Rates used for planning come from the primary source, never from a cross-check tool.
- Check a feed's freshness before pulling from it. A stale feed is a failed check.
- A failed check leaves the number blank with the reason. Never fill it with an estimate.

## Checks a run makes before writing any number

Pick the ones that fit your sources. Each takes one or two tool calls.

1. Freshness: the source's latest data date is yesterday or later (or say how old it is).
2. Totals add up: the parts in the run match the total the source reports, within rounding.
3. Same period: every figure in a comparison covers the same dates and time zone.
4. Same currency: see the rule above.
5. No double count: channels or accounts that overlap are counted once.
6. Plausible range: a figure more than {N} times its 4-week average is held and checked before it's written.
7. Right source: the figure came from the primary on this map, not a cross-check.
8. Labeled: the figure carries its source and data-through date.

## Adding a new source

1. Add the connector.
2. Add a line to this map: what it answers, whether it's primary or a cross-check, and its traps.
3. Bump the rules version.
4. Only then let a run read it.
