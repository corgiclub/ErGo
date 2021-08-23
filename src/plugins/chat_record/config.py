from pydantic import BaseSettings
from nonebot.permission import SUPERUSER


class Config(BaseSettings):

    name: str = "聊天记录"
    help: str = "记录聊天记录，保证匿名的情况下用于数据分析"
    command: str = ""
    vision_level = SUPERUSER


