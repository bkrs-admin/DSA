class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        # farthest = 0

        # for i in range(n):
        #     if i > farthest:
        #         return False
            
        #     farthest = max(farthest, i + nums[i])
        
        # return farthest >= n - 1

        target = n - 1

        for i in range(n-1, -1, -1):
            if i + nums[i] >= target:
                target = i

        return target == 0
    
# T: O(n)
# S: O(1)

# “i + nums[i] represents the farthest index we can reach from the current position i.
# By taking the max with the previous farthest, we continuously track the maximum reachable index.
# If at any point the current index exceeds this farthest value, we cannot proceed, so we return False.”

# Front to back
# “We iterate from the start, tracking the farthest index reachable.
# If at any point the current index exceeds farthest, the last index is unreachable.
# Otherwise, we update farthest with the maximum of itself and i + nums[i].
# Finally, if farthest reaches or passes the last index, the last index is reachable.
# Time complexity is O(n) and space complexity is O(1).”

# back to front
# “We start from the last index as the target.
# Iterating backwards, if the current index plus nums[i] reaches or exceeds the target, we update the target to the current index.
# If the target reaches 0, the last index is reachable from the start.
# This greedy approach is O(n) time and O(1) space because we traverse the array once and use constant extra memory.”