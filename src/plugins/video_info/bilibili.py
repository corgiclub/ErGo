import re, json, aiohttp, asyncio
import lxml.html
import urllib.parse
from bilibili_api import video


async def bili_keyword(text):

    try:
        # 提取url
        vid, vtype = await extract(text)

        # 小程序
        if not vid:
            pattern = re.compile(r'"desc":".*?"')
            desc = re.findall(pattern, text)
            i = 0
            while i < len(desc):
                title_dict = "{" + desc[i] + "}"
                title = eval(title_dict)
                vurl = await search_bili_by_title(title['desc'])
                if vurl:
                    vid, vtype = await extract(vurl)
                    break
                i += 1

        # 获取视频详细信息
        msg = await video_detail(vid, vtype)

    except Exception as e:
        msg = "Error: {}".format(type(e))
    return msg


async def b23_extract(text):
    b23 = re.compile(r'b23.tv\\/(\w+)').search(text)
    if not b23:
        b23 = re.compile(r'b23.tv/(\w+)').search(text)
    url = f'https://b23.tv/{b23[1]}'
    async with aiohttp.request('GET', url, timeout=aiohttp.client.ClientTimeout(10)) as resp:
        text_long = str(resp.url)
    return text_long


async def extract(text: str):
    aid = re.compile(r'(av|AV)\d+').search(text)
    bvid = re.compile(r'(BV|bv)([a-zA-Z0-9])+').search(text)
    if bvid:
        id_ = bvid[0]
        type_ = 'bv'
    elif aid:
        id_ = aid[0][2:]
        type_ = 'av'
    else:
        id_ = None
        type_ = None
    return id_, type_


async def search_bili_by_title(title: str):
    brackets_pattern = re.compile(r'[()\[\]{}（）【】]')
    title_without_brackets = brackets_pattern.sub(' ', title).strip()
    search_url = f'https://search.bilibili.com/video?keyword={urllib.parse.quote(title_without_brackets)}'

    try:
        async with aiohttp.request('GET', search_url, timeout=aiohttp.client.ClientTimeout(10)) as resp:
            text = await resp.text(encoding='utf8')
            content: lxml.html.HtmlElement = lxml.html.fromstring(text)
    except asyncio.TimeoutError:
        return None

    for video in content.xpath('//li[@class="video-item matrix"]/a[@class="img-anchor"]'):
        if title == ''.join(video.xpath('./attribute::title')):
            url = ''.join(video.xpath('./attribute::href'))
            break
    else:
        url = None
    return url


async def video_detail(id_, type_):
    try:
        if type_ == 'bv':
            v = video.Video(bvid=id_)
        else:
            v = video.Video(aid=id_)
        info = await v.get_info()
        msg = [
            {
                "type": "image",
                "data": {
                    "file": info['pic']
                }
            },
            {
                "type": "text",
                "data": {
                    "text": f'《{info["title"]}》\n' +\
                            f'Up主: {info["owner"]["name"]}\n' +\
                            f'URL: https://bilibili.com/video/av{info["aid"]}'
                }
            }
        ]

        return msg
    except Exception as e:
        msg = "解析出错--Error: {}".format(type(e))
        return msg
