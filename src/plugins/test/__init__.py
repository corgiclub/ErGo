import nonebot

from nonebot import on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import Permission, SUPERUSER

from .config import Config

cfg = Config()

te = on_regex(cfg.test_word, permission=SUPERUSER)


@te.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await test_func()


async def test_func():
    from extensions.glances import get_info
    msg = await get_info()
    await te.send(msg)



