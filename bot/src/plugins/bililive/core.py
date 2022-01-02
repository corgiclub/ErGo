import datetime

import nonebot
from bilibili_api import live
from nonebot.adapters.cqhttp import Bot, Message

from src.extensions.mongodb import get_collection

driver = nonebot.get_driver()
col = get_collection('ergo', 'bililive')


async def detect_living(roomid, groups):
    room_living = live.LiveDanmaku(roomid)

    @driver.on_bot_connect
    async def _(bot):
        await room_living.connect()

    @room_living.on('LIVE')
    async def on_(event):

        line = {
            "room_id": roomid,
            "time": datetime.datetime.utcnow()
        }
        if col.find_one({"room_id": roomid}):
            return

        col.insert_one(line)
        room = live.LiveRoom(roomid)
        room_info = await room.get_room_info()

        msg = Message([
            {
                "type": "image",
                "data": {
                    "file": room_info['room_info']['cover']
                }
            },
            {
                "type": "text",
                "data": {
                    "text": f"{room_info['anchor_info']['base_info']['uname']} 正在直播\n"
                            f"【{room_info['room_info']['title']}】\n"
                            f"https://live.bilibili.com/{event['room_display_id']}"
                }
            }
        ])
        bot: Bot = nonebot.get_bot()
        for group in groups:
            await bot.send_group_msg(group_id=group, message=msg)
