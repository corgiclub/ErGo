import requests
import re
import io
import PIL.Image as Img
import imghdr
from bs4 import BeautifulSoup


r = requests.get(url='https://mp.sohu.com/profile?xpt=OTk3YTMwMWYtOGNmZS00MzMxLWEzYjktOGE4MjdjZjgwMGI0&_f=index_pagemp_1&spm=smpc.content.author.2.1606837412545xZ4rTlY')

print(r.status_code)

bs = BeautifulSoup(r.text, 'lxml')
divs = bs.find_all(class_='feed-title')
# data = [div.span.get_text() for div in divs]
for div in divs:
    print(div.a.get_text()[8:])
    print(div.a['href'])

import time
timeStamp = time.localtime(time.time())
strTime = time.strftime("%m月%d日", timeStamp)
print(strTime)

url2 = 'http:'+divs[0].a['href']

art = requests.get(url2)
# print(art.text)
bs2 = BeautifulSoup(art.text, 'lxml')
div = bs2.article.find_all('p')
div = div[2:-2]
print('\n'.join([p.text for p in div]))
