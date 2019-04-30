import tweepy


class Search:

    def __init__(self, auth, db):
        self.db = db
        self.auth = auth
        self.api = tweepy.API(auth)

    def run(self):
        pass
