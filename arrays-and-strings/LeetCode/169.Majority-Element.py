def majorityElement(nums):
        n = len(nums)
        freq = n/2
        h_map = {}
        
        for num in nums:
            h_map[num] = h_map.get(num, 0) + 1

        for num in nums:
            if h_map[num] >= freq:
                return num
        