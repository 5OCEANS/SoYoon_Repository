import sys

N = int(sys.stdin.readline())
xyList = []
for _ in range(N):
  x, y = map(int, sys.stdin.readline().strip().split())
  xyList.append((x, y))
xyList.sort(key= lambda x:(x[1]))
print(xyList[0][0], xyList[0][1])