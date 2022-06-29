from asyncio import get_running_loop

import nonebot
from bilibili_api import live
from nonebot.adapters.onebot.v11 import Bot, Message, MessageSegment

driver = nonebot.get_driver()
debounce_time = 30
debounced = []


async def detect_living(roomid, groups):
    room_living = live.LiveDanmaku(roomid)

    @driver.on_bot_connect
    async def _():
        await room_living.connect()

    @room_living.on('LIVE')
    async def on_(event):

        if roomid in debounced:
            return
        else:
            debounced.append(roomid)
            loop = get_running_loop()
            loop.call_later(debounce_time, lambda: debounced.remove(roomid))

        room = live.LiveRoom(roomid)
        room_info = await room.get_room_info()

        msg = Message([
            MessageSegment.image(room_info['room_info']['cover']),
            MessageSegment.text(f"{room_info['anchor_info']['base_info']['uname']} 开播了\n"
                                f"【{room_info['room_info']['title']}】\n"
                                f"https://live.bilibili.com/{event['room_display_id']}")
        ])
        bot: Bot = nonebot.get_bot()
        for group in groups:
            await bot.send_group_msg(group_id=group, message=msg)
