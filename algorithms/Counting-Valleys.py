def countingValleys(steps, path):
    alt = 0
    valleys = 0
    
    for s in path:
        if s == "U":
            alt += 1
        else:
            alt -= 1
        
        if alt == 0 and s == "U":
            valleys += 1
    
    return valleys

# T: O(n)
# S: O(n)