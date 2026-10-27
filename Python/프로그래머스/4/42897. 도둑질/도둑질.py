def solution(money):
    first_money = money[:-1]
    second_money = money[1:]
    
    def house_robber(homes) -> int:
        if len(homes) < 3:
            return max(homes)
        
        homes[1] = max(homes[0], homes[1])
        
        for i in range(2, len(homes)):
            homes[i] = max(homes[i - 2] + homes[i], homes[i - 1])
        
        return homes[-1]
    
    first_candidate = house_robber(first_money)
    second_candidate = house_robber(second_money)
    
    return max(first_candidate, second_candidate)