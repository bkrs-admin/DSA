# Original Version
def majorityElement(nums):
    n = len(nums)
    freq = n/2
    h_map = {}
    
    for num in nums:
        h_map[num] = h_map.get(num, 0) + 1

    for num in nums:
        if h_map[num] >= freq:
            return num

# T: O(n)
# S: O(n)

# Optimized Version - Boyer-Moore Voting Algorithm
def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

# T: O(n)
# S: O(1)!