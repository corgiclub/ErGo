import math
from asyncio import get_running_loop
from datetime import datetime, timedelta
from src.extensions import coolperm

from nonebot import on_command, on_startswith, on_regex, get_driver
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment
from src.extensions import CQ, get_config
from PicImageSearch import SauceNAO, Network

searching_by_pic = on_regex(r'pic*|sauce*|pixiv*', priority=10, block=False)
searching_by_text = on_command('setu', aliases={'色图', 'pixiv'}, priority=10, block=False)


@searching_by_pic.handle(parameterless=[coolperm('.searching_by_pic')])
async def _(event: Event):
    message = event.get_message()
    pic_count = sum([msg.type == CQ.image.name for msg in message])
    print(pic_count)
    if pic_count == 0:
        return
    elif pic_count > 1:
        await searching_by_pic.send(MessageSegment.text('查询的图片过多，请一张张查询哦'))
    else:
        for msg in message:
            if msg.type == CQ.image.name:
                img, remaining = await search_sauce(msg.data['url'])
                print(img, remaining)
                await searching_by_pic.send(
                    Message([
                        msg,
                        MessageSegment.text(f"\n{img.title}\n作者：{img.author}\n{img.url}"),
                        # MessageSegment.text(remaining is True)
                    ])
                )
                break


async def search_sauce(pic):
    saucenao_api_key = get_config('picky')['saucenao_api_key']
    async with Network() as client:  # 可以设置代理 Network(proxies='http://127.0.0.1:10809')
        sauce = SauceNAO(client=client, api_key=saucenao_api_key, minsim=50)
        res = await sauce.search(pic)
        return res.raw[0], res.long_remaining > 0
