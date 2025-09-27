def reorderList(self, head: Optional[ListNode]) -> None:
    # first, divide half  using slow, fast
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # second, reverse second half
    second = slow.next
    prev = slow.next = None # make sure disconnect slow.next from divided half
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # third, merge divided half
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

# T: O(n)
# S: O(1)