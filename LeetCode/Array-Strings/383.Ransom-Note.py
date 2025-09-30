def canConstruct(ransomNote, magazine):
    h_map = {}

    for char in magazine:
        h_map[char] = h_map.get(char, 0) + 1
    
    for char in ransomNote:
        if char in h_map and h_map[char] > 0 :
            h_map[char] -= 1
        else:
            return False

    return True

r = "aa" 
m = "aab"
a = canConstruct(r, m)

print(a) # expected true

