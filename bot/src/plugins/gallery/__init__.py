
from nonebot import on_command, on_startswith, on_regex, get_driver
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment
from src.extensions import CQ, get_config
from PicImageSearch import SauceNAO, Network

keys = ['vtb', 'th', 'vc', 'akn']

searching_by_pic = on_regex(r'pic*|sauce*|pixiv*', priority=10, block=False)
searching_by_text = on_command('setu', aliases={'色图', 'pixiv'}, priority=10, block=False)