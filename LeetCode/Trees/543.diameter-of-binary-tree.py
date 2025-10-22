# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]

        def dfsR(root):
            if not root: return 0

            left = dfsR(root.left)
            right = dfsR(root.right)
            diameter = left + right
            largest_diameter[0] = max(largest_diameter[0], diameter)

            return 1 + max(left, right)

        dfsR(root)

        return largest_diameter[0]
    
# T: O(n)
# S: O(h)