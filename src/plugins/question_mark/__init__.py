from nonebot import on_keyword
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

index = on_keyword({'？', '?'})


@index.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sender = event.get_user_id()
    from_msg = str(event.get_message())
    if event.is_tome() and (from_msg.startswith("?") or from_msg.startswith("？")):
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
                    'text': f'啥b，不带问号不会说话了是吧？'
                }
            }
        ]
        await index.send(msg)
