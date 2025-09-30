
def searchInsert(nums, target):
    # if target val index found - return its index
    # if not found, best index for target val
    left, right = 0, len(nums) - 1 # set two pointers

    while left <= right:
        mid = left + (right - left) // 2 # mid pointer for binary search with prevent integer overflow
        if nums[mid] == target: # if found the target index, return immediately
            return mid
        elif nums[mid] < target: # if smaller than target, move left pointer to mid + 1
            left = mid + 1
        else:                   # if grater than target, move right pointer to mid - 1
            right = mid - 1
            
    return left # return left pointer for potential index position if value not found 

# T: O(log n)
# S: O(1)