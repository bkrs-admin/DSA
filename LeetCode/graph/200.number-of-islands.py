class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        num_islands = 0

        def dfsR(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'):
                return 

            grid[r][c] = '0'

            dfsR(r+1, c)
            dfsR(r-1, c)
            dfsR(r, c+1)
            dfsR(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfsR(r, c)

        return num_islands

# O(m * n)
# O(h), worst case O(m * n)


# The algorithm performs a DFS from every unvisited land cell ('1').
# Each DFS marks all connected land as visited, effectively counting one island per DFS start.

# Time complexity is O(m × n) since each cell is visited once.
# Space complexity is O(h), where h is the recursion depth — in the worst case, it could be O(m × n) if the grid is filled with land.