import nonebot
from nonebot import on_command, on_keyword, on_regex
from nonebot.typing import T_State
from typing import Tuple, Union
from nonebot.permission import Permission
from datetime import datetime
from nonebot.adapters.onebot.v11 import Bot, Message, MessageSegment, MessageEvent

from nonebot.adapters.onebot.v11.helpers import Cooldown
from src.extensions import coolperm
from nonebot.params import Command
from nonebot.matcher import Matcher

from pprint import pformat


# class Permissions:
#
#     def __init__(self, plugin_name=None, permission_file_path=None):
#         self.plugin_name = plugin_name
#         self.permissions = ['test']
#         self.load(permission_file_path)
#
#
#     def load(self, permission_file_path):
#         return self
#
#     def __call__(self):
#         return self.pp
#
#     def has(self, event):
#         return 'test' in self.permissions
#
#
# p = Permissions()
test = on_keyword({'test'}, priority=1, block=False)


@test.handle(parameterless=[coolperm(permission='test.test_perm', prompt_permission=True)])
# @test.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State, matcher: Matcher):
    sender = event.get_user_id()
    print(matcher.module, matcher.module_name, matcher.plugin_name)
    info = await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id, no_cache=False)
    print(event)
    # print(foo)
    msg = Message([
        MessageSegment.text(sender),
        MessageSegment.text('拥有权限\n'),
        # MessageSegment.text(pformat(state)),
        MessageSegment.text(pformat(info)),

    ])
    await test.send(msg)



