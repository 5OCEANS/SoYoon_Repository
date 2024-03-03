import sys

K, D, A = map(int, sys.stdin.readline().strip().split('/'))

if K+A < D or D == 0:
  print('hasu')
else:
  print('gosu')