class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
                return
            grid[row][col] = '0'  # Mark as visited
            dfs(row + 1, col)     # Down
            dfs(row - 1, col)     # Up
            dfs(row, col + 1)     # Right
            dfs(row, col - 1)     # Left
        
        num_islands = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands