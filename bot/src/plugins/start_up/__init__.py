import os
from pathlib import Path

import nonebot
import yaml
from nonebot.log import logger
from nonebot import require

driver = nonebot.get_driver()
monitor_live = require('bililive').monitor_live
test_picky = require('picky').test
refresh_daily_pixiv = require("picky").refresh_daily_pixiv


@driver.on_startup
async def start_up():
    await load_configs()
    await monitor_live()
    await refresh_daily_pixiv()


async def load_configs():
    plugins = nonebot.get_loaded_plugins()
    names = [p.name for p in plugins]
    paths = ['src/config' / Path(p.name).with_suffix('.yml') for p in plugins]
    paths_example = ['src/config.example' / Path(p.name).with_suffix('.yml') for p in plugins]
    for n, p, pe in zip(names, paths, paths_example):
        if not os.path.exists(p):
            logger.warning(f'插件 {n} 的自定义配置文件不存在，尝试加载示例配置，'
                           f'若希望使用自定义配置或写入隐私信息，请参照 {pe} 的内容在 {p} 编写自定义配置，'
                           f'希望使用默认配置可忽略该警告')
            p = pe
        try:
            driver.config.__dict__.setdefault(n, yaml.safe_load(open(p, 'r', encoding='utf-8')))
        except FileNotFoundError:
            logger.warning(f'插件 {n} 的默认配置文件不存在，读取将被跳过，请开发者检查 {pe} 文件完整性')
        else:
            logger.info(f'成功读取了配置文件 {p}')
