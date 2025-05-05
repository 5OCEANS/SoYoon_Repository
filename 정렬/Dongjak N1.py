import sys

n = int(sys.stdin.readline())
stops = list(map(int, sys.stdin.readline().split()))
stops.sort()

min_dist = float('inf')
count = 0

for i in range(n - 1):
  diff = stops[i + 1] - stops[i]
  if diff < min_dist:
    min_dist = diff
    count = 1
  elif diff == min_dist:
    count += 1

print(min_dist, count)