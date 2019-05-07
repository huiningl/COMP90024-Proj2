import json

import tweepy
from tweepy import OAuthHandler
import sys
import multiprocessing

from harvester import StreamTwitter, Database
from harvester.SearchTwitter import Search


def main(argv):
    with open("./harvester/harvester_config.json", 'r') as template:
        data = json.load(template)
        Groups = data["Groups"]
        new_groups = keyword_distribution(Groups)
        url = data["db_url"]
        db_name = data["db_name"]
        geocode = data["geocode"]

        # connect to db
        db = Database.DB(url, db_name)

        i = int(argv[2])
        if argv[1] == 'stream' and 0 < i <= len(new_groups):
            print("Now start Streaming...")
            stream_mode = StreamTwitter.StreamRunner(db)
            stream_mode.run(new_groups[i-1])
        elif argv[1] == 'search' and 0 < i <= len(new_groups):
            print("Now start Searching...")
            search_mode = Search(db, geocode)
            search_mode.run(new_groups[i-1])
        else:
            print("Incorrect or lack of Harvesting mode!")

            # for convenient testing
            print("Now start Searching...")
            # search_mode = Search(auth, db, geocode)
            # search_mode.run(keywords)


def keyword_distribution(Groups):
    with open("./harvester/offensive_words_corpus.txt", 'r') as corpus:
        indicator = 0
        group_size = len(Groups)
        for keyword in corpus:
            Groups[indicator % group_size]["keywords"].append(keyword[:-1])
            indicator += 1
    return Groups


if __name__ == '__main__':
    # main("stream")
    # main(sys.argv)

    # for testing
    main(["", "search", "4"])
