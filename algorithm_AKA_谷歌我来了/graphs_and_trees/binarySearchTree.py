#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Title: Binary Search Tree
#
#  Reference:
# 1. https://www.youtube.com/watch?v=oSWTXtMglKE  #大致
# 2. https://www.youtube.com/watch?v=gm8DUJJhmY4  #PreOrder,InOrder，和PostOrder讲得好
#=======================================================================
class Node(object):
    def __init__(self, data, left=None, right=None, parent=None):
        self.left = left  #左护法
        self.data = data
        self.right = right   #右护法


class Tree(object):
    def __init__(self):
        #先设置一个空的Node，之后再Insert的时候往里面放数
        self.root = Node(None)

        #test purpose lists
        self.preOrderList = []
        self.inOrderList = []
        self.postOrderList = []

    def search(self, newData):
        if self.root.data == None:
            return False
        else:
            return self.__search(self.root, newData)

    def __search(self, root, newData):
        if root.data == newData:
            return True
        else:
            if newData < root.data:
                if root.left:
                    return self.__search(root.left, newData)
                else:
                    return False
            else:
                if root.right:
                    return self.__search(root.right, newData)
                else:
                    return False

    def insert(self, newData):
        if self.root.data == None:
            self.root.data = newData
        else:
            self.__insert(self.root, newData)

    def __insert(self, root, newData):
        if newData < root.data:
            if root.left:
                self.__insert(root.left, newData)
            else:
                root.left = Node(newData)
        elif newData > root.data:
            if root.right:
                self.__insert(root.right, newData)
            else:
                root.right = Node(newData)
        else:
            print newData,' is Already in the list'

    def inOrderTraversal(self):
        if self.root:
            self.__inOrderTraversal(self.root)

    def __inOrderTraversal(self,root):
        if root.left:
            self.__inOrderTraversal(root.left)
        #Append list & Print
        self.inOrderList.append(root.data)
        print root.data
        if root.right:
            self.__inOrderTraversal(root.right)

    def preOrderTraversal(self):
        if self.root:
            self.__preOrderTraversal(self.root)

    def __preOrderTraversal(self,root):
        #Append list & Print
        self.preOrderList.append(root.data)
        print root.data
        if root.left:
            self.__preOrderTraversal(root.left)
        if root.right:
            self.__preOrderTraversal(root.right)


    def postOrderTraversal(self):
        if self.root:
            self.__postOrderTraversal(self.root)

    def __postOrderTraversal(self,root):
        if root.left:
            self.__postOrderTraversal(root.left)
        if root.right:
            self.__postOrderTraversal(root.right)
        #Append list & Print
        self.postOrderList.append(root.data)
        print root.data







#test
if __name__ == '__main__':

    bst = Tree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(1)
    bst.insert(7)

    print("pre order")
    bst.preOrderTraversal()
    # self.assertEqual(bst.preOrderList, [5,3,1,4,7])

    print("in order")
    bst.inOrderTraversal()
    # self.assertEqual(bst.inOrderList, [1,3,4,5,7])

    print("post order")
    bst.postOrderTraversal()
    # self.assertEqual(bt.postOrderList, [1,3,4,5,7])
