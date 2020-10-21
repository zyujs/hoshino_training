import nonebot

def scheduler_replace(func_ref, func):
    jobs = nonebot.scheduler.get_jobs()
    for job in jobs:
        if job.func_ref == func_ref:
            job.func = func
            return True
    return False
