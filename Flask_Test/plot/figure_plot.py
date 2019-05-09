from collections import Counter

import couchdb
import matplotlib.pyplot as plt
import vincent
from vincent import AxisProperties, PropertySet, ValueRef


class Plotter:
    def __init__(self):
        self.url = 'http://localhost:5984'
        self.couch_server = couchdb.Server(url=self.url)

    def bar_plot(self, doc_id, db_name):
        db = self.couch_server[db_name]
        data = db.get(doc_id)

        plt.clf()
        fig = plt.figure()
        for each in data['data']:
            plt.plot(each['coordinates'])
        plt.show()
        fig.savefig('./static/images/figures/sample.png')


    def other_plot(self):
        pass