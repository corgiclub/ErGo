import nonebot
import yaml
import datetime
from bilibili_api import live
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Message, Event

from src.extensions.mongodb import get_collection


yaml_path = 'src/plugins/bililive/bilibili_live.yml'

driver = nonebot.get_driver()
col = get_collection('ergo', 'bililive')


@driver.on_startup
async def startup():
    with open(yaml_path, 'r') as fi:
        data: dict = yaml.safe_load(fi)['rooms_data']
    for room_id, target_id in data.items():
        await detect_living(room_id, target_id)


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
        # pprint(event)


async def set_config():
    pass


bililive = on_command('bililive', priority=10, block=False)


@bililive.handle()
async def send_config(bot: Bot, event: Event):

    with open(yaml_path, 'r') as fi:
        data: dict = yaml.safe_load(fi)['rooms_data']

    group_id = int(event.get_session_id().split('_')[1])
    room_id_list = [k for k, v in data.items() if group_id in v]
    room_uname_list = []

    for room_id in room_id_list:
        room = live.LiveRoom(int(room_id))
        room_info = await room.get_room_info()
        live_statu = "🎤 直播中" if room_info['room_info']['live_status'] else "🕊 未开播"
        room_uname_list.append(f"{live_statu} - {room_info['anchor_info']['base_info']['uname']}")

    msg = f"本群当前检测的直播间有 {len(room_id_list)} 个：\n" + '\n'.join(room_uname_list)

    await bililive.send(msg)
