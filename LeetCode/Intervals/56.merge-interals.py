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
    
# “First, we sort the intervals by start time, which costs O(n log n).
# Then we iterate through the intervals once to merge overlapping intervals, which is O(n).
# Therefore, total time complexity is O(n log n).
# Space complexity is O(n) because we store the merged intervals and sorted() creates a new list.”