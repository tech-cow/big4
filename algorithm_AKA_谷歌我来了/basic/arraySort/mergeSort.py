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
    if len(alist) <= 1:
        return alist

    #Array给拆了，先得把它拆解掉
    mid = len(alist)/2
    #因为Recursive了，所以mergeSort这个方程会进行到底，知道list里只剩下一个值
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    return merge(left,right)


def merge(leftAlist,rightAlist):
    result = []
    #当两边的Array都还有数的时候，互相对比，然后把最小值放进新的Array
    while(len(leftAlist) > 0 and len(rightAlist) > 0):
        if leftAlist[0] < rightAlist[0]:
            result.append(leftAlist[0])
            leftAlist.pop(0)
        else:
            result.append(rightAlist[0])
            rightAlist.pop(0)

    #当一边已经没有数的时候，把另一边所有的数都放进信的Array
    while(len(leftAlist) > 0):
        result.append(leftAlist[0])
        leftAlist.pop(0)

    while(len(rightAlist) > 0):
        result.append(rightAlist[0])
        rightAlist.pop(0)

    return result



#Test
if __name__ == "__main__":
    A = [3,2,1,4,6,5,66,111,77,88,99]
    print mergeSort(A)
