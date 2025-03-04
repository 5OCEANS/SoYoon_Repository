import sys

N, K = map(int, sys.stdin.readline().strip().split())
chocoList = list(map(int, sys.stdin.readline().strip().split()))
count = 0
days = 0
for i in range(1, N):
  if chocoList[0] < chocoList[i]:
    days += 1
    count += (chocoList[i]-chocoList[0])
print(count, days)