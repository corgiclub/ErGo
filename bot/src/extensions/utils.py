import os
from enum import Enum
from pathlib import Path
from shutil import copyfile
from asyncio import sleep

import yaml
import nonebot
from nonebot import require, export, get_driver
from nonebot.log import logger



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



def ham_dist(a, b):
    """
        计算以 (二进制) 数字形式输入的汉明距离
    """
    return bin(a ^ b).count('1')


if __name__ == '__main__':
    
    pass

