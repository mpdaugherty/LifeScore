import os
import glob
import math

from config import ACTIVE_PLUGINS

# This is from http://martyalchin.com/2008/jan/10/simple-plugin-framework/
# Great article, BTW
class PluginMount(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            # This branch only executes when processing the mount point itself.
            # So, since this is a new plugin type, not an implementation, this
            # class shouldn't be registered as a plugin. Instead, it sets up a
            # list where plugins can be registered later.
            cls.plugins = []
        else:
            # This must be a plugin implementation, which should be registered.
            # Simply appending it to the list is all that's needed to keep
            # track of it later.
            cls.plugins.append(cls)

    def get_plugins(cls, *args, **kwargs):
        return [p(*args, **kwargs) for p in cls.plugins]

class Plugin(object):
    __metaclass__ = PluginMount

    _score_multiplier = 1.10
    _level_points = []

    score = 0
    message = ''
    base_score = 10
    name = ''

    @property
    def level(self):
        _level = 1;
        while (self.get_points_for_level(_level) <= self.score):
            _level += 1
        return _level - 1

    def get_points_for_level(self, level):
        try:
            return self._level_points[level]
        except IndexError:
            if level < 2:
                self._level_points = [0, 0]
            else:
                # Every level requires 1.1 * the score required for the previous level
                self._level_points.append(self.get_points_for_level(level - 1) + math.ceil(math.pow(self._score_multiplier, level - 2) * self.base_score))

        return self._level_points[level]

    @property
    def points_to_next_level(self):
        return self.get_points_for_level(self.level + 1) - self.score;

    @property
    def pct_to_next_level(self):
        return (max(self.score, self.get_points_for_level(self.level)) -
                self.get_points_for_level(self.level)) / (self.get_points_for_level(self.level + 1) -
                                                          self.get_points_for_level(self.level))

    def __init__(self):
        self.calculate()

# Import all the plugins in this directory
__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]
# Filter so we only have the active plugins enabled
__all__ = filter(lambda x: x in ACTIVE_PLUGINS, __all__)
from . import *

# Expose the list of plugins in a slightly better way
plugins = Plugin.get_plugins()


if __name__ == '__main__':
    for action in Plugin.plugins:
        print action
