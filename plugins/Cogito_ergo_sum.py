from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get
import re

__plugin_name__ = '氦'
__plugin_description__ = '呼唤bot'
__plugin_usage__ = '发送"氦"'
__plugin_pattern__ = '氦'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def video_info(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if re.match(__plugin_pattern__, message.asDisplay()):
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(f"Cogito, ergo sum."),
        ]))

