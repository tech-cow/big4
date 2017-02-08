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
    def __init__(self, l=None, r=None):
        self.left = l
        self.right = r
