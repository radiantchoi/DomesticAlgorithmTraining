def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    words = []
    existance = {}
    found = False
    
    for vowel in vowels:
        if found:
            continue
        
        stack = [vowel]
        
        while stack:
            current = stack.pop()
            
            if not existance.get(current, False):
                existance[current] = True
                words.append(current)
                
                if current == word:
                    found = True
                    break
            
            if len(current) < 5:
                for trailing in reversed(vowels):
                    stack.append(current + trailing)
    
    return len(words)