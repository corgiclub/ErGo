import random

from nonebot import on_keyword
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

from .core import ZaunBot

zb = ZaunBot()
nmsl = on_keyword(zb.keywords)


async def send_msg(sender: str, from_msg: str, generic=False):
    text = zb.get_one_generic_answer()
    if not generic:
        text = zb.match_text(from_msg)
    msg = [
        {
            'type': 'at',
            'data': {
                'qq': sender
            }
        },
        {
            'type': 'text',
            'data': {
                'text': text
            }
        }
    ]
    await nmsl.send(msg)


@nmsl.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sender = event.get_user_id()
    from_msg = str(event.get_message())
    cnt = 0
    init = 0.5
    while random.random() > init:
        cnt += 1
        init *= 1.5

    await send_msg(sender, from_msg)
    answers = zb.get_some_generic_answer(cnt)
    for to_msg in answers:
        await send_msg(sender, to_msg, generic=True)
