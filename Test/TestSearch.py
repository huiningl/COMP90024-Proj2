# Import the necessary methods from tweepy library
from time import sleep

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
access_token = "1117988833436397568-vtgxrL2x0lhJvcPi8tKuRLntAKVqGB"
access_token_secret = "Uwioa9O9RNsA5JygK0bHX84UxsOKiMF283OQpeporN334"
consumer_key = "IzabACqOqQ2XNshVSjA1lRWHp"
consumer_secret = "rzVQDBOggdsO5NsKj6rzKYCRIMEI94t9Ka2XlkICNxg3gnt63i"

AUS_BOUND_BOX = (113.338953078, -43.6345972634, 153.569469029, -10.6681857235)

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    since_id = None
    max_id = -1
    count_limit = 100
    query = 'fuckyou'

    while True:
        if max_id <= 0:
            if not since_id:
                new_tweets = api.search(q=query, count=count_limit, lang='en')
            else:
                new_tweets = api.search(q=query, count=count_limit, since_id=since_id)
        else:
            if not since_id:
                new_tweets = api.search(q=query, count=count_limit, max_id=str(max_id - 1))
            else:
                new_tweets = api.search(q=query, count=count_limit, max_id=str(max_id - 1),
                                        since_id=since_id)

        if new_tweets:
            i = 1
            for tweet in new_tweets:

                print(int(new_tweets[i+1]._json["id"]) - int(new_tweets[i]._json["id"]))
                i += 1

            max_id = new_tweets[-1].id

        sleep(600)

