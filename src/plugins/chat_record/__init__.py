import nonebot
from pprint import pprint

from nonebot import on_command, on_message
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, Message, MessageSegment
from src.extensions.message import CQ
from src.extensions.mongodb import get_collection

from .config import Config

cfg = Config()

# fixme 在 main 分支中重新设计全部优先级
record = on_message(priority=1, block=False)


@record.handle()
async def log2database(bot: Bot, event: Event, state: T_State):
    # print(event.dict())
    # print(event)
    # print(event.get_event_description())
    # print(event.get_event_name())
    # print(event.get_log_string())
    message_id = event.get_event_description().split()[1]
    session_id = event.get_session_id().split("_")
    self_id = bot.self_id
    if session_id[0] == 'group':
        group_id = session_id[1]
        user_id = session_id[2]
        col = get_collection('group_chat', group_id)
    else:
        group_id = ''
        user_id = session_id[0]
        col = get_collection('private_chat', self_id)

    msg: Message[MessageSegment] = event.get_message()
    for m in msg:
        line = {
            "mid": message_id,
            "uid": user_id,
            "mtp": m.type,
            **m.data,
        }

        col.insert_one(line)
        pprint(line)


