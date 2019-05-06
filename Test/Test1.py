# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
from harvester import Database

access_token = "1083653718581497857-VSyJpAIMjFZaWpg0eJ0M8G409KPkJJ"
access_token_secret = "3SGS9VfU3UvaXw84y0yRULfdIXFDryxIuxpYD83aMMygP"
consumer_key = "DYMWGxnSrF8aG5rISt1oBSBSO"
consumer_secret = "of33s312AnD247lDcCQGHHK6ciAsdVmqqbm58nwiJo9TAp0lj9"

AUS_BOUND_BOX = (113.338953078, -43.6345972634, 153.569469029, -10.6681857235)


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def __init__(self, auth, db):
        self.auth = auth
        self.db = db

    def on_data(self, data):
        # self.file.writelines(json.dumps(data, ensure_ascii=False))
        # write_tweets(self.file, data, self.count)
        print(self.db.queue)
        self.db.queue.put(data)
        return True

    def on_status(self, status):
        print("status gives data: ", status)

    def on_error(self, status_code):
        print(status_code)


def write_tweets(file, data, count):
    if count == 1:
        file.write('{ "rows":[\n')

    tweet = json.loads(data)
    jsonStr = json.dumps(tweet, ensure_ascii=False)
    file.write(jsonStr + ',\n')

    if count == 100:
        file.write("]}\n")
    if count > 100:
        exit(0)


if __name__ == '__main__':
    keywords = ['teat', 'shithappens', 'assjockey', 'asscowboy']
    url = "http://localhost:5984"
    db_name = 'new_test'
    db = Database.DB(url, db_name)
    # This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    l = StdOutListener(auth, db)
    stream = Stream(auth, l)

# This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=keywords, locations=AUS_BOUND_BOX)
