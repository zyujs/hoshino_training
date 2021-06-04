import hoshino
import re

def rex_replace(rex_pattern, func, new_rex_pattern = None):
    rex = hoshino.trigger.rex
    if new_rex_pattern:
        new_rex = re.compile(new_rex_pattern)
    for k in list(rex.allrex.keys()):
        if rex_pattern in k.pattern:
            rex.allrex[k].func = func
            if new_rex:
                rex.allrex[new_rex] = rex.allrex.pop(k)
            return True
    return False
