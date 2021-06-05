import sys
from pixivpy3 import *

if sys.version_info >= (3, 0):
    import imp
    imp.reload(sys)
else:
    reload(sys)
    sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True


# change _USERNAME,_PASSWORD first!
_USERNAME = ""
_PASSWORD = ""
_TEST_WRITE = False

# If a special network environment is meet, please configure requests as you need.
# Otherwise, just keep it empty.
_REQUESTS_KWARGS = {
    'proxies': {
        'https': 'http://127.0.0.1:1081',
    },
    # 'verify': False,       # PAPI use https, an easy way is disable requests SSL verify
}

api = AppPixivAPI(**_REQUESTS_KWARGS)
api.login(_USERNAME, _PASSWORD)
print(000)
json_result = api.illust_detail(59580629)
illust = json_result.illust
print(illust)
