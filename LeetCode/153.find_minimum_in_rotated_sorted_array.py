class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_value = float('inf')

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                min_value = min(min_value, nums[mid])
                right = mid - 1
        
        return min_value