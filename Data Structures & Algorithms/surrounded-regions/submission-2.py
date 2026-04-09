class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs():
            q = deque()
            for row in range(ROWS):
                for col in range(COLS):
                    if (row in [0,ROWS-1] or col in [0, COLS-1]) and board[row][col] == "O": 
                        q.append([row,col])

            while q:
                r,c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                
                    for dr, dc in dirs:
                        nr , nc = r +dr, c + dc
                        if 0<= nr < ROWS and 0<= nc < COLS:
                            q.append([nr, nc])
                    
            
        bfs()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
                