from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # edge case handling
        if not p and not q:
            return True
        queue = deque([(p, q)]) # queue it's first root val

        while queue: # iterate through while node exists in queue
            p_node, q_node = queue.popleft() # pop each node to compare

            if not p_node and not q_node: # if both node is missing, continue
                continue

            if not p_node or not q_node or p_node.val != q_node.val : # if each node value not equal or one of node is missing
                return False # return False

            # append each node's left and right node to queue
            queue.append((p_node.left, q_node.left))
            queue.append((p_node.right, q_node.right))
        
        return True # return True if passed all
