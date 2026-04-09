class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac_flow = [[False] * COLS for _ in range(ROWS)]
        atl_flow = [[False] * COLS for _ in range(ROWS)]

        def bfs(queue, ocean_flow):
            q = deque(queue)
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]


            while q:
                r, c = q.popleft()
                ocean_flow[r][c] = True

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if 0<= nr <ROWS and 0<= nc < COLS and (not ocean_flow[nr][nc]) and heights[r][c] <= heights[nr][nc]: 
                        q.append([nr,nc])


        
        # create queue for pacific ocean and one for atlantic ocean
        pacific_queue = []
        atlantic_queue = []  

        for j in range(COLS):
            pacific_queue.append([0,j])
            atlantic_queue.append([ROWS-1,j])

        for i in range(ROWS):
            pacific_queue.append([i,0])
            atlantic_queue.append([i,COLS-1])
        
        bfs(pacific_queue, pac_flow)
        bfs(atlantic_queue, atl_flow)

        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if pac_flow[i][j] and atl_flow[i][j]:
                    result.append([i,j])

        return result