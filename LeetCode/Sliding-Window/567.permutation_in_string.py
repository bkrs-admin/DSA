class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        s1_map = {}
        s2_map = {}
        
        for i in range(len1):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

        if s1_map == s2_map:
            return True 
        
        for i in range(len1, len2):
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

            old_char = s2[i - len1]
            s2_map[old_char] -= 1
            
            if s2_map[old_char] == 0:
                del s2_map[old_char]
            
            if s1_map == s2_map:
                return True
        
        return False