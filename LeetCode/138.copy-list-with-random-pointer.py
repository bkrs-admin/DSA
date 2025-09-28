def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    # Edge case first
    if not head:
        return None

    h_map = {} # get empty hash map to store key:value fair for curr pointer and its val/random/next pointer info
    curr = head # get a pointer that point to head

    while curr: # iterate through til end of list
        val = Node(curr.val) # using curr.val, get a value 
        h_map[curr] = val # add val to hash map as curr(key):val(value) pair
        curr = curr.next #move pointer to next

    curr = head # reset the pointer to point head
    while curr: # once again iterate linked list til end(None)
        if curr.next: # if curr.next exists
            h_map[curr].next = h_map[curr.next] # now add curr.next info to hash_map
        if curr.random: # if curr.random exists
            h_map[curr].random = h_map[curr.random] # now add curr.random info to hash_map
        curr = curr.next # and move pointer to next

    return h_map[head] # return h_map[head] 

# T: O(n)
# S: O(n), cause used hash map to save values