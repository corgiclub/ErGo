import datetime
import os
from enum import Enum
from pathlib import Path
from shutil import copyfile
from asyncio import sleep

import yaml
import nonebot
from nonebot import require, export, get_driver
from nonebot.log import logger
import httpx
from src.extensions.imghdr_byte import what
from src.models.image import Image
import asyncio

driver = get_driver()
pic_base_path = Path(r'D:\LuneZ99')


def get_config(key):
    return driver.config.__dict__[key]['config']


def regex_equal(keywords) -> str:
    return '|'.join(('^'+k+'$' for k in keywords))


class PicSource(str, Enum):
    Chat = 'chat'
    ChatRecord = 'chat_record'
    Pixiv = 'pixiv'
    Twitter = 'twitter'
    SauceNAO = 'saucenao'


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
    music = 14      # 只发送，不做适配
    forward = 15    # 需要适配转发消息
    node = 16       # 格式复杂

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

    img_sql = await get_image(url, file, path, img_type)

    if img_sql.file_existed:
        return img_sql

    if timeout < retry_times:
        logger.info(f"图片获取失败 {timeout} 次，重试中，地址 {url}")
        await asyncio.sleep(wait_time)
        return await get_chat_image(url, file, path, img_type, timeout + 1)

    return img_sql


async def get_image(url, file, path, img_type, proxies=None):
    img_sql, _ = Image.get_or_create(filename=file, type_id=img_type.value)

    async with httpx.AsyncClient(
        proxies=proxies
    ) as cli:
        resp = await cli.get(url)

        if resp.status_code == 200:
            img = resp.content
            suffix = what(img)
            if not os.path.exists(path):
                print(f'创建路径 {path}')
                os.makedirs(path)
            with open(path / f"{file}.{suffix}", 'wb') as fi:
                fi.write(img)

            img_sql.suffix = suffix
            img_sql.file_existed = True
            img_sql.update_time = datetime.datetime.now()
            img_sql.save()

    return img_sql

if __name__ == '__main__':
    
    pass

