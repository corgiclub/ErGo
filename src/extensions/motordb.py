# from motor.motor_asyncio import AsyncIOMotorClient
# from src.extensions.config import MongoDB
# from src.extensions.utils import PicSource
# from src.extensions.imghdr_byte import what
# import httpx
# import os
# import cv2
# from src.extensions.utils import get_img_phash
# from nonebot.adapters.cqhttp import Bot, Event, Message, MessageSegment
# from src.extensions.utils import PicSource, CQ
# import numpy as np
# import asyncio
# from typing import Tuple
# from nonebot.log import logger
#
#
# class MotorDB:
#     def __init__(self):
#         # loop = asyncio.get_event_loop()
#         # loop.run_until_complete(self._init())
#         asyncio.run(self._init())
#
#     async def _init(self):
#         self.cfg = MongoDB()
#         self.client = AsyncIOMotorClient(self.cfg.host)
#
#     async def async_get_pic(self, url, timeout=0) -> Tuple:
#         async with httpx.AsyncClient() as cli:
#             resp = await cli.get(url)
#             if resp.status_code == 200:
#                 pic = resp.content
#                 suffix = what(pic)
#                 if suffix in ('jpg', 'jpeg', 'png', 'bmp', None):
#                     phash = get_img_phash(cv2.imdecode(np.frombuffer(pic, np.uint8), cv2.IMREAD_COLOR))
#                 else:
#                     phash = None
#                 return pic, suffix, phash
#
#         if timeout < self.cfg.retry_times:
#             logger.info(f"图片获取失败 {timeout} 次，重试中，地址 {url}")
#             await asyncio.sleep(self.cfg.wait_time)
#             await self.async_get_pic(url, timeout+1)
#
#         logger.warning(f"图片获取失败 {self.cfg.retry_times} 次，停止重试，地址 {url}")
#         return None, None, None
#
#     async def process_line(self, msg: MessageSegment, user_id, message_id, group_id=None):
#         if group_id is None:
#             group_id = 'private'
#         if msg.type == CQ.Image:
#             await self.log_picture(msg.data['file'], msg.data['url'], group_id, 'chat')
#         if msg.type == CQ.Record:
#             await self.log_audio(msg.data['file'], msg.data['url'], group_id, 'chat')
#         return {
#             "mid": int(message_id),
#             "uid": user_id,
#             "type": msg.type,
#             "data": msg.data,
#         }
#
#     async def log_chat(self, messages: Message, user_id, message_id, group_id, self_id):
#         if group_id:
#             col = self.client['group_chat'][group_id]
#         else:
#             col = self.client['private_chat'][self_id]
#         tasks = []
#         for m in messages:
#             tasks.append(self.process_line(m, user_id, message_id, group_id))
#         print(tasks)
#         lines = await asyncio.gather(*tasks)
#         if lines:
#             loop = asyncio.get_event_loop()
#             loop.run_until_complete(col.insert_many(lines))
#             # await col.insert_many(lines)
#
#     async def log_picture(self, file: str, url: str, group_id: str, sub_path, base_pic_path=None,
#                           **kwargs):
#         if base_pic_path is None:
#             base_pic_path: str = self.cfg.base_path + 'picture'
#
#         col = self.client['picture'][group_id]
#         loop = asyncio.get_event_loop()
#
#         line_existed = await col.find_one({"file": file})
#         path = f"{base_pic_path}/{sub_path}/"
#         if not os.path.exists(path):
#             os.makedirs(path)
#
#         if line_existed:
#             if 'failed_url' in line_existed.keys():
#                 pic, suffix, phash = await self.async_get_pic(url)
#                 if pic:
#                     with open(path + f"{file}.{suffix}", 'wb') as fi:
#                         fi.write(pic)
#                     loop.run_until_complete(
#                         col.update_one({"file": file},
#                                        {
#                                            "$set": {
#                                                "suffix": suffix,
#                                                "phash": phash,
#                                                "failure": None
#                                            },
#                                            "$inc": {
#                                                "counts": 1
#                                            }
#                                        })
#                     )
#                 else:
#                     loop.run_until_complete(col.update_one({"file": file}, {"$inc": {"counts": 1}}))
#             else:
#                 loop.run_until_complete(col.update_one({"file": file}, {"$inc": {"counts": 1}}))
#         else:
#             line = {
#                 "file": file,
#             }
#             pic, suffix, phash = await self.async_get_pic(url)
#             if pic:
#                 with open(path + f"{file}.{suffix}", 'wb') as fi:
#                     fi.write(pic)
#                 line["suffix"] = suffix
#                 line["counts"] = 1
#                 if phash:
#                     line["phash"] = phash
#             else:
#                 line["failed_url"] = url
#
#             loop.run_until_complete(col.insert_one(line))
#
#     async def log_audio(self, file: str, url: str, group_id: str, sub_path, base_audio_path=None,
#                         **kwargs):
#         col = self.client['audio'][group_id]
#         if base_audio_path is None:
#             base_audio_path: str = self.cfg.base_path + 'audio'
#
#         if not col.find_one({"file": file}):
#             line = {
#                 "file": file,
#             }
#             res = httpx.get(url)
#             if res.status_code == 200:
#                 aud = res.content
#                 path = f"{base_audio_path}/{sub_path}/"
#                 if not os.path.exists(path):
#                     os.makedirs(path)
#                 with open(f"{path}{file}", 'wb') as fi:
#                     fi.write(aud)
#             else:
#                 line["failure"] = True
#
#             await col.insert_one(line)
