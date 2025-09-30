# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # edge case handling, root1 and root2 both null
        if not root1 and not root2:
            return None

        # get each root value to sum
        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0

        # create a new tree with sum of val1 and val2
        root = TreeNode(val1 + val2)

        # call mergeTrees function recursively to merge both left and right and store to new merged tree
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        
        # return root which our merged tree
        return root