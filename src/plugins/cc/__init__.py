import json
import httpx
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

index = on_command('rp')


@index.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sender = event.get_user_id()
    from_msg = str(event.get_message())

    url = "https://asoulcnki.asia/v1/api/check"

    payload = json.dumps({
        "text": from_msg
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = httpx.request("POST", url, headers=headers, data=payload)

    print(response.text)
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
                'text': f'(简单算法版)你今天的人品是%'
            }
        }
    ]
    await index.send(msg)
