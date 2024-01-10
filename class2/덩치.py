pCnt = int(input())
xyList = []
cnt = 0

for i in range(pCnt):
  x, y = map(int, input().split())
  xyList.append([x, y])

for i in range(pCnt):
  cnt = 1
  for j in range(pCnt):
    if xyList[i][0] < xyList[j][0] and xyList[i][1] < xyList[j][1]: # 자기자신보다 x와 y 둘 다 크다면 자기자신의 등수가 떨어짐. 만약 둘 중 하나만 비교대상이 크다면 같은 등수로 생각함.
      cnt += 1
  print(cnt, end=' ')