import httpx
import os
import nonebot
import math

from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, Message
from random import randint
import yaml
import datetime

# from .config import Config

# cfg = Config()

jrrp = on_command('jrrp')


@jrrp.handle()
async def _(bot: Bot, event: Event, state: T_State):
    yml_path = "src/plugins/jrrp/jrrp.yml"

    if not event.is_tome():
        sender = event.get_user_id()
        if os.path.exists(yml_path):
            with open(yml_path, 'r', encoding="utf-8") as f:
                jrrp_log = yaml.load(f, Loader=yaml.FullLoader)
            today = datetime.date.today()
            if not jrrp_log['date'] == today:
                jrrp_log = {
                    'date': today
                }
        else:
            jrrp_log = {
                'date': datetime.date.today()
            }

        if sender in jrrp_log.keys():
            rp = jrrp_log[sender]
        else:
            rp = await get_normal_random()
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


async def get_normal_random(mu=50, sig=25, limit=(0, 100)):

    data_type = 'uint16'
    data_one = 65536
    array_length = 2

    anu_api_url = f'https://qrng.anu.edu.au/API/jsonI.php?length={array_length}&type={data_type}'
    resp = httpx.get(anu_api_url)

    x1, x2 = resp.json()['data']    # x_1, x_2 \in U(0, 65536)
    x1 /= data_one
    x2 /= data_one
    z = (-2 * math.log(x1)) ** 0.5 * math.cos(2 * math.pi * x2)
    x = z * sig + mu

    if limit[0] < x < limit[1]:
        return round(x)
    else:
        return await get_normal_random(mu, sig, limit)
