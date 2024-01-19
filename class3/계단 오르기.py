# DP
# 계단을 올라가는 앞에서 생각하는 방식보다는 도착지부터 생각하는 방식의 접근이 더 쉬움

# n-1번째 계단으로 오는 경우
# dp[n] = dp[n-3] + dp[n-1] + dp[n]

# n-2번째 계단으로 오는 경우

#   이 중에서 더 큰 수가 dp[n]이 된다.

import sys

n = int(sys.stdin.readline())

# 계단의 숫자를 초기화. 1층은 1번째 index
stairs = [0] * 301

for i in range(1, n+1):
  stairs[i] = int(sys.stdin.readline())

# dp 배열 초기화
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2]+stairs[3])

# 점화식을 계산
for i in range(4, n+1):
  dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2] + stairs[i])

print(dp[n])