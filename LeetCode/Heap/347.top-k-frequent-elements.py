from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Top K frequent = need to check freq, I will use counter 
        count = Counter(nums)

        return [num for num, _ in count.most_common(k)]
    
# T: O(n log k)
# S: O(k)