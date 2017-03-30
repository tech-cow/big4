from LinkedList import LinkedList

#With Temp Buffer, Checking cur.next
#Function takes a list as its parameter
def remove_dups(ll):
    counts = {}
    #Set a runner
    cur = ll.head
    #Edge Case
    counts[cur.value] = 1

    while cur.next:
        if cur.next.value in counts:
            cur.next = cur.next.next
        else:
            counts[cur.next.value] = 1
            #This is super important, don't forget
            cur = cur.next
    return ll


#With Temp Buffer, Checking cur
def remove_dups_2(ll):
    counts = {}
    cur = ll.head

    while cur:
        if cur.value in counts:
            if cur.next:
                cur.value = cur.next.value
                cur.next = cur.next.next
            else:
                # This doesn't really solve the edge Case....
                cur.value = None
        else:
            counts[cur.value] = 1
            cur = cur.next
    return ll





ll = LinkedList()
ll.generate(10, 0, 9)
print(ll)
remove_dups(ll)
print(ll)
