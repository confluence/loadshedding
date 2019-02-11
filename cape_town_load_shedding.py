#!/usr/bin/env python3

import sys
import datetime

try:
    zone, stage = [int(a) for a in sys.argv[1:3]]
    only = True if len(sys.argv) > 3 and sys.argv[3].lower() == "only" else False
except:
    sys.exit("""Usage: `cape_town_load_shedding.py ZONE STAGE [only]`

ZONE and STAGE must be integers. Stage 4 is stage 4, not 3A, because I'm not a politician.

Passing `only` as the third parameter outputs a calendar with ONLY the shedding periods ADDED in the given stage.
""")

if not 1 <= zone <= 16:
    sys.exit("I only know about zones from 1 to 16.")

if not 1 <= stage <= 4:
    sys.exit("I only know about stages from 1 to 4.")

slots = []

def add_stage(zone, block, s):
    startday = block * 4 + 1
    stage_offset = (0, 8, 12, 4)[s]
    
    for count in range(3):
        day_offset, slot = divmod((zone - 1 - stage_offset) % 16 - block + 16 * count, 12)
        day_offset %= 4
        day_of_month = startday + day_offset
        slots.append((day_of_month, slot, s)) # 1-indexed, 0-indexed, 0-indexed
        slots.append((day_of_month + 16, slot, s)) # ignore 32nd day later, not now

for block in range(4):
    if only:
        add_stage(zone, block, stage - 1)
    
    else:
        for s in range(stage):
            add_stage(zone, block, s)

ical_head = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//confluence//bar/cape_town_load_shedding.py/EN
"""

ical_event = """BEGIN:VEVENT
UID:{start_time}@cape_town_load_shedding.py
DTSTAMP;TZID=Africa/Johannesburg:{start_time}
DTSTART;TZID=Africa/Johannesburg:{start_time}
RRULE:FREQ=MONTHLY;BYMONTHDAY={day_of_month}
DTEND;TZID=Africa/Johannesburg:{end_time}
SUMMARY:Loadshedding (stage {min_stage}+)
END:VEVENT
"""

ical_foot = """END:VCALENDAR
"""

date_format = "%Y%m%dT%H%M%S"
year = datetime.datetime.now().year
duration = datetime.timedelta(hours=2, minutes=30)

with open("zone_%d_stage_%d%s.ics" % (zone, stage, "_only" if only else ""), "w") as ical_file:
    ical_file.write(ical_head)

    for day_of_month, slot, s in slots:
        if day_of_month == 32:
            continue
        
        start = datetime.datetime(year=year, month=1, day=day_of_month, hour=slot * 2)
        end = start + duration
        
        ical_file.write(ical_event.format(
            start_time=start.strftime(date_format),
            end_time=end.strftime(date_format),
            day_of_month=day_of_month,
            min_stage=s + 1
        ))
    
    ical_file.write(ical_foot)
