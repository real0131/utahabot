#-*- coding: utf-8 -*-

#import urllib2 (for python 2)
from urllib.request import urlopen
from bs4 import BeautifulSoup
import schedule
import time
from twitter import *

t = Twitter(auth=OAuth('Access Token',
                       'Access Token Secret',
                       'Consumer Key',
                       'Consumer Key Secret'))
isServer = True

def bot():
    try:
        global isServer
        #html = urllib2.urlopen("http://utaha.moe") (for python 2)
        html = urlopen("http://utaha.moe")
        moe = BeautifulSoup(html)
        header = moe.find('head').findAll('meta', {'name': 'description'})
        if isServer is False:
            recover()
            isServer = True
    except:
        if isServer is True:
            tweet()
            isServer = False
        else:
            return 0

def tweet():
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    tweets = ""
    tweets += str(s) + "\n" + "현재 utaha.moe는?" + "\n"
    tweets += "\n" + "퍼퍼펑"
    tweets += "\n" + "http://utaha.moe"
    t.statuses.update(status=tweets)
def recover():
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    tweets = ""
    tweets += str(s) + "\n" + "현재 utaha.moe는?" + "\n"
    tweets += "\n" + "복구"
    tweets += "\n" + "http://utaha.moe"
    t.statuses.update(status=tweets)

schedule.every(1).minutes.do(bot)

while True:
    schedule.run_pending()
