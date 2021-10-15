import nonebot
from nonebot.adapters.cqhttp import Bot
from nonebot.plugin.export import export

from src.extensions.utils import get_config


async def reload():
    cfg.update(get_config(__file__))


driver = nonebot.get_driver()
cfg = get_config(__file__)
export().reload = reload


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
