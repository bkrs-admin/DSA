
def hasCycle(self, head: Optional[ListNode]) -> bool:
    # set two pointer for fast and slow, both pointing head
    slow, fast = head, head

    while fast and fast.next: # if fast.next.next is none, then loop stopped
        # move pointer each speed
        slow = slow.next
        fast = fast.next.next

        # if slow and fast met, return True
        if slow == fast:
            return True

    return False # if not met and loop is over, it is false

# T: O(n)
# S: O(1)