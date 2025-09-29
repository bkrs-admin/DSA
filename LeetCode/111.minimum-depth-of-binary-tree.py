from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # edge case handling
        if not root: 
            return 0
        
        # because of min depth, BFS(queue) is useful and efficient.
        queue = deque([(root, 1)]) # queue root with its depth

        while queue:

            #get root and its depth
            curr_root, curr_depth = queue.popleft()

            # if curr_root's left and right are null, return current depth
            if not curr_root.right and not curr_root.left: 
                return curr_depth

            # append child node to queue to search more
            if curr_root.left:
                queue.append((curr_root.left, curr_depth + 1))
            
            if curr_root.right:
                queue.append((curr_root.right, curr_depth + 1))

        
# T: O(n)
# S: O(h), worst case O(n)
            
