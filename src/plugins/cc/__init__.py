import json
import httpx
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
import datetime

index = on_command('cc')


@index.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sender = event.get_user_id()
    from_msg = str(event.get_message())
    if len(from_msg) < 10 or len(from_msg) > 1000:
        await index.send([
            {
                'type': 'at',
                'data': {
                    'qq': sender
                }
            },
            {
                'type': 'text',
                'data': {
                    'text': '查重字数需要在 10~1000 字以内捏'
                }
            }])
        return

    url = "https://asoulcnki.asia/v1/api/check"

    payload = json.dumps({
        "text": from_msg
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = httpx.request("POST", url, headers=headers, data=payload)
    data = response.json()

    if data['data']['related']:
        first_doc = data['data']['related'][0]
        template = f'''枝网文本复制检测报告(简洁)
查重时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
总文字复制比: {data['data']['rate'] * 100}%
相似小作文: {first_doc['reply_url']}
作者: {first_doc['reply']['m_name']}
发表时间: {datetime.datetime.fromtimestamp(first_doc['reply']['ctime']).strftime('%Y-%m-%d %H:%M:%S')}
-------------
{first_doc['reply']['content']}

查重结果仅作参考，请注意辨别是否为原创'''
    else:
        template = f'''枝网文本复制检测报告(简洁)
查重时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
总文字复制比: 0.00%
查重结果仅作参考，请注意辨别是否为原创'''

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
                'text': f'{template}'
            }
        }
    ]
    await index.send(msg)
