import math

def pageCount(n, p):
    front = math.floor(p / 2)
    
    if n % 2 == 1:
        back = math.floor((n-p) / 2)
    else:
        if p == n -1:
            back = 1
        else:
            back = math.floor((n-p) / 2)
            
    return min(front, back)

# T: O(1)
# S: O(1)