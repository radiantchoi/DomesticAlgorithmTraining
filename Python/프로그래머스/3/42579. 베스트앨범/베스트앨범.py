def solution(genres, plays):
    numbers = [x for x in range(len(genres))]
    tracks = zip(numbers, genres, plays)
    
    tracklists = {}
    totalplays = {}
    
    for track in tracks:
        sublist = tracklists.get(track[1], [])
        sublist.append(track)
        tracklists[track[1]] = sublist
        
        plays = totalplays.get(track[1], 0)
        totalplays[track[1]] = plays + track[2]
    
    answer = []
    priority = sorted(totalplays.keys(), key=lambda x: -totalplays[x])
    
    for genre in priority:
        sublist = tracklists[genre]
        
        sublist.sort(key=lambda x: -x[0])
        sublist.sort(key=lambda x: x[2])

        count = 0
        
        while sublist and count < 2:
            answer.append(sublist.pop()[0])
            count += 1
    
    return answer