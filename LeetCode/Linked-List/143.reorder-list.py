def reorderList(self, head: Optional[ListNode]) -> None:
    # first, divide by half
    slow, fast = head, head # set a two pointer pointing head
    while fast and fast.next: # iterate through while fast and fast.next exists == fast.next.next not exists
        #move each pointer by each speed
        slow = slow.next
        fast = fast.next.next

    # second, reverse divided half
    second = slow.next # set second to point slow.next which divided half
    prev = slow.next = None # and make sure slow.next point to None so it is sperated and prev = None for reverse

    while second: # while second is iterated/reversed
        tmp = second.next # store second.next to temp pointer
        second.next = prev # and switch second.next pointer to point to prev
        prev = second # and now prev pointer move to second 
        second = tmp # and second pointer move to temp which second.next

    # third, merge two lists
    first, second = head, prev # in order to merge two list, make sure first and second pointing right list
    while second: # while second is all merged
        tmp1, tmp2 = first.next, second.next # need to store first.next and second.next to temporary pointers
        first.next = second # now merge it. so first.next should be second
        second.next = tmp1 # and second.next should be tmp1 which is first.next 
        first, second = tmp1, tmp2 # and move first and second to its .next pointing to,

# T: O(n)
# S: O(1)