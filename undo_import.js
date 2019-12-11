/* 
 * 
 * This script, modified appropriately, may be helpful in undoing an accidental import of loadshedding schedules into your main Google calendar (an easy mistake to make!). I'm providing it as-is; use it at your own risk!
 * 
 * Script goes here: https://script.google.com/
 * 
 * Adapted from this thread: https://webapps.stackexchange.com/questions/19513/how-to-delete-all-events-on-many-dates-all-at-once-but-not-the-whole-calendar-in
 * 
 * API documentation: https://developers.google.com/apps-script/reference/calendar/
 * 
*/

function delete_events()
{
  // Date function starts at 0 for the month (January=0)
  var fromDate = new Date(2020,0,1,0,0,0); // change these dates to make sure it's a month which contains events
  var toDate = new Date(2020,1,1,0,0,0);
 
  var calendar = CalendarApp.getCalendarById('CALENDAR_ID_GOES_HERE'); // if this is your main calendar, it's your gmail address
  var events = calendar.getEvents(fromDate, toDate);
  for(var i=0; i<events.length;i++)
  {
    var ev = events[i];
    if(ev.getDescription().indexOf("Loadshedding") > -1)
    {
      Logger.log('Item '+ev.getTitle()+' found on '+ev.getStartTime()); // first run with this uncommented to see a log of matching events
      // ev.getEventSeries().deleteEventSeries(); // then uncomment this to do the actual deletion
    }
  }
}
