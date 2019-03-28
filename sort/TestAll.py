# 测试所有的排序算法的效率
import random
import sys
import BubbleSort
import InsertSort
import MergeSort
import QuickSort
import SelectionSort
import ShellSort
import threading
import copy

if __name__ == '__main__':
    # 快速排序递归可能溢出，这里设置大一点的值
    # sys.setrecursionlimit(1000000)
    ls = [i for i in range(1, 10001)]
    random.shuffle(ls)
    # 复制，否则前面的排序会影响到后面的计算
    ls1 = copy.copy(ls)
    ls2 = copy.copy(ls)
    ls3 = copy.copy(ls)
    ls4 = copy.copy(ls)
    ls5 = copy.copy(ls)
    # 挨个运行
    BubbleSort.bubbleSort(ls)
    SelectionSort.selectionSort(ls1)
    InsertSort.insertSort(ls2)
    ShellSort.shellSort(ls3)
    MergeSort.mergeSort(ls4)
    QuickSort.quickSort(ls5)
