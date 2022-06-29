import re

from nonebot import on_regex, CommandGroup
from nonebot.adapters.onebot.v11 import Event, MessageSegment, Bot
from peewee import fn

from src.extensions import coolperm, CQ, regex_equal, regex_startswith_key_with_image, get_chat_image, pic_base_path
from src.models.image import ImageGallery, Image

themes = {
    # ACG
    'touhou_project': ['touhou', 'th'],
    'virtual_singer': ['vocaloid', 'vc', 'v+', 'sv', 'cevio'],
    'kantai_collection': ['kancolle', 'kc', 'jc'],
    'THE_IDOLM@STER': ['imas'],
    'lovelive': ['ll'],
    'fate': [],
    'virtual_liver': ['vtb', 'vup', 'liver'],
    'gundam': ['gd'],

    # popular mobile game
    'azur_lane': ['blhx', 'al'],
    'blue_archive': ['blda', 'ba'],
    'arknights': ['mrfz', 'ak'],
    'honkai_impact': ['honkai', 'bbb', 'hi'],
    'genshin_impact': ['genshin', 'gs', 'gi', 'ys'],
    'pretty_derby': ['umamusume', 'umamu', 'smn', 'umm'],
    'granblue_fantasy': ['gbf'],
    'Princess_Connect!_Re:Dive': ['pcr'],

    # popular tag
    'yuri': ['les'],
    'knee_socks': ['gxw'],
    'capoo': [],

    # meme
    'mars': ['m'],
    'inm': [],

    # others
    'supermikimiki': ['mxmk', 'miki'],
    'kaguramahiru': ['mhr', 'mahiru'],
    'mihiru': [],
    'fake_miki': ['fmiki'],
    'fake_mahiru': ['fmhr'],
    'hoshimori_rena': ['rena'],
    'mayuzumi_fuyuko': ['fuyuko', 'fyk'],

}

for a in themes:
    themes[a] += [a]
themes_all = sum(themes.values(), [])


# 向下兼容至 py 3.8
def h(x):
    return x


save_image_regex = regex_startswith_key_with_image(themes_all)
take_image_regex = regex_equal(themes_all)
cg_gallery = CommandGroup('gallery')

save_image = on_regex(save_image_regex, flags=re.S, priority=10, block=False)
take_image = on_regex(take_image_regex, priority=10, block=False)


@save_image.handle(parameterless=[coolperm('.save_image')])
async def _(event: Event):
    message = event.get_message()
    theme = theme_text = message[0].data['text'].strip()

    if theme_text not in themes_all:
        return

    for theme in themes:
        if theme_text in themes[theme]:
            break

    for msg in message:
        if msg.type == CQ.image.name:
            img_sql = await get_chat_image(msg.data['url'], msg.data['file'].split('.')[0], path=f'gallery/{theme}')
            ImageGallery.get_or_create(image_id=img_sql.id, theme=theme)

    await save_image.finish(MessageSegment.text(text='已存储图片'))


@take_image.handle(parameterless=[coolperm('.take_image')])
async def _(event: Event):
    message = event.get_message()
    theme_text = message[0].data['text'].strip()

    for theme in themes:
        if theme_text in themes[theme]:
            query = ImageGallery.select(Image.filename, Image.suffix). \
                where(ImageGallery.theme == theme, Image.file_existed is True). \
                join(Image, on=(Image.id == ImageGallery.image_id)).order_by(fn.Rand()).get()

            await take_image.finish(
                MessageSegment.image(
                    file=pic_base_path / f'gallery/{theme}/{query.image.filename}.{query.image.suffix}'
                )
            )


@h(cg_gallery.command('list', aliases={'list_tag'}).handle(parameterless=[coolperm('.list')]))
async def _(bot: Bot, event: Event):
    message = '目前支持的 tag (包括全名/简写):'
    for theme in themes:
        message += f"\n{theme}({'/'.join(themes[theme][:-1])})" if len(themes[theme]) > 1 else f"\n{theme}"

    await bot.send(event, message=MessageSegment.text(text=message))
