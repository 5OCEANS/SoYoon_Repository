import sys

t = int(sys.stdin.readline())
for i in range(t):
  n, a, b = map(int, sys.stdin.readline().strip().split())

  day = bin((min(a, b)))[::-1].index('1')
  print(n-day)