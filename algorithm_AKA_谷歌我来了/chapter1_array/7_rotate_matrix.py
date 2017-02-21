#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================================
# Author: Yu Zhou
# CTCI 1.7 Rotate Matrix:
#       Rotate a MxM clockwise by 90 degree
#================================================================================

class ClassName(object):
    def rotate(self, matrix):
        #运用layer, layer的层数是MxM总长度M的一半
        size = len(matrix)
        layers = size / 2

        #外层的Loop用来进行Layer的向内跌进
        for layer in range(layers):

            first = layer     #跌进到第二层layer的时候，first 和 last的值会dynamically改变
            last = size - first - 1

            for element in range(first, last):
                offset = element - first

                #shallow copy, need to assign back to the original matrix later
                top = matrix[first][element]
                right = matrix[element][last]
                bot = matrix[last][last-offset]
                left = matrix[last-offset][first]

                #top = left
                matrix[first][element] = left
                #right = top
                matrix[element][last] = top
                #bot = right
                matrix[last][last-offset] = right
                #left = bot
                matrix[last-offset][first] = bot
        return matrix

#Main
if __name__ == '__main__':
    m = ClassName()
    mx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    #expected [[7,4,1],[8,5,2],[9,6,3]]
    print m.rotate(mx)
