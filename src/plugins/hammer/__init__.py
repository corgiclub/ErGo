import random

import httpx
from nonebot import on_regex
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
import jieba.posseg as peg

hammer = on_regex('[我|好].*[想|要].+')


@hammer.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sender = event.get_user_id()
    from_msg = str(event.get_message())
    verb = '想' if '想' in from_msg else '要'
    idx = from_msg.index(verb)
    verb2 = from_msg[idx + 1]

    text = f'你{verb2}个🔨，就你还{verb2}'
    if random.random() > 0.9:
        text = '在测试我？你测试你妈呢傻逼东西'
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
    await hammer.send(msg)
