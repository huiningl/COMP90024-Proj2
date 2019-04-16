import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import harvester.api

# derived from <https://gist.github.com/graydon/11198540>
AUS_BOUND_BOX = (113.338953078, -43.6345972634, 153.569469029, -10.6681857235)


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


class MyListener (StreamListener):
    """
    In case we want to “keep the connection open”, and gather all
    the upcoming tweets about a particular event, the streaming API
    is what we need. We need to extend the StreamListener() to
    customise the way we process the incoming data.
    """
    def on_data(self, raw_data):
        pass

    def on_status(self, status):
        pass

    def on_error(self, status_code):
        pass


class SteamRunner:

    def run(self):
        twitter_stream = Stream(auth, MyListener())
        twitter_stream.filter(locations=AUS_BOUND_BOX)



