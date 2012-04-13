from pygithub3 import Github
from subprocess import Popen, PIPE
from config import GITHUB_LOGIN, GITHUB_PASSWORD

class GithubPlugin(object):
    score = 0
    message = ''

    def __init__(self):
        # API Login
        gh = Github(login=GITHUB_LOGIN, password=GITHUB_PASSWORD)

        user = gh.users.get()
        repos = gh.repos.list().all()

        numFollowers = user.followers

        numForks = 0
        numRepoWatchers = 0
        for repo in repos:
            numForks += repo.forks
            numRepoWatchers += repo.watchers

        self.score = 5 * numForks + 5 * numFollowers + 3 * numRepoWatchers

        self.message = '''
  Number of forks for all your repos: {}
  Number of watchers for  your repos: {}
  Number of followers:                {}
'''.format(numForks, numRepoWatchers, numFollowers)

ghp = GithubPlugin()

print ghp.message

