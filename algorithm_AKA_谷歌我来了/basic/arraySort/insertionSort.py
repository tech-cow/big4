#!/usr/bin/python
#coding:utf-8   这样就可以打中文了
#=======================================================================
#  Author: Yu Zhou
#  Title: Insertion Sort
#
# Time Complexity of Solution:
#  Best O(1); Average O(log n); Worst O(log n).
#
# 算法核心：
# 从Index[1]开始向左比较，不从Index[0]因为只要Index[1]和Index[0]比较，
# Index[0] 自然就Sort好了，不需要重复的从0开始。
# 若是左边的数比current的值小，就和其交换位置，知道没有更小，在进行下一组的循环
#=======================================================================


#Sort
def insertionSort(alist):
    for i in range(1,len(alist)):  # INDEX从1开始,因为从0开始的话，左边没有数比较
        j = i   #直接在接下来的While Loop用i的话，会导致外圈的ForLoop崩盘，所以建一个小白鼠j
        while j > 0 and alist[j] < alist[j-1]:  #j>0是因为，当j等于1的时候，就已经和左边的0比过了，所以没必要循环到0，0会对你很无语的。
            alist[j-1],alist[j] = alist[j],alist[j-1]  #pyhon里面特有的Swap格式
            j = j -1  #递减
    return alist

# Test
print "-------------Test-------------"
A = [2,1,3,9,7,99,10,38,18]
print insertionSort(A)
