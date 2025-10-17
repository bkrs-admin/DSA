class Solution:
    def isValid(self, s: str) -> bool:
        h_map = {'}':'{', ')':'(', ']':'['}

        stk = []

        for char in s:
            if char not in h_map:
                stk.append(char)
            else:
                if not stk:
                    return False
                else:
                    p = stk.pop()

                    if p != h_map[char]:
                        return False
        
        return not stk
    
# O(n)
# O(1)