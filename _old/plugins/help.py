from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from _old.mirai_core import judge
from _old.mirai_core import Get

from _old.mirai_core import loaded_plugins
import re

__plugin_name__ = '帮助'
__plugin_description__ = '查看插件帮助'
__plugin_usage__ = '发送"help"或"帮助"'
__plugin_pattern__ = 'help*|帮助'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def help_(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    mes = message.asDisplay()
    if re.match(__plugin_pattern__, mes):
        text = ''
        if mes == 'help':
            text += '插件名\n' + '\n'.join([p.name + ' - ' + p.description for p in loaded_plugins]) \
                    + '\n\n输入"help 插件名"查询插件用法'
        else:
            mes = mes[4:].strip()
            for p in loaded_plugins:
                if mes == p.name:
                    text += '插件：{}\n描述：{}\n用法：{}'.format(p.name, p.description, p.usage)
            if not text:
                text += '没有该插件！'

        await app.sendGroupMessage(group, MessageChain.create([
            Plain(text),
        ]))


