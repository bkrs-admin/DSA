import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min heap and self k , will use heap in init and add, and k in add
        self.min_heap, self.k = nums, k 
        # heapify min heap 
        heapq.heapify(self.min_heap)
        # if heap is longer than k, then pop until it's smaller than k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # heap push val to min_heap 
        heapq.heappush(self.min_heap, val)
        # if heap is greater then k, pop it
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        #return [0] index which is the k largest element in heap
        return self.min_heap[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# T: O(k)
# S: O(k)