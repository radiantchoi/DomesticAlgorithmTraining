def solution(money):
    first = money[:len(money) - 1]
    first[1] = max(first[0], first[1])
    
    for i in range(2, len(first)):
        first[i] = max(first[i - 2] + money[i], first[i - 1])
    
    second = money[1:]
    second[1] = max(second[0], second[1])
    for j in range(2, len(second)):
        second[j] = max(second[j - 2] + money[j + 1], second[j - 1])
    
    return max(first[-1], second[-1])