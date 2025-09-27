def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return None

    h_map = {} # needs hash map for copying unique values from current value/random/next 

    curr = head # set pointer to head
    while curr:
        val = Node(curr.val) # get current values next, random, value info
        h_map[curr] = val # insert it to h_map
        curr = curr.next # move pointer to next

    curr = head # reset the pointer to head
    while curr:
        if curr.next: # if curr.next exists, then update hash map's curr val's next 
            h_map[curr].next = h_map[curr.next]
        if curr.random: # same thing for curr random
            h_map[curr].random = h_map[curr.random]
        curr = curr.next # move pointer to next
    
    return h_map[head] # return final h_map 

# T: O(n)
# S: O(n), cause used hash map to save values