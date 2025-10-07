class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            m = left + (right - left) // 2

            if nums[m] == target:
                return m
            
            if nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        
        return -1
  
#T: O(log n)
#S: O(1)

# This is a classic Binary Search problem.
# Since the input array is sorted, I can use two pointers, left and right, to define the current search boundaries.
# I repeatedly check the middle element — if it matches the target, I return its index.
# If the middle element is smaller than the target, I move the left pointer to m + 1; otherwise, I move the right pointer to m - 1.
# This way, the search space is reduced by half in every iteration.

# The time complexity is O(log n) because we divide the array in half each step, and the space complexity is O(1) since we only use a few variables.
