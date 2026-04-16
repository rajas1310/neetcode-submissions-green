class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        res = 0

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        q = deque()

        found = False
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    q.append([i,j])
                    found = True
                    break    
            if found: break
        
        while q:
            r,c = q.popleft()
            if grid[r][c] == -1:
                continue

            grid[r][c] = -1

            for dr, dc in dirs:
                nr, nc = r+dr , c+dc
                if not (0<=nr<ROWS and 0<=nc<COLS):
                    res += 1
                elif grid[nr][nc] == 0:
                    res += 1
                elif grid[nr][nc] == 1:
                    q.append([nr, nc])
          
        return res