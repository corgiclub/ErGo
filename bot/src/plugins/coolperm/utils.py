from typing import Optional, Set, Dict
from nonebot.params import Depends, EventMessage
from nonebot.matcher import Matcher
from asyncio import get_running_loop
from enum import Enum

from nonebot.adapters.onebot.v11 import Message, MessageEvent, GroupMessageEvent



def cooldown(
    cooldown: float = 5,
    *,
    prompt: Optional[str] = None,
    isolate_level: CooldownIsolateLevel = CooldownIsolateLevel.USER,
) -> None:
    if not isinstance(isolate_level, CooldownIsolateLevel):
        raise ValueError(
            f"invalid isolate level: {isolate_level!r}, "
            "isolate level must use provided enumerate value."
        )
    debounced: Set[str] = set()

    async def dependency(matcher: Matcher, event: MessageEvent):
        loop = get_running_loop()

        if isolate_level is CooldownIsolateLevel.GROUP:
            key = str(
                event.group_id
                if isinstance(event, GroupMessageEvent)
                else event.user_id,
            )
        elif isolate_level is CooldownIsolateLevel.USER:
            key = str(event.user_id)
        elif isolate_level is CooldownIsolateLevel.GROUP_USER:
            key = (
                f"{event.group_id}_{event.user_id}"
                if isinstance(event, GroupMessageEvent)
                else str(event.user_id)
            )
        else:
            key = CooldownIsolateLevel.GLOBAL.name

        if key in debounced:
            await matcher.finish(prompt)
        else:
            debounced.add(key)
            loop.call_later(cooldown, lambda: debounced.remove(key))
        return

    return Depends(dependency)