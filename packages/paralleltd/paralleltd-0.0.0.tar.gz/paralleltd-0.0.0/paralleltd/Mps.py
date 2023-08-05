# -*- coding: utf-8 -*-
# @Time     : 2023/4/15 16:43
# @Author   : Leslie Pan
# @Site     : 
# @File     : Mps.py
# @Software : PyCharm

import multiprocessing

class Mps:
    def __init__(self, func = print, queue = ['hello parallel 1', 'hello parallel 2'], retrieve = True):
        self.func = func
        self.queue = queue
        self.retrieve = retrieve
        self.results = []

    def proceed(self, cores = 1):
        cores = min(cores, multiprocessing.cpu_count() - 1)
        pool = multiprocessing.Pool(processes = cores)
        for arg in self.queue:
            if self.retrieve:
                self.results.append(pool.apply_async(self.func, (arg)).get())
            else:
                pool.apply_async(self.func, (arg))
        pool.close()
        pool.join()
        return self.results



