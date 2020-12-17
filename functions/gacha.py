from hoshino.util import DailyNumberLimiter
from hoshino.modules.hoshino_training.util.module import *

tenjo_limit = DailyNumberLimiter(5)

TENJO_EXCEED_NOTICE = f'您今天已经抽过{tenjo_limit.max}张天井券了，欢迎明早5点后再来！'

async def silence(ev, ban_time, skip_su=True):
    pass

module_replace('hoshino.modules.priconne.gacha', 'tenjo_limit', tenjo_limit)
module_replace('hoshino.modules.priconne.gacha', 'TENJO_EXCEED_NOTICE', TENJO_EXCEED_NOTICE)
module_replace('hoshino.modules.priconne.gacha', 'silence', silence)