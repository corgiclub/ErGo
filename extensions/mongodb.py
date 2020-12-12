import re
import pymongo
import requests
from extensions.load_config import load_config
from graia.application.message.elements.internal import *
from graia.application.message.chain import MessageChain
from mirai_core import loaded_plugins

config = load_config('log_to_database')
client = pymongo.MongoClient(config.db_host)


def log_info(group, member):
    db = client['InteractionObjects']
    groups_col = db['groups']
    users_col = db['users']

    if group_dict := groups_col.find_one({"group_id": group.id}):
        if group_dict['group_names'][-1] != group.name:
            group_names = group_dict['group_names'] + [group.name]
            groups_col.update_one({"group_id": group.id}, {'$set': {'group_names': group_names}})
    else:
        group_dict = {
            'group_id': group.id,
            'group_names': [group.name]
        }
        groups_col.insert_one(group_dict)

    if user_dict := users_col.find_one({"user_id": member.id}):
        if member.name not in user_dict['user_names']:
            user_names = user_dict['user_names'] + [member.name]
            users_col.update_one({"user_id": member.id}, {'$set': {'user_names': user_names}})
        if member.group.id not in user_dict['user_groups']:
            user_groups = user_dict['user_groups'] + [member.group.id]
            users_col.update_one({"user_id": member.id}, {'$set': {'user_groups': user_groups}})
    else:
        user_dict = {
            'user_id': member.id,
            'user_names': [member.name],
            'user_groups': [member.group.id]
        }
        users_col.insert_one(user_dict)


def log_message(message: MessageChain, group, member, is_bot=False):
    db = client['GroupChats']
    col = db[str(group.id)]

    message_list = []
    base_dict = {
        'user_id': member.id,
        'source': message.get(Source)[0].id,
        'is_instruction': is_instruction(message.asDisplay()),
        'is_bot': is_bot
        }

    for mes in message.__root__:
        line_dict = base_dict.copy()
        if isinstance(mes, Source):
            continue
        if isinstance(mes, Plain):
            if not mes.text.isspace():
                line_dict['type'] = 'Plain'
                line_dict['content'] = mes.text
            else:
                continue
        if isinstance(mes, Quote):
            line_dict['type'] = 'Quote'
            line_dict['content'] = mes.targetId
        if isinstance(mes, At):
            line_dict['type'] = 'At'
            line_dict['content'] = mes.target
        if isinstance(mes, AtAll):
            line_dict['type'] = 'AtAll'
            line_dict['content'] = None
        if isinstance(mes, Face):
            line_dict['type'] = 'Face'
            line_dict['content'] = mes.faceId
        if isinstance(mes, Image):
            line_dict['type'] = 'Image'
            line_dict['content'] = mes.imageId[1:-7]
            log_image('ImagesInGroupMessage', mes.imageId[1:-7], mes.url)
        if isinstance(mes, FlashImage):         # mirai 暂时不支持接收闪照
            continue
        if isinstance(mes, Voice):              # mirai 无法获取音频实际数据
            continue
        # mirai 的 Xml/Json/App/Poke 实际存储内容方式暂时不明
        if isinstance(mes, Xml):
            line_dict['type'] = 'Xml'
            line_dict['content'] = mes.xml
        if isinstance(mes, Json):
            line_dict['type'] = 'Json'
            line_dict['content'] = mes.Json
        if isinstance(mes, App):
            line_dict['type'] = 'App'
            line_dict['content'] = mes.content
        if isinstance(mes, Poke):
            line_dict['type'] = 'Poke'
            line_dict['content'] = mes.name
        message_list.append(line_dict)
        # print(message_list)

    if message_list:
        col.insert_many(message_list)


def log_image(db_name, id_, url):
    db = client['Images']
    col = db[db_name]

    if col.find_one({'image_id': id_}):
        col.update_one({'image_id': id_}, {'$inc': {'mentioned_times': 1}})
    else:
        col.insert_one({
            'image_id': id_,
            'content': requests.get(url).content,
            'mentioned_times': 1,
            'is_pron': is_pron()
        })


def is_instruction(text: str):

    for plugin in loaded_plugins:
        # print(plugin.pattern)
        if re.match(plugin.pattern, text):
            return True
    return False


def is_pron():
    return None


def log_debug(group):

    col = client['GroupChats'][str(group.id)]

    return str(next(col.aggregate([{'$sample': {'size': 1}}])))


def most_frequently_pic(group):

    col = client['Images']['ImagesInGroupMessage']

    return next(col.find().sort('mentioned_times', pymongo.DESCENDING))['content']
