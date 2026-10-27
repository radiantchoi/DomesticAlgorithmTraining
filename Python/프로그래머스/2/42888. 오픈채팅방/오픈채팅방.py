def solution(record):
    answer = []
    
    predefined = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    users = {}
    actions = []
    
    for r in record:
        info = r.split()
        
        action = info[0]
        uid = info[1]
        
        if action == "Change":
            users[uid] = info[2]
        elif action == "Enter":
            users[uid] = info[2]
            actions.append([action, uid])
        else:
            actions.append([action, uid])
    
    for action in actions:
        name = users.get(action[1], "알수없음")
        did = predefined.get(action[0], "님입니다.")
        
        answer.append("".join([name, did]))
    
    return answer