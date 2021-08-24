from enum import Enum


def regex_equal(keywords) -> str:
    return '|'.join(('^'+k+'$' for k in keywords))


class PicSource(str, Enum):
    Chat = 'chat'
    ChatRecord = 'chat_record'
    Pixiv = 'pixiv'
    Twitter = 'twitter'
    SauceNAO = 'saucenao'


class CQ(str, Enum):
    """
        已进行数据库适配的CQ消息段类型
    """
    Text = 'text'
    Face = 'face'
    Image = 'image'
    Record = 'record'
    Video = 'video'
    At = 'at'
    Poke = 'poke'
    Anonymous = 'anonymous'
    Share = 'share'
    Contact = 'contact'
    Location = 'location'
    Reply = 'reply'
    Xml = 'xml'
    Json = 'json'
    Music = 'music'         # 只发送，不做适配
    Forward = 'forward'     # 需要适配转发消息
    Node = 'node'           # 格式复杂

