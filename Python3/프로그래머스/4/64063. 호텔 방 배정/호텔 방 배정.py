def solution(k, room_number):
    rooms = {}
    result = []
    
    for number in room_number:
        current = number
        visiteds = [current]
        
        while current in rooms:
            current = rooms[current]
            visiteds.append(current)
        
        result.append(current)
        
        for visited in visiteds:
            rooms[visited] = current + 1
    
    return result