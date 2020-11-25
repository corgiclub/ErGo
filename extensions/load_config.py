import os
import json
import inspect


class Cfg(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


def load_config() -> object:
    """
    加载配置，要求文件名调用该函数的文件名与 config/ 文件夹下的配置文件相同。

    :return: class Config
    """
    path = inspect.stack()[1][1]
    name = os.path.basename(path)[:-3] if os.path.basename(path)[:-3] != '__init__' else os.path.basename(path[:-12])
    config_json = json.load(open('config/'+name+'.json', 'r'))

    return Cfg(**config_json)
