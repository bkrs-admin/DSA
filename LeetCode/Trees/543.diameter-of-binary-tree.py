# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # set non local variable for res value
        res = [0]

        def dfs(root): # helper function for dfs 
            # edge case, if not root, then return 0
            if not root:
                return 0
            
            # get l and r height
            l_height = dfs(root.left)
            r_height = dfs(root.right)

            # update res with diameter
            res[0] = max(res[0], l_height + r_height)

            return 1 + max(l_height, r_height) # return current subtree's height
        
        dfs(root) # call dfs at root

        return res[0] # return res which updated diameter