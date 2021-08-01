import nonebot

from nonebot import on_command, on_keyword, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, MessageSegment
from nonebot.permission import SUPERUSER
from extensions.glances import get_info
from pprint import pprint

# from .config import Config
#
# cfg = Config()

sta = on_startswith('', permission=SUPERUSER)


@sta.handle()
async def _(bot: Bot, event: Event, state: T_State):
    pprint(event.dict())
    # pprint([d.__dict__ for d in event.dict()['message']])
    # print(type(event.dict()))
    pprint(event.get_message())

