class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):          

            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
                grid[r][c] = "0"

                dirs = [(0,1), (0,-1), (1,0), (-1, 0)]
                for dr, dc in dirs:
                    dfs(r + dr, c +dc)
            

        
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        
        return count