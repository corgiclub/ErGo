import re

from PicImageSearch import SauceNAO, Network
from nonebot import on_command, on_regex
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment

from src.extensions import CQ, get_config, pic_base_path, ImageType, proxies, coolperm, get_image, \
    regex_startswith_key_with_image
from src.models.image import ImageSauce

searching_by_pic = on_regex(regex_startswith_key_with_image(['search', 'pic']), flags=re.S, priority=10, block=False)
searching_by_text = on_command('setu', aliases={'色图', 'pixiv'}, priority=10, block=False)


@searching_by_pic.handle(parameterless=[coolperm('.searching_by_pic')])
async def _(event: Event):
    message = event.get_message()
    pic_count = sum([msg.type == CQ.image.name for msg in message])
    if pic_count == 0:
        return
    elif pic_count > 1:
        await searching_by_pic.send(MessageSegment.text('查询的图片过多，请一张张查询哦'))
    else:
        for msg in message:
            if msg.type == CQ.image.name:
                img, img_path, remaining = await search_sauce(msg.data['url'])
                if not remaining:
                    # todo 收款码
                    await searching_by_pic.send(MessageSegment.text(f"今日 API 调用次数超限，"
                                                                    f"有兴趣的话可以赞助开发者付费 API 费用哦"))
                if img:
                    await searching_by_pic.send(
                        Message([
                            MessageSegment.image(file=img_path),
                            MessageSegment.text(
                                f"\n{img.title}\n作者：{img.author}\n{img.url}".replace('\n\n', '\n').strip('\n')
                            ),
                        ])
                    )
                else:
                    await searching_by_pic.send(MessageSegment.text(f"未搜到相似图片"))


async def search_sauce(pic):
    saucenao_api_key = get_config('picky')['saucenao_api_key']
    async with Network(
            proxies=proxies
    ) as client:
        sauce = SauceNAO(client=client, api_key=saucenao_api_key, minsim=85)
        resp = await sauce.search(pic)
        if len(resp.raw) > 0 and resp.raw[0].similarity > 85:
            img = resp.raw[0]
            url_thumbnail = img.thumbnail
            img_sql = await get_image(url=url_thumbnail,
                                      file=img.index_name.split(' ')[-1].split('.')[0],
                                      path=pic_base_path / 'saucenao',
                                      img_type=ImageType.saucenao,
                                      _proxies=proxies)
            ImageSauce.get_or_create(
                origin=str(img.origin),
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
            img_path = pic_base_path / f"saucenao/{img_sql.filename}.{img_sql.suffix}"
            return img, img_path, resp.long_remaining > 0
        else:
            return None, '', resp.long_remaining > 0
