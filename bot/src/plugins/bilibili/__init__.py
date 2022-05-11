from nonebot import on_regex
from nonebot.adapters.onebot.v11 import MessageEvent

from src.extensions import coolperm
from .core import b23_extract, bili_keyword

analysis_bv = on_regex(r"(b23.tv)|(www.bilibili.com/video)|(www.bilibili.com/bangumi)|(^(BV|bv)([0-9A-Za-z]{10}))|"
                       r"(^(av|AV)([0-9]+)(/.*|\\?.*|)$)|(\[\[QQ小程序\]哔哩哔哩\])|(QQ小程序&amp;#93;哔哩哔哩)|"
                       r"(QQ小程序&#93;哔哩哔哩)", priority=20, block=False)


@analysis_bv.handle(parameterless=[coolperm('.analysis_bv')])
async def analysis_main(event: MessageEvent):
    text = event.get_plaintext().strip()

    if "b23.tv" in text:
        # 提前处理短链接，避免解析到其他的
        text = await b23_extract(text)

    msg = await bili_keyword(text)

    if msg:
        await analysis_bv.send(msg)
