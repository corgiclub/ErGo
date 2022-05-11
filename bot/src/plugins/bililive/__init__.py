import nonebot
from .core import detect_living

detecting = []
driver = nonebot.get_driver()
cfg = nonebot.get_bot().config['bililive']


@driver.on_startup
async def load_monitors():
    for room_id, target_id in cfg['config']['rooms_data'].items():
        if room_id not in detecting:
            await detect_living(room_id, target_id)
            detecting.append(room_id)
