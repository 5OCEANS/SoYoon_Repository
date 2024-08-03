import sys

# i번째 데이터 이전까지 합을 계산해 봤을 때 최대값을 지속적으로 기록한다.
# 이전까지의 합이, 그냥 i번째 숫자보다 작은 경우 이전의 기록들은 무의미하다.
# 그러니까 그냥 i번째 숫자를 최대값으로 설정한다.

n = int(sys.stdin.readline())

numList = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n):
  numList[i] = max(numList[i], numList[i] + numList[i-1])

print(max(numList))