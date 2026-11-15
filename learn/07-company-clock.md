# The company clock

Fixed weekday slots, so everyone's runs land in a predictable order and the shared pieces are ready when the next run needs them.

## A starting clock

Example times in the company's home time zone. Change them to fit your day.

| Slot | Run | Who |
|---|---|---|
| 5:15 am | Numbers | Organizers and owners |
| 6:05 am | Agendas | Meeting organizers |
| 7:00 to 7:20 am | Morning brief | Everyone, one person per minute or two |
| 8:15 am | Send check | Anyone who drafts a lot |
| 3:30 pm | Send check | Same |
| 4:00 to 4:20 pm | Evening debrief | Everyone, staggered |
| One weekday morning | Weekly team update | The meeting owner |

Why the order matters: debriefs write "what I'd add" files in the evening, agendas read them in the morning, and briefs link the agendas. A brief that runs before the agendas links nothing.

## Stagger people

Put each person in their own minute inside a slot. Runs that start together compete for the same sources, and logs become hard to read.

## Time zones

Anyone outside the home time zone gets their debrief at the same minute in their own time zone (for example 4:15 pm where they are), so it lands at the end of their day, not after it. Use the full time zone name (such as America/New_York), not a fixed offset, so clock changes don't move the run.

A brief's reading window starts at the start of the person's last debrief that both started and finished on an earlier day. A debrief run by hand this morning, or one that never finished, is skipped. This keeps a brief from cutting off the previous evening.

## Runs can start late

A scheduled run can start 20 minutes or more after its set time. A run that checks on another run treats "not yet fired" as waiting, never as missing. Don't build watchdogs that rebuild a brief because the first one is late; you'll get two.

## Approval mode

A scheduled run has nobody to click "Allow". Set each scheduled task to approve automatically in its settings, if your organization allows it, and check the first run of each one. A tool set to "ask" can stop a run cold or be missing from it entirely.

Even with automatic approval, some actions can still stop a run (we saw scripts that read files from disk do this). Keep runs to the tools they need: build pages with Claude's file tools, use code for calculations, and avoid scripts that read local files.

## Clock stamps

Every time a run writes down (log lines, "Checked through" stamps, receipt read times) comes from a clock tool or the date command at that moment. Claude's own sense of the time drifts.
