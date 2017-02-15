class Stack():
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        self.arr.remove(self.arr[len(self.arr)-1])

    def display(self):
        print self.arr

if __name__ == '__main__':
    arr = Stack()
    for i in range(1,10):
        arr.push(i)
    arr.display()
    arr.pop()
    arr.display()
