class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # unsorted array of integers, return longest consecutive sequence 
        # must O(n) time, no sorting.

        # base/edge case, if length of nums 0 => return 0
        if len(nums) == 0: return 0

        # create a hash set using nums 
        sett = set(nums)

        # need a variable for return maximum(longest) length
        max_len = 0

        # get element from sett using for loop
        for num in sett:

        # if element - 1 not in sett which means it could be our starting point, then set it as our current num and current length would be 1
            if (num - 1) not in sett:
                curr_num = num
                curr_len = 1

                # get another loop while current_num + 1 in sett, then update current_num and current_length in while loop on each iteration     
                while (curr_num + 1) in sett:
                    curr_num += 1
                    curr_len += 1
                
                # once while loop is over, compare with current length with max length using max function
                max_len = max(max_len, curr_len)

        #return max length 
        return max_len
    
  # T: O(n)
  # S: O(n)