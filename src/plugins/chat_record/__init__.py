from nonebot import on_message
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, Message, MessageSegment
from src.extensions.mongodb import MongoChat

from .config import Config

cfg = Config()
db = MongoChat()

record = on_message(priority=100, block=False)


@record.handle()
async def log2database(bot: Bot, event: Event, state: T_State):

    message_id = event.get_event_description().split()[1]
    session_id = event.get_session_id().split("_")

    if session_id[0] == 'group':
        group_id = session_id[1]
        user_id = session_id[2]
        self_id = None
        msg: Message[MessageSegment] = event.get_message()
    else:
        group_id = None
        user_id = session_id[0]
        self_id = bot.self_id
        msg: Message[MessageSegment] = event.get_message()

    await db.log_chat(msg, user_id, message_id, group_id, self_id)
