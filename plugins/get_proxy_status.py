from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

import requests
from bs4 import BeautifulSoup
from extensions.load_config import load_config

__plugin_name__ = '查询梯子状态'
__plugin_description__ = '查询梯子状态，包括剩余流量、通道数等信息。'
__plugin_usage__ = '发送"氦"'

bcc = Get.bcc()
cfg = load_config()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def video_info(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if message.asDisplay() == '梯子':
        req = requests.get(url=cfg.url, headers=cfg.hdr)
        bs = BeautifulSoup(req.text, 'lxml')
        divs = bs.find_all(class_='card card-statistic-2')
        data = [div.span.get_text() for div in divs]

        await app.sendGroupMessage(group, MessageChain.create([
            Plain('剩余流量 {}GB，当前在线 {}/3'.format(data[1], data[2])),
        ]))


