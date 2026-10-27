def solution(s):
    stack = []
    
    for letter in s:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    
    return 1 if len(stack) == 0 else 0        