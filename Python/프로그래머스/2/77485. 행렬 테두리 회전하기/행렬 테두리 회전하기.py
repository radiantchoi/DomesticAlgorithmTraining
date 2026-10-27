def solution(rows, columns, queries):
    answer = []
    
    grid = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = (i * columns) + j + 1
    
    for query in queries:
        starting_x = query[0] - 1
        starting_y = query[1] - 1
        ending_x = query[2] - 1
        ending_y = query[3] - 1
        
        storage = grid[starting_x + 1][starting_y]
        minimum = storage
        
        # 위
        for i in range(starting_y, ending_y + 1):
            temp_i = grid[starting_x][i]
            grid[starting_x][i] = storage
            storage = temp_i
            minimum = min(minimum, storage)
        
        # 오른쪽
        for j in range(starting_x + 1, ending_x + 1):
            temp_j = grid[j][ending_y]
            grid[j][ending_y] = storage
            storage = temp_j
            minimum = min(minimum, storage)
        
        # 아래
        for k in reversed(range(starting_y, ending_y)):
            temp_k = grid[ending_x][k]
            grid[ending_x][k] = storage
            storage = temp_k
            minimum = min(minimum, storage)
        
        # 왼쪽
        for l in reversed(range(starting_x + 1, ending_x)):
            temp_l = grid[l][starting_y]
            grid[l][starting_y] = storage
            storage = temp_l
            minimum = min(minimum, storage)
        
        answer.append(minimum)
    
    return answer