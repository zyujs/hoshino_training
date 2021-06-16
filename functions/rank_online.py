# hoshino\modules\priconne\query\query.py
# 从priconne/quick读取rxx-xx-server.png文件名rank图并发送
from hoshino import util, R
import os
import re
from hoshino.modules.hoshino_training.util.rex import *
import asyncio
from functools import partial
import nonebot
try:
    from git import Repo
except:
    print('[rank_online]请使用pip安装GitPython模块')

startup_job = None

route = {
    'ffby': '/rank/stable/cn/ffby/',
    'xbg': '/rank/stable/cn/xbg/',
    'wy': '/rank/stable/tw/wy/',
    'ymnt': '/rank/stable/tw/ymnt/',
    'sl': '/rank/stable/jp/sl/',
}

async def run_sync_func(func, *args, **kwargs):
    return await asyncio.get_event_loop().run_in_executor(
        None, partial(func, *args, **kwargs))

async def check_online_data():
    global startup_job
    if startup_job:
        startup_job.remove()
        startup_job = None

    res = R.img(f'priconne/quick/pcr-rank_data')
    if not os.path.exists(res.path):
        repo = await run_sync_func(Repo.clone_from,'https://github.com/pcrbot/pcr-rank_data.git', res.path)
    else:
        repo = Repo(res.path)
    if repo:
        await run_sync_func(repo.remote().pull)
    else:
        print('check_online_data failed')

startup_job = nonebot.scheduler.add_job(check_online_data, 'interval', seconds=5)
nonebot.scheduler.add_job(check_online_data, 'interval', hours=4)


def get_rank_pic(server='xbg'):
    path = f'priconne/quick/pcr-rank_data'
    res = R.img(path + route[server])
    if not os.path.exists(res.path):
        return None
    fnlist = os.listdir(res.path)
    rank_list = []
    maxn = 0
    for fn in fnlist:
        args = re.split(r'\.|-|_', fn)
        if len(args) < 4 or not args[0].isdigit() or not args[1].isdigit():
            continue
        n = int(args[0]) * 10 + int(args[1])
        if n > maxn:
            maxn = n
            rank_list = [fn]
        elif n == maxn:
            rank_list.append(fn)
    rank_list.sort()
    return rank_list

async def rank_sheet(bot, ev):
    match = ev['match']
    if not match.group(2):
        server = None
    elif match.group(2) in '国陆b':
        server = 'xbg'
    elif match.group(2) == 'x':
        server = 'xbg'
    elif match.group(2) == 'f':
        server = 'ffby'
    elif match.group(2) in '日':
        server = 'sl'
    elif match.group(2) in '台':
        server = 'wy'
    elif match.group(2) == 'w':
        server = 'wy'
    elif match.group(2) == 'y':
        server = 'ymnt'
    else:
        server = None

    if not server:
        await bot.send(ev, '\n请问您要查询哪个服务器的rank表？\n*日rank表\n*台rank表\n*陆rank表', at_sender=True)
        return

    msg = [
        '\n※表格仅供参考，升r有风险，强化需谨慎\n※一切以会长要求为准——',
    ]

    flist = get_rank_pic(server)

    if len(flist) == 0:
        await bot.send(ev, '无数据', at_sender=True)
        return

    args = re.split(r'\.|-|_', flist[0])
    msg.append(f'{args[0]}-{args[1]} rank表：')

    for fn in flist:
        p = R.img('priconne/quick/pcr-rank_data' + route[server] + fn).cqcode
        print(p)
        msg.append(f'{p}')
    await bot.send(ev, '\n'.join(msg), at_sender=True)
    await util.silence(ev, 60)

rex_replace(r'^(\*?([日台国陆b])服?([前中后]*)卫?)?rank(表|推荐|指南)?$', rank_sheet, r'^(\*?([日台国陆bxfwy])服?([前中后]*)卫?)?rank(表|推荐|指南)?$')
