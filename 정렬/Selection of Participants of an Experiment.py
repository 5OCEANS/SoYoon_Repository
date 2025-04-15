import sys

while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  pList = list(map(int, sys.stdin.readline().strip().split()))
  minDiff = 10000001
  pList.sort()
  for i in range(n-1, 0, -1):
    diff = pList[i] - pList[i-1]
    if diff < minDiff:
      minDiff = diff
  print(minDiff)