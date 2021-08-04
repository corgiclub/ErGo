import nonebot

from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, Message
from nonebot.permission import SUPERUSER
from extensions.glances import get_info
from random import randint
from pprint import pprint
import yaml
import os
import datetime

# from .config import Config

# cfg = Config()

jrrp = on_command('jrrp')


@jrrp.handle()
async def _(bot: Bot, event: Event, state: T_State):

    yml_path = "src/plugins/jrrp/jrrp.yml"
    if not event.is_tome():
        sender = event.get_user_id()

        with open(yml_path, "r", encoding="utf-8") as f:
            jrrp_log = yaml.load(f, Loader=yaml.FullLoader)

        today = datetime.date.today()
        if not jrrp_log['date'] == today:
            jrrp_log = {
                'date': today
            }

        if sender in jrrp_log.keys():
            rp = jrrp_log[sender]
        else:
            rp = randint(0, 100)
            jrrp_log[sender] = rp
            with open("src/plugins/jrrp/jrrp.yml", "w", encoding="utf-8") as f:
                yaml.dump(jrrp_log, f)

        msg = [
            {
                'type': 'at',
                'data': {
                    'qq': sender
                }
            },
            {
                'type': 'text',
                'data': {
                    'text': f'你今天的人品是 {rp}%'
                }
            }
        ]
        await jrrp.send(msg)

