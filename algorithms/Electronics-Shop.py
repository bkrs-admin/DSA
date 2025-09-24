# Original Solution
def getMoneySpent(keyboards, drives, b):
    n = len(keyboards)
    m = len(drives)
    
    max_val = float('-inf')
    sum = 0
    
    for i in range(n):
        for j in range(m):
            sum = keyboards[i] + drives[j]
            if sum <= b:
                max_val = max(max_val, sum)
        

    return max_val if max_val > 0 else -1

# T: O(n * m)
# S: O(1)

# Optimized Solution
def getMoneySpent(keyboards, drives, b):
    i, j = 0, 0
    keyboard = sorted(keyboards)
    drives = sorted(drives, reverse=True)
    
    sum = 0
    max_val = float('-inf')
    
    while i < len(keyboard) and j < len(drives):
        sum = keyboard[i] + drives[j]
        
        if sum <= b:
            max_val = max (sum, max_val)
            i += 1
        else:
            j += 1    

    return max_val if max_val > 0 else -1

# T: O(n log n + m log m)
# S: O(1)