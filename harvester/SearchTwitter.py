from time import sleep

import tweepy


class Search:

    def __init__(self, auth, db):
        self.db = db
        self.auth = auth
        self.api = tweepy.API(auth)

    def search_by_keyword(self, para_set):
        # config : keyword : 'String'
        #          max_id
        #          since_id

        # If results only below a specific ID are, set max_id to that ID.
        # else default to no upper limit, start from the most recent tweet matching the search query.
        max_id = -1

        # If results from a specific ID onwards are reqd, set since_id to that ID.
        # else default to no lower limit, go as far back as API allows
        since_id = None if para_set["since_id"] == -1 else para_set["since_id"] #retrieve from the db
        tweets_per_query = 100

        query = para_set["keyword"]

        if max_id <= 0:
            if not since_id:
                new_tweets = self.api.search(q=query, count=tweets_per_query)
            else:
                new_tweets = self.api.search(q=query, count=tweets_per_query, since_id=since_id)
        else:
            if not since_id:
                new_tweets = self.api.search(q=query, count=tweets_per_query, max_id=str(max_id - 1))
            else:
                new_tweets = self.api.search(q=query, count=tweets_per_query, max_id=str(max_id - 1),
                                             since_id=since_id)
        if new_tweets:
            para_set["since_id"] = new_tweets[0].id  # the most recent id are stored, as use as the starting point
            for tweet in new_tweets:

                # sentiment analysis --to be added
                # gender identification --to be added
                self.db.store(tweet)
            max_id = new_tweets[-1].id  # oldest id was used, as we continue retrieving tweets posted even more earlier

        while True:
            if max_id <= 0:
                if not since_id:
                    new_tweets = self.api.search(q=query, count=tweets_per_query)
                else:
                    new_tweets = self.api.search(q=query, count=tweets_per_query, since_id=since_id)
            else:
                if not since_id:
                    new_tweets = self.api.search(q=query, count=tweets_per_query, max_id=str(max_id - 1))
                else:
                    new_tweets = self.api.search(q=query, count=tweets_per_query, max_id=str(max_id - 1),
                                                 since_id=since_id)
            if new_tweets:
                para_set["since_id"] = new_tweets[
                    0].id  # the most recent id are stored, as use as the starting point
                for tweet in new_tweets:
                    # sentiment analysis --to be added
                    # gender identification --to be added
                    self.db.store(tweet)
                max_id = new_tweets[-1].id

        # self.search_by_keyword(para_set)

    def run(self):
        sets = None  # function to fetch the set of para_sets from the DB

        while True:
            for para_set in sets:
                self.search_by_keyword(para_set)
            sleep(500)

