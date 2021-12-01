from nonebot.plugin.export import export

from . import cmds
from .plugin import register, plugins
from .cmds import reload as reload_perm
from extensions.utils import get_config

export().register = register
export().plugins_handle = plugins
export().reload_perm = reload_perm()

del export, cmds, register


@export()
async def reload():
    global cfg
    cfg.update(get_config(__file__))

cfg = get_config(__file__)
