class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #nums of islands, we can approach to solve this question using DFS and BFS
        # I prefer to use DFS cause it's more simple, easy to read.

        # in this case, if not grid: return 0 is not required cause m,n is at least 1 which will have at least 1 element

        # get leng th of rows and cols to search
        rows, cols = len(grid), len(grid[0])
        # a variable to count total islands
        total_islands = 0

        # now we are going to write a function for Depth first search
        def dfs(r, c):
            # edge case here, 
            # 1. if out of bound of rows (left and right) or
            # 2. if out of bound of cols (top and bottom) or
            # or if not near island ( ==0 or != 1)
            # just return it

            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'):
                return 
            
            # and now make current visited island to 0 so we don't come to visit repeatly 

            grid[r][c] = '0'

            # and now search near islands (left, right, top, bottom)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # nested for loop that search possible or every elements in 2D grid
        for r in range(rows):
            for c in range(cols):
                #if we found the islands which value == 1, then increase number of islands(total_islands) and using dfs for search
                if grid[r][c] == '1':
                    total_islands += 1
                    dfs(r,c)

        return total_islands

# T: O(r * c)
# S: O(r * c)