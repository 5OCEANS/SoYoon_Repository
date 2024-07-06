import sys

N, M = map(int, sys.stdin.readline().strip().split())

aMList = []
sumList = []

for i in range(N):
  aM = list(map(int, sys.stdin.readline().strip().split()))
  aMList.append(aM)

for i in range(N):
  bM = list(map(int, sys.stdin.readline().strip().split()))
  sum = []
  for j in range(M):
    sum.append(str(aMList[i][j] + bM[j]))
  print(' '.join(sum))