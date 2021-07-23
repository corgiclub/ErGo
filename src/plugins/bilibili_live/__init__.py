import asyncio
from pprint import pprint
from bilibili_api import live
from nonebot import on_regex
import nonebot
from nonebot.adapters import Bot, Event
from extensions import load_config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.schedulers.background import BackgroundScheduler

# analysis_bili = on_regex(r"(b23.tv)|(www.bilibili.com/video)|(www.bilibili.com/bangumi)|(^(BV|bv)([0-9A-Za-z]{10}))|"
#                          r"(^(av|AV)([0-9]+)(/.*|\\?.*|)$)|(\[\[QQ小程序\]哔哩哔哩\])|(QQ小程序&amp;#93;哔哩哔哩)|"
#                          r"(QQ小程序&#93;哔哩哔哩)")
config = load_config()
live_status_global = {k: 0 for k in config.rooms.keys()}
# bot = nonebot.get_bots()


async def track_rooms():
    for liver, room_id in config.rooms.items():
        print(room_id)
        room = live.LiveRoom(room_id)
        info = await room.get_room_info()
        live_status = info['room_info']['live_status']

        if live_status - live_status_global[liver] == 1:
            # face = info['anchor_info']['base_info']['face']
            cover = info['room_info']['cover']
            # keyframe = info['room_info']['keyframe']
            # online = info['room_info']['online']
            title = info['room_info']['title']
            print(f'{liver}在直播！')
            with open('i.txt', 'w') as fi:
                fi.write('xxx')

        elif live_status - live_status_global[liver] == -1:
            print(f'{liver}下播了！')
            with open('i.txt', 'w') as fi:
                fi.write('xxx')

        else:
            print(f'xxx')
            with open('i.txt', 'w') as fi:
                fi.write('xxx')

        # return info


if __name__ == '__main__':
    # t = asyncio.get_event_loop().run_until_complete(track_rooms())
    # pprint(t)
    # pprint(config)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(track_rooms, 'interval', seconds=5)
    scheduler.start()

    print(scheduler.get_jobs())

    while True:
        pass
