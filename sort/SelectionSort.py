# 选择排序(冒泡排序改进，每次只记录最大值的位置，不交换)
def selectionSort(alist):
    if len(alist) <= 1:
        return alist
    for i in range(len(alist) - 1, 0, -1):
        maxIndex = 0
        for j in range(i + 1):
            if alist[j] > alist[maxIndex]:
                maxIndex = j
        # 最大值和i处值交换位置
        alist[maxIndex], alist[i] = alist[i], alist[maxIndex]
    return alist


alist = [1, 3, 2, 0, 5, 4, 9, 8, 6, 7]
print(selectionSort(alist))
