# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # get a variable to store return value, make sure allocate it
        counter = [0]

        # need helper function taking node and max_val for dfs
        def dfs(node, max_val):
            # edge case, if not node, then stop
            if not node:
                return

            # if node.val is greater or equal to max_val, then counter + 1
            if node.val >= max_val:
                counter[0] += 1

            # create new max val from current node val and max val
            new_max_val = max(node.val, max_val)

            # if node has left and right then dfs with new max val
            if node.left:
                dfs(node.left, new_max_val)
            if node.right:
                dfs(node.right, new_max_val)
        
        # call dfs function with root and root.val which is always good node
        dfs(root, root.val)
        
        # return exact counter value
        return counter[0]
    
# T: O(n)
# S: O(h) worst case O(n)