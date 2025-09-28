# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode() # set a dummy node 
        curr = d # set a pointer to dummy node
        carry = 0 # set carry value as 0

        while l1 or l2 or carry: #iterate thorugh while l1 or l2 or carry exists, 
            #get a value from l1 and l2 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # get sum of v1 and v2 make sure add carry over to it
            sum_val = v1 + v2 + carry
            # update carry int division by 10
            carry = sum_val // 10
            # get a digit from sum_val using modulo operation by 10
            digit = sum_val % 10
            # set curr.next point to new digit node
            curr.next = ListNode(digit)

            #now move each pointer(curr, l1, l2) to its next pointer if exists
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        #after all done, return dummy.next which pointing a new head from digit
        return d.next


# T: O(n)
# S: O(1)
            