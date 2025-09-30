def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head # set pointer to point head

    while curr and curr.next: # set loop is over when curr.next.next is none
        if curr.val == curr.next.val: # if curr.val is duplicate with curr.next.val
            curr.next = curr.next.next # we are going to skip 
        else:
            curr = curr.next # else, move curr to curr.next 

    return head # return head which removed duplicate

# T: O(n)
# S: O(1)