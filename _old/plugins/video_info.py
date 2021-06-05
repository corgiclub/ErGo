from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain, Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from _old.mirai_core import judge
from _old.mirai_core import Get

import re
import aiohttp
import requests

__plugin_name__ = '视频'
__plugin_description__ = '查看B站/油管视频详细信息'
__plugin_usage__ = '发送任意av/BV号，或分享链接、小程序，获取视频信息'
__plugin_pattern__ = 'av[1-9][0-9]{0,8}|bv[0-9a-z]{10}|https://b23.tv/[0-9a-zA-z]{6}'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def video_info(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    msg = message.asDisplay()
    if re.match(__plugin_pattern__, msg):
        id_type, num = detect_vid(msg)
        url = f'https://api.bilibili.com/x/web-interface/view?{id_type}={num}'
        async with aiohttp.request("GET", url) as r:
            get = await r.json()

        if 'data' in get:
            data = get['data']
            print(data)
            during = '{}分{}秒'.format(data['duration'] // 60, data['duration'] % 60)

            await app.sendGroupMessage(group, MessageChain.create([
                Image.fromNetworkAddress(get['data']['pic']),
                Plain(f"\n标题:{data['title']}"),
                Plain(f"\nUp主:{data['owner']['name']}"),
                Plain(f"\n链接:https://bilibili.com/video/av{data['aid']}")
            ]))
        else:
            await app.sendGroupMessage(group, MessageChain.create([
                Plain(f"搜索不到视频信息"),
            ]))


def detect_vid(text):

    pat_aid = 'av[1-9][0-9]{0,8}'
    pat_bid = 'bv[0-9a-z]{10}'
    pat_srt = 'https://b23.tv/[0-9a-zA-z]{6}'

    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }

    if string := re.search(pat_aid, text, re.I):
        id_type = 'aid'
        num = re.sub('av', '', string.group(), flags=re.I)
    elif string := re.search(pat_bid, text, re.I):
        id_type = 'bvid'
        num = string.group()
    elif url := re.search(pat_srt, text, re.I):
        req = requests.get(url.group(), headers=hdr)
        if string := re.search(pat_aid, req.text, re.I):
            id_type = 'aid'
            num = re.sub('av', '', string.group(), flags=re.I)
        else:
            id_type, num = '', ''
    else:
        id_type, num = '', ''

    return id_type, num


"""
av号             av
bv号     
含av链接
含bv链接
移动端短链接


"""