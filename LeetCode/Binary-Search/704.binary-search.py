def search(nums, target):
    left, right = 0, len(nums) - 1 # two pointer for binary search

    while left <= right:
        mid = left + (right - left) // 2 # integer division with integer overflow prevention

        if nums[mid] == target: # if found, return mid pointer index
            return mid
        elif nums[mid] < target: # if smaller than target, move left to mid +1
            left = mid + 1
        else:                    # if greater than target, move right to mid -1
            right = mid - 1

    return -1 # return -1 if target not in nums

# T: O(log n)
# S: O(1)