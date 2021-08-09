import httpx
from nonebot import on_command, on_keyword, get_driver
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

driver = get_driver()

BASE_URL = 'http://localhost:5000'

keywords = set('狗东西')
nmsl = on_keyword(keywords)


@driver.on_bot_connect
async def _(bot: Bot):
    data = httpx.get(f'{BASE_URL}/words').json().get('data')
    for k in data:
        keywords.add(k)


async def get_answer(q: str):
    bot_api = f'http://localhost:5000'
    res = httpx.get(bot_api, params={'q': q})
    return res.json().get('data')


@nmsl.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sender = event.get_user_id()
    from_msg = str(event.get_message())
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
                'text': await get_answer(from_msg)
            }
        }
    ]
    await nmsl.send(msg)
