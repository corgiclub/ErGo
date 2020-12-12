from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

from pixivpy_async import *

__plugin_name__ = 'pixiv'
__plugin_description__ = '使用 pixiv 的相关功能'
__plugin_usage__ = '搜索：p [关键词/pid]\n搜图：p [图片]\n查找流行瑟图：se图\n'
__plugin_pattern__ = 'pixiv*'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def pixiv(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if message.asDisplay().startswith('p '):
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(f"Cogito, ergo sum."),
        ]))

    async with PixivClient() as client:
        aapi = AppPixivAPI(client=client)
        # Doing stuff...
