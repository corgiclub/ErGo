from nonebot.plugin.export import export

from . import cmds
from .plugin import register
from .cmds import reload

export().register = register

del export, cmds, register
