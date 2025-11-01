import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    command = sys.stdin.readline().strip()

    if command == "0":
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, int(command))