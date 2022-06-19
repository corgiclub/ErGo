import re

from nonebot import on_command, on_startswith, on_regex, get_driver, export
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment
from src.extensions import CQ, get_config
from PicImageSearch import SauceNAO, Network
from .func import *

from src.extensions import CQ, get_config, pic_base_path, ImageType, proxies, coolperm, get_image, \
    regex_startswith_key_with_image
from src.models.image import ImageSauce

searching_by_pic = on_regex(regex_startswith_key_with_image(['search', 'pic']), flags=re.S, priority=10, block=False)
searching_by_text = on_command('setu', aliases={'色图', 'pixiv'}, priority=10, block=False)


@searching_by_pic.handle(parameterless=[coolperm('.searching_by_pic')])
async def _(event: Event):
    message = event.get_message()
    pic_count = sum([msg.type == CQ.image.name for msg in message])
    if pic_count == 0:
        return
    elif pic_count > 1:
        await searching_by_pic.send(MessageSegment.text('查询的图片过多，请一张张查询哦'))
    else:
        for msg in message:
            if msg.type == CQ.image.name:
                img, img_path, remaining = await search_sauce(msg.data['url'])
                if not remaining:
                    # todo 收款码
                    await searching_by_pic.send(MessageSegment.text(f"今日 API 调用次数超限，"
                                                                    f"有兴趣的话可以赞助开发者付费 API 费用哦"))
                if img:
                    await searching_by_pic.send(
                        Message([
                            MessageSegment.image(file=img_path),
                            MessageSegment.text(
                                f"\n{img.title}\n作者：{img.author}\n{img.url}".replace('\n\n', '\n').strip('\n')
                            ),
                        ])
                    )
                else:
                    await searching_by_pic.send(MessageSegment.text(f"未搜到相似图片"))


@searching_by_text.handle(parameterless=[coolperm('.searching_by_text')])
async def _(event: Event):
    message = event.get_message().extract_plain_text()
    if message.strip() == '':
        img = await get_daily_pixiv()
    else:
        img = await search_pixiv()


async def test_on_startup():
    await get_daily_pixiv()


export().test = test_on_startup
