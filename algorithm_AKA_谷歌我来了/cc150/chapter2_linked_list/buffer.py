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
