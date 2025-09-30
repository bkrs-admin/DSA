# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # edge case handling 
        if not root:
            return 0
        
        # return 1 (root) + maxDepth compared value from call root.left and root.left recursively
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# T: O(n)
# S: O(h), worst case O(n)