import sys

T = int(sys.stdin.readline())

for i in range(T):
  numList = list(map(int, sys.stdin.readline().strip().split()))

  print(sum(numList))