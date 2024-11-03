import sys, math

x1, y1, r1 = map(int, sys.stdin.readline().strip().split())
x2, y2, r2 = map(int, sys.stdin.readline().strip().split())

if (math.sqrt((x1-x2)**2 + (y1-y2)**2)) >= (r1+r2):
  print('NO')
else:
  print('YES')