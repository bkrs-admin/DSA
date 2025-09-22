def dynamicArray(n, queries):

    # declare 2d array arr, n empty arrays all zero indexed
    arr = [[] for _ in range(n)]
    
    # declare last answer and initialize it to 0
    lastAnswer = 0
    result = []
    
    # size of array 2, size of queries 5
    # queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
    # query 1, x, y
    # index = x + lastAnswer , y to arr[index]
    # query 1,0,5  1, x, y
    # index = 0(x) + 0(lastAnswer) = arr[0]  and y val = 5
        
    for q,x,y in queries:
        #case 1, if query 1, x, y
        if q == 1:
            #compute idx = (x ^ lastAnswer) % 2
            idx = (x ^ lastAnswer) % 2
            
            #append the integer y to arr[idx]
            arr[idx].append(y)
            
        # else case,
        else:
            #compute idx = (x ^ lastAnswer) % 2
            index = (x ^ lastAnswer) % 2
            
            #set lastAnswer = arr[idx][y%len(arr[idx])]
            # due to get y%len(arr[idx]), handle in seperate line/variable
            z = y % len(arr[index])
            lastAnswer = arr[index][z]
            
            #stor the new value of lastanswer in an answers array
            result.append(lastAnswer)
            
    #return answers array
    return result

n = 2
queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]

a =dynamicArray(n, queries)

print(a)