from nonebot.plugin.export import export

from . import cmds
from .plugin import register, plugins
from .cmds import reload

export().register = register
export().plugins_handle = plugins

del export, cmds, register
