import httpx
from nonebot import on_regex
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment

from src.extensions import coolperm

eva2_api = 'http://i.tech.corgi.plus:6666/api/inference'
header = {
    'Content-Type': 'application/json'
}

eva = on_regex(r'^:.*|^：.*', priority=50, block=False)


@eva.handle(parameterless=[coolperm('.eva')])
async def _(event: Event):
    sender = event.get_user_id
    message = event.get_plaintext()[1:]
    data = {
        "query_context": [message]
    }
    async with httpx.AsyncClient(proxies=None, headers=header) as cli:
        resp = await cli.post(url=eva2_api, json=data)
        answer = resp.json()['answer']

    msg = Message([
        MessageSegment.reply(sender),
        MessageSegment.text(f'{answer}')
    ])

    await eva.finish(msg)
