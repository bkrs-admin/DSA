class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i != j != k 
        # and nums[i] + nums[j] + nums[k] == 0
        # and not contain duplicate triplets

        # first, sort nums
        nums.sort()

        #second, empty array for result value
        result = []

        # optionally, n for len(nums)
        n = len(nums)

        # iterate nums array using for loop and range of n
        for i in range(n):
            # if nums[i] is greater than 0, then just break 
            if nums[i] > 0:
                break
            
            # if i is greater than 0 and nums[i] == nums[i -1], then skip to continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # now our game is started, get two pointer to search 
            low, high = i + 1, n - 1
            # while low is smaller than high,
            while low < high: 
                #get curr sum using current index, low, high value
                curr_sum = nums[i] + nums[low] + nums[high]
                # curr sum is equal to zero, then append to result
                if curr_sum == 0: 
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    # while two pointer not met and low and its prev value the same, then move low pointer - 1
                    while low < high and nums[low] == nums[low - 1]: 
                        low += 1
                    # while two pointer not met and low and its prev value the same, then move high pointer + 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                # if curr_sum is greater than 0, we need more bigger value, move low pointer + 1
                elif curr_sum < 0:
                    low += 1
                else:
                    high -= 1
        
        return result
  
  # T: O(n^2)
  # S: O(n)