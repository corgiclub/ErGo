from nonebot import get_driver, export, require

from src.extensions.utils import get_config, get_permissions
from . import cmds


@export()
async def reload():
    global cfg
    global P
    cfg = get_config(__file__)
    P = get_permissions(__file__)


cfg = get_config(__file__)
P = get_permissions(__file__)
