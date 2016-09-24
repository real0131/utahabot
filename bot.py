from urllib.request import urlopen
from bs4 import BeautifulSoup
import schedule
import time
from twitter import *

t = Twitter(auth=OAuth('778842210317979648-8sLyyVyQX1iS3FD1euWbrU0GoR7KB5q',
                       'x1wmaZhler7l5uYpaXyATNLGBOs2hFuYLOVBhEcrI4yj8',
                       'dKi9X6qmkhzsbNr0NWJz5ch9J',
                       '4EF4rzZDuuUPToCxEaeUMQehff3hciglmqZ1WEY1tBgAKr8Lb2'))

def bot():
    html  = urlopen("http://utaha.moe")
    moe = BeautifulSoup(html)
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
    t.statuses.update(status=tweets)

schedule.every(1).minutes.do(bot)

while True:
    schedule.run_pending()