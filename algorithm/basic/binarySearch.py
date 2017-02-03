#=======================================================================
#  Author: Yu Zhou
#  Title: Binary Search
#
#  Statement:
#  Given a ordered list of integers
#  Search by value
#
#  Sample Input:  3
#  Sample Output: Found
#
# Time Complexity of Solution:
#  Best O(1); Average O(log n); Worst O(log n).
#
#  Approach:
#   Split the Array in half. Average out Max and Min, set the value as Mid
#   While loop: min < max
#   Compare input value to Mid
#        if input > Mid: Get rid of the left side of array, Low = Mid+1
#        if input < Mid: Get rid of the right side of array, High = Mid-1
#   Repeat the same procedure until Mid = input value
#       if found: Return found it
#           else: Return Couldn't find it
#=======================================================================

def binarySearch(array, input):
    #Set Index Value
    min = 0
    max = len(array)-1
    found = False

    while min <= max and not found:
        mid = (min+max)/2
        # print mid
        if array[mid] == input:
            found = True
        else:
            if array[mid] < input:
                min = mid + 1
            elif array[mid]> input:
                max = mid -1
    return found




# Test
print "-------------Test-------------"
sortedArray = [1,2,3,4,5,6,7,8,9,11,12]
print binarySearch(sortedArray, 4) #true
print binarySearch(sortedArray, 10) #false
