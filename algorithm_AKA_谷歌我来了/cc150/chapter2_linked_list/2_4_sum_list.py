from LinkedList import LinkedList


def sum_lists(ll_a, ll_b):
    carry = 0
    n1, n2  = ll_a.head, ll_b.head
    ll = LinkedList()

    while n1 or n2:
        sum_count = carry
        if n1:
            sum_count += n1.value
            n1 = n1.next
        if n2:
            sum_count += n2.value
            n2 = n2.next

        ll.add(sum_count% 10)
        carry = sum_count // 10

    if carry:
        res.add(carry)

    return ll



ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print(sum_lists(ll_a, ll_b))
# print(sum_lists_followup(ll_a, ll_b))
