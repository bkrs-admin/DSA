class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        # min length of subarray whose sum is greater than or equal to target

        # we need a variable for min length, set it as inf value to whichever comes, it updates
        min_length = float('inf')
        
        # left pointer 
        left = 0
        
        # length of array
        n = len(nums)

        # curr_sum variable to store current sum value
        curr_sum = 0

        # will iterate nums using for loop and index as right pointer
        for right in range(n):
            # expand window until curr_sum is greater or equal to target
            curr_sum += nums[right]

            # in while curr_sum is greater than or equal to target
            while curr_sum >= target:
                # update current window size
                window = (right - left) + 1
                min_length = min(min_length, window)
                
                #then substract left pointer value from curr_sum
                curr_sum -= nums[left]
                # and move left pointer + 1
                left += 1
        
        # return min_length if updated, else return 0
        return min_length
# T: O(n)
# S: O(1), worst case O(n)

"I use a sliding window with two pointers. "
"The right pointer expands the window, and once the sum reaches or exceeds the target, "
"I shrink the window from the left to minimize length. Time complexity is O(n) and space is O(1)."