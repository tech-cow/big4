from LinkedList import LinkedList

def del_mid_node(n):
    n.next = n.next.next
    n.value = n.next.next.value


ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
del_mid_node(middle_node)
print(ll)
