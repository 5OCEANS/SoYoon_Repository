import sys

N, K = map(int, sys.stdin.readline().strip().split())
timeList = list(map(int, sys.stdin.readline().strip().split()))
ans = 1
presentTime = timeList[0] + K

for time in timeList:
  if presentTime >= time:
    continue
  else:
    ans += 1
    presentTime = time + K
print(ans)