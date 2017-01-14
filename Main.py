# 3.5
# pip install -r requirements.txt

import config
import praw
import time  # need more time
import urllib.request

reddit = praw.Reddit(client_id=config.reddit_client_id,
                     client_secret=config.reddit_client_secret,
                     password=config.reddit_password,
                     user_agent=config.reddit_user_agent,
                     username=config.reddit_username)

print('Trying to log in...')
print('Logged in as:' + reddit.user.me())

class request:
    Hearthstone = 'wtcg'
    Overwatch = 'Pro'
    Starcraft2 = 'sc2'
    Warcraft = 'WoW'
    Diablo = 'd3'
    HOTS = 'heroes'
    def get_patchnotes(self, game):
        print('Getting patchnotes for ' + game + ' in language english')
        url = 'https://us.battle.net/connect/en/app/%s/patch-notes?productType=%s', game, game

        headers = {'User-Agent': 'Battle.net/1.0.8.4217'}
        req = urllib.Request('www.example.com', None, headers)
        html = urllib.urlopen(req).read()
        print(html)

def main_timer():
    print('handle timer')

while True:
    request.get_patchnotes('live')
    time.sleep(config.timerInterval)


