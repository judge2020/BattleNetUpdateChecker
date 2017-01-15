# 3.5
# pip install -r requirements.txt

import config
import praw
import time  # need more time
import urllib.request
from bs4 import BeautifulSoup
import pypandoc

reddit = praw.Reddit(client_id=config.reddit_client_id,
                     client_secret=config.reddit_client_secret,
                     password=config.reddit_password,
                     user_agent=config.reddit_user_agent,
                     username=config.reddit_username)

print('Trying to log in...')
print('Logged in as:' + reddit.user.me().name)


class MDhandler:
    Hearthstone = 'wtcg'
    Overwatch = 'Pro'
    Starcraft2 = 'sc2'
    Warcraft = 'WoW'
    Diablo = 'd3'
    HOTS = 'heroes'

    def get_patchnotes_raw(game):
        url = 'https://us.battle.net/connect/en/app/' + game + '/patch-notes?productType=' + game

        headers = {'User-Agent': 'Battle.net/1.0.8.4217'}
        req = urllib.request.Request(url, None, headers)
        html = urllib.request.urlopen(req).read()
        return html

    def markupify(str):
        md = pypandoc.convert_text(str, 'md', format='html')
        return md

    def get_patch_notes_maincontent(str):
        mySoup = BeautifulSoup(str, 'html.parser')
        stuff = mySoup.find('div', {"class": "patch-notes-interior"})
        return stuff

    def fix(byte):
        str = byte.decode('utf8')
        str = str.strip('\n')
        return str

    def get_patchnotes_md(self, game):
        raw = self.get_patchnotes_raw(game)
        fixed = self.fix(raw)
        mc = self.get_patch_notes_maincontent(raw)
        md = self.markupify(mc)
        md = md.replace('<div class="patch-notes-interior">', '')
        md = md.replace('</div>', '')
        return md

    def get_patch_version(self, game):
        raw = self.get_patchnotes_raw(game)
        fixed = self.fix(raw)
        mc = self.get_patch_notes_maincontent(fixed)
        striped = str(mc).split('\n')
        return striped[1]




def main_timer():
    Last_ver = open('latest.txt', 'r')
    ver = MDhandler.get_patch_version(MDhandler, MDhandler.Hearthstone)
    if (ver in Last_ver.read()):
        Last_ver.close()
        pass
    else:
        try:
            Last_ver.close()
            Last_ver = open('latest.txt', 'w')
            print('New update: ' + ver)
            Last_ver.write(ver)
            bnet = reddit.subreddit('Hearthstone')
            bnet.submit('Hearthstone Update ' + time.strftime("%m/%d/%Y"),
                        MDhandler.get_patchnotes_md(MDhandler, MDhandler.Hearthstone))
        except:
            print('err')
    Last_ver.close()

    Last_verOW = open('latest-OW.txt', 'r')
    ver = MDhandler.get_patch_version(MDhandler, MDhandler.Overwatch)
    if (ver in Last_verOW.read()):
        Last_verOW.close()
        pass
    else:
        try:
            Last_verOW.close()
            Last_verOW = open('latest-OW.txt', 'w')
            print('New update OW: ' + ver)
            Last_verOW.write(ver)
            bnet = reddit.subreddit('Overwatch')
            bnet.submit('Overwatch Update ' + time.strftime("%m/%d/%Y"),
                        MDhandler.get_patchnotes_md(MDhandler, MDhandler.Overwatch))
        except:
            print('err OW')
    Last_ver.close()


try:
    pypandoc._ensure_pandoc_path()
except:
    # need 2 download pandoc
    pypandoc.download_pandoc()

while True:
    main_timer()
    time.sleep(config.timerInterval)
