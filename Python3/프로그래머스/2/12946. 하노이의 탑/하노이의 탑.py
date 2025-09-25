def hanoi(n, starting, mid, ending, answer):
    if n == 1:
        answer.append([starting, ending])
        return
    
    hanoi(n - 1, starting, ending, mid, answer)
    answer.append([starting, ending])
    hanoi(n - 1, mid, starting, ending, answer)

def solution(n):
    answer = []
    
    hanoi(n, 1, 2, 3, answer)
    
    return answer