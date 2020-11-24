from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

__plugin_name__ = '氦'
__plugin_description__ = '呼唤bot'
__plugin_usage__ = '发送"氦"'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def video_info(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if message.asDisplay() == '氦':
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(f"Cogito, ergo sum."),
        ]))

