from analytics import create_views, text_tokenizer
from analytics.sentiment import SentimentAnalyzer
from harvester import Database

ALL_DOC_VIEW_FUNC = "function (doc) {\n emit(doc._id, doc); \n}"
HAS_GEO_VIEW_FUNC = "function (doc) {\n  if (doc.geo != null) {\n     emit(doc._id, doc.geo);\n  }\n}"

if __name__ == '__main__':
    url = "http://localhost:5984"
    db_name = "raw_tweets"
    db = Database.DB(url, db_name)
    view = db.database.view(name="_design/analyze/_view/all_view", limit=100)
    # for each in view.rows:
        # print(each.value["text"])
        # sentiment = SentimentAnalyzer.get_scores(each.value)
        # print(sentiment)
    # print(SentimentAnalyzer.get_scores())
    text = "RT @WByng: U.N. human rights office on Wednesday condemned the beheadings of 37 Saudi minority Shi’ite Muslims, following false confessions… @ReclaimAnglesea Wonderful news 😊 "
    # print(text_tokenizer.tokenize())
    print(SentimentAnalyzer.get_scores(text_tokenizer.tokenize(text)))
    print(SentimentAnalyzer.get_scores(text))

    # path = create_views.create_view(url=url, db_name=db_name, view_name="all_view", mapFunc=ALL_DOC_VIEW_FUNC, recreate=True)
    # print(path)
