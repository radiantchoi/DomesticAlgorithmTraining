def push(letter, n):
    current = ord(letter)
    
    if 64 < current < 91:
        current = (current - ord("A") + n) % 26
        return chr(current + ord("A"))
    elif 96 < current < 123:
        current = (current - ord("a") + n) % 26
        return chr(current + ord("a"))
    else:
        return letter
    
def solution(s, n):
    return "".join(list(map(lambda x: push(x, n), s)))