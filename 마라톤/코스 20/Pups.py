import sys

n = int(sys.stdin.readline())
for i in range(n):
  d, f, p = map(float, sys.stdin.readline().strip().split())
  print('$%0.02f'%(d*f*p))