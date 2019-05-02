import tweepy
from tweepy import OAuthHandler

import sys

# to be added
from harvester import StreamTwitter, Database
from harvester.SearchTwitter import Search

access_token = "1117988833436397568-vtgxrL2x0lhJvcPi8tKuRLntAKVqGB"
access_token_secret = "Uwioa9O9RNsA5JygK0bHX84UxsOKiMF283OQpeporN334"
consumer_key = "IzabACqOqQ2XNshVSjA1lRWHp"
consumer_secret = "rzVQDBOggdsO5NsKj6rzKYCRIMEI94t9Ka2XlkICNxg3gnt63i"

# Authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# api is our entry point for most of operations we can do with Twitter
# api = tweepy.API(auth)

# connect to db
url = "http://localhost:5984"
db_name = "tweet_test"

db = Database.DB(url, db_name)


def main(argv):
    if argv == 'stream':
        stream_mode = StreamTwitter.StreamRunner(auth, db)
        stream_mode.run()
    elif argv == 'search':
        search_mode = Search(auth, db)
        search_mode.run()


if __name__ == '__main__':
    main("stream")
    # main(sys.argv)
