class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l = m * n

        l, r = 0, l - 1
        
        while l <= r:
            m = l + (r - l) // 2
            
            if matrix[m//n][m%n] == target:
                return True

            if matrix[m//n][m%n] < target:
                l = m + 1
            else: 
                r = m - 1
            
        return False