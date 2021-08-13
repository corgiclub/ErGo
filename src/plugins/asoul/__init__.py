from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

index = on_command('asoul')


@index.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sender = event.get_user_id()
    from_msg = str(event.get_message())
    text = 'asoul bot 开发中'
    if from_msg == '小作文':
        text = '随机小作文功能开发中'
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
    await index.send(msg)
