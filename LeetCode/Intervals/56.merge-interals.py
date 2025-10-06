class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        
        return merged 
    
    # “We first sort the intervals by their start time (O(n log n))
    #  and then merge them in a single linear scan (O(n)). 
    # So overall, it’s O(n log n) time and O(n) space.”