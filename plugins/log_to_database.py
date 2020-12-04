from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain, Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

from extensions.mongodb import *
from extensions.load_config import load_config

__plugin_name__ = '数据库存储'
__plugin_description__ = '存储群聊相关数据'
__plugin_usage__ = ''

bcc = Get.bcc()
config = load_config()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def log_to_database(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    log_info(group, member)
    log_message(message, group, member)
    if message.asDisplay().startswith('数据库测试'):
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(log_debug(group)),
        ]))
