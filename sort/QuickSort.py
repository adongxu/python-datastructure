# 快速排序
import TimeUtils


@TimeUtils.getTimeOfFunc
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, start, end):
    if start < end:

        part = partition(alist, start, end)
        # 排序前半部分
        quickSortHelper(alist, start, part - 1)
        # 排序后半部分
        quickSortHelper(alist, part + 1, end)


def partition(alist, start, end):
    pivot_value = alist[start]
    left = start + 1
    right = end
    while left <= right:

        # left移动到第一次大于key
        while left <= right and alist[left] <= pivot_value:
            left += 1

        # right移动到第一次小于key
        while left <= right and alist[right] >= pivot_value:
            right -= 1
        # 还要判断到没到边界，到了直接退出
        if left > right:
            break
        # 交换逆序对
        alist[left], alist[right] = alist[right], alist[left]

    # key就位
    alist[start], alist[right] = alist[right], alist[start]
    return right
