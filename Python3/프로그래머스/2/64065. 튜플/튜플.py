def solution(s):
    n = len(s)
    trimmed = s[2:n-2]
    chunks = trimmed.split("},{")
    
    occurence = {}
    
    for chunk in chunks:
        numbers = chunk.split(",")
        
        for number in numbers:
            occurence[int(number)] = occurence.get(int(number), 0) + 1
    
    return sorted(list(occurence.keys()), key=lambda x: occurence[x], reverse=True)