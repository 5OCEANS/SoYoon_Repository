import sys

l, r = map(int, sys.stdin.readline().strip().split())

if l == r:
  if l == 0 and r == 0:
    print('Not a moose')
  else:
    print('Even ' + str(2*l))
else:
  print('Odd ' + str(2*max(l, r)))