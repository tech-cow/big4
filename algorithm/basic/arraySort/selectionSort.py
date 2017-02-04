#!/usr/bin/python
#coding:utf-8   这样就可以打中文了

def swap(arr, num_1, num_2):
    temp = arr[num_1]
    arr[num_1] = arr[num_2]
    arr[num_2] = temp

#-------------------！
#初始尝试：
    #1、外层循环的结束条件不妥,因为循环排序到最后一个就是最大/小值了,不需要在进行比较,所以应该去除
    #2、内层循环的初始条件不妥,如果从i开始就是和自身进行比较了,多余
def BAD_selectionSort(alist):
    for i in range(len(alist)):
        min = i
        for j in range(i, len(alist)):
            if alist[j] < alist[min]:
                min = j
        if min != i :
            swap(alist,i,min)
    return alist
#-------------------！


def GOOD_selectionSort(alist):
    # 这里len(alist)之所以减一，是因为当外层循环到了len(alist)-1的时候，所有的换位已经终结了
    for i in range(len(alist)-1):
        min = i
        # 这里i+1的原因是，i不需要和自己再次做比较
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min]:
                min = j
        if min != i :
            swap(alist,i,min)
    return alist


# Test
print "-------------Test-------------"
A = [2,1,9,3,4,100,31,19,33,99,30]
print GOOD_selectionSort(A)
