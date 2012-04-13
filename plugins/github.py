from pygithub3 import Github
from subprocess import Popen, PIPE
from config import GITHUB_LOGIN, GITHUB_PASSWORD
from . import Plugin

class GithubPlugin(Plugin):
    score = 0
    message = ''
    base_score = 20
    name = 'GitHub'

    def calculate(self):
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

        self.score = 3 * numForks + 2 * numFollowers + 1 * numRepoWatchers

        self.message = '''
  Number of forks for all your repos: {}
  Number of watchers for your repos:  {}
  Number of followers:                {}
'''.format(numForks, numRepoWatchers, numFollowers)


