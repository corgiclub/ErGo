from .bilibili_video import b23_extract, bili_keyword
from nonebot import on_regex
from nonebot.adapters import Bot, Event

analysis_bili = on_regex(r"(b23.tv)|(www.bilibili.com/video)|(www.bilibili.com/bangumi)|(^(BV|bv)([0-9A-Za-z]{10}))|"
                         r"(^(av|AV)([0-9]+)(/.*|\\?.*|)$)|(\[\[QQ小程序\]哔哩哔哩\])|(QQ小程序&amp;#93;哔哩哔哩)|"
                         r"(QQ小程序&#93;哔哩哔哩)", priority=10, block=False)


@analysis_bili.handle()
async def analysis_main(bot: Bot, event: Event, state: dict):
    text = str(event.get_message()).strip()

    if "b23.tv" in text:
        # 提前处理短链接，避免解析到其他的
        text = await b23_extract(text)

    msg = await bili_keyword(text)
    if msg:
        await analysis_bili.send(msg)
        # try:
        #     await analysis_bili.send(msg)
        # except Exception as e:
        #     await analysis_bili.send(str(e)+"此次解析可能被风控，尝试去除简介后发送！")
        #     msg = re.sub(r"简介.*", "", msg)
        #     await analysis_bili.send(msg)
