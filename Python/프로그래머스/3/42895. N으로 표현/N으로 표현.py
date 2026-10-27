def solution(N, number):
    if N == number:
        return 1
    
    times = {1: set([N])}
    
    for time in range(2, 9):
        cases = set([int("".join([str(N) for _ in range(time)]))])
        
        for i in range(1, time):
            leadings = times[i]
            trailings = times[time - i]
            
            for j in leadings:
                for k in trailings:
                    cases.add(j + k)
                    cases.add(j - k)
                    cases.add(k - j)
                    cases.add(j * k)
                    
                    if j > 0:
                        cases.add(k // j)
                    
                    if k > 0:
                        cases.add(j // k)
        
        if number in cases:
            return time
        
        times[time] = cases
    
    return -1