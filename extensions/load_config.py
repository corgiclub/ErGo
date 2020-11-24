import os
import json
import inspect


class Cfg:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def load_config():

    name = os.path.basename(inspect.stack()[1][1])[:-3]
    config_json = json.load(open('config/'+name+'.json', 'r'))

    return Cfg(**config_json)

