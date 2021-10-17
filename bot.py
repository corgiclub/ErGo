import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
from nonebot.log import logger

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
# nonebot.load_builtin_plugins()
nonebot.load_plugins("src/plugins")

if __name__ == "__main__":
    nonebot.run(port=8080)
    logger.add("file_1.log", rotation="4096 MB")

