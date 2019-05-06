from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAnalyzer:

    def get_scores(self, sentence):
        try:
            analyzer = SentimentIntensityAnalyzer()
            temp_scores = analyzer.polarity_scores(sentence)
            self.count_sentiment(temp_scores)
        except Exception as e:
            pass

    def count_sentiment(self, temp_scores):
        pass