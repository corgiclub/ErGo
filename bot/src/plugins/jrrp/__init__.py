import httpx
import os
import math
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, Message
import yaml
from datetime import datetime, date

jrrp = on_command('jrrp', priority=10, block=False)


@jrrp.handle()
async def _(bot: Bot, event: Event, state: T_State):
    yml_path = "src/shared_data/jrrp.yml"

    # if not event.is_tome():
    sender = event.get_user_id()
    if os.path.exists(yml_path):
        with open(yml_path, 'r', encoding="utf-8") as fi:
            jrrp_log = yaml.load(fi, Loader=yaml.FullLoader)

        today = date.today()
        if not jrrp_log['date'] == today:
            jrrp_log = {
                'date': today
            }
    else:
        jrrp_log = {
                    'date': date.today()
                }

    if sender in jrrp_log.keys():
        rp = jrrp_log[sender]
    else:
        rp = await get_normal_random(qq=int(event.get_user_id()))
        jrrp_log[sender] = rp
        with open(yml_path, 'w', encoding="utf-8") as fi:
            yaml.safe_dump(jrrp_log, fi, encoding='utf-8', allow_unicode=True)

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
                'text': f'你今天的人品是 {rp}%'
            }
        }
    ])
    await jrrp.send(msg)


async def get_normal_random(mu=50, sig=50, limit=(0, 100), qq: int = 0):

    data_type = 'uint16'
    data_one = 65536
    array_length = 1

    anu_api_url = f'https://qrng.anu.edu.au/API/jsonI.php?length={array_length}&type={data_type}'
    resp = httpx.get(anu_api_url)

    x1 = resp.json()['data'][0]    # x_1, x_2 \in U(0, 65536)
    x2 = get_rp(qq)
    x1 /= data_one
    x2 /= data_one
    z = (-2 * math.log(x1)) ** 0.5 * math.cos(2 * math.pi * x2)
    x = z * sig + mu

    if limit[0] < x < limit[1]:
        return round(x)
    else:
        return await get_normal_random(mu, sig, limit)


def get_rp(qq: int):
    date1 = datetime.strptime("1970-01-01", "%Y-%m-%d")
    date2 = datetime.today()
    days = (date2 - date1).days
    random = round((qq + 101 * days) * days)
    rp_num = random % 65536
    return rp_num
