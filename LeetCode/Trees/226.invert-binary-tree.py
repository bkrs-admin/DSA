# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # so we need to invert binary tree
        # which mean node's left to right and right to left

        # base/edge case 
        if not root: return root

        # now process the inverting binary tree
        root.left, root.right = root.right, root.left
        
        # will do the left and right node as well
        self.invertTree(root.left)
        self.invertTree(root.right)

        #finally return root
        return root 

# T: O(n)
# S: O(h)