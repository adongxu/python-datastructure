# 归并排序
import TimeUtils


@TimeUtils.getTimeOfFunc
def mergeSort(alist):
    mergeSortHelper(alist)


def mergeSortHelper(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist) // 2

    left = mergeSortHelper(alist[:mid])
    right = mergeSortHelper(alist[mid:])

    return merge(left, right)


def merge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # 打扫战场
    res.extend(left[i:])
    res.extend(right[j:])
    return res
