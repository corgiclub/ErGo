import nonebot
from pprint import pprint

from nonebot import on_command, on_message
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, Message, MessageSegment
from nonebot.permission import SUPERUSER
from src.extensions.glances import get_info

from .config import Config

cfg = Config()

record = on_message(priority=-1)


@record.handle()
async def log2database(bot: Bot, event: Event, state: T_State):
    msg: Message[MessageSegment] = event.get_message()
    event.get_user_id()
    print(event.self_id)
    for mss in msg:
        # print(mss.type)
        # pprint(mss.data)
        # print(mss.items())

        # await sta.send(mss)

        data = {
            "sid": event.self_id,
            "type": mss.type,
            "data": mss.data
        }

        pprint(data)