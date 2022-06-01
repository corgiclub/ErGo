import nonebot
from .core import detect_living
from .cmds import *
from nonebot import export

detecting = []
driver = nonebot.get_driver()


async def monitor_live():

    cfg = driver.config.__dict__['bililive']

    for room_id, target_id in cfg['config']['rooms_data'].items():
        if room_id not in detecting:
            await detect_living(room_id, target_id)
            detecting.append(room_id)

export().monitor_live = monitor_live
