# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode() # in order to handling edge case, set a dummy node
        d.next = head # and dummy.next point to head
        a, b = d, d # set two pointers for removing nth node, start it from dummy node 

        for _ in range(n + 1): # move a pointer to n + 1
            a = a.next # so it will be stopped at n th node
        
        while a: #now need to move a,b node while a is not none
            a = a.next
            b = b.next

        b.next = b.next.next # now set next pointer to .next.next 

        return d.next # return dummy.next which pointing head
    
# T: O(n)
# S: O(1)

        