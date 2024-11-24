import sys

N = int(sys.stdin.readline())
timeList = [0 for _ in range(1000)]
workList = list()

for _ in range(N):
  start_time, end_time = map(int, sys.stdin.readline().strip().split())
  workList.append((start_time, end_time))
  for i in range(start_time, end_time):
    timeList[i] += 1

ans = 0

for w in workList:
  start_time, end_time = w[0], w[1]
  for i in range(start_time, end_time):
    timeList[i] -= 1
  time = 0
  for t in timeList:
    if t > 0:
      time += 1
  ans = max(time, ans)
  for i in range(start_time, end_time):
    timeList[i] += 1

print(ans)