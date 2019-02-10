# loadshedding
A script for converting the Cape Town loadshedding schedule to iCalendar format

Usage: cape\_town\_load\_shedding.py ZONE STAGE

ZONE and STAGE must be integers. Stage 4 is stage 4, not 3A, because I'm not a politician.

Passing `only` as the third parameter outputs a calendar with ONLY the shedding periods ADDED in the given stage. This is useful if you want to import each additional set of periods as a separate calendar so that you can toggle them on and off.

Very hurriedly written; very briefly tested. File an issue if you find a bug!
