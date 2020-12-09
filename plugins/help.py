from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

from mirai_core import loaded_plugins
from time import sleep

__plugin_name__ = '帮助'
__plugin_description__ = '查看插件帮助'
__plugin_usage__ = '发送"help"或"帮助"'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def help_(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    mes = message.asDisplay()
    if mes.startswith('help'):
        text = ''
        if mes == 'help':
            # print([p.description for p in loaded_plugins])
            text += '插件名 - 插件描述\n'
            text += '\n'.join([p.name+' - '+p.description for p in loaded_plugins])
            text += '\n\n输入"help 插件名"查询插件用法'
        else:
            mes = mes[5:]
            for p in loaded_plugins:
                if mes == p.name:
                    text += '插件：{}\n描述：{}\n用法：{}'.format(p.name, p.description, p.usage)
            if not text:
                text += '没有该插件！'

        # sleep(1)
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(text)
        ]))


