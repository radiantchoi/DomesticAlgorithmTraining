# ticket은 [m, n] 형태이며 m은 이진 변환 횟수, n은 제거된 0의 갯수
def binary_transformation(binary, ticket):
    if binary == "1":
        return ticket
    
    length = len(binary)
    
    for digit in binary:
        if digit == "0":
            ticket[1] += 1
            length -= 1
    
    binary = bin(length)[2:]
    ticket[0] += 1
    
    return binary_transformation(binary, ticket)

def solution(s):
    return binary_transformation(s, [0, 0])