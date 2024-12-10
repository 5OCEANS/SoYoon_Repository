import sys

N = int(sys.stdin.readline())
bucketList = [0 for _ in range(1001)]
for i in range(N):
  s, t, b = map(int, sys.stdin.readline().strip().split())
  for j in range(s,t+1):
    bucketList[j] += b
print(max(bucketList))