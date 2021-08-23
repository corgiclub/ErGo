from pymongo import MongoClient
from src.extensions.config import MongoDB
from src.extensions.utils import PicSource
from src.extensions.imghdr_byte import what
import httpx
import os


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


async def log_picture(file: str, url: str, source: PicSource, base_pic_path: str = cfg.base_path + 'picture/'):
    col = get_collection('picture', source)
    if not col.find_one({"file": file}):
        line = {
            "file": file,
        }
        res = httpx.get(url)
        if res.status_code == 200:
            pic = res.content
            suffix = what(pic)
            path = f"{base_pic_path}{source}/{file}.{suffix}"
            with open(path, 'wb') as fi:
                fi.write(pic)
            line["suffix"] = suffix
        else:
            line["failure"] = True

        col.insert_one(line)
