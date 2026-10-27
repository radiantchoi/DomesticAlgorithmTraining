def solution(s):
    s = list(s)
    answer = len(s)

    width = 1
    
    while width < len(s):
        result = []
        quote = []
        repeating = 1
        current = 0
        
        while current < len(s):
            ending = current + width
            chunk = s[current:] if ending > len(s) else s[current:ending]
            
            if not quote:
                quote = chunk
            elif chunk == quote:
                repeating += 1
            else:
                if repeating > 1: quote.append(str(repeating))
                
                quote_string = "".join(quote)
                result.append(quote_string)
                quote = chunk
                repeating = 1
            
            current = ending
        
        if repeating > 1: quote.append(str(repeating))
        quote_string = "".join(quote)
        result.append(quote_string)

        answer = min(answer, len("".join(result)))
        
        width += 1
    
    return answer