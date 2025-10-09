import re

def solution(phone_book):
    phone_book.sort()
    
    previous = {}
    prevphone = ""
    
    for phone in phone_book:
        current = {}
        
        for digit in phone:
            current[digit] = current.get(digit, 0) + 1
        
        different = False if previous else True
        
        for key in previous.keys():
            if key not in current or current[key] < previous[key]:
                different = True
                break
        
        if not different:
            if phone[:len(prevphone)] == prevphone:
                return False
            
        prevphone = phone
        previous = current
    
    return True