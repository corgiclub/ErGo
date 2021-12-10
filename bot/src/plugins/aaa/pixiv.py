from pixivpy_async import *


client = PixivClient(env=True)
aapi = AppPixivAPI(client=client.start())
await aapi.login(username, password)






await client.close()
