from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first solution using counter + sort
        # freq = Counter(nums)
        # items = list(freq.items())
        # items.sort(key = lambda x:x[1], reverse = True)
        # result = []        
        # for i in range(k):
        #     result.append(items[i][0])

        # return result

        # second solution using counter + most_common 
        # freq = Counter(nums)
        # return [nums for nums, _ in freq.most_common(k)]

        
        # third solution - bucket sort 
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq.items():
            bucket[freq].append(num) 

        result = []

        for i in range(len(nums), 0, -1):
            result.extend(bucket[i])
            if len(result) == k:
                return result[:k]

        return result
    
        # fourth solution - min heap
        # freq = Counter(nums)
        # min_heap = []

        # for num, freq in freq.items():
        #     heapq.heappush(min_heap, (freq, num))


        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)

        # result = []
        # while min_heap:
        #     result.append(heapq.heappop(min_heap)[1])

        # return result
# T: O(n log k) or O(n) with bucket sort
# S: O(n)
