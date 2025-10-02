import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # so will have an array to store k closest values 
        
        res = []

        # so are going to iterate points array, and get a sqrt, and then push that to res array while the length is equla to k
        # if conditions met and if res is getting greater than K then pop it first then push it 

        for x, y in points:
            # get sqrt
            sqrt = (x*x) + (y*y)
            
            # now we need to append sqrt and it's origin point, make sure push it as max_heap
            if len(res) < k:
                heapq.heappush(res, (-sqrt, [x, y]))
            else:
                # current sqrt is smaller than -res[0][0], then replace it.
                if sqrt < -res[0][0]:
                    heapq.heapreplace(res, (-sqrt, [x,y]))

        # now need to return the k closest points from res and in array 
        return [points for _, points in res]
    
    # T: O(n log k)
    # S: O(k)