# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # edge case first
        if not subRoot: # if not subRoot, then True
            return True 

        if not root: # if not root, return False
            return False
        
        # needs helper function to check if it is same tree
        def isSameTree(r, s):
            #edge case
            if not r and not s: #if root and subroot both null, return True
                return True 
            
            if not r or not s: # if one of them is missing, return False
                return False

            # if both value and right and left equal, then it's SameTree
            return (r.val == s.val and isSameTree(r.right, s.right) and isSameTree(r.left, s.left))

        if isSameTree(root, subRoot): # if it passed the sametree condition, return true
            return True

        # return boolean val if root.left and subroot is the same, or root.right, subroot is the same
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# T: O(n * m)
# S: O(ht + hs)