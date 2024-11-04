import sys

xList = list()
yList = list()
resultx = 0
resulty = 0

for i in range(3):
  x, y = map(int, sys.stdin.readline().strip().split())
  xList.append(x)
  yList.append(y)

for i in range(3):
  if xList.count(xList[i]) == 1:
    resultx = xList[i]
  if yList.count(yList[i]) == 1:
    resulty = yList[i]

print(resultx, resulty)