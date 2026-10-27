def solution(clothes):
    clothings = {}
    
    for c in clothes:
        clothings[c[1]] = clothings.get(c[1], 0) + 1
    
    result = 1
    
    cases = list(map(lambda x: x + 1, clothings.values()))
    
    for case in cases:
        result *= case
    
    return result - 1