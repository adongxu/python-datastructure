# 希尔排序
import TimeUtils


@TimeUtils.getTimeOfFunc
def shellSort(alist):
    n = len(alist)
    while n >= 1:
        n = n // 2
        for start in range(n):
            gapInsertSort(alist, start, n)
    return alist


def gapInsertSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        cur = alist[i]
        pos = i - gap
        while pos >= 0 and cur < alist[pos]:
            alist[pos + gap] = alist[pos]
            pos -= gap
        alist[pos + gap] = cur
