import time
import sys
import nonebot
from nonebot.adapters.onebot.v11 import Adapter, Bot
from nonebot.log import logger


sys.path.append('./bot/')
sys.path.append('./bot/src/')
nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(Adapter)
# nonebot.load_builtin_plugins()
nonebot.load_plugins('src/plugins')
# nonebot.load_all_plugins({"src.plugins.nonebot_plugin_gocqhttp"}, set())
# nonebot.load_all_plugins(["src.plugins.test", "src.plugins.bilibili", "src.plugins.bililive"], [])

if __name__ == "__main__":
    nonebot.run(port=9080)

    logger.add("file_1.log", rotation="4096 MB")

