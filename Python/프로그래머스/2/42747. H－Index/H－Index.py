def solution(citations):
    for (index, citation) in enumerate(sorted(citations)):
        h = len(citations) - index
        
        if citation >= h:
            return h
    
    return 0