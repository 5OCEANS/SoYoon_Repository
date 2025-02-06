import sys

N = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().strip().split())
sameSet = set([i for i in range(a, b+1)])
for i in range(N-1):
  a, b = map(int, sys.stdin.readline().strip().split())
  numSet = set(i for i in range(a, b+1))
  sameSet = sameSet.intersection(numSet)

if sameSet:
  print('gunilla has a point')
else:
  print('edward is right')