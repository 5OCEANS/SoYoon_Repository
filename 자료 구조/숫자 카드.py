import sys

N = int(sys.stdin.readline().strip())
numList = set(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().strip().split()))

for i in range(M):
  if mList[i] in numList:
    print(1, end=' ')
  else:
    print(0, end = ' ')