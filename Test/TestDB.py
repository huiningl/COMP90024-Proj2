from harvester import Database


if __name__ == '__main__':
    url = "http://localhost:5984"
    db_name = "tweet_test"
    view = "view"
    db = Database.DB(url, db_name)
    x = db.database.get("1123896368244961282")
