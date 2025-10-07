# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = [True]  # To store result across recursive calls

        def dfsR(node):
            if not node:
                return 0

            left_height = dfsR(node.left)

            # Early stop if already unbalanced
            if not res[0]:
                return 0

            right_height = dfsR(node.right)

            # If the difference in height > 1 → unbalanced
            if abs(left_height - right_height) > 1:
                res[0] = False
                return 0

            # Return height for current node
            return 1 + max(left_height, right_height)

        dfsR(root)
        return res[0]
# T: O(n)
# S: O(h) becaue of ealry return 

# This problem asks whether a binary tree is height-balanced.
# I use a bottom-up DFS approach to calculate the height of each subtree.

# For every node, I compare the heights of its left and right subtrees.
# If the difference is more than one, I mark the tree as unbalanced and stop further recursion.

# This runs in O(n) time since each node is visited once, and it uses O(h) space due to the recursion stack.