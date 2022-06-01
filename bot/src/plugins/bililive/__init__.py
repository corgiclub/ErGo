from .core import detect_living
from .cmds import *
from nonebot import export

from src.extensions import get_config

detecting = []


async def monitor_live():

    cfg = get_config('bililive')

    for room_id, target_id in cfg['rooms_data'].items():
        if room_id not in detecting:
            await detect_living(room_id, target_id)
            detecting.append(room_id)

export().monitor_live = monitor_live
