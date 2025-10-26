class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []

        def dfs():
            if len(nums) == len(curr):
                res.append(curr[:])
                return

            for x in nums:
                if x not in curr:
                    curr.append(x)
                    dfs()
                    curr.pop()

        dfs()

        return res

# T: O(n^2)
# S: O(n)