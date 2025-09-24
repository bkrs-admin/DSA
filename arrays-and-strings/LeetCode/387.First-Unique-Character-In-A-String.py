# Original solved
def firstUniqChar(s):
    h_map = {}

    for char in s:
        h_map[char] = h_map.get(char, 0) +1

    for i, char in enumerate(s):
        if h_map[char] == 1:
            return i

    return -1

#Using Counter
from collections import Counter
def firstUniqChar(s):
    freq = Counter(s)
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1

#T: O(n)
#S: Worst case - O(n),  in this case O(1)
