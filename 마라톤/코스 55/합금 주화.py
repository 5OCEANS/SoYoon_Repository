import sys

d1, d2, x = map(int, sys.stdin.readline().split())

if d1 < d2:
  d1, d2 = d2, d1

density = (100 * d1 * d2) / (d2 * x + d1 * (100 - x))

print(f"{density:.14f}")