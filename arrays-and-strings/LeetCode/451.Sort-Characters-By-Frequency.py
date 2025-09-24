# Original Solution
def frequencySort(s):
    h_map = {}
    res = ""
    for char in s:
        h_map[char] = h_map.get(char, 0) + 1

    sorted_map = sorted(h_map.items(), key=lambda x:x[1], reverse = True)

    for i, val in enumerate(sorted_map):
        for j in range(val[1]):
            res += val[0]
            
    return 

#T: O(n log n)
#S: O(n)


# Optimized Solution - Using Bucket Sort
import collections 
def frequencySort(s):
    # 1. 빈도수 계산: O(N)
    freq_map = collections.Counter(s)
    
    # 2. 버킷 생성: 최대 빈도수 + 1 크기
    max_freq = max(freq_map.values()) if freq_map else 0
    buckets = [[] for _ in range(max_freq + 1)]
    
    # 3. 버킷에 문자 채우기: O(N)
    for char, freq in freq_map.items():
        buckets[freq].append(char)
        
    # 4. 결과 문자열 생성: O(N)
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        if buckets[i]:
            for char in buckets[i]:
                result.append(char * i)
                
    return "".join(result)

#T: O(n) !!
#S: O(n)