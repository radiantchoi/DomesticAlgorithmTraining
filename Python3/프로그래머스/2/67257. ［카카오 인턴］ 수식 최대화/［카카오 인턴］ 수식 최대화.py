from itertools import permutations as permu

def enumerator(expression):
    result = []
    current = ["("]
    
    for letter in expression:
        if ord(letter) in range(ord("0"), ord("9") + 1):
            current.append(letter)
        else:
            current.append(")")
            result.append("".join(current))
            current = ["("]
            result.append(letter)
    
    current.append(")")
    result.append("".join(current))
    return result
        
def traverse(case, i, current):
    if i >= 3:
        final = int(current[0][1:-1])
        return abs(final)
    
    operator = case[i]
    
    calculating = False
    stack = []
    
    for component in current:
        if calculating:
            leading = stack.pop()
            leading = int(leading[1:-1])
            trailing = int(component[1:-1])
            result = ["("]
            
            if operator == "*":
                result.append(str(leading * trailing))
            elif operator == "+":
                result.append(str(leading + trailing))
            else:
                result.append(str(leading - trailing))
            
            result.append(")")
            stack.append("".join(result))
            calculating = False
        else:
            if operator == component:
                calculating = True
            else:
                stack.append(component)
    
    return traverse(case, i+1, stack)

def solution(expression):
    answer = 0
    
    operators = ["+", "-", "*"]
    cases = list(permu(operators, 3))
    
    exp = enumerator(expression)

    for case in cases:
        current = [x for x in exp]
        result = traverse(case, 0, current)
        answer = max(answer, result)
    
    return answer