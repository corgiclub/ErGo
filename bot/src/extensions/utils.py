import asyncio
import datetime
import os
import sys
from enum import Enum
from pathlib import Path
from glob import glob

import httpx
from nonebot import get_driver
from nonebot.log import logger

from src.extensions.imghdr_byte import what
from src.models.image import Image

from pixivpy_async import PixivClient, AppPixivAPI

driver = get_driver()
pic_base_path = Path(driver.config.pic_base_path)
proxies = driver.config.proxies


def get_config(key):
    return driver.config.__dict__[key]['config']


def regex_startswith_key_with_image(keywords):
    return '.*CQ:image.*|'.join(keywords) + '.*CQ:image.*'


def regex_equal(keywords) -> str:
    return '|'.join(('^' + k + '$' for k in keywords))


class CQ(Enum):
    """
        已进行数据库适配的CQ消息段类型
    """
    text = 1
    face = 2
    image = 3
    record = 4
    video = 5
    at = 6
    poke = 7
    anonymous = 8
    share = 9
    contact = 9
    location = 10
    reply = 11
    xml = 12
    json = 13
    music = 14  # 只发送，不做适配
    forward = 15  # 需要适配转发消息
    node = 16  # 格式复杂

    @classmethod
    def get_type(cls, msg_type):
        for name, member in cls.__members__.items():
            if msg_type == name:
                return member.name, member.value
        return KeyError, '无法找到该 CQ code 类型'


class ImageType(Enum):
    chat = 1
    saucenao = 2
    pixiv = 3
    gallery = 4


def ham_dist(a, b):
    """
        计算以 (二进制) 数字形式输入的汉明距离
    """
    return bin(a ^ b).count('1')


async def get_chat_image(url, file, path, img_type=ImageType.chat, timeout=0, retry_times=5, wait_time=5):
    """

    获取聊天消息中的图片并保存
    url: image.url
    file: image.file
    path: 存储目录
    """
    path = Path(pic_base_path) / path

    if not os.path.exists(path):
        os.makedirs(path)

    img_sql = await get_image(url, file, img_type, path)

    if img_sql.file_existed:
        return img_sql

    if timeout < retry_times:
        logger.info(f"图片获取失败 {timeout} 次，重试中，地址 {url}")
        await asyncio.sleep(wait_time)
        return await get_chat_image(url, file, path, img_type, timeout + 1)

    return img_sql


async def get_image(url, filename, img_type, path=None, _proxies=None, app: AppPixivAPI = None):
    img_sql, _ = Image.get_or_create(filename=filename, type_id=img_type.value)

    if not img_sql.file_existed:
        if not path:
            path = pic_base_path / img_type.name
        if not os.path.exists(path):
            print(f'创建路径 {path}')
            os.makedirs(path)

        if img_type == ImageType.pixiv:
            try:
                await app.download(url, name=filename, path=path)
                suffix = glob(str(path/filename)+'*')[0].split('.')[-1]
                file_existed = True
            except asyncio.exceptions.TimeoutError as e:
                suffix = ''
                file_existed = False
                logger.warning(f'图片获取错误 - {img_type} - {e}')
        else:
            async with httpx.AsyncClient(proxies=_proxies) as cli:
                resp = await cli.get(url)
                if resp.status_code == 200:
                    img = resp.content
                    suffix = what(img)
                    file_existed = True
                    with open(path / f"{filename}.{suffix}", 'wb') as fi:
                        fi.write(img)
                else:
                    logger.warning(f'图片获取错误 - {img_type} - http code {resp.status_code}')
                    suffix = ''
                    file_existed = False

        img_sql.suffix=suffix
        img_sql.file_existed=file_existed
        img_sql.save()

    return img_sql


if __name__ == '__main__':
    pass
