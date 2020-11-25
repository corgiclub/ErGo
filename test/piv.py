import asyncio
from pixivpy_async import *


async def main():
    async with PixivClient() as client:
        aapi = AppPixivAPI(client=client)
        await aapi.login("user_mpfv2437", "zhaoyinzhi?..")
        p = await aapi.illust_detail(59580629)
        print(p)

asyncio.run(main())

# from pixivpy3 import *
#
# api = AppPixivAPI()
# # api.login("username", "password")   # Not required
#
# # get origin url
# json_result = api.illust_detail(59580629)
# illust = json_result.illust
# print(">>> origin url: %s" % illust.image_urls['large'])
