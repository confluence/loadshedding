#!/usr/bin/env python3

import datetime
import argparse
import sys

# ----------- CALENDAR CONSTANTS ----------- #

ical_head = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//confluence//bar/cape_town_load_shedding.py/EN
X-WR-CALNAME:Cape Town Loadshedding Calendar
X-WR-CALDESC:Generated with command "%s"
""" % " ".join(sys.argv)

ical_event = """BEGIN:VEVENT
UID:{start_time}@cape_town_load_shedding.py
DTSTAMP;TZID=Africa/Johannesburg:{start_time}
DTSTART;TZID=Africa/Johannesburg:{start_time}
RRULE:FREQ=MONTHLY;BYMONTHDAY={day_of_month}
DTEND;TZID=Africa/Johannesburg:{end_time}
SUMMARY:{summary}
DESCRIPTION:{description}
END:VEVENT
"""

ical_foot = """END:VCALENDAR
"""

date_format = "%Y%m%dT%H%M%S"
year = datetime.datetime.now().year
duration = datetime.timedelta(hours=2, minutes=30)

# ----------- FUNCTIONS ----------- #

def add_zone(zone, stage, only):
    events = []

    def add_stage(zone, block, s):
        startday = block * 4 + 1
        stage_offset = (0, 8, 12, 4, 1, 9, 13, 5)[s]
        
        for count in range(3):
            day_offset, slot = divmod((zone - 1 - stage_offset) % 16 - block + 16 * count, 12)
            day_offset %= 4
            day_of_month = startday + day_offset
            events.append((day_of_month, slot, s)) # 1-indexed, 0-indexed, 0-indexed
            events.append((day_of_month + 16, slot, s)) # ignore 32nd day later, not now

    for block in range(4):
        if only:
            add_stage(zone, block, stage - 1)
        
        else:
            for s in range(stage):
                add_stage(zone, block, s)
                
    return events

def write_calendar(all_events, filename, labels):
    with open(filename, "w") as ical_file:
        ical_file.write(ical_head)
        
        for i, (zone, events) in enumerate(all_events):
            for day_of_month, slot, s in events:
                if day_of_month == 32:
                    continue
                
                start = datetime.datetime(year=year, month=1, day=day_of_month, hour=slot * 2)
                end = start + duration
                
                if len(labels) > i:
                    summary = "%s (Z %d) %d+" % (labels[i], zone, s + 1)
                    description = "%s (Zone %d) Loadshedding (stage %d+)" % (labels[i], zone, s + 1)
                else:
                    summary = "Z %d S %d+" % (zone, s + 1)
                    description = "Zone %d Loadshedding (stage %d+)" % (zone, s + 1)
                
                ical_file.write(ical_event.format(
                    start_time=start.strftime(date_format),
                    end_time=end.strftime(date_format),
                    day_of_month=day_of_month,
                    summary=summary,
                    description=description
                ))
        
        ical_file.write(ical_foot)

# ----------- MAIN ----------- #

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a loadshedding calendar for a zone managed by the City of Cape Town")
    parser.add_argument('-z', '--zone', nargs="+", help="Add zone. Multiple zones can be added to the same calendar.", type=int, choices=range(1, 16+1), metavar="[1-16]", required=True)
    parser.add_argument('-s', '--stage', help="The stage", type=int, choices=range(1, 1+8), metavar="[1-8]", required=True)
    parser.add_argument('-o', '--only', help="Add only the specified stage (by default, all stages up to and including the specified stage will be added).", action="store_true")
    parser.add_argument('-l', '--label', nargs="+", help="Custom zone label. If multiple zones and labels are specified, they will be combined in the order in which they are given.", default=[])
    parser.add_argument('-f', '--filename', help="Name of the output calendar file.")
    args = parser.parse_args()
    
    all_events = []
    
    for zone in args.zone:
        all_events.append((zone, add_zone(zone, args.stage, args.only)))
    
    if not args.filename:
        zonelist = "_".join(str(z) for z in args.zone)
        only = "_only" if args.only else ""
        filename = "zone_%s_stage_%d%s.ics" % (zonelist, args.stage, only)
    else:
        filename = args.filename
        
    write_calendar(all_events, filename, args.label)
