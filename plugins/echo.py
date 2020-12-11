from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

from mirai_core import loaded_plugins
from time import sleep

from random import random

__plugin_name__ = '复读机'
__plugin_description__ = '随机复读句子'
__plugin_usage__ = '发送“复读概率x”将复读概率设为x'

bcc = Get.bcc()

echo_freq = 0.1


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def echo(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    global echo_freq
    mes = message.asDisplay()
    if mes.startswith('复读概率'):
        try:
            freq = float(mes[4:])
            if not (freq >= 0 and freq <= 1):
                raise Exception("复读概率应在 [0, 1] 之间")
            echo_freq = freq
            await app.sendGroupMessage(group, MessageChain.create([
                Plain(f"复读概率已被设置为{echo_freq}")
            ]))
        except Exception as e:
            await app.sendGroupMessage(group, MessageChain.create([
                Plain(f"复读概率设置失败:{e}")
            ]))
    if random() < echo_freq:
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(mes)
        ]))
