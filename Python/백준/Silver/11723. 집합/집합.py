import sys

n = int(sys.stdin.readline())

pool = {}

for _ in range(n):
    line = sys.stdin.readline().strip().split()

    command = line[0]
    
    if command == "add":
        element = int(line[1])
        if not pool.get(element, False):
            pool[element] = True
    elif command == "remove":
        element = int(line[1])
        if pool.get(element, False):
            pool[element] = False
    elif command == "check":
        element = int(line[1])
        print("1" if pool.get(element, False) else "0")
    elif command == "toggle":
        element = int(line[1])
        if pool.get(element, False):
            pool[element] = False
        else:
            pool[element] = True
    elif command == "all":
        for i in range(1, 21):
            pool[i] = True
    elif command == "empty":
        pool.clear()