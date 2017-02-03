def arrayLength(array):
    print len(array)

a = [1,2,3,4]
arrayLength(a)

# The reason we need to subtract arraySize by one, is because index starts from 0
# And if we plug in our arraySize into array[arraySize], it will exceed the index by 1 if not been
# Subtracting earlier.
