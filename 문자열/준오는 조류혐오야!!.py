import sys

n, m = map(int, sys.stdin.readline().strip().split())

bingo = [0 for _ in range(m)]

maxNineCnt = 0
nineCnt = 0

for i in range(n):
  num = sys.stdin.readline().strip()

  nineCnt += num.count('9')

  if maxNineCnt < num.count('9'):
    maxNineCnt = num.count('9')
  
  numList = num.split()

  for j in range(m):
    bingo[j] += numList[j].count('9')

if maxNineCnt > max(bingo):
  print(nineCnt - maxNineCnt)
else:
  print(nineCnt - max(bingo))

