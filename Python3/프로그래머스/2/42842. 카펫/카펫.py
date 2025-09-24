def solution(brown, yellow):
    answer = []
    
    hor = (brown - 4) // 2 - 1
    ver = 1
    
    while hor >= ver:
        if hor * ver == yellow:
            answer.append(hor + 2)
            answer.append(ver + 2)
            break
        
        hor -= 1
        ver += 1
    
    return answer