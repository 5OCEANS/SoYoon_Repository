cardCnt, maxNum = map(int, input().split())

cardList = list(map(int, input().split()))

resList = []

for i in range(0, cardCnt-2):
  for d in range(i+1, cardCnt-1):
    for k in range(d+1, cardCnt):
      num = 0
      num = cardList[i] + cardList[d] + cardList[k]

      if num <= maxNum:
        resList.append(num)
print(max(resList))