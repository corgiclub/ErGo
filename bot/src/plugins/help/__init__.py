from nonebot import on_command, get_driver
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment
from src.extensions import coolperm
from nonebot import CommandGroup, get_loaded_plugins
from pprint import pprint

cg_help = on_command('help', priority=10, block=False)


@cg_help.handle(parameterless=[coolperm('.help')])
async def _(bot: Bot, event: MessageEvent):
    cfg = get_driver().config
    msg = event.get_plaintext().split(' ')
    plugins = {p.name: cfg.__dict__[p.name] for p in get_loaded_plugins()}
    plugins = {p: plugins[p] for p in sorted(plugins.keys()) if plugins[p]['meta']['visible_in_help']}

    if len(msg) == 1:
        msg = f'欢迎使用帮助，请输入 `/help <插件名>` 查看插件详细帮助\n' + \
              f'插件列表（插件名 - 功能）：\n' + \
              '\n'.join(f"{p} - {v['meta']['name']}" for p, v in plugins.items())
    else:
        plugin = msg[1]
        if plugin not in plugins:
            msg = f'插件 {plugin} 不存在'
        else:
            meta = plugins[plugin]['meta']
            msg = f'【{plugin} - {meta["name"]}】\n' + \
                  f'{meta["description"]}\n' + \
                  f'使用方法：\n - ' + \
                  '\n - '.join(meta['help'])

    await cg_help.send(MessageSegment.text(msg))

