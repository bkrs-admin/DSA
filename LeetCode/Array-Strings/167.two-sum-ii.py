class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h_map = {}

        for index, num in enumerate(numbers):
            diff = target - num
            if diff in h_map:
                return [h_map[diff] + 1, index + 1]
            h_map[num] = index

        return []

# T: O(n)
# S: O(n)