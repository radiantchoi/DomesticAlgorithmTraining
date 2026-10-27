def solution(m, n, puddles):
    grid = [[0] * m for _ in range(n)]
    
    for puddle in puddles:
        grid[puddle[1]-1][puddle[0]-1] = -1
        
    grid[0][0] = 1
    
    for k in range(n):
        for l in range(m):
            if grid[k][l] < 0:
                continue
            elif k == 0 and l == 0:
                continue
            else:
                top_candidate = grid[k-1][l]
                left_candidate = grid[k][l-1]
                
                if top_candidate >= 0:
                    grid[k][l] += top_candidate
                
                if left_candidate >= 0:
                    grid[k][l] += left_candidate
    
    return grid[-1][-1] % 1_000_000_007