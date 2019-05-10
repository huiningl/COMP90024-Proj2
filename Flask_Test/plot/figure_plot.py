from collections import Counter

import couchdb
import matplotlib.pyplot as plt
import numpy as np
import vincent
from vincent import AxisProperties, PropertySet, ValueRef


class Plotter:
    def __init__(self):
        # self.url = 'http://localhost:5984'
        self.url = 'http://10.9.131.64:5984'
        self.couch_server = couchdb.Server(url=self.url)

    def bar_plot(self, doc_id, db_name):
        db = self.couch_server[db_name]
        data = db.get(doc_id)
        top10 = sorted(data['data'].itmes(), reverse=True, key=lambda x: x[-1])[:10]
        # count_terms_only = Counter()
        # count_terms_only.update(data['data'])
        # top10 = count_terms_only.most_common(10)
        #hashtag, occurrences = zip(*top10)
        dict_top10 = dict(top10)
        hashTags = list(dict_top10.keys())
        occurrences = list(dict_top10.values())
        fig = plt.figure()
        N = 10
        ind = np.arrange(N)
        width = 0.2

        p = plt.bar(ind,occurrences,width,bottom=None)

        plt.ylabel('Occurences')
        plt.xlabel('Hashtags')
        plt.title('Hashtag Occurrence')
        plt.xticks(ind,hashTags)
        plt.yticks(np.arrange(0,100,10))

        # plt.clf()
        # # an empty figure with no axes
        # fig = plt.figure()
        # for each in data['data']:
        #     plt.plot(each['coordinates'])

        plt.show()
        fig.savefig('./static/images/figures/hashtag.png')


    def other_plot(self):
        pass


# count_terms_only = Counter()
# count_terms_only.update(hashtag_occurrence)
# top10 = count_terms_only.most_common(10)
# hashtag, occurrences = zip(*top10)