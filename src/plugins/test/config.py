from pydantic import BaseSettings


class Config(BaseSettings):

    # plugin custom config
    # plugin_setting: str = "default"

    test_word: str = '测试'

