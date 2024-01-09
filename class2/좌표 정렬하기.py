pointCnt = int(input())
pointList = []

for i in range(pointCnt):
  pointList.append([])
  x, y = map(int, input().split())
  pointList[i].extend([x, y])

pointList.sort(key=lambda x:(x[0], x[1]))

for i in range(pointCnt):
  print(pointList[i][0], pointList[i][1])