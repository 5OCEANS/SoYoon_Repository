n = int(input())
xyList = []

for i in range(n):
  x, y = map(int, input().split())
  xyList.append([x, y])

xyList.sort(key=lambda x:(x[1], x[0]))

for i in range(n):
  print(xyList[i][0], xyList[i][1])