from typing import Optional, Set, Dict, Tuple, Union
from nonebot.params import Depends, EventMessage
from nonebot.matcher import Matcher
from asyncio import get_running_loop
from enum import Enum
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import Message, PrivateMessageEvent, GroupMessageEvent
from nonebot.params import Command
import yaml
from time import time
from nonebot.permission import SUPERUSER


permissions_all = yaml.safe_load(open('src/permissions/test.yml', 'r'))


def combine_dict(da, db):
    """

        合并两个 dict 并让子 dict 也合并。
        该函数在逻辑上是不完善的，可能出现输出不符合描述预期的情况或报错，但在该插件中刚好适用。
    """
    d = {**da, **db}
    for k in set(da.keys()) & set(db.keys()):
        if isinstance(da[k], dict):
            d[k] = {**da[k], **db[k]}
        else:
            d[k] = db[k]
    return d


def coolperm(
    permission: str = 'global',
    cooldown_default: float = -1,
    *,
    prompt_cooldown: Optional[bool] = True,
    prompt_permission: Optional[bool] = False,
) -> None:

    debounced: Dict[str: float] = dict()

    async def dependency(bot: Bot, matcher: Matcher, event: Union[PrivateMessageEvent, GroupMessageEvent]):

        cooldown = cooldown_default
        group_id = 0
        user_id = event.user_id

        # 权限判断
        if permission in permissions_all:
            permission_dic: Dict = combine_dict(permissions_all[permission], permissions_all['global'])
        else:
            permission_dic = permissions_all['global']
        permission_keys = list(permission_dic.keys())

        if isinstance(event, GroupMessageEvent):
            group_id = event.group_id
            user_info = await bot.get_group_member_info(group_id=group_id, user_id=user_id, no_cache=False)

            if 'users' in permission_keys and user_id in permission_dic['users']:
                cooldown = permission_dic['users'][user_id]
            elif 'group_owner' in permission_keys and user_info['role'] == 'owner':
                cooldown = permission_dic['group_owner']
            elif 'group_admin' in permission_keys and (user_info['role'] == 'admin' or user_info['role'] == 'owner'):
                cooldown = permission_dic['group_admin']
            elif 'groups' in permission_keys and group_id in permission_dic['groups']:
                cooldown = permission_dic['groups'][group_id]
            elif 'group' in permission_keys:
                cooldown = permission_dic['group']
            else:
                cooldown = -1

        if isinstance(event, PrivateMessageEvent):

            if 'users' in permission_keys and user_id in permission_dic['users']:
                cooldown = permission_dic['users'][user_id]
            elif 'private' in permission_keys:
                cooldown = permission_dic['private']
            else:
                cooldown = -1

        if cooldown == -1 and 'anyone' in permission_keys:
            cooldown = permission_dic['anyone']

        if cooldown == -1:
            await matcher.finish(f'你没有 {permission} 权限！' if prompt_permission else None)
        elif cooldown > 0:
            key = f'{group_id}_{user_id}'
            if key in debounced:
                await matcher.finish(f'指令 {permission} 冷却中 ⌛ {cooldown - time() + debounced[key]:.2f}s'
                                     if prompt_cooldown else None)
            else:
                debounced[key] = time()
                loop = get_running_loop()
                loop.call_later(cooldown, lambda: debounced.pop(key))
        return

    return Depends(dependency)
