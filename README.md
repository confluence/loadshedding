# Loadshedding Calendar Generator

This is a script for converting the Cape Town loadshedding schedule to iCalendar format. All possible calendars have been generated and are also in this repo, so you don't actually need to run the script yourself.

Please note that support for stages 5 to 8 is **experimental** -- please check the calendar against the official schedule and report any bugs.

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
5. Click on `Select file from your computer` and select the file you downloaded. Select the calendar you just created from the `Add to calendar` menu and click `Import`. **BE CAREFUL**; the default is your main calendar, and the import can't easily be undone (but see below).


## OH @#$%&*, I IMPORTED A CALENDAR INTO MY MAIN CALENDAR BY MISTAKE! NOW WHAT?!

Don't panic; you can fix it with a Google Apps script. I'm providing a script template in this repo; adapt and use it at your own risk. Detailed support is outside the scope of this project. Please don't blow up your calendar.

# Updating your calendar(s)

Because adding a calendar by URL is called a "subscription", you might expect to get updates automatically if the calendar changes (which may happen if I find a bug in the code -- see the disclaimer!). But it appears that Google refreshes external calendars very infrequently, and also caches them, so if you want to get an updated calendar immediately the only 100% reliable way is to import it.

# Running the script yourself

Basic usage: `cape_town_load_shedding.py -z ZONE -s STAGE`

`ZONE` and `STAGE` must be integers. Stages go up to 8 now, regrettably.

Adding `-o` outputs a calendar with ONLY the shedding periods ADDED in the given stage. This is useful if you want to import each additional set of periods as a separate calendar so that you can toggle them on and off.

For advanced usage information, use the help flag: `cape_town_load_shedding.py -h`

It's possible to add multiple zones to a single calendar and to specify custom labels for zones. This makes it easier to aggregate multiple notable landmarks in a single calendar efficiently. The command used to generate the calendar file is now written to the header, so that you can recreate it more easily if you want to change something. It's probably easiest to regenerate the whole calendar and delete the old one.

Note that importing a very large calendar file into Google Calendar may time out, and either fail entirely or leave you with a partial import. Read the messages carefully and consider importing each zone separately if you run into trouble. This is most likely to happen if you create a combined calendar for a high stage.

# Disclaimer

I'm not affiliated with the City of Cape Town in any way. Support for stages above 4 was added recently and hurriedly, and very briefly tested. Please check the calendar against the official schedule, and file an issue if you find a bug!

Also, just to be absolutely clear, this is just the City's (theoretical) shedding schedule translated into calendar form to make planning easier. The calendar has no idea what stage you're in or if you're actually going to be shed!
