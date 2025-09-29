# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # edge case handling
            return root
        
        root.left, root.right = root.right, root.left # intert tree

        self.invertTree(root.left) # recursively call for tree's left
        self.invertTree(root.right) # recursively call for tree's right

        return root #return inverted root tree
    
# T: O(n)
# S: O(h) - height of tree