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
