from bilibili_api import live
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message
from src.extensions import coolperm
from . import cfg


live_list = on_command('bililive', priority=10, block=False)


@live_list.handle(parameterless=[coolperm('.list')])
async def send_config(bot: Bot, event: MessageEvent):
    data = cfg['rooms_data']

    group_id = int(event.get_session_id().split('_')[1])
    room_id_list = [k for k, v in data.items() if group_id in v]
    room_uname_list = []

    for room_id in room_id_list:
        room = live.LiveRoom(int(room_id))
        room_info = await room.get_room_info()
        live_statu = "🎤 直播中" if room_info['room_info']['live_status'] else "🕊 未开播"
        room_uname_list.append(f"{live_statu} - {room_info['anchor_info']['base_info']['uname']}")

    msg = Message("本群当前检测的直播间有 {len(room_id_list)} 个：\n" + '\n'.join(room_uname_list))

    await live_list.send(msg)
