# Structure is /plugins/x
# Config file specifies which plugins are active and what weight is for each plugin.  Some plugins also require config

import config

for name in config.ACTIVE_PLUGINS:
    __import__('plugins.{}'.format(name), fromlist=['plugins'])


for plugin in pluginRegistry:
    score += plugin.score * plugin weight
    message += calcHeader()
    message += plugin.message
