from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain, Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

import json
import io
import re
import pymongo
import PIL.Image as Img
import imghdr
from extensions.load_config import load_config

__plugin_name__ = '数据库存储'
__plugin_usage__ = '存储每一条群聊数据'

bcc = Get.bcc()
config = load_config()

client = pymongo.MongoClient(config.db_host)


# noinspection PyTypeChecker
@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def log_to_database(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    log_info(group, member)
    log_message(message)

    _debug()
    pass






async def save_imgs(imgs):
    pic_fp = 'plugins/log_to_database/pic_cache/'
    for img in imgs:
        _img_bytes = await img.http_to_bytes()
        _img = Img.open(io.BytesIO(_img_bytes))
        _img_type = imghdr.what(file=None, h=_img_bytes)

        if _img_type == 'gif':
            # fixme 这种方法保存的 gif 帧间隔不变，导致速度不对
            pass
            # _gif_list = []
            # for i in range(_img.n_frames):
            #     _img.seek(i)
            #     _gif_list.append(_img)
            # _gif_list[0].save(pic_fp + img.imageId[1: -7] + '.' + _img_type, save_all=True, loop=True,
            #                   append_images=_gif_list[1:], duration=_img.info['duration'])
        else:
            _img.save(pic_fp + img.imageId[1: -7] + '.' + _img_type)


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


def log_message(message):
    pass


def log_text():
    pass


def log_picture():
    pass


def log_audio():
    pass


def _debug():
    db = client['InteractionObjects']
    groups_col = db['groups']
    users_col = db['users']

    print([x for x in groups_col.find()])
    print([x for x in users_col.find()])
