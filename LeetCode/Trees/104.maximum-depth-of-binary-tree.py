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

# This solution uses DFS recursion to compute the maximum depth of a binary tree.
# For each node, we return 1 plus the maximum of the depths of its left and right subtrees.

# Time complexity: O(n), since every node is visited once.
# Space complexity: O(h), where h is the height of the tree (O(log n) for balanced, O(n) for skewed).