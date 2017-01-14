# 3.5
# pip install -r requirements.txt

import config
import praw
import time #need more time
from urllib.request import urlopen

reddit = praw.Reddit(client_id=config.reddit_client_id,
                     client_secret=config.reddit_client_secret,
                     password=config.reddit_password,
                     user_agent=config.reddit_user_agent,
                     username=config.reddit_username)

print('Trying to log in...')
print('Logged in as:' + reddit.user.me())

def main_timer():
    print('handle timer')

while True:
    main_timer()
    time.sleep(config.timerInterval)