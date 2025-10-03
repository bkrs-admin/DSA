class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # in order to solve it, divide and conquer 
        # first, where not collapsed each other 
        # second where it collapsed each other
        # third where not collapsed til ends 
        # no need to sort it, it's already sorted

        # get global variable for index
        i = 0
        
        # n which length of intervals 
        n = len(intervals)

        # empty array to return 
        res = []

        # first loop, if not collapsed then append it to res
        while i < n and intervals[i][1] < newInterval[0]: 
            # append current value to res
            res.append(intervals[i])

            #increase index to + 1 so it cans search the next 
            i += 1

        # second loop, if collapsed then we need to get final value 
        while i < n and intervals[i][0] <= newInterval[1]:
            # update newInterval where if collapsed point
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])

            #increase index to + 1 so it cans search the next 
            i += 1

        # once newInterval is updated, then append to res
        res.append(newInterval)

        # third loop, just append everything else
        while i < n:
            res.append(intervals[i])
            #increase index to + 1 so it cans search the next 
            i += 1
    
        #return res 
        return res