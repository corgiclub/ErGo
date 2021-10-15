import nonebot

from src.extensions.utils import get_config
from . import cmds
from .core import detect_living

cfg = get_config(__file__)
detecting = []
driver = nonebot.get_driver()


@driver.on_startup
async def load_monitors():
    for room_id, target_id in cfg['rooms_data'].items():
        if room_id not in detecting:
            await detect_living(room_id, target_id)
            detecting.append(room_id)


async def reload():
    cfg.update(get_config(__file__))
    load_monitors()
