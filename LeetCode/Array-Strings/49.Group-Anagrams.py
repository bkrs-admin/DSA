from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # it's simple and difficult at the same time 
        # so we have to check which are pair of anagram
        # in order to do that, we need a key to group anagram str in strs as values

        # so there is a couple way to create a key, will use defaultdict for this now
        # using default dict, will be T:(n * k log k) 

        # first, create a defaultdict with list, make sure import defaultdict 
        # d_dict = defaultdict(list)

        # # second, now we need to iterate str from strs
        # for s in strs: 
        #     # third, we are going to create key, make sure sort s in order to get a unique key
        #     key = "".join(sorted(s)) => tuple(sotred(s)) also works!
            
        #     # forth, then now append s to key's array 
        #     d_dict[key].append(s)

        # return list(d_dict.values())

        # actually we can optimize that to T: O(n * k), k = length of strings(s)
        
        # same for defaultdict, it's much easier and simple 
        d_dict = defaultdict(list)

        # also same method to iterate str in strs
        for s in strs:

            #instead of using sorted, we can create some special key cause there's only 26 characters in english 
            count = [0] * 26 # set an array with 26 0
            for c in s: # iterate char in s, and get a distance as a key and increased it 
                count[ord(c) - ord('a')] += 1

            # same method, in our count key position, append s            
            d_dict[tuple(count)].append(s)

        # same method, return list type of d_dict values
        return list(d_dict.values())