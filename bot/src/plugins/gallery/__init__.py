
# from nonebot import on_command, on_startswith, on_regex, get_driver
# from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment
# from src.extensions import CQ, get_config
# from PicImageSearch import SauceNAO, Network

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

regex_keys = '*|'.join(sum(aliases.values(), [])) + '*'


print(regex_keys)

# searching_by_pic = on_regex(r'pic*|sauce*|pixiv*', priority=10, block=False)
# searching_by_text = on_command('setu', aliases={'色图', 'pixiv'}, priority=10, block=False)