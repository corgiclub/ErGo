import nonebot

from nonebot import on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event


driver = nonebot.get_driver()


@driver.on_bot_connect
async def _(bot: Bot):
    with open('src/plugins/version_info/first_run', 'r+') as fi:
        if fi.read() == '1':
            await bot.send_private_msg(user_id=634493876, message='123')
            fi.seek(0)
            fi.write('0')
            fi.truncate()
