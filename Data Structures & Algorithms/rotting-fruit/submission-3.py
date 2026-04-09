class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        time = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        while q and fresh > 0:

            qlen = len(q)

            for i in range(qlen):
                r,c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0<= nr < ROWS and 0<= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append([nr, nc])
                
            time += 1
        
        return time if fresh == 0 else -1