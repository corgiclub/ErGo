import aiohttp
from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member

from extensions.load_config import load_config
from mirai_core import judge
from mirai_core import Get
import re

__plugin_name__ = 'shell'
__plugin_description__ = '跑服务器脚本'
__plugin_usage__ = '发送"重启vpn"'
__plugin_pattern__ = '重启测试'

cfg = load_config()
bcc = Get.bcc()


async def request_server():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(cfg.url) as r:
                resp = await r.json()
                return f"zerotier 重启好了，你再试试, {resp}"
    except Exception as e:
        return str(e)


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def restart_zerotier(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if re.match(__plugin_pattern__, message.asDisplay()):
        msg = await request_server()
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(msg),
        ]))