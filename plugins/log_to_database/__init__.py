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
import PIL.Image as Img
import imghdr
from extensions.load_config import load_config

__plugin_name__ = '数据库存储'
__plugin_usage__ = '存储每一条群聊数据'

bcc = Get.bcc()
# config = load_config()


# noinspection PyTypeChecker
@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def log_to_database(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):

    pic_fp = 'plugins/log_to_database/pic_cache/'

    if message.has(Image):
        imgs = message.get(Image)
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

