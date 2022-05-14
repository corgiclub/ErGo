import time

import nonebot
from nonebot.adapters.onebot.v11 import Adapter, Bot
from nonebot.log import logger


nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(Adapter)
# nonebot.load_builtin_plugins()
nonebot.load_all_plugins(["src.plugins.start_up"], [])
nonebot.load_all_plugins(["src.plugins.test", "src.plugins.bilibili", "src.plugins.bililive"], [])

if __name__ == "__main__":
    nonebot.run(port=8080)

    logger.add("file_1.log", rotation="4096 MB")

