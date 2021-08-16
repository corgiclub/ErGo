from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

from nonebot import require

scheduler = require("nonebot_plugin_apscheduler").scheduler

nonebot.init()


@scheduler.scheduled_job('cron', second='*/5')
async def _():
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=600302544,
                                 message=f'还不提肛？！')
    except CQHttpError:
        pass
