import sys

n = int(sys.stdin.readline())
xList = list()
yList = list()
for i in range(n):
  x, y = map(int, sys.stdin.readline().strip().split())
  xList.append(x)
  yList.append(y)

sX = sum(xList)
sY = sum(yList)
sXX = 0
sXY = 0
for i in range(n):
  sXX += xList[i] ** 2
  sXY += (xList[i] * yList[i])

if (n*sXX) == (sX ** 2):
  print('EZPZ')
  exit()

a2 = (n*sXY - sX*sY) / (n*sXX - sX**2)
b2 = (sY - a2*sX) / n

print(a2, b2)