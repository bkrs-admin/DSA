import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # condition == if x and y the same, destoryed. else, push difference to array again until most one stone left. if no stones left, then return 0

        # I would approach maxHeap since no min heap in python 
        
        # Edge case, if len of stone == 0 return 0
        if len(stones) == 0: 
            return 0

        #let's convert element to negetive number so we can use max heap
        max_heap = [-stone for stone in stones]
        
        heapq.heapify(max_heap)

    
        # while len of max_heap greater than 1, will iterate the elements from maxHeap and compare if it's the same(destroy), else push back to max_heap until len of max_heap == 1
        while len(max_heap) > 1:
            
            # get first and second element, expecting -8 and -7
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            # check condition if first and second not the same, 
            if first != second:
                #then get a difference and push back to max_heap
                diff = first - second
                heapq.heappush(max_heap, diff)

        # return non negetive number for fianl result if element exists in max_heap else return 0
        return -max_heap[0] if max_heap else 0 