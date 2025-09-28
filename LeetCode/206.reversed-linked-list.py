class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # set pointer to head
        prev = None # set prev as None

        while curr: # while curr pointer iterate through
            tmp = curr.next # stor/save curr.next to tmp
            curr.next = prev # switch curr.next pointer to prev 
            prev = curr # and move prev pointer to curr
            curr = tmp # and move curr pointer to tmp which curr.next 

        return prev # return prev which is the new beginning 
    
    # T: O(n)
    # S: O(1), only use a variable to store pointer