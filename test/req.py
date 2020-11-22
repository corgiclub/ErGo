import requests
import re

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


req = requests.get(url='https://b23.tv/123456', headers=hdr)

print(req.text)
print(req.status_code)
# print(res.read().decode('utf8'))

pat_aid = 'av[1-9][0-9]{0,8}'

g = re.search(pat_aid, req.text, flags=re.I)

print(g.group())

