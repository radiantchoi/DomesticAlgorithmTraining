def tri(n):
    result = []
    
    while n > 0:
        n, k = divmod(n, 3)
        result.append(str(k))
    
    return "".join(result)

def solution(n):
    return int(tri(n), 3)
    