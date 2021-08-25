from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import SUPERUSER
from src.extensions.glances import get_info

from .config import Config

cfg = Config()

sta = on_command('系统状态', permission=SUPERUSER, priority=10, block=False)


@sta.handle()
async def _(bot: Bot, event: Event, state: T_State):
    msg = await get_info()
    await sta.send(msg)
