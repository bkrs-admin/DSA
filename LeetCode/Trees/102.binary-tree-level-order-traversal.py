# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level order traversal = BFS Breadth First Search

        # so Queue will be helpful, add root to queue, then iterate while q, make sure nested in order to save level by level
        # if not, it will save each individual node by node instead of grouping by level
        
        # base/edge case:
        if not root: return []

        # get queue and append root to queue
        q = deque([root])
        # get an empty array to save each level
        res = []

        # loop through while q is not empty
        while q:
            # temporary array to store each level
            level = []

            # key part. loop over again as long as each level length in q
            for _ in range(len(q)):
                # then popleft the node from queue
                node = q.popleft()

                # now, save node.val to level
                level.append(node.val)

                # if node has left and right, then add it back to queue for next traversal
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            #once for loop is over which mean a level is searched, then add each level to res for our return
            res.append(level)
            
        return res

# T: O(n)
# T: O(n)