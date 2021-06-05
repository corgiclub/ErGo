from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from _old.mirai_core import judge
from _old.mirai_core import Get

__plugin_name__ = '键值响应'
__plugin_usage__ = '根据键值对回复'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def test(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    # print(message)
    print()







