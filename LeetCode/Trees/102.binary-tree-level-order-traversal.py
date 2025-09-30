from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

         #needs to append root to q
        q = deque([root])

        #and needs a variable to store result []
        result = []

        while q:
            #store each level's value to list
            level = []

            #for range of len(q)
            for _ in range(len(q)):
                #pop the first element from q using popleft
                node = q.popleft()

                #append node val to level
                level.append(node.val)

                #if node.left, then append it back to q also right as well
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            #after all level is completed, append level list to result
            result.append(level)

        return result

# T: O(n)
# S: O(w)