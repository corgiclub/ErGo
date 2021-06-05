from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from _old.mirai_core import judge
from _old.mirai_core import Get

import subprocess

__plugin_name__ = '日志'
__plugin_description__ = '显示最近日志'
__plugin_usage__ = '发送“日志”'
__plugin_pattern__ = '日志'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def show_log(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    mes = message.asDisplay()
    if mes == '日志':
        process = subprocess.Popen(
            "tail -n 100 logs/bot.log", stdout=subprocess.PIPE, shell=True)
        stdout = process.communicate()[0].strip()
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(str(stdout.decode()))
        ]))
