import sys

N = int(sys.stdin.readline())
xList = []
yList = []
for i in range(N):
  x, y = map(int, sys.stdin.readline().strip().split())
  if N == 1:
    print(0)
    exit()  
  xList.append(x)
  yList.append(y)

print(abs((max(xList) - min(xList))) * abs(((max(yList) - min(yList)))))