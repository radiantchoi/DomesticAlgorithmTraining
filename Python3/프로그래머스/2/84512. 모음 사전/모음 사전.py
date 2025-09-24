from itertools import product

def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    words = []
    
    for i in range(1, 6):
        selections = product(vowels, repeat=i)
        
        for selection in selections:
            words.append("".join(list(selection)))
    
    words.sort()
    
    return words.index(word) + 1