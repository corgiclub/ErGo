import re

from nonebot import on_command, on_regex, export, require
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment
from nonebot.matcher import Matcher

from src.extensions import CQ, coolperm, regex_startswith_key_with_image
from .sauce_func import *
from .pixiv_func import *


scheduler = require("apscheduler").scheduler
scheduler.add_job(refresh_daily_pixiv, "interval", days=1, id="refresh_pixiv_daily")
export().refresh_daily_pixiv = refresh_daily_pixiv

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
async def _(event: Event, matcher: Matcher):
    args = ' '.join(event.get_message().extract_plain_text().split(' ')[1:]).strip()
    print(args)
    if args == '':
        query = ImagePixiv.select(Image.filename, Image.suffix).where(ImagePixiv.illust_type == 'illust'). \
            join(Image, on=(Image.id == ImagePixiv.image_id)).order_by(fn.Rand()).get()
        await searching_by_text.finish(
            MessageSegment.image(
                file=pic_base_path / f'pixiv/{query.image.filename}.{query.image.suffix}'
            )
        )
    else:
        result = await search_pixiv(args)
        if len(result) == 0:
            await searching_by_text.finish(MessageSegment.text(f'网络错误或未搜索到结果'))
        else:
            await searching_by_text.finish(
                Message(
                    [
                        MessageSegment.image(
                            file=pic_base_path / f'pixiv/{_fn}'
                        ) for _fn in result
                    ]
                )
            )

