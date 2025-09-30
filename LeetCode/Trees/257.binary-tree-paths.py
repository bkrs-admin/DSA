# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # get array to store list value
        res = []
        
        # helper function to search dfs
        def dfs(node, current_path): 
            # if node has no left, right then it means leaf
            if not node.left and not node.right:
                # append current_path and return
                res.append(current_path)
                return

            # if left exists
            if node.left:
                # created a new path from current_path and left.val
                new_path = current_path + "->" + str(node.left.val)
                # and do dfs 
                dfs(node.left, new_path)
            
            # if right exists
            if node.right:
                # created a new path from current_path and right.val
                new_path = current_path + "->" + str(node.right.val)
                # and do dfs
                dfs(node.right, new_path)
        # first call helper function with root and root.val for current_path
        dfs(root, str(root.val))

        return res # return res array
  
# T: O(n * l), worst case O(n^2)
# S: O(n * l), worst case O(n^2)