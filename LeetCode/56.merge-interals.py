class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # for interval, always started with sort given value. 
        # either using .sort(key = lambda x : x[0]) or sorted(intervals)
        
        intervals = sorted(intervals)
        
        # and set an empty array to store merged intervals, staring with interval[0]
        merged = [intervals[0]]

        # will iterate each current value from interval[1:]
        for current in intervals[1:]:
            # compare one from merged and current, especially [-1][1] vs current[0]
            if merged[-1][1] >= current[0]: 
                # then update [-1][1] vs current[1]
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                # else, just append it
                merged.append(current)
        
        # return merged array 
        return merged 

# T: O(n)
# S: O(n)