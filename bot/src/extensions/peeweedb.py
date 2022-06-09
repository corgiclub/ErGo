import asyncio
import os
from pathlib import Path


from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.log import logger
from peewee import *

from src.extensions.utils import CQ, ImageType, get_chat_image, pic_base_path
from src.models.chat import *
from src.models.image import *

base_path = pic_base_path


async def process_line(self, msg: MessageSegment, user_id, message_id, group_id=None):
    if group_id is None:
        group_id = 0
    if msg.type == CQ.Image:
        await self.save_image(msg.data['file'], msg.data['url'], group_id, group_id)
    if msg.type == CQ.Record:
        await self.log_audio(msg.data['file'], msg.data['url'], group_id, group_id)
    return {
        "mid": int(message_id),
        "uid": user_id,
        "type": msg.type,
        "data": msg.data,
    }


async def log_chat(messages: Message, user_id, message_id, group_id):
    # todo 改为真正的异步写法
    # 私聊消息 group_id == None
    if group_id is None:
        group_id = 0
    for msg in messages:
        type_str, type_id = CQ.get_type(msg.type)
        chat = Chat(group_id=group_id, user_id=user_id, message_id=message_id, type_id=type_id)
        chat_id = chat.save()
        if msg.type == CQ.text.name:
            ChatText.create(chat_id=chat_id, text=msg.data['text'])
        elif msg.type == CQ.face.name:
            ChatFace.create(chat_id=chat_id, face_id=int(msg.data['id']))
        elif msg.type == CQ.image.name:
            img_id = await save_chat_image(msg.data['file'], msg.data['url'], group_id, user_id)
            ChatImage.create(chat_id=chat_id, img_id=img_id, qq_hash=msg.data['file'].split('.')[0], url=msg.data['url'])
        elif msg.type == CQ.record.name:
            # todo
            pass
        elif msg.type == CQ.at.name:
            ChatAt.create(chat_id=chat_id, qq=int(msg.data['qq']))
        elif msg.type == CQ.poke.name:
            ChatPoke.create(chat_id=chat_id, type=msg.data['type'], poke_id=int(msg.data['id']), name=msg.data['name'])
        elif msg.type == CQ.share.name:
            ChatShare.create(chat_id=chat_id, url=msg.data['url'], title=msg.data['title'])
        elif msg.type == CQ.contact.name:
            ChatContact.create(chat_id=chat_id, type=msg.data['type'], contact_id=int(msg.data['id']))
        elif msg.type == CQ.location.name:
            ChatLocation.create(chat_id=chat_id, lat=float(msg.data['lat']), lot=float(msg.data['lot']))
        elif msg.type == CQ.reply.name:
            ChatReply.create(chat_id=chat_id, message_id=int(msg.data['id']))
        elif msg.type == CQ.forward.name:
            ChatForward.create(chat_id=chat_id, message_id=int(msg.data['id']))
        elif msg.type == CQ.xml.name:
            ChatXml.create(chat_id=chat_id, data=msg.data['data'])
        elif msg.type == CQ.json.name:
            ChatJson.create(chat_id=chat_id, data=msg.data['data'])
        elif msg.type == CQ.node.name:
            # todo
            pass
        else:
            pass


async def save_chat_image(file, url, group_id, user_id, img_path=ImageType.chat.name):
    """
        本函数要求文件名与已有文件无重复，仅用于存储 QQ 聊天图片
    """

    file = file.split('.')[0]   # 去除 .image 后缀
    img_path /= str(group_id) if group_id else str(user_id)

    try:
        img_chat_db: ImageChat = ImageChat.get(ImageChat.qq_hash == file)

    except ImageChat.DoesNotExist:
        img_db = Image(filename=file, type_id=ImageType.chat.value)
        img_db.file_existed, img_db.suffix = await get_chat_image(url, file, img_path)
        img_id = img_db.save()

        img_chat_db = ImageChat(image_id=img_id, qq_hash=file, qq_count=1)
        img_chat_db.save()

        return img_id
    else:
        ImageChat.update(qq_count=ImageChat.qq_count + 1).where(ImageChat.qq_hash == file)
        img_db: Image = Image.get(id=img_chat_db.image_id)

        if not img_db.file_existed:
            img_db.file_existed, img_db.suffix = await get_chat_image(url, file, img_path)
            img_db.save()

        return 0





if __name__ == '__main__':
    i = ImageChat.update(qq_count=ImageChat.qq_count + 1).where(ImageChat.qq_hash == 'file')
    print(i)


