
def sortedSquares(nums):
    n = len(nums)
    left = 0
    right = n - 1

    result = [0] * n
    r_pointer = n - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[r_pointer] = (nums[left] * nums[left])
            left += 1
            r_pointer -= 1
        else:
            result[r_pointer] = (nums[right] * nums[right])
            right -= 1
            r_pointer -= 1
    
    return result

# T: O(n)
# S: O(n)