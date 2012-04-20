from pygithub3 import Github
from config import GITHUB_LOGIN, GITHUB_PASSWORD
from . import Plugin

class GithubPlugin(Plugin):
    score = 0
    numForks = 0
    numFollowers = 0
    numRepoWatchers = 0
    message = ''
    base_score = 20
    name = 'GitHub'

    def calculate(self):
        try:
            # API Login
            gh = Github(login=GITHUB_LOGIN, password=GITHUB_PASSWORD)

            user = gh.users.get()
            repos = gh.repos.list().all()

            self.numFollowers = user.followers

            numForks = 0
            numRepoWatchers = 0
            for repo in repos:
                numForks += repo.forks
                numRepoWatchers += repo.watchers

            self.numForks = numForks
            self.numRepoWatchers = numRepoWatcher
        except:
            # We can use the old data from the datastore to still calculate a score
            self.updated = False

        self.score = 3 * self.numForks + 2 * self.numFollowers + 1 * self.numRepoWatchers

        self.message = '''
  Number of forks for all your repos: {}
  Number of watchers for your repos:  {}
  Number of followers:                {}
'''.format(self.numForks, self.numRepoWatchers, self.numFollowers)


