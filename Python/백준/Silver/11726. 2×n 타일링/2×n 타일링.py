import sys

n = int(sys.stdin.readline())

cases = [0, 1, 2]

if n > 2:
    for _ in range(3, n+1):
        current = cases[-1] + cases[-2]
        cases.append(current)

print(cases[n] % 10007)