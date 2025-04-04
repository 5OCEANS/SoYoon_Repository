import sys

p1, p2, p3, x1, x2, x3 = map(int, sys.stdin.readline().split())

limit = p1 * p2 * p3 

for i in range(1, limit + 1):
  if (i % p1 == x1) and (i % p2 == x2) and (i % p3 == x3):
    print(i)
    break
else:
  print(-1)