import couchdb
import collections
import matplotlib.pylab as plt
import numpy as np
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure


if __name__ == '__main__':
    couch_server = couchdb.Server(url='http://10.9.131.221:5984')
    source_db = couch_server['test_db']
    data = source_db.get('time_distribution')
    original_data = data['data']
    modified_data = original_data
    modified_data['24'] = modified_data['0']
    del modified_data['0']
    print('modified_data: ',modified_data)

# TODO: Sort Key
    s_data = {}
    for k,v in modified_data.items():
        nk_list = []
        nk = int(k)
        nk_list.append(nk)
        for n in nk_list:
            s_data[n] = v
    print(s_data)
    od = collections.OrderedDict(sorted(s_data.items()))
    print('od: ',od)
    sorted_data = {}
    for k,v in od.items():
        sorted_data[k]=v
    print(sorted_data)
    r_data = {}
    for k,v in sorted_data.items():
        nk_list = []
        nk = str(k)
        nk_list.append(nk)
        for n in nk_list:
            r_data[n] = v
    print("r_data",r_data)

    time = []
    num = []
    for k,v in r_data.items():
        time.append(k)
        num.append(v)
    print("time:",time)
    print(num)
    rate_list = []
    suml = sum(num)
    for n in num:
        rate = n/suml
        rate_list.append(rate)
    print("rate_list: ",rate_list)

    TOOLTIPS =[("time","@x"),("rate","@y")]

    p = figure(x_range=time, plot_height=400, title="Time Distribution",
               toolbar_location=None,tools="hover", tooltips=TOOLTIPS)

    #p.vbar(x=time, top=num, width=0.9)
    p.line(time,rate_list,line_width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    show(p)











    # data = source_db.get('sentiment_time')
    # original_data = data['data']
    # time_list = list(original_data.keys())
    # print("time_list: " ,time_list)
    # print("original_data: ",original_data)
    #
    # sorted_original_data = {}
    # for time, info in original_data.items():
    #     sorted_item = {}
    #     sorted_item['neg'] = info['neg']
    #     sorted_item['neu'] = info['neu']
    #     sorted_item['pos'] = info['pos']
    #     # sorted_original_data = list(zip(time,sorted_item))
    #     sorted_original_data[time] = sorted_item
    # print("sorted_original_data", sorted_original_data)
    #
    # dict_list = list(sorted_original_data.values())
    # print("dict_list: ", dict_list)
    # bar_data_dict = {}
    # bar_data_dict['time'] = time_list
    # bar_data_dict['neg'] = []
    # bar_data_dict['neu'] = []
    # bar_data_dict['pos'] = []
    # for time,info in sorted_original_data.items():
    #     for k,v in info.items():
    #         bar_data_dict_item = {}
    #         bar_data_dict_item[k] = v
    #         if k == 'neg':
    #             bar_data_dict['neg'].append(v)
    #         if k == 'neu':
    #             bar_data_dict['neu'].append(v)
    #         if k == 'pos':
    #             bar_data_dict['pos'].append(v)
    # print("bar_data_dict: ", bar_data_dict)
    # counts = sum(zip(bar_data_dict['neg'], bar_data_dict['neu'], bar_data_dict['pos']), ())
    # print("counts: ",counts)
    #
    # sentiment_list = list(dict_list[0].keys())
    # print(sentiment_list)
    # x = [(time, sentiment) for time in time_list for sentiment in sentiment_list]
    # print("xlabel: ", x)
    #
    # source = ColumnDataSource(data = dict(x=x, counts=counts))
    #
    # p = figure(x_range=FactorRange(*x), plot_height=250, title="Sentiment Time",
    #            toolbar_location=None, tools="")
    # p.vbar(x='x', top='counts', width=0.9, source=source)
    # # p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white")
    #        # fill_color=factor_cmap('x', palette=palette, factors=sentiment_list, start=1, end=2))
    #
    # p.y_range.start = 0
    # p.x_range.range_padding = 0.1
    # p.xaxis.major_label_orientation = 1
    # p.xgrid.grid_line_color = None
    #
    #
    #
    # show(p)









    # sorted_dict_list = []
    # for item in dict_list:
    #     sorted_dict_list.append(sorted(item.items(), key=lambda x: x[0]))
    # print("sorted: ",sorted_dict_list)
    #
    # sentiment_list = []
    # for item in sorted_dict_list[0]:
    #     sentiment_list.append(item)
    # print("sentiment_list: ",sentiment_list)
    # xlabel = [(time, sentiment) for time in time_list for sentiment in sentiment_list]
    # print("xlabel: ", xlabel)
    #



    # top10 = sorted(data['data'].items(), reverse=True, key=lambda x: x[-1])[:10]
    # dict_top10 = dict(top10)
    # print(dict_top10)
    # hashTags = list(dict_top10.keys())
    # occurrences = list(dict_top10.values())
    # print(hashTags)
    # print(occurrences)
    # count_terms_only = Counter()
    # count_terms_only.update(data['data'])
    # top10 = count_terms_only.most_common(10)
    # hashtag, occurrences = zip(*top10)
    #
    # N = 10
    # ind = np.arrange(N)
    # width = 0.2
    #
    # p = plt.bar(ind, occurrences, width, bottom=None)
    #
    # plt.ylabel('Occurences')
    # plt.xlabel('Hashtags')
    # plt.title('Hashtag Occurrence')