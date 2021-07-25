import nonebot

from nonebot import on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import Permission, SUPERUSER

from .config import Config

cfg = Config()

aha = on_regex(r'|'.join(cfg.keywords), rule=to_me(), permission=SUPERUSER)


@aha.handle()
async def hai(bot: Bot, event: Event, state: T_State):
    await aha.send(event.get_message())


