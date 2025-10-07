# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = new_head
            new_head = curr
            curr = temp

        return new_head

#T: O(n)
#S: O(1)

# I use an iterative approach with two pointers.
# I start with a pointer curr at the head and a new_head set to None.
# In each iteration, I temporarily store the next node, 
# reverse the current node’s pointer to point to the previous head, 
# then move both pointers one step forward.
# When the loop finishes, new_head points to the reversed list’s head.

# The time complexity is O(n) since I visit each node once,
# and the space complexity is O(1) because I only use a few variables.


#  # Base case: empty list or last node reached
#         if not head or not head.next:
#             return head

#         # Recursively reverse the rest of the list
#         new_head = self.reverseList(head.next)

#         # Reverse the current node's link
#         head.next.next = head
#         head.next = None

#         return new_head