from motor.motor_asyncio import AsyncIOMotorClient
from src.extensions.config import MongoDB
from src.extensions.utils import PicSource
from src.extensions.imghdr_byte import what
import httpx
import os
import cv2
from src.extensions.utils import get_img_phash
from nonebot.adapters.cqhttp import Bot, Event, Message, MessageSegment
from src.extensions.utils import PicSource, CQ
import numpy as np
import asyncio
from typing import Tuple
from nonebot.log import logger

cfg = MongoDB()
client = AsyncIOMotorClient(cfg.host)


def get_collection(db_name: str, col_name: str):
    return client[db_name][col_name]


async def async_get_pic(url, timeout=0) -> Tuple:
    async with httpx.AsyncClient() as cli:
        resp = await cli.get(url)
        if resp.status_code == 200:
            pic = resp.content
            suffix = what(pic)
            if suffix in ('jpg', 'jpeg', 'png', 'bmp', None):
                phash = get_img_phash(cv2.imdecode(np.frombuffer(pic, np.uint8), cv2.IMREAD_COLOR))
            else:
                phash = None
            return pic, suffix, phash

    if timeout < cfg.retry_times:
        logger.info(f"图片获取失败 {timeout} 次，重试中，地址 {url}")
        await asyncio.sleep(cfg.wait_time)
        await async_get_pic(url, timeout+1)

    logger.warning(f"图片获取失败 {cfg.retry_times} 次，停止重试，地址 {url}")
    return None, None, None


async def process_line(msg: MessageSegment, user_id, message_id):
    if msg.type == CQ.Image:
        await log_picture(**msg.data, source=PicSource.Chat)
    if msg.type == CQ.Record:
        await log_audio(**msg.data)
    return {
        "mid": int(message_id),
        "uid": user_id,
        "type": msg.type,
        "date": msg.data,
    }


async def log_chat(messages: Message, user_id, message_id, collection):

    # lines = []
    # for m in messages:
    #     lines.append({
    #         "mid": int(message_id),
    #         "uid": user_id,
    #         "type": m.type,
    #         "date": m.data,
    #     })
    #     if m.type == CQ.Image:
    #         await log_picture(**m.data, source=PicSource.Chat)
    #     if m.type == CQ.Record:
    #         await log_audio(**m.data)

    tasks = []
    for m in messages:
        tasks.append(process_line(m, user_id, message_id))
    lines = await asyncio.gather(tasks)

    if lines:
        await collection.insert_many(lines)
    pass


async def log_picture(file: str, url: str, source: PicSource, base_pic_path: str = cfg.base_path + 'picture',
                      **kwargs):
    col = get_collection('picture', source)
    line_existed = await col.find_one({"file": file})
    path = f"{base_pic_path}/{source}/"
    if not os.path.exists(path):
        os.makedirs(path)

    if line_existed:
        if 'failed_url' in line_existed.keys():
            pic, suffix, phash = await async_get_pic(url)
            if pic:
                with open(path + f"{file}.{suffix}", 'wb') as fi:
                    fi.write(pic)
                await col.update_one({"file": file},
                                     {
                                         "$set": {
                                             "suffix": suffix,
                                             "phash": phash,
                                             "failure": None
                                         },
                                         "$inc": {
                                             "counts": 1
                                         }
                                     })
            else:
                await col.update_one({"file": file}, {"$inc": {"counts": 1}})
        else:
            await col.update_one({"file": file}, {"$inc": {"counts": 1}})
    else:
        line = {
            "file": file,
        }
        pic, suffix, phash = await async_get_pic(url)
        if pic:
            with open(path + f"{file}.{suffix}", 'wb') as fi:
                fi.write(pic)
            line["suffix"] = suffix
            line["counts"] = 1
            if phash:
                line["phash"] = phash
        else:
            line["failed_url"] = url

        await col.insert_one(line)


async def log_audio(file: str, url: str, source='chat', base_audio_path: str = cfg.base_path + 'audio',
                    **kwargs):

    col = get_collection('audio', source)

    if not await col.find_one({"file": file}):
        line = {
            "file": file,
        }
        res = httpx.get(url)
        if res.status_code == 200:
            aud = res.content
            path = f"{base_audio_path}/{source}/"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(f"{path}{file}", 'wb') as fi:
                fi.write(aud)
        else:
            line["failure"] = True

        await col.insert_one(line)
