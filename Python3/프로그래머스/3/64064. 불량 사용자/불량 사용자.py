import re

def traverse(i, bits, mask, answer, seen):
    state = (i, mask)
    
    if state in seen:
        return
    
    seen.add(state)

    if i == len(bits):
        answer.add(mask)
        return

    for bit in bits[i]:
        if mask & bit:
            continue
            
        traverse(i + 1, bits, mask | bit, answer, seen)

def solution(user_id, banned_id):
    patterns = [x.replace("*", ".") for x in banned_id]
    pools = [[user for user in user_id if re.fullmatch(pattern, user)] for pattern in patterns]
    
    if not pools: return 0

    indices = {user: index for (index, user) in enumerate(user_id)}
    bits = [[1 << indices[user] for user in pool] for pool in pools]

    answer = set()
    seen = set()
    
    traverse(0, bits, 0, answer, seen)
    
    return len(answer)