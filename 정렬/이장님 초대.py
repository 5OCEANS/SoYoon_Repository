import sys

N = int(sys.stdin.readline())
tList = list(map(int, sys.stdin.readline().strip().split()))
sortedList = sorted(tList, reverse=True)

maxTime = 0

for i in range(N):
  time = sortedList[i] + i + 2
  if maxTime < time:
    maxTime = time

print(maxTime)