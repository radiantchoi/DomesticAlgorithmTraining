def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == a[i % 5]:
            scores[0] += 1
        
        if answers[i] == b[i % 8]:
            scores[1] += 1
            
        if answers[i] == c[i % 10]:
            scores[2] += 1
    
    return [x[0] + 1 for x in enumerate(scores) if x[1] == max(scores)]
    