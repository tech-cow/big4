#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Title: Binary Search Tree
#
# Node Class诠释：
#
# Binary Search Tree ADT
#   Insert:
#       步骤一：创建新的Node
#
# Reference:
# 1. 视频： https://www.youtube.com/watch?v=oSWTXtMglKE
#=======================================================================
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self,newData):
        #Edge Case: 若value相等，怎么处理word天？
        if newData == self.data:
            return False

        elif newData < self.data:
            if self.leftChild == None:
                self.leftChild == Node(self.data)
            else:
                self.leftChild.insert(newData)

        else:
            if self.rightChild == None:
                self.rightChild == Node(self.data)
            else:
                self.rightChild.insert(newData)

    def findValue(self,newData):
        if newData == self.data:
            return True
        elif newData < self.data:
            if self.leftChild == None:
                return False
            else:
                return self.leftChild.findValue(newData)
        else:
            if self.rightChild == None:
                return False
            else:
                return self.rightChild.findValue(newData)



if __name__ == '__main__':
    testNode = Node(5)
    testNode.insert(6)
    testNode.insert(6)
    print testNode.findValue(6)
