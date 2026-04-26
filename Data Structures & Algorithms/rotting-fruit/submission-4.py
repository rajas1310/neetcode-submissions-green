class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        fresh_fruits = 0

        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        time =0 

        while q and fresh_fruits>0:
            # step for nodes at one level
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dirs:
                    nr , nc = r + dr , c + dc

                    if 0<= nr < ROWS and 0<= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_fruits -= 1
                        q.append([nr, nc])
                

            time += 1
        
        return time if fresh_fruits == 0 else -1

