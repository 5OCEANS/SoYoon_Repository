import sys

gridList = []
cnt = 0

for i in range(10):
  gridLine = list(sys.stdin.readline().strip().split())

  if len(set(gridLine)) == 1:
    cnt += 1

  gridList.append(gridLine)

for i in range(10):
  gridLengthLine = list(zip(*gridList))[i]

  if len(set(gridLengthLine)) == 1:
    cnt += 1

if cnt > 0:
  print(1)
else:
  print(0)