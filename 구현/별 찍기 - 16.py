import sys

N = int(sys.stdin.readline())

for i in range(N):
  space = (N-(i+1))
  print(' '*space+'* '*(i+1))