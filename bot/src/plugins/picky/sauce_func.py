import asyncio
from pprint import pprint

from PicImageSearch import SauceNAO, Network
from pixivpy_async import PixivClient, AppPixivAPI

from src.extensions import get_config, pic_base_path, ImageType, proxies, get_image
from src.models.image import ImageSauce





async def search_sauce(pic):
    saucenao_api_key = get_config('picky')['saucenao_api_key']
    proxies = None
    print(proxies)

    async with Network(
            proxies=proxies
    ) as client:
        sauce = SauceNAO(client=client, api_key=saucenao_api_key, minsim=85)
        resp = await sauce.search(pic)
        # from pprint import pprint
        # pprint(resp.raw[0].origin)
        if len(resp.raw) > 0 and resp.raw[0].similarity > 85:
            img = resp.raw[0]
            url_thumbnail = img.thumbnail
            img_sql = await get_image(url=url_thumbnail,
                                      filename=img.index_name.split(' ')[-1].split('.')[0],
                                      path=pic_base_path / ImageType.saucenao.name,
                                      img_type=ImageType.saucenao,
                                      _proxies=proxies)
            ImageSauce.get_or_create(
                similarity=img.similarity,
                thumbnail=img.thumbnail,
                index_id=img.index_id,
                index_name=img.index_name,
                title=img.title,
                url=img.url,
                author=img.author,
                pixiv_id=img.pixiv_id,
                member_id=img.member_id,
                image_id=img_sql.id
            )
            img_path = pic_base_path / f"{ImageType.saucenao.name}/{img_sql.filename}.{img_sql.suffix}"
            return img, img_path, resp.long_remaining > 0
        else:
            return None, '', resp.long_remaining > 0


