class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []


        def dfs(index):
            if len(nums) == index:
                res.append(cur[:])
                return
            
            dfs(index + 1)
            
            cur.append(nums[index])

            dfs(index + 1)

            cur.pop()

        dfs(0)

        return res
    
# T: O(n^2)
# S: O(n)