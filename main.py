import mirai_core as core
from pathlib import Path
from graia.application import Session

from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.application.message.elements.internal import Plain
from graia.application.friend import Friend

from extensions.load_config import load_config


if __name__ == '__main__':
    config = load_config()

    core.init(Session(
        host=config.host,
        authKey=config.authKey,
        account=config.account,
        websocket=True,
        debug_flag=True
    )
    )
    core.load_plugins(Path('plugins'), active_groups=config.active_groups)
    app = core.Get.app()
    bcc = core.Get.bcc()

    while True:
        try:
            app.launch_blocking()
        except KeyboardInterrupt:
            break
