import sys

sys.setrecursionlimit(2000)

def find(number, rooms, visiteds):
    visiteds.append(number)
    
    if number not in rooms:
        return number
    
    return find(rooms[number], rooms, visiteds)

def solution(k, room_number):
    rooms = {}
    result = []
    
    for number in room_number:
        visiteds = []
        current = find(number, rooms, visiteds)
        
        result.append(current)
        
        for visited in visiteds:
            rooms[visited] = current + 1
    
    return result