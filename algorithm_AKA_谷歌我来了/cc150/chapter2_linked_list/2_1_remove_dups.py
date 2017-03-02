from LinkedList import LinkedList

#Temp Buffer allowed: use hash table
def remove_dups(ll):
    if ll.head is None:
        return

    hash = {}
    cur = ll.head

    while cur.next:
        if cur.next.value in hash:
            cur.next = cur.next.next
        else:
            hash[cur.next.value] = 1
            cur = cur.next
    return ll

#Temp Buffer not allowed?
# 2 pointer
def remove_dups_followup(ll):
    if ll.head is None:
        return

    cur = ll.head
    while cur:
        runner = cur
        while runner.next:
            if runner.next.value == cur.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next
    return ll








ll = LinkedList()
ll.generate(10, 0, 9)
print(ll)
remove_dups(ll)
print(ll)

ll.generate(10, 0, 9)
print(ll)
remove_dups_followup(ll)
print(ll)
