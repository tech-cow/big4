#!/usr/bin/python
#coding:utf-8   这样就可以打中文了
#=======================================================================
#  Author: Yu Zhou
#  Title: Merge Sort
#
# 算法核心：
# 把Array对半分解，直到每个Array里面只有一个数，
# 然后在开始对这些subset进行排序，排序完了进行合并，直到合并完成
#=======================================================================
def mergeSort(alist):
    #再长度比20小的时候，调用系统内置的Timsort会大大提高效率
    if len(alist) < 20:
        return sorted(alist)
    #Array给拆了，先得把它拆解掉
    mid = len(alist)/2
    #因为Recursive了，所以mergeSort这个方程会进行到底，知道list里只剩下一个值
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    return merge(left,right)

def merge(leftAlist,rightAlist):
    result = []

    #当两边的Array都还有数的时候，互相对比，然后把最小值放进新的Array
    while(leftAlist and rightAlist):
        if leftAlist[0] < rightAlist[0]:
            result.append(leftAlist.pop(0))
        else:
            result.append(rightAlist.pop(0))

    #当一边已经没有数的时候，把另一边所有的数都放进信的Array
    while(leftAlist):
        result.append(leftAlist.pop(0))

    while(rightAlist):
        result.append(rightAlist.pop(0))

    return result

#Test
if __name__ == "__main__":
    A = [3,2,1,4,6,5,66,111,77,88,99]
    print mergeSort(A)
