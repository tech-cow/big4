#!/usr/bin/python
#coding:utf-8   这样就可以打中文了
#=======================================================================
#  Author: Yu Zhou
#  Title: Insertion Sort
#
# 算法核心：
# 把Array对半分解，直到每个Array里面只有一个数，
# 然后在开始对这些subset进行排序，排序完了进行合并，直到合并完成
#=======================================================================
def mergeSort(alist):
    #Array给拆了，先得把它拆解掉
    leftArray = []
    rightArray = []

    mid = len(alist)/2
    #把比中间值小的，弄到leftArray
    for i in range(0,mid):
        leftArray.append(alist[i])
        alist.pop(i)

    #把比中间值小的，弄到rightArray
    for j in range(mid,len(alist)):
        rightArray.append(alist[i])
        alist.pop(i)

    while(len(leftArray) > 1):
        mergeSort(leftArray)

    while(len(rightArray) > 1):
        mergeSort(rightArray)

    # print leftAlist
    # print rightArray



def merge(leftAlist,rightAlist,newAlist):
    #当两边的Array都还有数的时候，互相对比，然后把最小值放进新的Array
    while(len(leftAlist) > 0 and len(rightAlist) > 0):
        if leftAlist[0] < rightAlist[0]:
            newAlist.append(leftAlist[0])
            leftAlist.pop(0)
        else:
            newAlist.append(rightAlist[0])
            rightAlist.pop(0)

    #当一边已经没有数的时候，把另一边所有的数都放进信的Array
    while(len(leftAlist) > 0):
        newAlist.append(leftAlist[0])
        leftAlist.pop(0)

    while(len(rightAlist) > 0):
        newAlist.append(rightAlist[0])
        rightAlist.pop(0)

    return newAlist



#Test
if __name__ == "__main__":
