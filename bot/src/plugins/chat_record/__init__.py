from nonebot import on_message
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment

from src.extensions import log_chat

record = on_message(priority=100, block=False)


# 默认不过权限检查代码，加快速度
@record.handle()
async def log2database(event: Event):
    message_id = event.get_event_description().split()[1]
    session_id = event.get_session_id().split("_")

    if session_id[0] == 'group':
        group_id = session_id[1]
        user_id = session_id[2]
        msg: Message[MessageSegment] = event.get_message()
    else:
        group_id = None
        user_id = session_id[0]
        msg: Message[MessageSegment] = event.get_message()

    await log_chat(msg, user_id, message_id, group_id)
