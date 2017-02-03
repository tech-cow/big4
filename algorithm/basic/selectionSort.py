#Go over the loop, find the smallest num
def swap(arr, num_1, num_2):
    temp = arr[num_1]
    arr[num_1] = arr[num_2]
    arr[num_2] = temp

def selectionSort(alist):
    for i in range(0, len(alist)-1):
        min = i
        # for j in range(i+1, len(alist)):
        for j in range(i, len(alist)-1):
            if alist[j] < alist[min]:
                min = j
        if min != i :
            swap(alist,i,min)
    return alist

0 1 2 3 4
2 2 3 4 5 


# Test
print "-------------Test-------------"
A = [2,1,9,3,4,100,99,30]
print selectionSort(A)

     2 3 4  5  6   7
A = [,3,4,100,99,30]

min = index
