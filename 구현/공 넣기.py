import sys

N, M = map(int, sys.stdin.readline().strip().split())
nDict = {(i+1): 0 for i in range(N)}

for i in range(M):
  i, j, k = map(int, sys.stdin.readline().strip().split())
  for number in range(i, j+1):
    nDict[number] = k

for i in range(1, N+1):
  print(nDict[i], end=' ')