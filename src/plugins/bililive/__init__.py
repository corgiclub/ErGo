import nonebot
from nonebot.plugin.export import export

from src.extensions.utils import get_config, get_permissions
from .core import detect_living


async def reload():
    global cfg
    global P
    cfg.update(get_config(__file__))
    P = get_permissions(__file__)


cfg = get_config(__file__)
P = get_permissions(__file__)
export().reload = reload

detecting = []
driver = nonebot.get_driver()


@driver.on_startup
async def load_monitors():
    for room_id, target_id in cfg['config']['rooms_data'].items():
        if room_id not in detecting:
            await detect_living(room_id, target_id)
            detecting.append(room_id)
