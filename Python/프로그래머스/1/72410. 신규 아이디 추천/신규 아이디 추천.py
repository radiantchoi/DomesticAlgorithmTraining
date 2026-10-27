from collections import deque

def first_step(new_id):
    return new_id.lower()

def second_step_criteria(x):
    if ord("a") <= ord(x) <= ord("z"):
        return True
    elif x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_", "."]:
        return True
    else:
        return False

def second_step(new_id):   
    return "".join(list(filter(second_step_criteria, new_id)))

def third_step(new_id):
    stack = []
    
    for letter in new_id:
        if stack and stack[-1] == "." and letter == ".":
            continue
        else:
            stack.append(letter)
    
    return "".join(stack)

def fourth_step(new_id):
    letters = deque(new_id)
    
    while letters and letters[0] == ".":
        letters.popleft()
    
    while letters and letters[-1] == ".":
        letters.pop()

    return "".join(letters)

def fifth_step(new_id):
    return new_id if new_id else "a"

def sixth_step(new_id):
    new_id = new_id if len(new_id) < 16 else new_id[:15]
    
    return fourth_step(new_id)

def seventh_step(new_id):
    spread = list(new_id)
    
    while len(spread) < 3:
        spread.append(spread[-1])
    
    return "".join(spread)

def solution(new_id):
    new_id = first_step(new_id)
    new_id = second_step(new_id)
    new_id = third_step(new_id)
    new_id = fourth_step(new_id)
    new_id = fifth_step(new_id)
    new_id = sixth_step(new_id)
    new_id = seventh_step(new_id)
    
    return new_id