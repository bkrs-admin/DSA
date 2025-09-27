def search(nums, target):
    left, right = 0, len(nums) - 1 # two pointer for binary search

    while left <= right:
        mid = left + (right - left) // 2 # get mid pointer with int overflow prevention 

        if nums[mid] == target: # if value found, return mid index
            return mid
        elif nums[mid] >= nums[left]: # mid val is greater or equal to left val,
            if nums[left] <= target <= nums[mid]: # if target still in left and mid val, move right mointer to mid - 1
                right = mid - 1
            else:
                left = mid + 1 # else move left pointer to mid + 1
        else:                  # or mid val is smaller or equal to left val 
            if nums[mid] <= target <= nums[right]: # then it target is in range or mid , right val, then move left pointer to mid + 1
                left = mid + 1
            else:
                right = mid - 1 # else move right pointer to mid - 1
        
    return -1 # return -1 if target not found in nums
