import couchdb
import json


class StoreTweets:

    def __init__(self, database):
        try:
            self.server = couchdb.Server(url="http://localhost:5984/")
            self.database = self.server.create(database)
        except Exception:
            self.database = self.server[database]

    def store_tweet(self, tweet):
        if isinstance(tweet, dict):
            temp_tweet = tweet
        else:
            temp_tweet = json.loads(tweet)

        record = self.database.get(temp_tweet["id_str"])
        if record is None:
            self.database.save(record)
        else:
            print("duplicates")