import math

import couchdb

# Connect to couch server
from couchdb import PreconditionFailed

from analytics import sentiment
from analytics.create_views import create_view

url = 'http://127.0.0.1:5984/'
raw_tweets = 'raw_tweets'

# map functions to be added or edited
ALL_DOC_VIEW_FUNC = "function (doc) {\n emit(doc._id, doc); \n}"
ALL_TEXT_VIEW_FUNC = "function (doc) {\n if (doc.text != null) {\n  emit(doc._id, doc.text);\n }\n}"
HAS_GEO_VIEW_FUNC = "function (doc) {\n  if (doc.geo != null) {\n     emit(doc._id, doc.geo);\n  }\n}"

# connect to couch server / raw_tweets db
couch_server = couchdb.Server(url=url)
raw_tweets_db = couch_server[raw_tweets]

# create views
view_path = create_view(url=url, db_name=raw_tweets, view_name="all_doc_view", mapFunc=ALL_DOC_VIEW_FUNC, overwrite=True)

# create new databases to store processed data
# try:
#     sentiment_db = couch_server.create('sentiment')
# except PreconditionFailed:
#     sentiment_db = couch_server['sentiment']

num_docs = raw_tweets_db.info()["doc_count"]
batch_size = 10000
iters = math.ceil(num_docs/batch_size)


# add sentiment attribute
for i in range(iters):
    batch_docs = raw_tweets_db.view(view_path, limit=batch_size, skip=i*batch_size)
    for row in batch_docs.rows:
        if 'sentiment' not in row.value.keys():
            sentiment_score = sentiment.SentimentAnalyzer.get_scores(row.value['text'])
            row.value['sentiment'] = sentiment_score
            raw_tweets_db.save(row.value)
            print(row.value)
