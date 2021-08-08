from nonebot import on_command, on_keyword
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

# from .config import Config

# cfg = Config()

nmsl = on_keyword({'nmsl', 'wdnmd'})

@nmsl.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if not event.is_tome():
        sender = event.get_user_id()
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
                    'text': f'你妈才死了'
                }
            }
        ]
        await nmsl.send(msg)
