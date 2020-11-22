import mirai_core as core
from pathlib import Path
from graia.application import Session

from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.application.message.elements.internal import Plain
from graia.application.friend import Friend

if __name__ == '__main__':
    core.init(Session(
        host="http://localhost:8765",
        authKey="ERGOBOTAUTHKEY",
        account=3254622926,
        websocket=True,
        debug_flag=True
        )
    )
    core.load_plugins(Path('plugins'), active_groups=[600302544, 722077615, 1168529926])
    app = core.Get.app()
    bcc = core.Get.bcc()

    while True:
        try:
            app.launch_blocking()
        except KeyboardInterrupt:
            break
