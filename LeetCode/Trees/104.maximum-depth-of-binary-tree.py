# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Maximum Depth of Binary Tree -> DFS, Depth First Search

        # in order to get it, we need to get each depth on root.left and root.right using DFS(recuisve)
        # then will return 1 (depth itself) + max value between left and right, keep doing the same work

        # base/edge case, if not root, then just return 0
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# T: O(n)
# S: O(h), worst case O(n)