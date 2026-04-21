class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        A = [[0]*COLS for _ in range(ROWS)]

        for i in range(ROWS):
            if obstacleGrid[i][0] != 1:
                A[i][0] = 1
            else:
                break
        
        for i in range(COLS):
            if obstacleGrid[0][i] != 1:
                A[0][i] = 1
            else:
                break
        
        for i in range(1,ROWS):
            for j in range(1, COLS):
                if obstacleGrid[i][j] != 1:
                    A[i][j] = A[i-1][j] + A[i][j-1]
        
        return A[-1][-1]