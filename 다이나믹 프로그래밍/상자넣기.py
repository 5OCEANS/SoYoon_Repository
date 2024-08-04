import sys

n = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().strip().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
  for j in range(i):
    if numList[i] > numList[j]:
      dp[i] = max(dp[i], dp[j]+ 1)

print(max(dp))
    
# numList 다음 것보다 현재 값이 작으면 + 1