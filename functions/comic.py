from hoshino import aiorequests

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

class Fake_aiorequests:
    def __init__(self):
        pass

    async def get(self, url, params=None, **kwargs):
        kwargs['timeout'] = timeout
        return await aiorequests.get(url, proxies=proxies, params=params, **kwargs)

fake_aiorequests = Fake_aiorequests()

replace_list = [
    {
        'mode': 'module',
        'module': 'hoshino.modules.priconne.comic',
        'func_name': 'aiorequests',
        'func': fake_aiorequests,
    }
]