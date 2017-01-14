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
print('Logged in as:' + reddit.user.me().name)


class Handler:
    Hearthstone = 'wtcg'
    Overwatch = 'Pro'
    Starcraft2 = 'sc2'
    Warcraft = 'WoW'
    Diablo = 'd3'
    HOTS = 'heroes'

    def get_patchnotes(self, game):
        print('Getting patch notes for ' + game + ' in language english')
        url = 'https://us.battle.net/connect/en/app/' + game + '/patch-notes?productType=' + game

        headers = {'User-Agent': 'Battle.net/1.0.8.4217'}
        req = urllib.request.Request(url, None, headers)
        html = urllib.request.urlopen(req).read()
        print(self.parse(str))


    def parse(str):
        words = str.split()
        for word in words:
            word.replace(r'\r\n', '')
            word.replace(r'\xe2\x80\x99', "'")

        return words


def main_timer():
    print('handle timer')


while True:
    #Handler.get_patchnotes(Handler.Hearthstone)
    Handler.parse(r'<p><strong>Hearthstone Update \xe2\x80\x93 11/29/16</strong></p>\r\n<p><strong>Patch 7.0.0.15590 </strong></p>\r\n<p></p>\r\n<p>The Tavern\xe2\x80\x99s never been more rough and tumble! This Hearthstone update paves the way for the arrival of The Mean Streets of Gadgetzan, Hearthstone\xe2\x80\x99s latest expansion. Join three crime families as they vie for power in the back alleys of Gadgetzan with all-new Tri-Class cards, and a gritty game board featuring each of the city\xe2\x80\x99s districts. This update also adds several swanky new card backs and fixes some bugs.</p>\r\n<p></p>\r\n<p>Read on for details!</p>\r\n<p></p>\r\n<p><strong>The Mean Streets of Gadgetzan</strong></p>\r\n<p></p>\r\n<ul>\r\n<li>Grab your shiniest brass knuckles and get ready to rumble on The Mean Streets of Gadgetzan. Hearthstone\xe2\x80\x99s latest expansion will be available beginning December 1<sup>st</sup> and includes:\r\n<ul style="list-style-type:circle;">\r\n<li>132 all-new cards.</li>\r\n<li>Tri-Class cards - special neutral minions that break the rules to be included in the decks of all three classes associated with each family:\r\n')
    time.sleep(config.timerInterval)
