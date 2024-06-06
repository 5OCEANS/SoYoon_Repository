import sys

R, C = map(int, sys.stdin.readline().split())

lastLocationList = [0 for _ in range(9)]

for i in range(R):
  row = list(sys.stdin.readline().strip()) # S.....111F
  row = row[1:C-1] # .....111 -- S, F가 빠지게 됨.
  row.reverse() # row를 뒤집음.
  for j in range(C-2):
    if row[j] != '.':
      lastLocationList[int(row[j])-1] = j # 0 1 2 3 4 5 4 3 2 
      break
  else:
    continue

rankList = [0 for _ in range(9)]
cnt = 1
# lastLocationList에서의 가장 최소의 값이 100보다 작을 때까지 while문 반복
# lastLocationList에서 가장 최소의 값을 찾음.
# lastLocationList.count() 값만큼 for 문을 돌림.
#   그 값의 인덱스를 구한 후 rankList[인덱스값]을 cnt 값으로 바꿈
#   그 값을 100으로 바꿈
# cnt += 1
# 


while min(lastLocationList) < 100:
  minVal = min(lastLocationList)
  for i in range(lastLocationList.count(minVal)):
    index = lastLocationList.index(minVal)
    rankList[index] = cnt
    lastLocationList[index] = 100
  cnt += 1

for i in range(len(rankList)):
  print(rankList[i])