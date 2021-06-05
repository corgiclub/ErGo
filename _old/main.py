from _old import mirai_core as core
from pathlib import Path

from graia.application import Session

from _old.extensions import load_config


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
