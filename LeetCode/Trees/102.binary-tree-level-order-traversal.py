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
        
        q = deque([root])
        
        ans = []

        while q: 
            level = []
            
            for _ in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)

        return ans 

# O(n)
# O(n)

# “I implemented a level order traversal using BFS with a queue.
# Each node is processed once, so the time complexity is O(n).
# The space complexity is O(n), since in the worst case the queue holds all nodes in the last level.”