def hanoi(n, starting, passing, ending, answer):
    if n == 1:
        answer.append([starting, ending])
        return
    
    hanoi(n - 1, starting, ending, passing, answer)
    answer.append([starting, ending])
    hanoi(n - 1, passing, starting, ending, answer)

def solution(n):
    answer = []
    
    hanoi(n, 1, 2, 3, answer)
    
    return answer