from LinkedList import LinkedList

#p1 is kth position apart from p2
#while p1 gets to null, return p2

def kth_to_last(ll, k):
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
