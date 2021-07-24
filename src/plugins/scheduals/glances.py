import httpx
from pprint import pprint
from enum import Enum
import os
from .config import Config

cfg = Config().Glances()


def gb(x):
    return f'{x // 1073741824:d}'


def get_load(api):
    r = httpx.get(api + 'load')
    if r.status_code == 200:
        dic = r.json()
        msg = f'负载: {dic["min1"]} {dic["min5"]} {dic["min15"]} / {dic["cpucore"]} 核'
        return msg
    else:
        return f'❌ 负载: 读取失败 {r.status_code}'


def get_mem(api):
    r = httpx.get(api + 'mem')
    if r.status_code == 200:
        dic = r.json()
        msg = f'内存: {gb(dic["available"])} / {gb(dic["total"])} GB'
        if dic['percent'] > cfg.memory_warning:
            msg = '⚠️' + msg
        return msg
    else:
        return f'❌内存: 读取失败'


def get_gpu(api):
    r = httpx.get(api + 'gpu')
    if r.status_code == 200:
        dic = r.json()
        if dic == list():
            t = os.popen('nvidia-smi').read().split('\n')
            if len(t) <= 2:
                return '⚠️显卡: 读取为空，无显卡 / 需要检查驱动状态'
            else:
                return f'❌显卡: 读取失败，错误未知'
        else:
            msg = f'显卡: \n' + \
                  f'{dic[0]["name"]}: {dic[0]["proc"]:>3d}% {dic[0]["mem"] * 24}/24GB {dic[0]["temperature"]}℃\n' + \
                  f'{dic[1]["name"]}: {dic[1]["proc"]:>3d}% {dic[1]["mem"] * 24}/24GB {dic[1]["temperature"]}℃'
            if dic[0]["temperature"] > cfg.gpu_warning_temp or dic[0]["temperature"] > cfg.gpu_warning_temp:
                msg = '⚠️' + msg
            return msg
    else:
        return f'显卡: 读取失败 {r.status_code}'


def get_file_sys(api):
    r = httpx.get(api + 'fs')
    if r.status_code == 200:
        dic = r.json()
        pprint(dic)
        if api == cfg.corgitech_api:
            msg = f'硬盘:\n' + \
                  f'{dic[0]["device_name"]} {gb(dic[0]["used"])} / {gb(dic[0]["used"])} GB\n' + \
                  f'{dic[10]["device_name"]} {gb(dic[10]["used"])} / {gb(dic[10]["size"])} GB'
        else:
            # todo nas硬盘
            msg = '🐛硬盘: 开发中'

        if max([d['percent'] for d in dic if d['size'] > 1073741824 * 120]) > cfg.file_sys_warning:
            msg = '⚠️' + msg
        return msg
    else:
        return f'❌硬盘: 读取失败'


print(get_file_sys(cfg.corgitech_api))
