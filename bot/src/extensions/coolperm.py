import os
from asyncio import get_running_loop
from functools import reduce
from pathlib import Path
from time import time
from typing import Optional, Dict, Union

import yaml
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import PrivateMessageEvent, GroupMessageEvent
from nonebot.matcher import Matcher
from nonebot.params import Depends


# todo 配置读取 配置重载 配置修改 SUPERUSER


debug = True


def load_all_permissions(path=Path('src/permissions/')):
    perm = [yaml.safe_load(open(path / p, 'r', encoding='utf-8')) for p in os.listdir(path)]

    if debug:
        return perm + [yaml.safe_load(open(Path('src/permissions.example/') / p, 'r', encoding='utf-8'))
                       for p in os.listdir(Path('src/permissions.example/'))]

    return perm


def add_permission():
    pass


def remove_permission():
    pass


permissions_all_list = load_all_permissions()
permissions_all = reduce(lambda x, y: {**x, **y}, permissions_all_list)

# 更为优化的写法
# import itertools
# dict(itertools.chain.from_iterable((d.items() for d in permissions_all_list)))

print(f'读取了 {sum(len(i) for i in permissions_all.values())} 条权限')


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
        cooldown_spec: Optional[float] = None,
        *,
        prompt_cooldown: Optional[bool] = True,
        prompt_permission: Optional[bool] = False,
) -> None:
    debounced: Dict[str: float] = dict()

    async def dependency(bot: Bot, matcher: Matcher, event: Union[PrivateMessageEvent, GroupMessageEvent]):

        cooldown = -1
        group_id = 0
        user_id = event.user_id
        permission_inner = matcher.plugin_name + permission if permission.startswith('.') else permission

        # 权限判断
        if permission_inner in permissions_all:
            permission_dic: Dict = combine_dict(permissions_all[permission_inner], permissions_all['global'])
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
            await matcher.finish(f'你没有 {permission_inner} 权限！' if prompt_permission else None)
            return

        if cooldown_spec:
            cooldown = cooldown_spec

        if cooldown > 0:
            key = f'{group_id}_{user_id}'
            if key in debounced:
                await matcher.finish(f'指令 {permission_inner} 冷却中 ⌛ {cooldown - time() + debounced[key]:.2f}s'
                                     if prompt_cooldown else None)
            else:
                debounced[key] = time()
                loop = get_running_loop()
                loop.call_later(cooldown, lambda: debounced.pop(key))

        return

    return Depends(dependency)
