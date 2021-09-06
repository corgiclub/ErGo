from nonebot import on_message
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, Message, MessageSegment
from src.extensions.mongodb import get_collection, log_picture, log_audio
from src.extensions.motordb import log_chat
from src.extensions.utils import PicSource, CQ

from .config import Config

cfg = Config()


record = on_message(priority=100, block=False)


@record.handle()
async def log2database(bot: Bot, event: Event, state: T_State):

    message_id = event.get_event_description().split()[1]
    session_id = event.get_session_id().split("_")
    self_id = bot.self_id
    if session_id[0] == 'group':
        group_id = session_id[1]
        user_id = session_id[2]
        col = get_collection('group_chat', group_id)
    else:
        # group_id = ''
        user_id = session_id[0]
        col = get_collection('private_chat', self_id)

    msg: Message[MessageSegment] = event.get_message()
    await log_chat(msg, user_id, message_id, col)

    lines = []
    for m in msg:
        lines.append({
            "mid": int(message_id),
            "uid": user_id,
            "mtp": m.type,
            **m.data,
        })
        if m.type == CQ.Image:
            await log_picture(**m.data, source=PicSource.Chat)
        if m.type == CQ.Record:
            await log_audio(**m.data)
    if lines:
        col.insert_many(lines)
