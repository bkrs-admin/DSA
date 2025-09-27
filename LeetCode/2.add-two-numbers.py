# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if sum of two val is greater than 10, then % get 1s and carry 10s
        dummy = ListNode() # set a dummy node
        curr = dummy # set a curr pointer to pointing to dummy
        carry = 0 # set carry as 0

        while l1 or l2 or carry: # iterate until l1 or l2 or carry not null
            # get each value to get sum value
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0

            sum_val = val1 + val2 + carry # get sum val 
            carry = sum_val // 10 # get carry value from sum values
            digit = sum_val % 10 # get  digit
            curr.next = ListNode(digit) # curr.next pointing new digit value
            
            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# T: O(n)
# S: O(1)
            