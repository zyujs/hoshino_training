import nonebot
import hoshino
import os
import importlib

def get_hoshino_module(module):
    plugins = nonebot.get_loaded_plugins()
    for plugin in plugins:
        m = str(plugin.module)
        m = m.replace('\\', '/').replace('//', '/')
        if module in m:
            return plugin.module
    return None

def replace_func_of_module(module_path, func_name, func):
    module = get_hoshino_module(module_path)
    if not module:
        return False
    if not hasattr(module, func_name):
        return False
    setattr(module, func_name, func)
    return True

def replace_func_of_rex(rex_pattern, func):
    rex = hoshino.trigger.rex
    for k in list(rex.allrex.keys()):
        #print(k.pattern)
        if rex_pattern in k.pattern:
            rex.allrex[k].func = func
            return True
    return False

def get_functions_list():
    path = os.path.join(os.path.dirname(__file__), 'functions')
    if not os.path.exists(path):
        return None
    fnlist = []
    for fn in os.listdir(path):
        s = fn.split('.')
        if len(s) >=2 and s[-1] == 'py':
            fnlist.append(s[0])
    return fnlist

def load_functions(flist):
    for name in flist:
        module = None
        try:
            module = importlib.import_module('hoshino.modules.hoshino_training.functions.' + name)
        except:
            print('load module', 'hoshino.modules.hoshino_training.functions.' + name, 'failed')
        if module and hasattr(module, 'replace_list'):
            for item in module.replace_list:
                if item['mode'] == 'module':
                    msg = f"replace {item['func_name']} of module {item['module']} "
                    if replace_func_of_module(item['module'], item['func_name'], item['func']):
                        msg += 'successed'
                    else:
                        msg += 'failed'
                    print(msg)
                elif item['mode'] == 'rex':
                    msg = f"replace {item['func_name']} of rex {item['module']} "
                    if replace_func_of_rex(item['module'], item['func']):
                        msg += 'successed'
                    else:
                        msg += 'failed'
                    print(msg)
        

@nonebot.on_startup
async def startup():
    path_list = get_functions_list()
    load_functions(path_list)

