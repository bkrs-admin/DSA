def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head # set two pointer to head
    
    while fast and fast.next: # while fast and fast.next exists, it stopped when fast.next.next is none:
        #move pointer with each speed
        slow = slow.next
        fast = fast.next.next

    return slow # return slow pointer's position

# T: O(n)
# S: O(1)