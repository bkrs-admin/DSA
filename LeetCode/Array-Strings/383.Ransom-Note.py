from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransom_count = Counter(ransomNote)
        # magazine_count = Counter(magazine)

        # # for char, cnt in ransom_count.items():
        # #     if magazine_count[char] < cnt:
        # #         return False
        
        # # return True

        # return not(ransom_count - magazine_count)

        h_map = {}

        for c in magazine:
            h_map[c] = h_map.get(c, 0) + 1

        for c in ransomNote:
            if c not in h_map or h_map[c] == 0:
                return False
            h_map[c] -= 1
        
        return True

# T: O(m + n)
# T: O(n)