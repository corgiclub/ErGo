import re

from nonebot import on_regex, on_command, CommandGroup
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment
from peewee import fn

from src.extensions import coolperm, CQ, regex_equal, get_chat_image
from src.models.image import ImageGallery, Image

aliases = {
    # ACG
    'touhou_project': ['touhou', 'th'],
    'virtual_singer': ['vocaloid', 'vc', 'v+', 'sv', 'cevio'],
    'kantai_collection': ['kancolle', 'kc', 'jc'],
    'THE_IDOLM@STER': ['imas'],
    'lovelive': ['ll'],
    'fate': [],
    'virtual_liver': ['vtb', 'vup', 'liver'],

    # popular mobile game
    'azur_lane': ['blhx', 'al'],
    'blue_archive': ['blda', 'ba'],
    'arknights': ['mrfz', 'ak'],
    'honkai_impact': ['honkai', 'bbb', 'hi'],
    'genshin_impact': ['genshin', 'gs', 'gi', 'ys', 'op'],
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

for a in aliases:
    aliases[a] += [a]

# 向下兼容至 py 3.8
def h(x):
    return x

save_image_regex = '.*CQ:image.*|'.join(sum(aliases.values(), [])) + '*CQ:image.*'
take_image_regex = regex_equal(sum(aliases.values(), []))
cg_gallery = CommandGroup('gallery')

save_image = on_regex(save_image_regex, flags=re.S, priority=10, block=False)
take_image = on_regex(take_image_regex, priority=10, block=False)


@save_image.handle(parameterless=[coolperm('.save_image')])
async def _(event: Event):
    message = event.get_message()
    theme_text = message[0].data['text'].strip()
    theme = '_'
    for al in aliases:
        if theme_text in aliases[al]:
            theme = al
            break

    for msg in message:
        if msg.type == CQ.image.name:
            _, _, img_id = await get_chat_image(msg.data['url'], msg.data['file'].split('.')[0], path=f'gallery/{theme}')
            ImageGallery.create(image_id=img_id, theme=theme)

    await save_image.finish(MessageSegment.text(text='已存储图片'))


@take_image.handle(parameterless=[coolperm('.take_image')])
async def _(event: Event):
    message = event.get_message()
    theme_text = message[0].data['text'].strip()
    theme = '_'
    for al in aliases:
        if theme_text in aliases[al]:
            theme = al
            break
    if theme == '_':
        return

    img = ImageGallery.select().where(ImageGallery.theme == theme).join(Image, on=(
            Image.id == ImageGallery.image_id)).order_by(fn.Rand()).get()

    await take_image.finish(
        Message([
            MessageSegment.image(file=img.image.filename),
        ])
    )


@h(cg_gallery.command('list_tag', aliases={'list'}).handle(parameterless=[coolperm('.list')]))
async def _(event: Event):
    message = ''
    for theme in

    await take_image.finish(
        Message([
            MessageSegment.image(file=img.image.filename),
        ])
    )
