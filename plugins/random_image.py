from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain, Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

import os
import random
from PIL import Image as PILImage
from PIL.ExifTags import TAGS
IMG_PATH = "/ErGo/plugins/log_to_database/pic_cache"


__plugin_name__ = '来图'
__plugin_description__ = '随机发一张图'
__plugin_usage__ = '发送 来张图 获得一张缓存的图片'
__plugin_pattern__ = '来张图'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def random_image(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if message.asDisplay() == '来张图':
        try:
            files = os.listdir(IMG_PATH)
            filepaths = list(map(lambda filename: os.path.join(
                IMG_PATH, filename), files))

            # 选择随机图片
            random_img_path = random.choice(filepaths)
            random_img = PILImage.open(random_img_path)

            # 获取随机图片信息
            img_meta_info = ""
            img_exif_data = random_img.getexif()
            for tag_id in img_exif_data:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = img_exif_data.get(tag_id)
                # decode bytes
                if isinstance(data, bytes):
                    data = data.decode()
                img_meta_info += f"{tag:25}: {data} \n"

           # 返回信息
            await app.sendGroupMessage(group, MessageChain.create([
                Image.fromLocalFile(random_img_path),
                Plain("\n"),
                Plain(img_meta_info)
            ]))
        except ValueError:
            return
