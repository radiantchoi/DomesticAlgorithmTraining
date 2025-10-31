m, n = map(int, input().split())

passwords = {}

for _ in range(m):
    site, password = input().split()
    passwords[site] = password

for _ in range(n):
    query = input()
    print(passwords[query])