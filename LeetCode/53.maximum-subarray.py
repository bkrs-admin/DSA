class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
# “We track the current subarray sum with curr_sum.
# If curr_sum becomes negative, it cannot contribute to a larger sum in the future, so we reset it to zero.
# max_sum keeps the largest sum found so far.
# This approach is O(n) time and O(1) space.”