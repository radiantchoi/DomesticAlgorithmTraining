def collatz(num, times):
    if num == 1:
        return times
    
    if times >= 500:
        return -1
    
    return collatz(num // 2, times + 1) if num % 2 == 0 else collatz(num * 3 + 1, times + 1)

def solution(num):
    return collatz(num, 0)