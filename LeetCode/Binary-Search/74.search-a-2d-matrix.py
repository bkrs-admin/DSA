# Original Solution
def searchMatrix(matrix, target):
    
    for i in range(len(matrix)):
        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    return False

# T: O(M log n)
# S: O(1)

# Optimized Solution - make 2d array to 1d array lol
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    l = m * n

    left, right = 0, l - 1

    while left <= right:
        mid = left + (right - left) // 2

        if matrix[mid//n][mid%n] == target:
            return True
        elif matrix[mid//n][mid%n] < target:
            left = mid + 1
        else:
            right = mid -1
    
    return False

# T: O(log(m * n))
# S: O(1)

"""
결론적으로, M*N 행렬을 1차원 인덱스 k로 접근할 때, 실제 2차원 좌표는 다음과 같습니다.

matrix[r][c]=matrix[k//N][k%N]
"""