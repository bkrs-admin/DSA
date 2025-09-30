from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # get empty array to return 
        res = []

        # in order to level order traversal, will use queue for bfs
        q = deque([root])

        while q: # loop conditionally iterate while queue
            rightSide = None # this will be used to store overwritten right side value

            for _ in range(len(q)): # will use for loop to iterate each level
                node = q.popleft() # pop node FIFO order
                
                if node : # if node exists
                    rightSide = node #override right side value
                    q.append(node.left) # append left and right, make sure append it in order
                    q.append(node.right)

            # after for loop is over, rightSide is override with latest value which right side view val, append to res
            if rightSide:
                res.append(rightSide.val)
        
        return res # return final res array

# T: O(n)
# S: O(n)