class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + (r - l) // 2
            hrs = sum(math.ceil(p/k) for p in piles)

            if hrs <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
    
# T: O(n log m)
# S: O(1)
# The point is not binary searching in an array.
# It needs to catch the speed of consuming, so start from 1 (left) to max(right)
# then get mid speed to consume in bananas from piles 
# if speed is faster, then update our min speed and move right pointer to k - 1 
# in order to find the real min speed to consume
# if hrs not enough to consume all piles, then move left pointer in order to speed up.