import couchdb
from couchdb import json, PreconditionFailed


class DB:

    def __init__(self, url, db_name):
        self.server = couchdb.Server(url)
        try:
            self.database = self.server.create(db_name)
        except PreconditionFailed:
            self.database = self.server[db_name]

    def store(self, data):
        if isinstance(data, dict):
            temp_tweet = data
        else:
            temp_tweet = json.loads(data)
        record = self.database.get(temp_tweet["id_str"])
        if record is None:
            self.database.save(record)
        else:
            print("duplicates")
