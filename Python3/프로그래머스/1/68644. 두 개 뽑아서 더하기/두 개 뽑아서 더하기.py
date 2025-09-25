from itertools import combinations as combi

def solution(numbers):
    return sorted(list(set(map(lambda x: x[0] + x[1], combi(numbers, 2)))))