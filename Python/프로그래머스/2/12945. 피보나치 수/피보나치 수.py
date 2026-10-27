def solution(n):
    result = [0, 1]
    
    if n > 1:
        for i in range(2, n+1):
            result.append(result[i-1] + result[i-2])
    
    return result[n] % 1234567