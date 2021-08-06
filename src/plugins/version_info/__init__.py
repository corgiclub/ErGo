import nonebot

from nonebot import on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event

from typing import List


driver = nonebot.get_driver()


@driver.on_bot_connect
async def _(bot: Bot):
    with open('src/plugins/version_info/first_run', 'r+') as fi:
        if fi.read() == '1':
            group_list = await bot.get_group_list()
            with open('src/plugins/version_info/update_log.txt', 'r', encoding='utf-8') as fj:
                msg = fj.read()
                for group in group_list:
                    # print(group['group_id'])
                    await bot.send_group_msg(group_id=group['group_id'], message=msg)
            fi.seek(0)
            fi.write('0')
            fi.truncate()
