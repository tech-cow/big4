#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Title: Binary Search Tree
#
#  Reference:
# 1. https://www.youtube.com/watch?v=oSWTXtMglKE  #大致
# 2. https://www.youtube.com/watch?v=gm8DUJJhmY4  #PreOrder,InOrder，和PostOrder讲得好
# 3. https://github.com/minsuk-heo/problemsolving/blob/master/data_structure/BinaryTree.py  写的让我舒服的代码
#=======================================================================
class Node(object):
    def __init__(self, data, left=None, right=None, parent=None):
        self.left = left  #左护法
        self.data = data
        self.right = right   #右护法
        self.parent = parent

class Tree(object):
    def __init__(self):
        #先设置一个空的Node，之后再Insert的时候往里面放数
        self.root = Node(None)

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
                root.left.parent = root

        elif newData > root.data:
            if root.right:
                self.__insert(root.right, newData)
            else:
                root.right = Node(newData)
                root.right.parent = root

        else:
            print newData,' is Already in the list'

    def inOrderTraversal(self):
        if self.root:
            self.__inOrderTraversal(self.root)

    def __inOrderTraversal(self,root):
        if root.left:
            self.__inOrderTraversal(root.left)
        print root.data
        if root.right:
            self.__inOrderTraversal(root.right)

    def preOrderTraversal(self):
        if self.root:
            self.__preOrderTraversal(self.root)

    def __preOrderTraversal(self,root):
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
        print root.data



#=======================================================================
# delete
# 该方程里面解决所有base case的比较
# 基于只有最初始的Root，和最初始的Root.left以及Root.right
# 若当输入的数，不符合Root，Root.left以及Root.right其中的值
# 将调用另外一个比较方程__delete
#=======================================================================
    def delete(self,newData):
        if self.root.data == None:
            print 'The tree is empty'
        else:
            self.__delete(self.root, newData)

    def __delete(self, root, newData):
        if newData < root.data:
            if root.left:
                self.__delete(root.left, newData)
            else:
                return False
        elif newData > root.data:
            if root.right:
                self.__delete(root.right, newData)
            else:
                return False
        elif newData == root.data:
            #case 1, root has no child
            if root.left is None and root.right is None:
                if root.parent == None:  #先确认老大他爹存不存在，不存在的话，这个就是起始的Root,然后将其删除
                    root = None
                elif root.parent.left == root: #要是现在这个Root Node是其他Node的Child，我们不删除Root本身，因为Pass by value，传递不上去
                    root.parent.left = None    #我们把Root.parent的Child删掉，这样可以向上传递
                else: #elif root.parent.right == root:
                    root.parent.right = None
                print 'case 1: deleting', newData
                return True

            #case 2, root has one child (left)
            elif root.left is not None and root.right is None:
                root.data = root.left.data      #root.data = root.parent.left.data
                #假如左边的Child还有Child的话：
                root.right = root.left.right
                root.left = root.left.left
                print('case 2: deleting', newData)
                return True

            #case 3, root has one child (right)
            elif root.right is not None and root.left is None:
                root.data = root.right.data
                #假如右边的Child还有Child的话：
                #if root.right.left :
                root.left = root.right.left
                root.right = root.right.right
                print 'case 3: deleting', newData
                return True

            #case 4, root has both children,
            # find the smallest node in the right subtree, and swipe value
            # delete smallest node in the right subtree
            else:
                minRightNode = self.__minValueToRightSubtree(root.right)
                root.data = minRightNode.data
                if minRightNode == root.right:
                    root.right = root.right.right
                else:
                    minRightNode.parent.left = None
                print 'case 4: deleting', newData
                return True
        else:
            print "Can't find this number"

    def __minValueToRightSubtree(self, root):
        if root.left is None:
            return root
        else:
            return self.__minValueToRightSubtree(root.left)

#test
if __name__ == '__main__':

    bst = Tree()
    bst.insert(6)
    bst.insert(4)
    bst.insert(8)
    bst.insert(7)
    bst.insert(1)
    bst.insert(5)
    bst.insert(9)
    bst.insert(10)
    print("in order")
    bst.inOrderTraversal()
    bst.delete(8)
    bst.inOrderTraversal()
