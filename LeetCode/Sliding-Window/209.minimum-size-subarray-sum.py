def minSubArrayLen(target, nums):
    
    min_len = float('inf')
    curr_sum = 0
    left = 0
    n = len(nums)
    
    for right in range(n):
        curr_sum += nums[right]

        while curr_sum >= target : 
            min_len = min(min_len, right - left +1)

            curr_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0