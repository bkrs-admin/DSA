
def hasCycle(self, head: Optional[ListNode]) -> bool:
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True
    
    return False

# T: O(n)
# S: O(1)