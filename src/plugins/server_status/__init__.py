import os
import re
# from .config import Config
from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event


status = on_regex("状态")


@status.handle()
async def func(bot: Bot, event: Event, state: T_State):

    msg = await get_status()
    await status.send(msg)


async def get_status():
    gpu_list = os.popen('nvidia-smi').read().split('\n')
    gpu0_info = re.findall('[a-zA-Z0-9]+', gpu_list[9].split('|')[1])
    gpu1_info = re.findall('[a-zA-Z0-9]+', gpu_list[13].split('|')[1])


    return ''.join(gpu0_info)
