from collections import deque

def solution(m, n, puddles):
    grid = [[0 for _ in range(m)] for _ in range(n)]
    grid[0][0] = 1
    
    for puddle in puddles:
        grid[puddle[1] - 1][puddle[0] - 1] = -1
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == -1:
                continue
            
            if (0 <= i - 1 < n) and grid[i-1][j] > -1:
                grid[i][j] += grid[i-1][j]
            
            if (0 <= j - 1 < m) and grid[i][j-1] > -1:
                grid[i][j] += grid[i][j-1]
            
    return grid[n - 1][m - 1] % 1_000_000_007