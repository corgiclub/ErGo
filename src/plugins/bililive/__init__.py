import nonebot
import yaml
from bilibili_api import live
from nonebot.adapters.cqhttp import Bot, Message

driver = nonebot.get_driver()


@driver.on_startup
async def startup():
    with open('src/plugins/bililive/bilibili_live.yml', 'r') as fi:
        rooms = yaml.safe_load(fi)['rooms']
    for r in rooms:
        await detect_living(r)


async def detect_living(roomid):
    room_living = live.LiveDanmaku(roomid)

    @driver.on_bot_connect
    async def _(bot):
        await room_living.connect()

    @room_living.on('LIVE')
    async def on_(event):
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
                            f"{room_info['room_info']['title']}\n"
                            f"https://live.bilibili.com/{event['room_display_id']}"
                }
            }
        ])
        bot: Bot = nonebot.get_bot()
        for group in await bot.get_group_list():
            await bot.send_group_msg(group_id=group['group_id'], message=msg)
        # pprint(event)


