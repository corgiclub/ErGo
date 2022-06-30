import asyncio
import os
from pathlib import Path

import nonebot
import yaml
from nonebot.log import logger
from nonebot import require, get_driver
from models.image import Image
from src.extensions import ImageType, download_image, pic_base_path
from pixivpy_async import PixivClient, AppPixivAPI

driver = get_driver()
proxies = driver.config.proxies

driver = nonebot.get_driver()
monitor_live = require('bililive').monitor_live
test_picky = require('picky').test
refresh_daily_pixiv = require("picky").refresh_daily_pixiv


@driver.on_startup
async def start_up():
    await load_configs()
    await monitor_live()


@driver.on_bot_connect
async def bot_connect():
    await refresh_daily_pixiv()
    await fix_image_library()


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


async def fix_image_library():
    async def fix_image(q: Image):
        image_type = ImageType.get_type(q.type_id)
        if q.fix_count > 10:
            q.file_existed = False
            q.save()
            return 0, 0
        if not os.path.exists(pic_base_path / image_type.name / f'{q.filename}.{q.suffix}'):
            if image_type == ImageType.pixiv:
                async with PixivClient(proxy=proxies) as client:
                    app = AppPixivAPI(client=client)
                    await download_image(q.url, q.filename, image_type, app=app)
            else:
                await download_image(q.url, q.filename, image_type)
            q.fix_count += 1
            if os.path.exists(pic_base_path / image_type.name / f'{q.filename}.{q.suffix}'):
                q.file_existed = True
                q.save()
                return 1, 1
            else:
                q.file_existed = False
                q.save()
                return 1, 0
        else:
            q.file_existed = True
            q.save()
            return 0, 0

    query = Image.select()
    count = await asyncio.gather(
        *[fix_image(q) for q in query]
    )
    logger.info(f'尝试修复了 {sum(c[0] for c in count)} 张图片, 共修复了 {sum(c[1] for c in count)} 张图片')
