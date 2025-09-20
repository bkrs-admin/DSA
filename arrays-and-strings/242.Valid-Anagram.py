from collections import Counter

def isAnagram(s: str, t: str) -> bool:
        # anagram = same letter but different combinations 
        
        # so it has to have the same letter count of each letter
        # we need to check the freq, so hashmap is great choice.
        # or sorted and compare 

        # edge case, if not the same lenth of s, t, return False
        if len(s) != len(t):
            return False

        # first solution - using hashmap + Counter
        s = Counter(s)
        t = Counter(t)

        return s == t

        # second, - hashmap without conter
        # a = {}
        # b = {}

        # for char in s:
        #     a[char] = a.get(char, 0) + 1
        
        # for char in t:
        #     b[char] = b.get(char, 0) + 1

        # return a == b

        # third - using sort + compare

        # return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"

a = isAnagram(s,t)

print(a)

# Time and Space Complexity
# 1. Counter & Hashmap- T: O(N), S: O(k), k= length of word <- The best solution, simple and clean
# 2. Sort and compare - T: O(N log N), S: O(N), 
    # if input contains unicode, it could return false due to different unicodes from characters, cases, and etc