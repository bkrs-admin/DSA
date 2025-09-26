
def twoSum(numbers, target):
    h_map = {}

    for i, val in enumerate(numbers):
        diff = target - val
        if diff in h_map:
            return [h_map[diff] + 1, i+1]
        else:
            h_map[val] = i


    return []

# T: O(n)
# T: O(n)