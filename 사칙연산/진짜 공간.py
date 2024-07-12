import sys, math


N = int(sys.stdin.readline())
sizeList = list(map(int, sys.stdin.readline().strip().split()))
clusterSize = int(sys.stdin.readline())

cnt = 0

for i in range(len(sizeList)):
  cnt += math.ceil(sizeList[i] / clusterSize)
cnt = cnt * clusterSize

print(cnt)