import asyncio
import aiohttp

# from pixivpy3 import AppPixivAPI as AAPI
from pixivpy_async import AppPixivAPI, PixivClient
from pixivpy_async.sync import AppPixivAPI as SAAPI

from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector

_USERNAME = 'lune_z@foxmail.com'
_PASSWORD = 'zhaoyinzhi?..'
proxy = 'socks5://127.0.0.1:1080'
proxy_dict = {
    'proxy_type': ProxyType.SOCKS5,
    'host': '127.0.0.1',
    'port':1080,
    'rdns':True
}


class PXC(PixivClient):
    def __init__(self):
        super(PXC, self).__init__(env=False)
        self.conn = self.conn = ProxyConnector(**proxy_dict, limit_per_host=30)
        self.client = aiohttp.ClientSession(
            connector=self.conn,
            timeout=aiohttp.ClientTimeout(total=10),
            trust_env=False,
        )


def test2():
    api = SAAPI(env=True)
    api.login(_USERNAME, _PASSWORD)
    print("test2 - finished")


async def test1():
    # client = PixivClient(env=True).start()
    client = PXC().start()
    api = AppPixivAPI(client=client)
    await api.login(_USERNAME, _PASSWORD)

    p = await api.illust_detail(59580629)

    print(p)
    await client.close()


    # await client.close()
    print("test1 - finished")


if __name__ == '__main__':
    # test0()
    # test2()
    # asyncio.run(test1())
    def get_local_proxy():
        from urllib.request import getproxies
        print(getproxies())
        proxy = getproxies()['http']
        return proxy

    a = get_local_proxy()
    print(a)
