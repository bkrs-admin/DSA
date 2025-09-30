
def findMaxAverage(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    n = len(nums)

    for i in range(k, n):
        curr_sum = curr_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, curr_sum)

    return float(max_sum/k)

# T: O(n)
# S: O(1)