# Loadshedding Calendar Generator

This is a script for converting the Cape Town loadshedding schedule to iCalendar format. All possible calendars have been generated and are also in this repo, so you don't actually need to run the script yourself.

# How to add to Google Calendar

## Get your calendar(s)

Find the calendar(s) for your zone in the repo:

* `calendars/combined` contains calendars with *all* the shedding periods for a given stage. If you add a stage 4 calendar from this directory, you will see all the shedding periods for stage 4, including all the shedding periods added in stages 1, 2 and 3. The stage in which a particular period is added is indicated in the event name.

* `calendars/individual` contains calendars with *only* the shedding periods *added* in each stage. If you add a stage 4 calendar from this directory, you will see *only* the periods added in stage 4, *not* the periods added in stages 1, 2 and 3. The stage in which a particular period is added is indicated in the event name.

Navigate to the calendar in the repo, and click the `Raw` button to be redirected to the actual file.

## Add by URL (calendar appears under "Other calendars")

1. Copy the URL of the calendar file.
2. In Google Calendar, expand the drop-down menu next to the `Add calendar` text box in the sidebar and select `From URL`.
3. Paste the URL in the text box provided and click `Add calendar`.

## Add by importing (calendar appears under "My calendars")

1. Download the calendar file.
2. In Google Calendar, expand the drop-down menu next to the `Add calendar` text box in the sidebar and select `New calendar`.
3. Enter a name and click `Create calendar`.
4. Click on `Import & export` in the sidebar.
5. Click on `Select file from your computer` and select the file you downloaded. Select the calendar you just created from the `Add to calendar` menu and click `Import`.

# Script

Usage: `cape_town_load_shedding.py ZONE STAGE`

`ZONE` and `STAGE` must be integers. Stage 4 is stage 4, not 3A, because I'm not a politician.

Passing `only` as the third parameter outputs a calendar with ONLY the shedding periods ADDED in the given stage. This is useful if you want to import each additional set of periods as a separate calendar so that you can toggle them on and off.

# Disclaimer

I'm not affiliated with the City of Cape Town in any way. This script was very hurriedly written and very briefly tested. Please check the calendar against the official schedule, and file an issue if you find a bug!
