#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Title: Binary Search Tree
#  Reference:
# 1. https://www.youtube.com/watch?v=oSWTXtMglKE  #大致
# 2. https://www.youtube.com/watch?v=gm8DUJJhmY4  #PreOrder,InOrder，和PostOrder讲得好
#=======================================================================
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None  #左护法
        self.rightChild = None   #右护法

    def insert(self,newData):
        if newData == self.data:
            return False
        elif newData < self.data:
            if self.leftChild == None:
                self.leftChild = Node(newData)
            else:
                self.leftChild.insert(newData)
        else:
            if self.rightChild == None:
                self.rightChild = Node(newData)
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


    #PreOrder: <Root><Left><Right>
    def preOrder(self):
        print self.data  #先打印Root
        if self.leftChild:  #设置Recursive的条件，self.leftChild = (self.leftChild != None)
            self.leftChild.preOrder()  #再打印左边，然后不停的按照<Root><Left>打印
        if self.rightChild:
            self.rightChild.preOrder()   #当<Left>成为Null的时候，向上返回，开始打印<Right>


    #InOrder: <Left><Root><Right>
    def inOrder(self):
        if self.leftChild:
            self.leftChild.inOrder()
        print self.data #打印leftChild最底层的数
        if self.rightChild:
            self.rightChild.inOrder()

    #PostOrder: <Left><Right><Root>
    def postOrder(self):
        if self.leftChild:
            self.leftChild.postOrder()
        if self.rightChild:
            self.rightChild.postOrder()
        print self.data

if __name__ == '__main__':

    a = [3,8,9,1,2]
    n = Node(5)
    for i in range(len(a)):
        n.insert(a[i])

    # testNode.printMin()
    # testNode.printMax()
    # n.preOrder()
    # n.inOrder()
    # n.postOrder()
