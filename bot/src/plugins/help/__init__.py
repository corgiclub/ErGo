from nonebot import on_command, get_driver
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment
from src.extensions import coolperm
from nonebot import CommandGroup, get_loaded_plugins


cg_help = on_command('help', priority=10, block=False)


@cg_help.handle(parameterless=[coolperm('.help')])
async def _(bot: Bot, event: MessageEvent):
    message = event.get_message()

    # plugin = message.extract_plain_text().split(' ')[1:]
    msg = [p.name for p in get_loaded_plugins()]

    await cg_help.send(MessageSegment.text('\n'.join(msg)))
