import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Kth largest in sorted order - maxHeap, get kth element to return , get it done without sorting 

        # in order to use max_heap, make elements to negetive number
        max_heap = [-num for num in nums]

        # and heapify max_heap, then will get sorted result
        heapq.heapify(max_heap)

        # will pop the element for k-1 times so, if k == 2, then we need to pop only once 
        for i in range(k-1):  
            heapq.heappop(max_heap)

        return -max_heap[0] # return the 0 index which our kth largest element with non negetive value
            