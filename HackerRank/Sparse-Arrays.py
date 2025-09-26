def matchingStrings(stringList, queries):
    n = len(stringList)
    q = len(queries)
    result = []
    h_map = {}
    
    for i in range(n):
        h_map[stringList[i]] = h_map.get(stringList[i], 0) + 1
    
    for i in range(q):
        if queries[i] in h_map:
            result.append(h_map[queries[i]])
        else:
            result.append(0)
    
    return result
