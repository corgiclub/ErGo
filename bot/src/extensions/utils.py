import os
from enum import Enum
from pathlib import Path
from shutil import copyfile

import yaml
from nonebot import require, export
from nonebot.log import logger


def get_config(plugin_path, yaml_name='config.yml', default_name='config.yml.example'):
    plugin_path = Path(plugin_path)
    cfg_path = plugin_path.with_name(yaml_name)
    if os.path.exists(cfg_path):
        with open(cfg_path, 'r', encoding='utf-8') as fi:
            cfg = yaml.safe_load(fi)
            export()['config'] = cfg
            return cfg
    else:
        exp_path = plugin_path.with_name(default_name)
        if os.path.exists(exp_path):
            copyfile(exp_path, cfg_path)
            logger.warning(f'存在未配置的新插件 {plugin_path.parent}，自动加载配置中，自定义配置请至 web 管理页面修改')
            with open(cfg_path, 'r', encoding='utf-8') as fi:
                cfg = yaml.safe_load(fi)
                export()['config'] = cfg
                return cfg
        else:
            raise FileNotFoundError(f'{plugin_path.parent} 缺少 config.yml.example，请重新拉取 repo')


def get_permissions(plugin_path, permission_name='permissions.yml', default_name='permissions.yml.example'):
    plugin_path = Path(plugin_path)
    permission_path = plugin_path.with_name(permission_name)
    if os.path.exists(permission_path):
        permission = require('flexperm').register('test_plugin').preset(permission_path)
        export()['permissions'] = permission
        return permission
    else:
        exp_path = plugin_path.with_name(default_name)
        if os.path.exists(exp_path):
            copyfile(exp_path, permission_path)
            logger.warning(f'存在未配置的新插件 {plugin_path.parent}，自动加载权限中，自定义配置请至 web 管理页面修改')
            permission = require('flexperm').register('test_plugin').preset(permission_path)
            export()['permissions'] = permission
            return permission
        else:
            raise FileNotFoundError(f'{plugin_path.parent} 缺少 permissions.yml.example，请重新拉取 repo')


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

