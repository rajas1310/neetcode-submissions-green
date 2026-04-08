class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        INF = 2147483647

        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i,j])
        
        dirs = [[0,1],[-1,0],[0,-1],[1,0]]

        while len(q):
            r, c = q.popleft()
            for dr, dc in dirs:
                next_r, next_c = r + dr , c+dc
                if (0<=next_r<ROWS and 0<=next_c<COLS and grid[next_r][next_c]==INF):
                    grid[next_r][next_c] = grid[r][c] + 1
                    q.append([next_r, next_c])