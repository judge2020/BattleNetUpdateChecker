# 3.5
# pip install -r requirements.txt

import config
import praw
import time  # need more time
import urllib.request
from bs4 import BeautifulSoup
import pypandoc
import sys




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



class timerHandler:
    interv = 1

    def post_reddit(self, subreddit, title, content):
        reddit = praw.Reddit(client_id=config.reddit_client_id,
                             client_secret=config.reddit_client_secret,
                             password=config.reddit_password,
                             user_agent=config.reddit_user_agent,
                             username=config.reddit_username)

        print('Trying to log in to reddit...')
        print('Logged in as:' + reddit.user.me().name)
        DeSubreddit = reddit.subreddit(subreddit)
        DeSubreddit.submit(title, content)
        return


    def CheckHS(self):
        Last_ver = open('latest.txt', 'r', encoding='utf8')
        read = Last_ver.read().strip('\n')
        ver = MDhandler.get_patch_version(MDhandler, MDhandler.Hearthstone)
        if ver == read:
            Last_ver.close()
            return
        else:
            Last_ver.close()
            Last_ver = open('latest.txt', 'w', encoding='utf8')
            print('New update: ' + ver)
            Last_ver.write(ver)
            Last_ver.close()
            self.post_reddit(self, 'Hearthstone', 'Hearthstone Update for ' + time.strftime("%m/%d/%Y"), MDhandler.get_patchnotes_md(MDhandler, MDhandler.Hearthstone))

        return

    def CheckOW(self):
        Last_verOW = open('latest-OW.txt', 'r', encoding='utf8')
        owRead = Last_verOW.read().strip('\n')
        ver = MDhandler.get_patch_version(MDhandler, MDhandler.Overwatch)
        if ver == owRead:
            Last_verOW.close()
            return
        else:
            Last_verOW.close()
            Last_verOW = open('latest-OW.txt', 'w', encoding='utf8')
            print('New update OW: ' + ver)
            Last_verOW.write(ver)
            Last_verOW.close()
            self.post_reddit(self, 'Overwatch', 'Overwatch update for ' + time.strftime("%m/%d/%Y"), MDhandler.get_patchnotes_md(MDhandler, MDhandler.Overwatch))
        return


    def mainTimer(self):
        try:
            if self.interv == 1:
                self.CheckHS(self)
                self.interv += 1
                pass

            elif self.interv == 2:
                self.CheckOW(self)
                self.interv == 1
                pass
        except:
            print('Unknown exception! '+ str(sys.exc_info()[0]))



try:
    pypandoc._ensure_pandoc_path()
except:
    # need 2 download pandoc
    pypandoc.download_pandoc()

while True:
    timerHandler.mainTimer(timerHandler)
    time.sleep(config.timerInterval)
