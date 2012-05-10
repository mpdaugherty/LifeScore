import urllib2
from BeautifulSoup import BeautifulSoup

from config import FITOCRACY_ID
from . import Plugin

class FitocracyPlugin(Plugin):
    score = 0
    message = ''
    name = 'Fitocracy'
    _level = 1

    def calculate(self):
        # Get the profile page of the user
        page_req = urllib2.urlopen(
            'http://www.fitocracy.com/profile/{}/'.format(FITOCRACY_ID))
        page = BeautifulSoup(page_req.read())

        self._level = 6
        self.score = 5

    @property
    def level(self):
        return self._level

    def get_points_for_level(self, level):
        return 7

    @property
    def points_to_next_level(self):
        return self.get_points_for_level(self.level + 1) - self.score;


