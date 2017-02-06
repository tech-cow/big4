#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Title: Quick Sort
#
#  时间复杂度
#  Avg: O(nlog(n))   Worst: O(n^2)
#  空间复杂度
#  O(log(n))
#
# 算法核心：
# 总算搞懂了。。妈蛋。。这个算法，有个“墙”的概念，稍微要说清楚
#
# 总体概括
# Step 1:
# 找Pivot，（这里使用一个Github上Python小哥的方法）
#   从Unsorted Array里面取index最小值，最大值，和中间值，
#   用系统自带的Sort进行排序，然后进行对比，将对比后的最小值设置成Pivot的Value
#   在开始Partition之前，把这个Pivot和首位的Value进行更换，然后从左向右循环。
#
# Step 2:
# Partition(拆散这个该死的数组吧！)
#   先调用刚写好的Pivot方程，把这个Pivot和首位的Value进行更换，然后从左向右循环。
#   设置一个Counter(一道墙)，这个墙从0开始。
#   每次当 alist[i] < pivotValue 的时候，这道墙就往右边增一，然后swap alist[i]和pivotValue，
#   否则i++，墙留在原点
#   最后墙的左边是比Pivot值要小的，墙的右边是比Pivot值要大的，AKA人生巅峰
#   慢着，这时候牛逼的来了，交换Pivot和Counter的index，Pivot就跑到中间去了
#   然后Pivot左边的数都比Pivot小，Pivot右边的都比Pivot大
#
# Step 3：
# quickSort就循环调用Partition，用Divide&Conquer，分成一半，然后慢慢的往下切割并排序
#=======================================================================
# def quickSort():
def quickSort(alist,min,max):
    #再长度比20小的时候，调用系统内置的Timsort会大大提高效率
    if len(alist) < 20:
        return sorted(alist)
    if min < max: #check一下有没有调皮的孩子乱输入
        mid = partition(alist,min,max)
        quickSort(alist,min,mid-1) #mid-1等于 counterWall+1
        quickSort(alist,mid+1,max)
    return alist

def getPivot(alist,min,max):
    mid = (min+max)/2
    tempAlist = [min,mid,max]
    newAlist = sorted(tempAlist)
    # 把新的sorted array里面的中间值返回
    if alist[min] == newAlist[1]:
        return min
    elif alist[mid] == newAlist[1]:
        return mid
    else:
        return max


def partition(alist,min,max):
    #Get the pivot index, move it to the first element
    pivotIndex = getPivot(alist,min,max)
    pivotValue = alist[pivotIndex]   #设个值，方便调用
    alist[pivotIndex],alist[min] = alist[min],alist[pivotIndex]

    counterWall = min    # “墙”来也

    for i in range(min,len(alist)):
        if alist[i] < pivotValue:
            counterWall += 1
            alist[i],A[counterWall] = A[counterWall],alist[i]
    alist[min],alist[counterWall] = alist[counterWall],alist[min]

    return counterWall


if __name__ == '__main__':
    A = [39,3,5,7,4,3,100,2,10,12,1]
    print quickSort(A,0,len(A)-1)
