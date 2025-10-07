class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
            
# T: O(n)
# S: O(1)

# I need to check if a string is a palindrome, ignoring non-alphanumeric characters and case.

# I use a two-pointer approach — one starting from the left and one from the right.
# I skip any characters that aren’t letters or digits, and compare the remaining ones.

# If all pairs match, it’s a palindrome.

# This runs in O(n) time since each character is checked once, and uses O(1) extra space.