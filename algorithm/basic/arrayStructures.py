from random import randint

# Create Array
arraySize = 9
indexArray = []
valueArray= []

print "\n"
print "  ARRAY"
for i in range(50):
    indexArray.append(i+1)
    valueArray.append(randint(10,20))

def displayArray():
    for i in range(arraySize):
        print "-----------"
        print indexArray[i] , "  |  " , valueArray[i]

# Find Value by Index
def findValueByIndex(index):
    if index <= len(indexArray) :
        return valueArray[index-1]

# Find if the array contains a value/ Boolean
def valueExistence(value):
    isExistence = False
    for i in range(arraySize):
        if value == valueArray[i]:
            isExistence = True
            return isExistence

# Delete Value
def deleteValueByIndex(index):
    if index < arraySize:
        for i in range(index-1,arraySize-1):
            valueArray[i] = valueArray[i+1]
        global arraySize
        arraySize -=  1

# Insert Value
def insertValueByIndex(index, value):
    if index < arraySize:
        # Reverse traversal, cur = cur - 1
        for i in range(arraySize+1,index-1,-1):
            valueArray[i]= valueArray[i-1]
        # Replace Value
        valueArray[index-1] = value
        global arraySize
        # Increment arraySize
        arraySize +=  1

#index + 1 =  index
# replace current index with intended value

#increment arraySize

# Linear search Value

# Sort array



# Main
displayArray()
print "\n"
print "-------------Test-------------"
print "Value 15 exists?           ", valueExistence(15)
print "Value at Index 3:          ",findValueByIndex(3)
# print "Delete Index 3:            ", deleteValueByIndex(1)
print "Insert (4,20)              ", insertValueByIndex(7,100)

displayArray()
