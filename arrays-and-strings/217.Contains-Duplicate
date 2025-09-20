def containsDuplicate(nums):
        # in order to check duplicate elements from array, hash set/map is great. 
        # what I need is only check if there is duplicate rather than its frequency,
        # so I would choose hash set instead of hashmap.

        # create a variable uisng set
        sett = set()
        
        # iterate elements from array nums
        for num in nums:
            # if element not in set, 
            if num not in sett:
                sett.add(num) # add element to set
            else:
                return True # else, found duplicate return True 
        
        return False #return false which it has no duplicate in nums
        # or simplyfied, Return len(set(nums)) != len(nums)

arr = [1,2,3,1]

a = containsDuplicate(arr)
print(a)

# T - O(n)
# S - O(s)



