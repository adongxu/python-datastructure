# 冒泡泡排序
def bubbleSort(alist):
    if len(alist) <= 1:
        return alist

    # 外循环表示就位的元素位置 从尾到头
    for i in range(len(alist) - 1, 0, -1):
        # 内循环不断交换逆序对
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


alist = [1, 3, 2, 0, 5, 4, 9, 8, 6, 7]
print(bubbleSort(alist))
