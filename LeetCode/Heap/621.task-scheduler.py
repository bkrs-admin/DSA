from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # needs to have frequency -> while max_heap -> get each frequency -> iterate -> increase times -> add it to temp -> then add back to max_heap unil over 
        # then return final times  -> will be +1 in each iteration 

        # get frequency using Counter
        count = Counter(tasks)
        
        # in order to use max_heap, negativeize freq from count 
        max_heap = [-val for val in count.values()]
        
        # heapify max_heap
        heapq.heapify(max_heap)

        # set empty variable store total times
        times = 0

        #iterate through until max_heap
        while max_heap:
            # set empty array to store freq after using
            temp = []

            # iterate through n + 1 times using for loop -> why n + 1? we need to include n time as well. 
            # so if we have restiriction of 2 then it must iterate 3 times in order to achieve the condition 
            for _ in range(n + 1):

                # so working condition, not idling
                if max_heap:  
                    # pop a freq from max_heap, it is negativeized, so make sure positiveized.
                    freq = -heapq.heappop(max_heap)

                    # if freq is greater than 1
                    if freq > 1: 
                        temp.append(freq - 1) # append it to temp after use and process.
                    
                    # make sure incresing times + 1
                    times += 1
                elif temp: #max heap is empty, all freq used and but element in temp which idling
                    times += 1
            
            #after first for loop for usage process done, then add element backto max_heap until freq == 0
            for element in temp:
                heapq.heappush(max_heap, -element) # makesure negativeized 
                
        #once max_heap is empty which means all freq been used, then return final times
        return times
        
                    
# T: O(n), has to iterate all element size of input
# S: O(n)