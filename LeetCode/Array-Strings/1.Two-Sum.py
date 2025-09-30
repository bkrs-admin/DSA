def twoSum(nums, target):
        # need to track of indexee as well as element's value 
        # to do so, will use hash map to store elements's value as key, its indexee as value

        # get an empty hashmap 
        h_map = {}

        # using enumerate(), iterate val and index at the same time
        for index, val in enumerate(nums):
            # get a difference(complement) from target and val
            diff = target - val
            
            #if diff in h_map:
            if diff in h_map:
                #return current index and diff's value which is its index in array
                return [index, h_map[diff]]
            else: # if diff not in h_map
                h_map[val] = index # add current value and its index as key:value pair

        # if not found, just return empty array
        return []


n = [2, 7, 11, 15]
t = 9

a = twoSum(n, t)
print(a)

# Time and Space complexity 
# T: O(n), S:O(s) 
# T - One for loop for time complexity, store key:value to hashmap is constant time 
# S - and worst case scenario is store length of array to hashmap which is O(n) space