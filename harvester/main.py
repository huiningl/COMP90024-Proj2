import tweepy
from tweepy import OAuthHandler

import db
import sys

# to be added
from harvester import StreamTwitter
from harvester.SearchTwitter import Search

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# Authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# api is our entry point for most of operations we can do with Twitter
api = tweepy.API(auth)

# connect to db
url = ""
db_name = ""

db = db.DB(url, db_name)


def main(argv):
    if argv == 'stream':
        stream_mode = StreamTwitter.StreamRunner(auth, db)
        stream_mode.run()
    elif argv == 'search':
        search_mode = Search(auth, db)
        search_mode.run()


if __name__ == '__main__':
    main(sys.argv)
