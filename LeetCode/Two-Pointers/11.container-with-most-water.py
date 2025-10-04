class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height array
        # n = len(height)

        #i, 0 and i, height[i]
        #find two lines that together with x-axis from a contationer that can contain most water
        # return max amount of water which mean max area 

        # in order to get the max area, will use two pointer that start it fron beginning and end
        
        left = 0
        right = len(height) - 1
        
        #also need a variable for max value , preset to -inf in order to store any amount of area(water)
        max_area = float('-inf')

        # while two pointers are not met, check and compare 
        while left < right:
            # in order to get area, we need width and height 
            w = right - left 
            h = min(height[left], height[right])
            curr_area = w * h
            max_area = max(max_area, curr_area)

            # after updating max_area comparing with current area, move pointer
            if height[left] < height[right]: # if right height is taller than left height, keep right, move left
                left += 1
            else:                            # else, keep left and move right
                right -= 1
        
        return max_area 
            

# T: O(n)
# S: O(1)