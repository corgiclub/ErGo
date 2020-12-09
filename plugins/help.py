from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

import os

__plugin_name__ = '帮助'
__plugin_description__ = '查看插件帮助'
__plugin_usage__ = '发送"help"或"帮助"'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def help_(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if message.asDisplay() in ('氦', 'help'):
        print(os.listdir('/ErGo/plugins/'))
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(''),
        ]))

