def solution(n):
    grid = [[0] * x for x in range(1, n+1)]
    
    handling = 1
    
    level = n
    mode = 0
    
    ceiling = 0
    wall = 0
    
    while level > 0:
        if mode == 0:
            for _ in range(level):
                grid[ceiling][wall] = handling
                handling += 1
                ceiling += 1
            
            ceiling -= 1
            wall += 1
        elif mode == 1:
            for _ in range(level):
                grid[ceiling][wall] = handling
                handling += 1
                wall += 1
            
            wall -= 2
            ceiling -= 1
        elif mode == 2:
            for _ in range(level):
                grid[ceiling][wall] = handling
                handling += 1
                ceiling -= 1
                wall -= 1
            
            ceiling += 2
            wall += 1
        
        if mode == 2:
            mode = 0
        else:
            mode += 1
        
        level -= 1
    
    answer = []
    for line in grid:
        answer += line
    
    return answer