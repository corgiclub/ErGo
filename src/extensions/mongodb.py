from pymongo import MongoClient
from src.extensions.config import MongoDB
from src.extensions.utils import PicSource
from src.extensions.imghdr_byte import what
import httpx
import os
import cv2
from .utils import get_img_phash
import numpy as np
from typing import Optional


cfg = MongoDB()
client = MongoClient(cfg.host)


def test():
    db = client['test']
    col = db['test_table']
    data = {
        'data': 'test'
    }
    return col.insert_one(data)


def get_collection(db_name: str, col_name: str):
    return client[db_name][col_name]


async def log_picture(file: str, url: str, source: PicSource, base_pic_path: str = cfg.base_path + 'picture',
                      **kwargs):
    col = get_collection('picture', source)
    # print(0)
    if not col.find_one({"file": file}):
        line = {
            "file": file,
        }
        res = httpx.get(url)
        if res.status_code == 200:
            pic = res.content

            suffix = what(pic)
            path = f"{base_pic_path}/{source}/"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path+f"{file}.{suffix}", 'wb') as fi:
                fi.write(pic)
            line["suffix"] = suffix
            line["phash"] = get_img_phash(cv2.imdecode(np.frombuffer(pic, np.uint8), cv2.IMREAD_COLOR))
        else:
            line["failure"] = True

        col.insert_one(line)


async def log_audio(file: str, url: str, source='chat', base_pic_path: str = cfg.base_path + 'audio',
                    **kwargs):

    col = get_collection('audio', source)

    if not col.find_one({"file": file}):
        line = {
            "file": file,
        }
        res = httpx.get(url)
        if res.status_code == 200:
            aud = res.content
            path = f"{base_pic_path}/{source}/"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(f"{path}{file}", 'wb') as fi:
                fi.write(aud)
        else:
            line["failure"] = True

        col.insert_one(line)


# async def log_video(file: str, source='chat', base_pic_path: str = cfg.base_path + 'video',
#                     **kwargs):
#
#     col = get_collection('video', source)
#
#     if not col.find_one({"file": file}):
#         line = {
#             "file": file,
#         }
#         res = httpx.get(file)
#         if res.status_code == 200:
#             vid = res.content
#             path = f"{base_pic_path}/{source}/"
#             if not os.path.exists(path):
#                 os.makedirs(path)
#             with open(f"{path}{file}", 'wb') as fi:
#                 fi.write(vid)
#         else:
#             line["failure"] = True
#
#         col.insert_one(line)
