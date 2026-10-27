def solution(s):
    words = list(s)
    current = 0
    
    for i in range(len(words)):
        if words[i] == " ":
            current = 0
        else:
            words[i] = words[i].upper() if current % 2 == 0 else words[i].lower()
            current += 1
    
    return "".join(words)