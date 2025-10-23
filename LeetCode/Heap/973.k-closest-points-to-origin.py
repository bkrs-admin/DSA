class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []

        for x, y in points:
            sqrt = (x*x) + (y*y)

            if len(res) < k:
                heapq.heappush(res, (-sqrt, [x, y]))
            else:
                if sqrt < -res[0][0]:
                    heapq.heapreplace(res, (-sqrt, [x, y]))
        
        return [points for _, points in res]
    
# T: O(n log k)
# S: O(k)