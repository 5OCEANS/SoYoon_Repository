import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  A, B = map(int, sys.stdin.readline().strip().split())

  print('Case #%d: %d + %d = %d' %(i+1, A, B, A+B))