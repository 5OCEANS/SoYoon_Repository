import sys

n = int(sys.stdin.readline().strip())
abList = list()
for i in range(n):
  ab = list(map(int, sys.stdin.readline().strip().split()))
  abList.append(ab)

for i in range(n, -1, -1):
  trueCount = 0
  for j in range(n):
    if abList[j][0] <= i <= abList[j][1]:
      trueCount += 1
  if trueCount == i:
    print(i)
    exit()
else:
  print(-1)