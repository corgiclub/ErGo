import math
from asyncio import get_running_loop
from datetime import datetime, timedelta
from src.extensions import coolperm

import httpx
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment

jrrp = on_command('jrrp', priority=10, block=False)

rp_today = {}


@jrrp.handle(parameterless=[coolperm('.jrrp')])
async def _(event: Event):
    sender = event.get_user_id()

    if sender in rp_today.keys():
        rp = rp_today[sender]
    else:
        rp = await get_normal_random(qq=int(event.get_user_id()))
        rp_today[sender] = rp

        now = datetime.now()
        tomorrow = datetime(now.year, now.month, now.day, 0, 0, 0) + timedelta(days=1)
        rest_time = (tomorrow - now).seconds

        loop = get_running_loop()
        loop.call_later(rest_time, lambda: rp_today.pop(sender))

    msg = Message([
        MessageSegment.at(sender),
        MessageSegment.text(f'你今天的人品是 {rp}%')
    ])

    await jrrp.send(msg)


async def get_normal_random(mu=50, sig=50, limit=(0, 100), qq: int = 0):
    data_type = 'uint16'
    data_one = 65536
    array_length = 1

    anu_api_url = f'http://qrng.anu.edu.au/API/jsonI.php?length={array_length}&type={data_type}'
    resp = httpx.get(anu_api_url,)

    x1 = resp.json()['data'][0]  # x_1, x_2 \in U(0, 65536)
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
