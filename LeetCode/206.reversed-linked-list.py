class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    
    # T: O(n)
    # S: O(1), only use a variable to store pointer