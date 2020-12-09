from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

from extensions.metric_util import get_metric

__plugin_name__ = '系统'
__plugin_description__ = '汇报系统运行状态'
__plugin_usage__ = '发送"系统状态"'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def system_stat(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if message.asDisplay() == '系统状态':
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(get_metric()),
        ]))
