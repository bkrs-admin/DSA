# Original Solution
def isPalindrome(s):
    s = s.lower()

    left = 0
    right = len(s) - 1 

    while left < right:
        if (s[left].isalnum() and s[right].isalnum()) and s[left] == s[right]:
            left += 1
            right -=1
        elif (s[left].isalnum() and s[right].isalnum()) and s[left] != s[right]:
            return False
        
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -=1
        
    
    return True
# T: O(n)
# S: O(1)


# Optimized Solution
def isPalindrome(s):
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