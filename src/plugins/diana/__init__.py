from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

index = on_command('diana')


@index.handle()
async def _(bot: Bot, event: Event, state: T_State):
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
                'text': '嘉然 bot 开发中'
            }
        }
    ]
    await index.send(msg)
