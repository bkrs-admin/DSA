from collections import defaultdict

def groupAnagrams(strs):
    # two way to solve this question
    # first - counting array, great for longer text, for alphanumeric, 
    # second - sorting , great for shorter text, for letter varierty than alphanumeric 

    # first solution - counting arr, contraints = lowercase english letters
    # T: O(N'M), S O(N'K), M = length of word, K = unique count(which 26)
    
    # reset defaultdict to list type so when access to key, if not exists, then it creates empty list automatically
    # res = defaultdict(list)

    # # iterate each value in strs
    # for s in strs:
    #     #create an array with size of 26 which lowercase letter counts
    #     count = [0] * 26

    #     for c in s: # iterate each letter again
    #         count[ord(c) - ord('a')] += 1 # calculate each letter is how far from 'a' and increase count + store to count
        
    #     #once each letter count is cleared, then append s in count index
    #     # since array is not hashable, so change it to tuple 
    #     res[tuple(count)].append(s)

    # # return final values (which is word) in list(array) format
    # return list(res.values())

    # Second solution - Sorting
    # T: O(N'M log M) , S: O(N'M)

    # reset defaultdict to list type so when access to key, if not exists, then it creates empty list automatically
    res = defaultdict(list)

    for s in strs: # iterate each values from given strs
        sig = "".join(sorted(s)) # create signature using sorted function

        # if not using defaultdict, then have to create empty array first
        # if sig not in res:
            # res[sig] = []

        res[sig].append(s) # then in signature key, append s value 
    
    # # return final values (which is word) in list(array) format
    return list(res.values())

s = ["eat","tea","tan","ate","nat","bat"]

a = groupAnagrams(s)

print(a)


# Another solution using only hash map without defaultdict
def groupAnagrams(strs):
    h_map = {}

    for s in strs:
        sig = "".join(sorted(s))

        if sig not in h_map:
            h_map[sig] = []
        
        h_map[sig].append(s)
            

    return list(h_map.values())