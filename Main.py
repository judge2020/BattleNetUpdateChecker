# 3.5
# pip install -r requirements.txt

import config
import praw
import time  # need more time
import urllib.request
from bs4 import BeautifulSoup
import html2text

reddit = praw.Reddit(client_id=config.reddit_client_id,
                     client_secret=config.reddit_client_secret,
                     password=config.reddit_password,
                     user_agent=config.reddit_user_agent,
                     username=config.reddit_username)

print('Trying to log in...')
print('Logged in as:' + reddit.user.me().name)


class Handler:
    Hearthstone = 'wtcg'
    Overwatch = 'Pro'
    Starcraft2 = 'sc2'
    Warcraft = 'WoW'
    Diablo = 'd3'
    HOTS = 'heroes'

    def get_patchnotes_raw(game):
        print('Getting patch notes for ' + game + ' in language english')
        url = 'https://us.battle.net/connect/en/app/' + game + '/patch-notes?productType=' + game

        headers = {'User-Agent': 'Battle.net/1.0.8.4217'}
        req = urllib.request.Request(url, None, headers)
        html = urllib.request.urlopen(req).read()
        return html

    def markupify(str):
        return html2text.html2text(str)

    def get_patch_notes_maincontent(str):
        mySoup = BeautifulSoup(str, 'html.parser')
        return mySoup.find('div', {"class":"patch-notes-interior"})

    def fix(byte):
        return byte.decode('utf8')

    def get_patchnotes_md(self, game):
        raw = self.get_patchnotes_raw(game)
        fixed = self.fix(raw) + '</script>'
        mc = self.get_patch_notes_maincontent(raw)
        return self.markupify(mc)


def main_timer():
    print('handle timer')


while True:
    print(Handler.get_patchnotes_md(Handler, Handler.Hearthstone))
    time.sleep(config.timerInterval)
