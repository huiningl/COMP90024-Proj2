import tweepy
from tweepy import OAuthHandler

# to be added
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# Authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# api is our entry point for most of operations we can do with Twitter
api = tweepy.API(auth)
