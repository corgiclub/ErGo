import asyncio
from bilibili_api import video
from pprint import pprint


async def main():
    # 实例化 Video 类
    v = video.Video(aid=3337)
    # 获取信息
    info = await v.get_info()
    # 打印信息
    pprint(info)
    return info

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
