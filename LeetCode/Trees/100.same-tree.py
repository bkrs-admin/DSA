from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p: return True

        q = deque([(p, q)])

        while q: 
            p_node, q_node = q.popleft()

            if not p_node and not q_node:
                continue
            
            if not p_node or not q_node or p_node.val != q_node.val:
                return False
            
            q.append((p_node.left, q_node.left))
            q.append((p_node.right, q_node.right))

        return True

# T: O(n)
# S: O(w) worst case O(n)

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # 둘 다 None이면 같음
#         if not p and not q:
#             return True
        
#         # 하나만 None이거나 값이 다르면 False
#         if not p or not q or p.val != q.val:
#             return False
        
#         # 좌우 서브트리 재귀 확인
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



# The goal is to check if two binary trees are structurally identical and have the same node values.

# DFS
# I use a simple DFS recursion that compares nodes pair by pair.
# If both nodes are None, they’re identical. If one is None or their values differ, return False.
# Otherwise, I recursively check the left and right subtrees.

# This runs in O(n) time since we visit each node once, and O(h) space due to the recursion stack.

# BFS
# You can also implement this iteratively using two queues — one for each tree.
# At each step, pop from both, compare values, and push their left/right children in sync.
# If any mismatch occurs (structure or value), return False.

# That BFS approach is logically equivalent, still O(n) time and O(n) space (queue).