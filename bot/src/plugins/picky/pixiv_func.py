import asyncio
import datetime
from collections import namedtuple
from typing import List, Tuple

from pixivpy_async import PixivClient, AppPixivAPI

from src.extensions import get_config, ImageType, proxies, get_image
from src.models.image import ImagePixiv, ImageTag, Image
from nonebot import logger
from peewee import fn
from pprint import pprint
import random

"""
sanity_level
    2 -> Completely SFW
    4 -> Moderately ecchi e.g. beach bikinis, slight upskirts
    6 -> Very ecchi e.g. more explicit and suggestive themes

x_restrict
    1 -> R18 e.g. nudity and penetration
"""

Page = namedtuple('Page', ['image', 'image_pixiv'])


def safety_illust(_img):
    return _img['type'] == 'illust' and _img['sanity_level'] < 5


async def _save_page(illust, app, page):
    img_p: ImagePixiv
    image_type = ImageType.pixiv
    url = illust['meta_single_page']['original_image_url'] if illust['page_count'] == 1 \
        else illust['meta_pages'][page]['image_urls']['original']

    img_sql = await get_image(
        url=url,
        filename=f"pixiv_{illust['id']}_p{page}",
        img_type=image_type,
        _proxies=proxies,
        app=app
    )

    img_p, create = ImagePixiv.get_or_create(
        image_id=img_sql.id
    )

    if img_sql.file_existed:

        if create:
            img_p.pixiv_id = illust['id']
            img_p.author_id = illust['user']['id']
            img_p.title = illust['title']
            img_p.illust_type = illust['type']
            img_p.page_count = illust['page_count']
            img_p.page = page
            img_p.sanity_level = illust['sanity_level']
            img_p.x_restrict = illust['x_restrict']
            img_p.image_url = url
            img_p.create_date = illust['create_date']

            ImageTag.insert_many(
                [dict(image_id=img_sql.id, tag_source=image_type.value, tag=tag['name']) for tag in illust['tags']]
            ).execute()

        img_p.bookmarks = illust['total_bookmarks']
        img_p.view = illust['total_view']
        img_p.save()

    return Page(image=img_sql, image_pixiv=img_p)


async def save_pixiv_img(illust, app):
    _ = await asyncio.gather(
        *[_save_page(illust, app, page) for page in range(illust['page_count'])]
    )
    return _


async def refresh_daily_pixiv(offset_total=1):

    logger.info(f'pixiv 每日热图更新中 ...')

    # refresh_token = get_config('picky')['refresh_token']
    # st = datetime.datetime.now()
    #
    # async with PixivClient(proxy=proxies) as client:
    #     app = AppPixivAPI(client=client)
    #     await app.login(refresh_token=refresh_token)
    #
    #     await asyncio.gather(
    #         *[save_pixiv_img(ill, app) for ill in
    #           sum([(await app.illust_ranking(mode="week", date=None, offset=offset))['illusts'] for offset in
    #                range(offset_total)], [])]
    #     )
    #
    # logger.info(f'pixiv 每日热图更新完成 耗时 {datetime.datetime.now() - st}')


async def search_pixiv(text):
    refresh_token = get_config('picky')['refresh_token']

    async with PixivClient(proxy=proxies) as client:
        app = AppPixivAPI(client=client)
        await app.login(refresh_token=refresh_token)
        illusts = await app.search_illust(text)
        illusts = [i for i in illusts['illusts'] if safety_illust(i)]
        if len(illusts) - 1 == 0:
            return []
        illusts = illusts[random.randint(0, len(illusts)-1)]
        page_all = await save_pixiv_img(illusts, app)
        if any(page.image.file_existed for page in page_all):
            return [f'{page.image.filename}.{page.image.suffix}' for page in page_all]
        else:
            return []
