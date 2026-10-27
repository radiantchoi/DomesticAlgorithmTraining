from functools import cmp_to_key

def solution(numbers):
    cards = [x for x in map(lambda x: str(x), numbers)]
    cards.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
    
    return str(int("".join(cards)))