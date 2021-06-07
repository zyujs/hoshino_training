import hoshino
import re

def rex_replace(rex_pattern, func, new_rex_pattern = None):
    rex = hoshino.trigger.rex
    if new_rex_pattern:
        new_rex = re.compile(new_rex_pattern)
    for k in list(rex.allrex.keys()):
        if rex_pattern in k.pattern:
            if isinstance(rex.allrex[k], list):
                for i in range(0, len(rex.allrex[k])):
                    rex.allrex[k][i].func = func
            else:
                rex.allrex[k].func = func
            if new_rex:
                rex.allrex[new_rex] = rex.allrex.pop(k)
            return True
    return False
