def catAndMouse(x, y, z):
    dist1 = z - x
    dist2 = z - y
    
    if abs(dist1) < abs(dist2):
        return "Cat A"
    elif abs(dist1) > abs(dist2):
        return "Cat B"
    else:
        return "Mouse C"

# T: O(1)
# S: O(1)