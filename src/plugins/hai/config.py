from pydantic import BaseSettings
from src.extensions.utils import regex_equal


class Config(BaseSettings):

    keywords: list = [
        '氦',
        'hi',
        'おはよ'
    ]

    regex: str = regex_equal(keywords)

