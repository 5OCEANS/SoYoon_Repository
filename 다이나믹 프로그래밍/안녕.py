import sys

# 배낭 알고리즘

n = int(sys.stdin.readline())
stamina_consum = [0] + list(map(int, sys.stdin.readline().strip().split()))
get_pleasure = [0] + list(map(int, sys.stdin.readline().strip().split()))

dp = [[0] * 101 for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1,101):
    if stamina_consum[i] <= j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-stamina_consum[i]] + get_pleasure[i])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][99])