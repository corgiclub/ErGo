from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain, Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

import re
from extensions.mongodb import *
from extensions.load_config import load_config

__plugin_name__ = '数据库'
__plugin_description__ = '存储至数据库'
__plugin_usage__ = '【需要管理员权限】\n发送 数据库测试 可以随机返回一条当前群数据。'
__plugin_pattern__ = '数据库测试*'

bcc = Get.bcc()
config = load_config()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def log_to_database(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    log_info(group, member)
    log_message(message, group, member)
    mes = message.asDisplay()
    if re.match(__plugin_pattern__, mes):
        if mes == '数据库测试':
            await app.sendGroupMessage(group, MessageChain.create([
                Plain(log_debug(group)),
            ]))
        if mes == '数据库测试图':
            pic_byte, pic_times = most_frequently_pic()
            mes_list = []
            for x in range(len(pic_times)):
                mes_list.append(Image.fromUnsafeBytes(pic_byte[x]))
                mes_list.append(Plain(f'发送次数：{pic_times[x]}'))
            await app.sendGroupMessage(group, MessageChain.create(mes_list))
