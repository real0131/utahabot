import urllib.request import urlopen
from bs4 import Beautifulsoup
import schedule
import time
from twitter import *

t = Twitter(auth=OAuth('',
                       '',
                       '',
                       ''))

def bot():
    html  = urlopen("http://utaha.moe")
    moe = Beautifulsoup(html)
    header = moe.find('head').findAll('meta',{'name' : 'description'})
    now = time.localtime()

    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    tweets = ""

    tweets += str(s) + "\n" + "현재 utaha.moe는?" + "\n"
    if not header:
        tweets += "\n" + "퍼퍼펑"
    else :
        tweets += "\n" + "정상작동중"
    tweets += "\n" + "http://utaha.moe"

schedule.every(30).minutes.do(bot)

while True:
    schedule.run_pending()