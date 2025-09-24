def formingMagicSquare(s):
    res = []
    min_cost = float('inf')
    magic_squre = [
        [8,3,4,1,5,9,6,7,2],
        [8,1,6,3,5,7,4,9,2],
        [6,7,2,1,5,9,8,3,4],
        [6,1,8,7,5,3,2,9,4],
        [4,9,2,3,5,7,8,1,6],
        [4,3,8,9,5,1,2,7,6],
        [2,7,6,9,5,1,4,3,8],
        [2,9,4,7,5,3,6,1,8],]
        
    for i, val in enumerate(s):
        for j, val2 in enumerate(val):
            res.append(val2)
    
    for i in range(len(magic_squre)):
        cost = 0
        for j in range(len(res)):
            cost += abs(res[j]- magic_squre[i][j])
            
        min_cost = min(min_cost, cost)
        
    return min_cost

# because input size is already set to size of 9 elements.
# T: O(1)
# S: O(1)