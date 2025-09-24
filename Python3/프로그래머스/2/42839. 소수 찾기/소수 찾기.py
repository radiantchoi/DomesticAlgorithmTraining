from math import sqrt
from itertools import permutations as permu

def is_prime(number):
    if number < 2:
        return False
    elif number < 3:
        return True
    
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    return True

def solution(numbers):    
    cards = list(numbers)
    chunks = {}
    
    for i in range(1, len(cards) + 1):
        pairs = permu(cards, i)
        
        for pair in pairs:
            chunks[int("".join(pair))] = True
    
    return len(list(filter(is_prime, chunks.keys())))