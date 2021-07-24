from enum import IntEnum

import aiohttp
import asyncio
import re
import traceback
import urllib.parse
from pprint import pprint

import lxml.html
from bilibili_api import live
from bilibili_api.exceptions import ResponseCodeException


async def get_live_info(room_id: int):
    room = live.LiveRoom(room_id)
    info = await room.get_room_info()

    face = info['anchor_info']['base_info']['face']
    cover = info['room_info']['cover']
    keyframe = info['room_info']['keyframe']
    # online = info['room_info']['online']
    live_status = info['room_info']['live_status']
    title = info['room_info']['title']

    return info


if __name__ == '__main__':
    pass

