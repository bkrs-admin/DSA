# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode() # val will be 0
        dummy.next = head # pointing head
        ahead, behind = dummy, dummy # both pointer pointing dummy 

        for _ in range(n + 1): # move ahead pointer to n + 1 position 
            ahead = ahead.next

        while ahead: # if ahead ends, that's at behind where needs to be removed 
            ahead = ahead.next
            behind = behind.next
            
        behind.next = behind.next.next # remove it to point to .next.next

        return dummy.next # return dummy.next which pointing head (or head.next)

        