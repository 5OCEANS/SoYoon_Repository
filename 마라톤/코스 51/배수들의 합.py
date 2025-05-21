import sys

N, M = map(int, sys.stdin.readline().strip().split())
mList = list(map(int, sys.stdin.readline().strip().split()))
sum = 0

for i in range(2, N+1):
  for j in mList:
    if i % j == 0:
      sum += i
      break
print(sum)    