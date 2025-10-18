import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    N, M = map(int, input().rstrip().split())
    priorities = list(map(int, input().rstrip().split()))
    remainings = sorted(priorities)
    priorities = deque(enumerate(priorities))

    printed = 0

    while priorities:
        current = priorities.popleft()

        while priorities and remainings and remainings[-1] != current[1]:
            priorities.append(current)
            current = priorities.popleft()
        
        printed += 1
        remainings.pop()

        if current[0] == M:
            print(printed)
            break