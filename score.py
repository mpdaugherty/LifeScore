from plugins import plugins
from sendmail import sendmail

score = 0
for plugin in plugins:
    score += plugin.level


message = 'Score for today: {}'.format(score)

for plugin in plugins:
    message += '''

{}:

  Level: {}, Score: {}
'''.format(plugin.name, plugin.level, plugin.score)
    message += plugin.message

print message

sendmail('Life Score: {}'.format(score), message)
