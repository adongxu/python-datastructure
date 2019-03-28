import time
# 装饰器，求各个函数运行的时间


def getTimeOfFunc(fn):
    def inner(*args):
        start = time.time()
        fn(*args)
        end = time.time()
        print(fn.__name__, 'run time= {0:.10f}s'.format(end - start))
    return inner
