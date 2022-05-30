from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import MessageSegment
from src.extensions import get_sys_info, coolperm


server_status = on_command('系统状态', aliases={'sys', 'glances'}, priority=10, block=False)


@server_status.handle(parameterless=[coolperm('.query')])
async def _():
    msg = await get_sys_info()
    await server_status.send(MessageSegment.text(msg))
