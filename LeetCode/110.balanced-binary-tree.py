# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # set boolean flag with exact memory location
        res = [True] 

        # helper function for 
        def dfs(root):
            if not root: # if not root, height is 0
                return 0
            
            left_height = dfs(root.left) # get left height
            if res[0] == False: # if res already turned to false, then height is 0
                return 0

            right_height = dfs(root.right)  # get right height

            if abs(left_height - right_height) > 1: # if absolute value left_height - right_height
                res[0] = False # res is False and return 0
                return 0

            return 1 + max(left_height, right_height) 
        
        dfs(root) # iterate through from root
        return res[0] #return res boolean value