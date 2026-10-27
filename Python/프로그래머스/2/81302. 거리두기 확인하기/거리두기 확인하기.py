def solution(places):
    answer = []
    
    for place in places:
        participants = []
        corrupted = False
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    participants.append([i, j, 0])
                    
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for participant in participants:
            checkout = [participant]
            visited = [[False] * 5 for _ in range(5)]
            
            while checkout and not corrupted:
                current = checkout.pop()
                visited[current[0]][current[1]] = True
                
                for d in range(4):
                    nx = current[0] + dx[d]
                    ny = current[1] + dy[d]
                    nd = current[2] + 1

                    if 0 <= nx < 5 and 0 <= ny < 5 and nd <= 2 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        
                        if place[nx][ny] == "P":
                            corrupted = True
                        elif place[nx][ny] == "X":
                            continue
                        else:
                            checkout.append([nx, ny, nd])

        if corrupted:
            answer.append(0)
        else:
            answer.append(1)
    
    return answer