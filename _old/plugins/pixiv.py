#
# __plugin_name__ = 'pixiv'
# __plugin_description__ = '使用 pixiv 的相关功能'
# __plugin_usage__ = '搜索：p [关键词/pid]\n搜图：p [图片]\n查找流行瑟图：se图\n'
# __plugin_pattern__ = 'p +|涩图|se图|色图'
#
# bcc = Get.bcc()
#
#
# @bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
# async def pixiv(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
#     if message.asDisplay().startswith('p '):
#         await app.sendGroupMessage(group, MessageChain.create([
#             Plain(f"Cogito, ergo sum."),
#         ]))
#
#     async with PixivClient() as client:
#         aapi = AppPixivAPI(client=client)
#         # Doing stuff...
