# Import the necessary methods from tweepy library
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


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def __init__(self, file):
        self.count = 1
        self.file = file

    def on_data(self, data):
        # self.file.writelines(json.dumps(data, ensure_ascii=False))
        write_tweets(self.file, data, self.count)
        print(self.count, " ", data)
        self.count += 1
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

    # This handles Twitter authetification and the connection to Twitter Streaming API
    with open("tweets.json", mode="w", encoding='utf-8') as f:
        # f.writelines('{ "rows":[\n')
        l = StdOutListener(f)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)

        # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
        stream.filter(locations=AUS_BOUND_BOX)
