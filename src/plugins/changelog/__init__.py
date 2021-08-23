import nonebot

from nonebot import on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event

from typing import List


driver = nonebot.get_driver()


@driver.on_bot_connect
async def _(bot: Bot):
    version_now = driver.config.version

    with open('src/plugins/changelog/version.txt', 'r+') as fi:

        version_last = fi.read()
        if not version_last == version_now:
            group_list = await bot.get_group_list()
            with open('changelog.txt', 'r', encoding='utf-8') as fj:
                msg = fj.read()
                for group in group_list:
                    await bot.send_group_msg(group_id=group['group_id'], message=msg)
            fi.seek(0)
            fi.write(version_now)
            fi.truncate()

