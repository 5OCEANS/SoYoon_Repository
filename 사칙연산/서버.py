import sys

n, T = map(int, sys.stdin.readline().strip().split())
timeList = list(map(int, sys.stdin.readline().strip().split()))

cnt = 0
current_sum = 0

for i in range(n):
  if current_sum + timeList[i] <= T:
    current_sum += timeList[i]
    cnt += 1
  else:
    break

print(cnt)