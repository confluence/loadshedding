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

# Updating your calendar(s)

Because adding a calendar by URL is called a "subscription", you might expect to get updates automatically if the calendar changes (which may happen if I find a bug in the code -- see the disclaimer!). But it appears that Google never actually refreshes external calendars, so it looks like you'll have to remove the calendar and re-add it manually no matter how you added it.

# Script

Basic usage: `cape_town_load_shedding.py -z ZONE -s STAGE`

`ZONE` and `STAGE` must be integers. Stage 4 is stage 4, not 3A, because I'm not a politician.

Adding `-o` outputs a calendar with ONLY the shedding periods ADDED in the given stage. This is useful if you want to import each additional set of periods as a separate calendar so that you can toggle them on and off.

For advanced usage information, use the help flag: `cape_town_load_shedding.py -h`

It's possible to add multiple zones to a single calendar and to specify custom labels for zones. This makes it easier to aggregate multiple notable landmarks in a single calendar efficiently. The command used to generate the calendar file is now written to the header, so that you can recreate it more easily if you want to change something. It's probably easiest to regenerate the whole calendar and delete the old one.

# Disclaimer

I'm not affiliated with the City of Cape Town in any way. This script was very hurriedly written and very briefly tested. Please check the calendar against the official schedule, and file an issue if you find a bug!

Also, just to be absolutely clear, this is just the City's (theoretical) shedding schedule translated into calendar form to make planning easier. The calendar has no idea what stage you're in or if you're actually going to be shed!
