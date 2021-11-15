from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import SUPERUSER
from nonebot import require
from nonebot import CommandGroup
from src.extensions.glances import get_info

from nonebot.plugin.export import export

from src.extensions.utils import get_config


async def reload():
    cfg.update(get_config(__file__))


cfg = get_config(__file__)
export().reload = reload
P = require('flexperm').register('test_plugin')

cg = CommandGroup('测试', priority=10, block=False)


def h(x):
    return x.handle()


@h(cg.command('鉴权'))
async def _(bot: Bot, event: Event, state: T_State):
    print(str(event.get_message()))
    if P.has(bot, event, str(event.get_message())):
        msg = '拥有权限'
    else:
        msg = '无该权限'
    await bot.send(event, msg)


@h(cg.command('复读', permission=P('repeat')))
async def _(bot: Bot, event: Event, state: T_State):
    msg = event.get_message()
    await bot.send(event, msg)


@h(cg.command('重载权限', permission=P('reload')))
async def _(bot: Bot, event: Event, state: T_State):
    await reload()
    await bot.send(event, '重载成功')
