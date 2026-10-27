from itertools import permutations as permu

def spread(expression):
    stack = []
    current = []
    
    for letter in expression:
        if letter.isdecimal():
            current.append(letter)
        else:
            stack.append("".join(current))
            current = []
            stack.append(letter)
    
    stack.append("".join(current))
    
    return stack

def register(components, rank):
    stack = []
    operators = []
    
    for component in components:
        if component.isdecimal():
            stack.append(component)
        else:
            while operators and rank[operators[-1]] >= rank[component]:
                stack.append(operators.pop())
            
            operators.append(component)
    
    while operators:
        stack.append(operators.pop())
    
    return stack

def resolve(registered):
    stack = []
    
    for component in registered:
        if component.isdecimal():
            stack.append(int(component))
        else:
            trailing = stack.pop()
            leading = stack.pop()
            
            if component == "+":
                stack.append(leading + trailing)
            elif component == "-":
                stack.append(leading - trailing)
            else:
                stack.append(leading * trailing)
    
    return abs(stack[0])

def solution(expression):
    answer = 0

    components = spread(expression)
    cases = list(permu(["+", "-", "*"], 3))
    
    for case in cases:
        rank = {y: x for x, y in enumerate(case)}
        registered = register(components, rank)
        answer = max(answer, resolve(registered))
    
    return answer