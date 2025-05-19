import sys

P, N = map(int, sys.stdin.readline().strip().split())
durations = list(map(int, sys.stdin.readline().strip().split()))

durations.sort()
time_limit = P - 1

cnt = 0
total_duration = 0

for duration in durations:
  if time_limit >= duration:
    total_duration += time_limit
    time_limit -= duration
    cnt += 1
  else:
    break

print(cnt, total_duration)