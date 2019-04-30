from tweepy import Stream
from tweepy.streaming import StreamListener

# derived from <https://gist.github.com/graydon/11198540>
AUS_BOUND_BOX = (113.338953078, -43.6345972634, 153.569469029, -10.6681857235)


class MyListener (StreamListener):
    """
    In case we want to “keep the connection open”, and gather all
    the upcoming tweets about a particular event, the streaming API
    is what we need. We need to extend the StreamListener() to
    customise the way we process the incoming data.
    """
    def __init__(self, db):
        self.db = db

    def on_data(self, raw_data):
        self.db.store(raw_data)
        print(raw_data)

    def on_status(self, status):
        print(status)

    def on_error(self, status_code):
        print(status_code)


class StreamRunner:
    def __init__(self, auth, db):
        self.db = db
        self.auth = auth

    def run(self):
        twitter_stream = Stream(self.auth, MyListener(self.db))
        twitter_stream.filter(locations=list(AUS_BOUND_BOX))



