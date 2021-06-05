# __plugin_name__ = '硬件监控'
# __plugin_description__ = '自动循环插件，用于监控服务器环境、报警等，亦可手动查询'
# __plugin_usage__ = '输入“硬件监控”查看信息[admin]'
# __plugin_pattern__ = '硬件监控'
#
# bcc = Get.bcc()
# config = load_config()
# sched = BackgroundScheduler()
#
#
# def get_loop_20():
#     message = []
#     warning = []
#     for func in m_func.__all__:
#         mes, war = getattr(m_func, func)()
#         message.append(mes)
#         warning.append(war) if war != '' else None
#
#     return '\n'.join(message), '\n'.join(warning)
#
#
# @sched.scheduled_job('interval', seconds=20)
# def auto_loop_warning():
#     _, warn = get_loop_20()
#     if warn != '':
#         GraiaMiraiApplication.sendGroupMessage(config.group, MessageChain.create([Plain(warn)]).asSendable())
#
#
# sched.start()  # 调用start方法
#
#
# @bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
# async def video_info(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
#     if re.match(__plugin_pattern__, message.asDisplay()):
#         mes, war = get_loop_20()
#         war = '<无>' if war == '' else war
#         await app.sendGroupMessage(group, MessageChain.create([
#             Plain('监控信息：\n'),
#             Plain(mes),
#             Plain('报警信息：\n'),
#             Plain(war),
#         ]))
#
