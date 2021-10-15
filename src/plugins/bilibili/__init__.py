from nonebot.plugin.export import export

from src.extensions.utils import get_config
from . import cmds


async def reload():
    cfg.update(get_config(__file__))


cfg = get_config(__file__)
export().reload = reload
