from collections import Counter

import vincent

class HashtagProcessor:

    def __init__(self, source_db, view_path, results_db):
        self.view_path = view_path
        self.source_db = source_db
        self.results_db = results_db

    def order_dict(self, dict_items):
        sorted_dict = sorted(dict_items, reverse=True, key=lambda x: x[-1])
        return sorted_dict

    def plot(self, dict_obj):
        pass
        # count_terms_only = Counter().update(dict_obj)
        # top10 = count_terms_only.most_common(10)
        # hashtag, occurrences = zip(*top10)
        # data = {'y': occurrences, 'x': hashtag}
        # bar_chart = vincent.Bar(data, iter_idx='x')
        # bar_chart.to_json('sample.json')

    def run(self):
        view = self.source_db.iterview(name=self.view_path, batch=10000)
        hashtag_occurrence ={}
        for row in view:
            for each in row.value:
                if each['text'].lower() not in hashtag_occurrence.keys():
                    hashtag_occurrence[each['text']] = 1
                else:
                    hashtag_occurrence[each['text']] += 1

        ordered_list = self.order_dict(hashtag_occurrence.items())
        # self.plot(hashtag_occurrence)
        record = {"_id": "trending_hashtags", "data": ordered_list}
        self.results_db.save(record)  # store the results to couchdb

