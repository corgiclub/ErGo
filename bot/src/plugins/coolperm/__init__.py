from nonebot import on_command, get_driver
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message
from src.extensions import coolperm
from nonebot import CommandGroup

cg_perm = CommandGroup('perm')
cg_cool = CommandGroup('perm')


# 向下兼容至 py 3.8
def h(x):
    return x


@h(cg_perm.command('add', aliases=set()).handle(parameterless=[coolperm('.add')]))
def add_perm():
    pass

