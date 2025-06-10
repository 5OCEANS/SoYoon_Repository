import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
  x, y = map(int, sys.stdin.readline().strip().split())
  print('NO BRAINS') if x < y else print('MMM BRAINS')