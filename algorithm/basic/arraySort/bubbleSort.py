#=======================================================================
#  Author: Yu Zhou
#  Title: Bubblesort
#
#  Statement:
#  Given a disordered list of integers (or any other items),
#  rearrange the integers in natural order.
#
#  Sample Input:  [1,2,9,3,4,100,99,30]
#  Sample Output: [1,2,3,4,9,30,99,100]
#
# Time Complexity of Solution:
#  Best O(n^2); Average O(n^2); Worst O(n^2).
#
#  Approach:
#   Bubblesort is an elementary sorting algorithm. The idea is to
#   imagine bubbling the smallest elements of a (vertical) array to the
#   top; then bubble the next smallest; then so on until the entire
#   array is sorted. Bubble sort is worse than both insertion sort and
#   selection sort. It moves elements as many times as insertion sort
#   (bad) and it takes as long as selection sort (bad). On the positive
#   side, bubble sort is easy to understand. Also there are highly
#   improved variants of bubble sort.
#
#  0] For each element at index i from 0 to n, loop:
#  1] For each element at index k, from n to i exclusive, loop:
#  2] If the element at k is less than that at k-1, swap them.
#=======================================================================
def swap(arr, num_1, num_2):
    temp = arr[num_1]
    arr[num_1] = arr[num_2]
    arr[num_2] = temp


def bubbleSort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(0,i):
            if (array[j] > array[j+1]):
                swap(array,j,j+1)
    return array


# Test
print "-------------Test-------------"
numArray_1 = [1,2,9,3,4,100,99,30]
print bubbleSort(numArray_1)
