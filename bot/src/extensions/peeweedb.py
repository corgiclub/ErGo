import asyncio
import datetime
import os
from pathlib import Path
import asyncio

from nonebot.adapters.onebot.v11 import Message, MessageSegment


from src.extensions.utils import CQ, ImageType, get_chat_image, pic_base_path
from src.models.chat import *
from src.models.image import *

base_path = pic_base_path


async def log_chat_once(msg, user_id, message_id, group_id):
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


async def log_chat(messages: Message, user_id, message_id, group_id):
    # todo 改为真正的异步写法
    # 私聊消息 group_id == None
    if group_id is None:
        group_id = 0
    await asyncio.gather(
        *[log_chat_once(msg, user_id, message_id, group_id) for msg in messages]
    )


async def save_chat_image(file, url, group_id, user_id, img_path=ImageType.chat.name):
    """
        本函数要求文件名与已有文件无重复，仅用于存储 QQ 聊天图片
    """

    file = file.split('.')[0]   # 去除 .image 后缀
    img_path = base_path / img_path
    img_path /= str(group_id) if group_id else str(user_id)

    img_sql = await get_chat_image(url, file, img_path)
    img_chat, _ = ImageChat.get_or_create(image_id=img_sql.id, qq_hash=file, session_id=group_id if group_id else user_id)
    img_chat.qq_count += 1
    img_chat.update_time = datetime.datetime.now()
    img_chat.save()

    return img_chat.id


if __name__ == '__main__':
    i = ImageChat.update(qq_count=ImageChat.qq_count + 1).where(ImageChat.qq_hash == 'file')
    print(i)


