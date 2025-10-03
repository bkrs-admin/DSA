class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # two way to solve this problem 
        # 1. simple, compare length of nums and set(nums), return True if not the same, else false, T: O(n), S:O(n)
        # 2. A bit longer, but possible situation for early return which could be fater in some case, T: O(1), worst O(n), S: O(n)


        # first way - simple comparison 
        # return len(set(nums)) != len(nums)

        # second way - early return
        
        # create a hashset
        sett = set()

        # using for loop , iteration num in nums
        for num in nums:
            # if num in sett, return True
            if num in sett:
                return True
            
            # if num not in sett, add num to sett
            sett.add(num)

        #if loop is over then no duplicate found, return False
        return False
            