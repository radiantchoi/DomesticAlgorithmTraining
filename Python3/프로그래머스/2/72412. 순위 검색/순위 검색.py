from collections import defaultdict
from bisect import bisect_left

def make_keys(lang, position, status, food):
    components = [
        [lang, position, status, food],
        ["-", position, status, food],
        [lang, "-", status, food],
        [lang, position, "-", food],
        [lang, position, status, "-"],
        ["-", "-", status, food],
        ["-", position, "-", food],
        ["-", position, status, "-"],
        [lang, "-", "-", food],
        [lang, "-", status, "-"],
        [lang, position, "-", "-"],
        ["-", "-", "-", food],
        ["-", "-", status, "-"],
        ["-", position, "-", "-"],
        [lang, "-", "-", "-"],
        ["-", "-", "-", "-"]
    ]
    
    return map(lambda x: " ".join(x), components)

def solution(info, query):
    answer = []
    scores = defaultdict(list)
    
    for user in info:
        lang, position, status, food, score = user.split()
        score = int(score)
        
        keys = make_keys(lang, position, status, food)
        for key in keys:
            scores[key].append(score)
    
    for data in scores.values():
        data.sort()

    for q in query:
        query_data = list(filter(lambda x: x != "and", q.split()))
        threshold = int(query_data.pop())
        query_key = " ".join(query_data)
        candidates = scores[query_key]
        
        answer.append(len(candidates) - bisect_left(candidates, threshold))
            
    return answer
        