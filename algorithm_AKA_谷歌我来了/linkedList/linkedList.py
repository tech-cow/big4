#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Title: Linked List
#
# Node Class诠释：
#   在Constructor里面设置一个初始Value还有一个指针， 指针初始的面向对象为NULL,
#    原因是，第一个插入的Node没有指向对象
#   之后在对指针的指向进行更改哟！
#
# Linked List ADT
#   Insert:
#       步骤一：创建新的Node
#       步骤二：把Node插入到最左边，然后将Node指向之前的HeadNode
#       步骤三：将刚插入的Node变成新的HeadNode，这样之后要插入新的Node时候，会指向现在这个Node
#
#   Size: 返回LinkedList的大小
#       步骤一: 写一个Current，将他设置成最左边的HeadNode，
#       步骤一: 写一个Counter,放入循环
#       步骤一: 循环到最后一个Node的时候，会指向NULL，然后结束LOOP。最终返还Counter

#   Search: 寻找LinkedList拥不拥有某个数，没有则返回Error
#   Delete: 先调用Search，然后删除。Search不到则返回Error

# Reference:
# 1. https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
#=======================================================================



class Node(object):
    def __init__ (self, data, n = None):
    #Private
        self._data = data
        self._next = n    #指针默认指向NULL

    #Getter & Setter
    def getData(self):
        return self._data

    def getNext(self):
        return self._next

    def setData(self, newData):
        self._data = newData

    def setNext(self,newNext):
        self._next = newNext


class LinkedList (object):
    def __init__ (self):
        self.head = None   #为当Linkedlist刚创建的时候，里面还没有Node，HeadNode只能指向NULL

    def isEmpty(self):
        return self.head == None   #若Head不是Null，return False, Vice Versa

    def insert(self,data):
        new_node = Node(data)  #创建新的Node
        new_node.setNext(self.head) #把Node插入到最左边，然后将Node指向之前的HeadNode
        self.head = new_node   #将刚插入的Node变成新的HeadNode，这样之后要插入新的Node时候，会指向现在这个Node

    def size(self):
        current = self.head
        count = 0

        while current:  #当Current循环到最后一个Node，会自动指向NULL，所以会结束While循环
            count += 1
            current = current.getNext()
        return count

    def display(self):
        alist = []
        current = self.head
        while current:
            alist.append(current.getData())
            current = current.getNext()
        return alist

    def search(self,data):
        current = self.head
        found = False
        while current and found is False:   #这里用and和or都行？
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        if current is None:  #当Loop完以后，current指向Null，切没有按照While里面的Condition找到数，就返回Error
            raise ValueError("Data not found")
        return current

    def delete(self,data):
        current = self.head
        previous = None
        found = False

        while current and found is False:   #这里用and和or都行？
            if current.getData() == data:
                found = True
            else:
                previous = current        # Loop，每次循环一次，将循环完的Node保存到一个函数Previous，之后方便调用
                current = current.getNext()
        if current is None:  #当Loop完以后，current指向Null，切没有按照While里面的Condition找到数，就返回Error
            raise ValueError("Data not found")
        if previous is None:        #What is this corner case for?    
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())



# test
if __name__ == '__main__':
    newList = LinkedList()
    print newList.isEmpty()
    newList.insert("ads")
    newList.insert(5)
    newList.insert(10)
    print newList.isEmpty()
    print newList.display()
    newList.delete("ads")
    print newList.display()
