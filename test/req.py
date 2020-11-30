import requests
import re
import io
import PIL.Image as Img
import imghdr

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


req = requests.get(url='http://gchat.qpic.cn/gchatpic_new/634493876/600302544-2365113437-473F03C6C09E53D498B5BFD18D1E51A9/0?term=2',
                   # headers=hdr
                   )

print(req.content)
print(req.status_code)
_img_bytes = req.content
_img = Img.open(io.BytesIO(_img_bytes))
_img_type = imghdr.what(file=None, h=_img_bytes)
_img.save('tete' + '.' + _img_type)
print(_img_type)

with open('tes33.' + _img_type, 'wb') as f:
    f.write(_img_bytes)
