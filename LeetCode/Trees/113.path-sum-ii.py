# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # get empty array to store path and return
        res = []

        # get helper function taking node, remaining_sum, current_path for dfs 
        def dfs(node, remaining_sum, curret_path):
            # edge case
            if not node:
                return 
            
            # append node.val to current path to track 
            current_path.append(node.val)

            # subtract node.val from remaining sum
            remaining_sum -= node.val 

            # if all searched left and right and remaining sum == 0: 
            if not node.right and node.left and remaining_sum == 0:
                res.append(current_path[:]) # then append current_path deep copy to res

            # call dfs until it gets to leap which the end from left 
            if node.left:
                dfs(node.left, remaining_sum, current_path)
            if node.right:
                dfs(node.left, remaining_sum, current_path)

            current_path.pop() # if it got to the leap, then pop to go back which is backtracking

        
        # call the function to start
        dfs(root, targetSum, [])

        # return res 
        return result
    
# T: O(n)
# S: O(n)