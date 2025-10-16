n = int(input())
sizes = list(map(int, input().split()))
shirt_unit, pen_unit = map(int, input().split())

print(sum((size + shirt_unit - 1) // shirt_unit for size in sizes))
print(n // pen_unit, n % pen_unit)