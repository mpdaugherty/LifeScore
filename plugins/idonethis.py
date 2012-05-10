import urllib2
import icalendar

from config import IDONETHIS_CALENDAR
from . import Plugin

class IDoneThisPlugin(Plugin):
    name = 'idonethis'
    base_score = 15
    _score_multiplier = 1.12
    current_streak = 0

    def calculate(self):
        # Get the profile page of the user
        download_cal = urllib2.urlopen(IDONETHIS_CALENDAR)
        cal = icalendar.Calendar.from_ical(download_cal.read())
        # For each ical event, get the DTSTART param to say when it started
        start_dates = [x.get('DTSTART') for x in cal.walk()]
        # Next, filter out "None" (this shows up for the description element of the calendar, since
        # it is an element as well) and get the datetime.date representation of each event
        dates = [x.dt for x in start_dates if x]
        # Sort so the dates are in order
        dates.sort()

        daily_points = []
        for i in range(0, len(dates)):
            if i == 0:
                # The first day you do anything is always worth a point.
                daily_points.append(1)
            elif (dates[i] - dates[i-1]).days == 1:
                # If the user did their activity two days in a row, this day
                # is worth one more point than the day before
                daily_points.append(daily_points[i-1] + 1)
            elif (dates[i] - dates[i-1]).days > 1:
                # If the user skipped a day, their points/day is reset to 1
                daily_points.append(1)
            else:
                # If the day is the same as the last event, skip it.  You only
                # get points once per day
                pass

        self.score = sum(daily_points)
        self.message = '''
  Current streak       = {} days
  Max streak           = {} days
  Points to next level = {}
  Keep it up!
'''.format(daily_points[-1], max(daily_points), self.points_to_next_level)



