from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

import re

from cpm_lm.sample import sample


__plugin_name__ = '二狗QA'
__plugin_usage__ = '召唤bot使用模型推理'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def video_info(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if message.asDisplay().startswith(('二狗')):
        try:
            query = str(re.sub('av', '', message.asDisplay(), flags=re.I))
            await app.sendGroupMessage(group, MessageChain.create([
                Plain(sample(query)),
            ]))
        except ValueError:
            return
