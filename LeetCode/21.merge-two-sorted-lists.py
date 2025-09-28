# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    d = ListNode() # set a dummy node 
    curr = d # set a pointer that pointing to dummy node

    while list1 and list2: # iterate through list1 and list2 which ever longer
        if list1.val < list2.val: #if list1 val is smaller than list2.val, 
            curr.next = list1 # curr.next point to smaller linked list 
            list1 = list1.next # move list1 to list1.next 
        else:                 # else, do it opposite way
            curr.next = list2
            list2 = list2.next
        #move curr pointer to curr.next
        curr = curr.next

    curr.next = list1 if list1 else list2 # connect remaining linked list

    return d.next # return d.next which pointing to beginning of merged list


# T: O(n)
# S: O(1)