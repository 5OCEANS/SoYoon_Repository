import sys

chessList = list(map(int, sys.stdin.readline().strip().split()))

chessDic = [1, 1, 2, 2, 2, 8]

for i in range(6):
  print(chessDic[i] - chessList[i], end = ' ')