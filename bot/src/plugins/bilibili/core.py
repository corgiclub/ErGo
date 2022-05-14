import asyncio
import re
import time
import urllib.parse
from nonebot.log import logger

import httpx
import lxml.html
from bilibili_api import video
from bilibili_api.exceptions import ResponseCodeException
from nonebot.adapters.onebot.v11 import Message, MessageSegment


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

        if not vid:
            return Message('暂不支持的格式')
        # 获取视频详细信息
        msg = await video_detail(vid, vtype)

    except Exception as e:
        msg = Message("Error: {}".format(type(e)))

    return msg


async def b23_extract(text):
    b23 = re.compile(r'b23.tv\\/(\w+)').search(text)
    if not b23:
        b23 = re.compile(r'b23.tv/(\w+)').search(text)

    resp = httpx.get(f'https://b23.tv/{b23[1]}')
    text_long = str(resp.url)
    return text_long


async def extract(text: str):
    aid, bvid = re.compile(r'(av|AV)\d+').search(text), re.compile(r'(BV|bv)([a-zA-Z0-9])+').search(text)
    if aid or bvid:
        return bvid[0] if bvid else aid[0][2:], 'bv' if bvid else 'av'
    else:
        return None, None


async def search_bili_by_title(title: str):
    brackets_pattern = re.compile(r'[()\[\]{}（）【】]')
    title_without_brackets = brackets_pattern.sub(' ', title).strip()
    search_url = f'https://search.bilibili.com/video?keyword={urllib.parse.quote(title_without_brackets)}'

    try:
        resp = httpx.get(search_url)
        text = resp.text
        content: lxml.html.HtmlElement = lxml.html.fromstring(text)
    except asyncio.TimeoutError:
        return None

    for video_ in content.xpath('//li[@class="video-item matrix"]/a[@class="img-anchor"]'):
        if title == ''.join(video_.xpath('./attribute::title')):
            url = ''.join(video_.xpath('./attribute::href'))
            break
    else:
        url = None
    return url


async def video_detail(id_, type_):
    try:
        v = video.Video(bvid=id_) if type_ == 'bv' else video.Video(aid=int(id_))
        info = await v.get_info()

        return Message([
            MessageSegment.image(info['pic']),
            MessageSegment.text(f'《{info["title"]}》\n'
                                f'up主: {info["owner"]["name"]}\n'
                                f'投稿时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["pubdate"]))}\n'
                                f'播放量：{format_view(info["stat"]["view"])}\n'
                                f'URL: https://bilibili.com/video/av{info["aid"]}'),
        ])

    except ResponseCodeException:
        return Message('没有找到视频信息')

    except Exception as e:
        logger.error(e)
        return Message("解析出错--Error: {}\n".format(type(e)))


def format_view(v):
    return f'{v/10000:.2f} 万' if v > 10000 else v
