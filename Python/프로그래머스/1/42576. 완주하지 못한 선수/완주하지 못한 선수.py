def solution(participant, completion):
    p = {}
    
    for person in participant:
        p[person] = p.get(person, 0) + 1
        
    for person in completion:
        status = p.get(person, 0)
        
        if status == 0:
            return person
        
        if status == 1:
            del p[person]
        else:
            p[person] = status - 1
        
    return list(p.keys())[0]