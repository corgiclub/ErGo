import os
import yaml


class CFG(dict):
    def __init__(self, entries: dict):
        self.__dict__.update({k: CFG(v) if isinstance(v, dict) else v for k, v in entries.items()})
        super(CFG, self).__init__(self.__dict__)


def load_config(name=None):
    """
    加载配置，要求文件名调用该函数的文件名与 config/ 文件夹下的配置文件相同。

    :return: class Config
    """
    if not name:
        name = os.getcwd().split('/')[-1]
    config_yaml = yaml.load(open('../../config/'+name+'.yml', 'r'), Loader=yaml.FullLoader)

    return CFG(config_yaml)


if __name__ == '__main__':
    load_config(name='dev')
