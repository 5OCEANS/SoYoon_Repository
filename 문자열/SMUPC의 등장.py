import sys

S = sys.stdin.readline().strip()

for i in S:
  num = str(ord(i))
  numCnt = 0

  for j in num:
    numCnt += int(j)

  print(i*numCnt)