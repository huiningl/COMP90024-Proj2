import json
import genderizer
import naiveBayesClassifier.ExceptionNotSeen

from analytics import gender

if __name__ == '__main__':
    with open('sample_tweets.json', 'r', encoding='utf-8') as f:
        tweets = json.load(f)
        for tweet in tweets["rows"]:
            predict = gender.GenderDector.infer_gender(tweet["value"]["doc"]["text"])
            print(predict)