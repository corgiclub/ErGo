from nonebot import on_command, on_keyword
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
from datetime import datetime
from nonebot.adapters.cqhttp import Message

rp = on_command('rp', priority=10, block=False)


def today_from_1970():
    date1 = datetime.strptime("1970-01-01", "%Y-%m-%d")
    date2 = datetime.today()
    return (date2 - date1).days


def get_rp(qq: int):
    days = today_from_1970()
    random = round((qq + 101 * days) * days) % 101
    rp_num = random % 100
    return rp_num


@rp.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if not event.is_tome():
        sender = event.get_user_id()
        qq = int(sender)
        msg = Message([
            {
                'type': 'at',
                'data': {
                    'qq': sender
                }
            },
            {
                'type': 'text',
                'data': {
                    'text': f'(简单算法版)你今天的人品是 {get_rp(qq)}%'
                }
            }
        ])
        await rp.send(msg)
