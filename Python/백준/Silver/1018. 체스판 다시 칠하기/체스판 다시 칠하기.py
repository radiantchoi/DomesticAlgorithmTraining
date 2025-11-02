import sys

first = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"]         
]

second = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"]
]


n, m = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().strip()) for _ in range(n)]

def compare(starting, board, premade):
    count = 0
    
    for i in range(8):
        for j in range(8):
            if premade[i][j] != board[starting[0] + i][starting[1] + j]:
                count += 1
    
    return count
                

result = 64

for i in range(n - 7):
    for j in range(m - 7):

        starting = (i, j)
        result = min(result, compare(starting, board, first), compare(starting, board, second))

print(result)