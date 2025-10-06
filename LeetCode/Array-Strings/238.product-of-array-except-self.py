class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums : integer array
        # answer[i] : is equal to the product of all the elements of nums except itself

        # algorithm runs O(n) time -> no nested loop without using the division operation 

        # we need to have an size of nums array to store return value
        n = len(nums)
        res = [1] * n

        left = 1        
        # multiply previous result by the lement just before current index 
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # set a variable with 1 becaue no element to the right of last index
        right = 1  
        # using for loop, this time iterate from back to front of nums[i]
        for i in range(n - 1, -1, -1):
            # multiply existing left product by current right product
            res[i] *= right

            # update right product to include current element for next ietration 
            right *= nums[i]

        return res
    
#T: O(n)
#S: O(n)
"I build the result array in two passes. "
"First, I accumulate the product of elements to the left of each index. "
"Then I multiply by the product of elements to the right of each index in a second pass. "
"This avoids using division and runs in O(n) time with O(n) space."