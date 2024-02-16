import sys

N, A, B = map(int, sys.stdin.readline().split())

if A < B:
  print('Bus')
elif A > B:
  print('Subway')
else:
  print('Anything')