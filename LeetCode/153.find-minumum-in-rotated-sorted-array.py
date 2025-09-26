
def findMin(nums):
    left, right = 0, len(nums) - 1 # two pointer
    ans = float('inf') # tmp variable with infinity value to compare minimum for return value

    while left <= right:
        mid = left + (right - left) // 2 # mid pointer using int overflow
        
        if nums[mid] > nums[right]: # right value is greater than mid, move left to mid + 1
            left = mid + 1 
        else:                       # else, save potential min value to ans and move right to mid -1
            ans = min(ans, nums[mid])
            right = mid - 1
            
    return ans # return ans

# T: O(log n)
# S: O(1)