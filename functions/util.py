# hoshino\util\__init__.py

async def silence(ev, ban_time, skip_su=True):
    pass

replace_list = [
    {
        'mode': 'module',
        'module': 'hoshino.modules.priconne.gacha',
        'func_name': 'silence',
        'func': silence,
    }
]