# -*- coding: utf-8 -*-
# @Time     : 2023/4/18 15:53
# @Author   : Leslie Pan
# @Site     : 
# @File     : ToolFunc.py
# @Software : PyCharm

import time
import functools


def counting(text=''):
    start_time = time.time()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    print('%s takes %.4f seconds' % (text, time.time() - start_time))
    return decorator
