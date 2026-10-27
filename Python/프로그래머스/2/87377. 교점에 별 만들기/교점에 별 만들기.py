def solution(line):
    n = len(line)
    
    points = []
    max_x = -int(1e15)
    max_y = -int(1e15)
    min_x = int(1e15)
    min_y = int(1e15)
    
    for i in range(len(line) - 1):
        front = line[i]
        a, b, e = front
        
        for j in range(i+1, len(line)):
            back = line[j]
            c, d, f = back
            
            if a * d == b * c:
                continue

            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if int(x) == x and int(y) == y:
                x = int(x)
                y = int(y)

                points.append([x, y])
                if x > max_x: max_x = x
                if y > max_y: max_y = y
                if x < min_x: min_x = x
                if y < min_y: min_y = y
            
    
    length = max_x - min_x + 1
    height = max_y - min_y + 1
    
    answer = [["."] * length for _ in range(height)]
    
    for point in points:
        ax = point[0] - min_x
        ay = point[1] - min_y
        
        answer[ay][ax] = "*"
    
    return ["".join(x) for x in reversed(answer)]