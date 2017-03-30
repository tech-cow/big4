from LinkedList import LinkedList

#Iterate Method 1:
def kth_to_last(ll, k):
    count = 0
    runner = ll.head

    # Calculate Length
    while runner:
        count += 1
        runner = runner.next

    size = count - k
    
    index = 0
    cur = ll.head

    for _ in xrange(size):
        cur = cur.next
    return cur


#Iterate Method 2:
def kth_to_last_2(ll, k):
    p1 = p2 = ll.head

    #set p1's position to be kth apart from p2
    for _ in range(k):
        if not p1:
            return
        p1 = p1.next

    #iterate them @ the same pace until p1 reaches null
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2



ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))
print(kth_to_last_2(ll, 3))
