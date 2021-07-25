from pydantic import BaseSettings


class Config(BaseSettings):

    # plugin custom config
    # plugin_setting: str = "default"

    keywords: list = [
        '氦',
        'Hi',
        '嗨',
        'はい'
    ]

    test_word: str = '测试'

