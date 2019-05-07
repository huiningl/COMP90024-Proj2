# Import the necessary methods from tweepy library
from time import sleep

import tweepy

from harvester import Database
from harvester.SearchTwitter import Search
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
access_token = "1083653718581497857-VSyJpAIMjFZaWpg0eJ0M8G409KPkJJ"
access_token_secret = "3SGS9VfU3UvaXw84y0yRULfdIXFDryxIuxpYD83aMMygP"
consumer_key = "DYMWGxnSrF8aG5rISt1oBSBSO"
consumer_secret = "of33s312AnD247lDcCQGHHK6ciAsdVmqqbm58nwiJo9TAp0lj9"

AUS_BOUND_BOX = (113.338953078, -43.6345972634, 153.569469029, -10.6681857235)
geocode = "-28.7,133.9,2127.5km"

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    since_id = None
    max_id = -1
    count_limit = 100
    keywords = ['teat', 'cocaine', 'wuss', 'cumshot', 'hymen', 'japcrap', 'rapey', 'juggalo', "niggard's", 'minority',
                'fingerfucker ', 'crappy', 'pimped', 'sextoys', 'punani', 'shitlist', 'meatbeatter', 'gatorbait',
                'whorehouse', 'whiskey', 'scallywag', 'pikey', 'vulva', 'trannie', 'footfucker', 'papist', 'nutter',
                'felatio', 'assassin', 'tard', 'mastabate', 'sniggered', 'kinky', 'sodomy', 'blowjob', 'nancy',
                'pussyfucker', 'slapper', 'enemy', 'buggered', 'kaffre', 'motherfuckings', 'eatballs', 'jiggabo',
                'dumbbitch', 'fore', 'pornking', 'greaseball', 'skankbitch', 'buttplug', 'conspiracy', 'pussies',
                'mufflikcer', 'buttpirate', 'motherfuckin', 'motherfucking', 'jade', 'deapthroat', 'seppo',
                'skankywhore', 'mothafuckings', 'breastlover', 'goddamn', 'pornography', 'bible', 'intercourse',
                'buttfucker', 'motherfucker', 'bitchslap', 'pindick', 'fastfuck', 'butchdyke', 'fistfucked ',
                'whitetrash', 'poop', 'fuckfest', 'bigbutt', 'beatoff', 'wop', 'penises', 'slanteye', 'slutwear',
                'corruption', 'sissy', 'enema', 'loverocket', 'incest', 'niggardly', 'cocktease', 'molestor',
                'butt fucker', 'hoser', 'itch', 'taig', 'shitface', 'titlicker', 'hiscock', 'skankfuck', 'toilet',
                'jihad', 'masturbate', 'spooge', 'pusy', 'barelylegal', 'cocksucked ', 'ginger', 'beef curtains',
                'clitoris', 'drug', 'shithapens', 'fucking', 'lez', 'hodgie', 'whites', 'jigg', 'dripdick', 'pisser',
                'niggerhole', 'sexwhore', 'nip', 'evl', 'whacker', 'lezz', 'nignog', 'wanker', 'jizz', 'ejaculating ',
                'brea5t', 'snatchpatch', 'bumclat', 'jackoff', 'titlover', 'stringer', 'spankthemonkey', 'sambo',
                'butchbabes', 'fucked', 'fucka', 'niggah', 'areola', 'jugs', 'bullshit', 'naked', 'dirty', 'darkie',
                'dive', 'pussylips', 'shitted', 'cuntfucker', 'cunteyed', 'pissed off', 'clit', 'premature',
                'suckmydick', 'crotchjockey', 'slutting', 'shitting', 'fingerfucked ', 'twat', 'spic', 'floo',
                'mastabater', 'spastic', 'nazi', 'fingerfuck ', 'dicklick', 'gyppy', 'pee', 'dike', 'vagina',
                'bestiality', 'barfface', 'fok', 'clogwog', "niggardliness's", 'tang', 'kumquat', 'whiz', 'cuntfuck',
                'pimpjuic', 'lezbefriends', 'splittail', 'fraud', 'pimpsimp', 'bomb', 'nigerian', 'vomit', 'quickie',
                'beatyourmeat', 'motherfuck', 'insest', 'fuuck', 'psycho', 'niggarding', 'mockie', 'tranny', 'shithead',
                'skumbag', 'lezbe', 'analsex', 'hamas', 'hustler', 'spermhearder', 'triplex', 'masturbating', 'whitey',
                'handjob', 'knob', 'cohee', 'muff diver', 'sexhouse', 'fat', 'abo', 'smackthemonkey', 'slaughter',
                'licker', 'kraut', 'nastyslut', 'mothafucker', 'slave', 'son of a bitch', 'fucck', 'pussypounder',
                'stiffy', 'beastial', 'butt fuckers', 'shitfaced', 'filipina', 'whorefucker', 'dumb', 'tunneloflove',
                'raghead', 'pros', 'killer', 'old bag', 'crotch', 'thirdleg', 'buttmunch', 'pocketpool', 'lovemuscle',
                'whiskydick', 'urine', 'assassination', "israel's", 'gypo', 'wetback', 'sleezeball', 'slutty',
                'mattressprincess', 'sexhound', 'asspuppies', 'libido', 'bong', 'sucker', 'redlight', 'crotchrot',
                'payo', 'cunilingus', 'titties', 'nig', 'jacktheripper', 'jigga', 'bender', 'lickme', 'boobs', 'boob',
                'flatulence', 'pisses', 'screwyou', 'bellend', 'redneck', 'purinapricness', 'fuckers', 'deth',
                'meatrack', 'nlggor', 'ethnic', 'nutfucker', 'felcher', 'funeral', 'dildo', 'mulatto', 'headfuck',
                'balllicker', 'disease', 'window licker', 'goldenshower', 'upthebutt', 'interracial', 'pud', 'pudd',
                'muffdiver', 'primetime', 'niggers', 'cra5h', 'horney', 'cockblock', 'batty boy', 'manhater', 'jigger ',
                'horny', 'slideitin', 'wog', 'feltcher', 'willy', 'sextoy', 'transvestite', 'virginbreaker',
                'junglebunny', 'fatso', 'pearlnecklace', 'orgies', 'sandnigger', 'groe', 'sextogo', 'jigaboo',
                'cocklover', 'clamdiver', 'laid', 'cocksmoker', 'israel', 'lotion', 'muslim', 'crap', 'fuckedup',
                'chin', 'backdoorman', 'weenie', 'canadian', 'bollocks', 'sod off', 'mafia', 'asskisser', 'gipp',
                'honger', 'piker', 'sexpot', 'magicwand', 'wetspot', 'turnon', 'negroid', 'fuck', 'fisting']

    print(len(keywords))
    query = " OR ".join(keywords[:10])
    query.strip()
    print(query)

    # query = 'fuck OR bitch OR bollocks'

    url = "http://localhost:5984"
    db_name = 'new_test'

    db = Database.DB(url, db_name)
    # searchmode = Search(auth, db, geocode)
    # searchmode.run(keywords)

    if max_id <= 0:
        if since_id is None:
            new_tweets = api.search(q=query, count=100, lang='en', geocode=geocode)
        else:
            new_tweets = api.search(q=query, count=100, since_id=since_id, lang='en', geocode=geocode)
    else:
        if since_id is None:
            new_tweets = api.search(q=query, count=100, max_id=str(max_id - 1), lang='en', geocode=geocode)
        else:
            new_tweets = api.search(q=query, count=100, max_id=str(max_id - 1),
                                    since_id=since_id, lang='en', geocode=geocode)
    if new_tweets:
        for tweet in new_tweets:
            print(tweet)
            db.store(tweet._json)

    sleep(20)
