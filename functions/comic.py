from hoshino import aiorequests
from hoshino.modules.hoshino_training.util.module import *

#超时时间
timeout = 120

#代理, 必须使用http代理, 不使用请留空
proxy = ''
#proxy = 'http://172.17.0.1:1081'

proxies={
    'http': proxy,
    'https': proxy,
}

async def get(url, params=None, **kwargs):
    return None

class NewAaiorequests:
    def __init__(self):
        pass

    async def get(self, url, params=None, **kwargs):
        kwargs['timeout'] = timeout
        return await aiorequests.get(url, proxies=proxies, params=params, **kwargs)

new_aiorequests = NewAaiorequests()

module_replace('hoshino.modules.priconne.comic', 'aiorequests', new_aiorequests)
