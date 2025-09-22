# 0 find the minimum value 
# 1 diagonal sum, no matter negetive/positive number 
# 2 compare with max value, and update max value
# return max value

# constaints  = 6x6 limited  so total 4 loop 
# 1st loop [0][0] + [0][1] + [0][2] + [1][1] + [2][0] + [2][1]+ [2][2]
# 2nd loop [0][1] + [0][2] + [0][3] + [1][2] + [2][1] + [2][2]+ [2][3]
            
# 3rd loop [0][2] + [0][3] + [0][4] + [1][3] + [2][2] + [2][3]+ [2][4]
# 4th loop [0][3] + [0][4] + [0][5] + [1][4] + [2][3] + [2][4]+ [2][5]
#                 [i][j]         
# first loop      0   0 1 2      
#                 1   1          
#                 2   0 1 2
# second loop     0   1 2 3     
#                 1   2
#                 2   1 2 3
# third           0   2 3 4     
#                 1   3
#                 2   2 3 4
# fourth          0   3 4 5     
#                 1   4
#                 2   3 4 5

def hourglassSum(arr):    
    n = len(arr)
    max_val = float('-inf')
    curr_sum = 0
    
    for i in range(n - 2): # i = 0, 1,2,3,
        for j in range(n - 2):
            curr_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] 
                                  + arr[i+1][j+1] 
                    + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
                    
            max_val = max(max_val, curr_sum)

    return max_val

ar = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
a = hourglassSum(ar)

print(a)