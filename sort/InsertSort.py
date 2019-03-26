# 直接插入排序 从前往后
def insertSort(alist):
    for i in range(1, len(alist)):
        # 新进来的那个数
        cur = alist[i]
        # 移动的位置
        pos = i-1
        while pos >=0 and cur<alist[pos]:
            alist[pos+1] = alist[pos]
            pos-=1
        alist[pos+1] = cur

    return alist

alist = [1, 3, 2, 0, 5, 4, 9, 8, 6, 7]
print(insertSort(alist))
