import sys

r = 31
M = 1234567891

L = int(sys.stdin.readline())
letters = sys.stdin.readline().rstrip()

base = 0

for (index, letter) in enumerate(letters):
    i = ord(letter) - ord("a") + 1
    base += i * (r ** (index))

print(int(base % M))