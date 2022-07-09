import httpx
from pprint import pprint
from enum import Enum
import os
from .config import Glances


cfg = Glances()
GB = 1073741824


def b(x):
    x = float(x)
    if x > 1024 ** 4:
        return f'{x / 1024 ** 4:>8.2f} TB'
    else:
        return f'{x / 1024 ** 3:>8.2f} GB'


async def get_load(api) -> str:
    r = httpx.get(api + 'load')
    if r.status_code == 200:
        dic = r.json()
        msg = f'CPU Intel Core i9-7960X 负载:\n┗{dic["min1"]} {dic["min5"]} {dic["min15"]} / {dic["cpucore"]}'
        return msg
    else:
        return f'❌ 处理器: 读取失败 {r.status_code}'


async def get_temperature(api) -> str:
    r = httpx.get(api + 'sensors')
    if r.status_code == 200:
        dic = r.json()
        msg = f'CPU 温度:\n' + \
              '\n'.join([f'┗{d["label"]} - {d["value"]}℃' for d in dic if d["label"] == "Package id 0"])
        for d in dic:
            if d['value'] > cfg.cpu_warning_temp:
                msg += f'\n⚠️{d["label"]} - {d["value"]}℃ 温度过高'

        return msg


async def get_mem(api) -> str:
    r = httpx.get(api + 'mem')
    if r.status_code == 200:
        dic = r.json()
        msg = f'内存:\n┗{b(dic["used"])} / {b(dic["total"])}'
        if dic['percent'] > cfg.memory_warning:
            msg = '⚠️' + msg
        return msg
    else:
        return f'❌内存: 读取失败'


async def get_gpu(api) -> str:
    r = httpx.get(api + 'gpu')
    if r.status_code == 200:
        dic = r.json()
        # pprint(dic)
        if dic == list():
            t = os.popen('nvidia-smi').read().split('\n')
            if len(t) <= 2:
                return '⚠️显卡: 无显卡 / 需要检查驱动状态'
            else:
                return f'❌显卡: 读取失败，错误未知'
        else:
            msg = f'显卡: \n' + \
                  '\n'.join([f'┃{d["gpu_id"]} {d["name"]}\n┗{d["proc"]:>2d}% {d["mem"] * 0.24:>4.1f}/24GB'
                             f' {d["temperature"]}℃' for d in dic])

            if max(d['temperature'] for d in dic) > cfg.gpu_warning_temp:
                msg = '⚠️' + msg
            return msg
    else:
        return f'❌显卡: 读取失败 {r.status_code}'


async def get_file_sys(api) -> str:
    r = httpx.get(api + 'fs')
    if r.status_code == 200:
        dic = r.json()
        dic = [d for d in dic if d["size"] > 128 * GB]
        if api == cfg.corgitech_api:
            msg = f'硬盘:\n' + \
                  '\n'.join([f'┃{d["mnt_point"]}\n┗{b(d["used"])} / {b(d["size"])}' for d in dic]) + \
                  '\n' + \
                  '\n'.join([f'┃{d.split()[-1]}\n┗{b(float(d.split()[2])*1024)} / {b(float(d.split()[1])*1024)}'
                             for d in os.popen('df | grep 192.168').read().split('\n')[:-1]])
        else:
            # todo nas硬盘
            msg = '🐛硬盘: 开发中'

        if max([d['percent'] for d in dic]) > cfg.file_sys_warning:
            msg = '⚠️' + msg
        return msg
    else:
        return f'❌硬盘: 读取失败'


async def get_sys_info(api=cfg.corgitech_api):
    msg = '\n'.join((await get_load(api), await get_temperature(api), await get_mem(api), await get_gpu(api), await get_file_sys(api)))
    return msg
