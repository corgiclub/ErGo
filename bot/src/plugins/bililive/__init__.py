import nonebot
from .core import detect_living
from .cmds import *
from src.extensions import get_config_late

detecting = []
driver = nonebot.get_driver()


@driver.on_startup
async def load_monitors():

    cfg = get_config_late('bililive')

    for room_id, target_id in cfg['config']['rooms_data'].items():
        if room_id not in detecting:
            await detect_living(room_id, target_id)
            detecting.append(room_id)
