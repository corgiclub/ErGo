from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

import translators as ts

__plugin_name__ = '翻译'
__plugin_description__ = '翻译文字，支持谷歌，DeepL，百度，阿里等多种接口'
__plugin_usage__ = '发送"翻译 ...获取翻译"'

bcc = Get.bcc()


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def video_info(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if message.asDisplay().startswith('翻译 '):
        text = message.asDisplay()[3:]

        translation = ts.deepl(text, to_language='zh-CHS')

        await app.sendGroupMessage(group, MessageChain.create([
            Plain(translation),
        ]))
