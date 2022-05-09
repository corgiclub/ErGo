from nonebot import on_command, on_keyword, on_regex
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
from nonebot.permission import Permission
from datetime import datetime
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.adapters.onebot.v11.helpers import Cooldown


class Permissions:

    def __init__(self, plugin_name=None, permission_file_path=None):
        self.plugin_name = plugin_name
        self.permissions = ['test']
        self.load(permission_file_path)


    def load(self, permission_file_path):
        return self

    def __call__(self):
        return self.pp

    def has(self, event):
        return 'test' in self.permissions


p = Permissions()
test = on_keyword({'test'}, priority=1, block=False)


@test.handle(parameterless=[Cooldown(cooldown=11.4514)])
async def _(bot: Bot, event: Event, state: T_State):
    sender = event.get_user_id()
    msg = Message([
        MessageSegment.text(sender),
        MessageSegment.text('拥有权限' if p.has(event) else '未拥有权限'),
    ])
    await test.send(msg)



