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

__plugin_name__ = '键值响应'
__plugin_usage__ = '根据键值对回复'

bcc = Get.bcc()


# noinspection PyTypeChecker
@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def video_info(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):

    pic_fp = 'plugins/log_to_database/pic_cache/'

    if message.has(Image):
        imgs = message.get(Image)
        for img in imgs:
            _img_bytes = await img.http_to_bytes()
            _img = Img.open(io.BytesIO(_img_bytes))
            _img_type = imghdr.what(file=None, h=_img_bytes)

            if _img_type == 'gif':
                _gif_list = []
                for i in range(_img.n_frames):
                    _img.seek(i)
                    _gif_list.append(_img)
                _gif_list[0].save(pic_fp + img.imageId[1: -7] + '.' + _img_type, save_all=True, loop=True,
                                  append_images=_gif_list[1:], duration=_img.info['duration'])
            else:
                _img.save(pic_fp + img.imageId[1: -7] + '.' + _img_type)






#todo 开发中

