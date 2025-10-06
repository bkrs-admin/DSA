# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = [True]
        
        def dfsR(root):
            if not root:
                return 0
            
            l_height = dfsR(root.left)
            if res[0] == False:
                return 0

            r_height = dfsR(root.right)

            if abs(l_height - r_height) > 1:
                res[0] = False
                return 0
            
            return 1 + max(l_height, r_height)

        dfsR(root)

        return res[0]
# T: O(n)
# S: O(h) becaue of ealry return 